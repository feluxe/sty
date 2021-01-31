"""
The Register class: Sty's heart.
"""
from collections import namedtuple
from copy import deepcopy
from typing import Callable, Dict, Iterable, List, NamedTuple, Tuple, Type, Union

from .rendertype import RenderType

Renderfuncs = Dict[Type[RenderType], Callable]

StylingRule = Union["Style", RenderType]


class Style(str):
    """
    This type stores the different styling rules for the registers and the resulting
    ANSI-sequence as a string.

    For example:

        fg.orange = Style(RgbFg(1,5,10), Sgr(1))

        isinstance(fg.orange, Style) # True

        isinstance(fg.orange, str) # True

        str(fg.orange) # '\x1b[38;2;1;5;10m\x1b[1m' (The ASNI sequence for orange and bold)

    """

    rules: Iterable[StylingRule]

    def __new__(cls, *rules: StylingRule, value: str = "") -> "Style":
        new_cls = str.__new__(cls, value)  # type: ignore
        setattr(new_cls, "rules", rules)
        return new_cls


def _render_rules(
    renderfuncs: Renderfuncs,
    rules: Iterable[StylingRule],
) -> Tuple[str, Iterable[StylingRule]]:

    rendered: str = ""
    flattened_rules: List[StylingRule] = []

    for rule in rules:

        if isinstance(rule, RenderType):
            f1: Callable = renderfuncs[type(rule)]
            rendered += f1(*rule.args)
            flattened_rules.append(rule)

        elif isinstance(rule, Style):
            r1, r2 = _render_rules(renderfuncs, rule.rules)
            rendered += r1
            flattened_rules.extend(r2)

        else:
            raise ValueError("Parameter 'rules' must be of type Iterable[Rule].")

    return rendered, flattened_rules


class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are
    created from this class. You can use it to create your own custom registers.
    """

    def __init__(self):
        self.renderfuncs: Renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def __setattr__(self, name: str, value: Style):

        if isinstance(value, Style):

            if self.is_muted:
                rendered_style = Style(*value.rules, value="")
            else:
                rendered, rules = _render_rules(self.renderfuncs, value.rules)
                rendered_style = Style(*rules, value=rendered)

            return super().__setattr__(name, rendered_style)
        else:
            # TODO: Why do we need this??? What should be set here?
            return super().__setattr__(name, value)

    def __call__(self, *args: Union[int, str], **kwargs) -> str:
        """
        This function is to handle calls such as `fg(42)`, `bg(102, 49, 42)`, `fg('red')`.
        """

        # Return empty str if object is muted.
        if self.is_muted:
            return ""

        len_args = len(args)

        if len_args == 1:

            # If input is an 8bit color code, run 8bit render function.
            if isinstance(args[0], int):
                return self.eightbit_call(*args, **kwargs)

            # If input is a string, return attribute with the name that matches
            # input.
            else:
                return getattr(self, args[0])

        # If input is an 24bit color code, run 24bit render function.
        elif len_args == 3:
            return self.rgb_call(*args, **kwargs)

        else:
            return ""

    def set_eightbit_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(144)``
        is a Eightbit-call. With this method you can define the render-type for such calls.

        :param rendertype: The new rendertype that is used for Eightbit-calls.
        """
        func: Callable = self.renderfuncs[rendertype]
        self.eightbit_call = func

    def set_rgb_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(10, 42, 255)``
        is a RGB-call. With this method you can define the render-type for such calls.

        :param rendertype: The new rendertype that is used for RGB-calls.
        """
        func: Callable = self.renderfuncs[rendertype]
        self.rgb_call = func

    def set_renderfunc(self, rendertype: Type[RenderType], func: Callable) -> None:
        """
        With this method you can add or replace render-functions for a given register-object:

        :param rendertype: The render type for which the new renderfunc is used.
        :param func: The new render function.
        """
        # Save new render-func in register
        self.renderfuncs.update({rendertype: func})

        # Update style atributes and styles with the new renderfunc.
        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, Style):
                setattr(self, attr_name, val)

    def mute(self) -> None:
        """
        Sometimes it is useful to disable the formatting for a register-object. You can
        do so by invoking this method.
        """
        self.is_muted = True

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, Style):
                setattr(self, attr_name, val)

    def unmute(self) -> None:
        """
        Use this method to unmute a previously muted register object.
        """
        self.is_muted = False

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, Style):
                setattr(self, attr_name, val)

    def as_dict(self) -> Dict[str, str]:
        """
        Export color register as dict.
        """
        items: Dict[str, str] = {}

        for name in dir(self):

            if not name.startswith("_") and isinstance(getattr(self, name), str):

                items.update({name: str(getattr(self, name))})

        return items

    def as_namedtuple(self):
        """
        Export color register as namedtuple.
        """
        d = self.as_dict()
        return namedtuple("StyleRegister", d.keys())(*d.values())

    def copy(self) -> "Register":
        """
        Make a deepcopy of a register-object.
        """
        return deepcopy(self)
