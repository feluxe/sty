"""
The Register class: Sty's heart.
"""
from collections import namedtuple
from typing import Union, Callable, Dict, List, Tuple, Iterable
from copy import deepcopy
from .rendertype import RenderType


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

    def __new__(cls, *rules, value=''):
        cls = str.__new__(cls, value)
        cls.rules = rules
        return cls


def _render_rules(
    renderfuncs,
    rules,
) -> Tuple[str, List[RenderType]]:

    rendered: str = ''
    flattened_rules = []

    if isinstance(rules, RenderType):
        f1: Callable = renderfuncs[type(rules)]
        rendered += f1(*rules.args)
        flattened_rules.append(rules)

    elif isinstance(rules, Style):
        r1, r2 = _render_rules(renderfuncs, rules.rules)
        rendered += r1
        flattened_rules.extend(r2)

    elif isinstance(rules, (list, tuple)):

        for rule in rules:

            r1, r2 = _render_rules(renderfuncs, rule)
            rendered += r1
            flattened_rules.extend(r2)

    else:
        raise ValueError("Parameter 'rules' must be of type Rule or Tuple[Rule].")

    return rendered, flattened_rules


class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are
    created from this class. You can use it to create your own custom registers.
    """

    def __init__(self):
        self.renderfuncs: Dict[RenderType, Callable] = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def __setattr__(self, name: str, value: Union[Style, Tuple[Style]]):

        if isinstance(value, Style):

            if self.is_muted:
                rendered_style = Style(value.rules, value='')
            else:
                rendered, rules = _render_rules(self.renderfuncs, value.rules)
                rendered_style = Style(rules, value=rendered)

            return super().__setattr__(name, rendered_style)
        else:
            return super().__setattr__(name, value)

    def __call__(self, *args, **kwargs) -> str:
        """
        This function is to handle calls such as `fg(42)`, `bg(102, 49, 42)`, `fg('red')`.
        """

        # # Return empty str if object is muted.
        if self.is_muted:
            return ''

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
            return ''

    def set_style(
        self,
        name: str,
        *rules: Union[RenderType, Tuple[RenderType, ...]],
    ) -> None:
        """
        DEPRECATED: This method will be removed in favour of the Style() type.

        With this method, you can add or change styles for a register-object.

        :param name: The field name for the new style.
        """
        setattr(self, name, Style(*rules))

    def get_style(
        self,
        name: str,
    ) -> Tuple[RenderType, ...]:
        """
        DEPRECATED: This method will be removed in favour of the Style() type.

        Retrieve styling rules from a register-object.
        This is useful in case you want to compose new styles out of existing styles.

        :param name: The name of the style for which you want to retrieve the styling rules.
        """
        return getattr(self, name).rules

    def set_eightbit_call(self, rendertype: RenderType) -> None:
        """
        You can call a register-object directly. A call like this ``fg(144)``
        is a Eightbit-call. With this method you can define the render-type for such calls.

        :param rendertype: The new rendertype that is used for Eightbit-calls.
        """
        func: Callable = self.renderfuncs[rendertype]
        self.eightbit_call = func

    def set_rgb_call(self, rendertype: RenderType) -> None:
        """
        You can call a register-object directly. A call like this ``fg(10, 42, 255)``
        is a RGB-call. With this method you can define the render-type for such calls.

        :param rendertype: The new rendertype that is used for RGB-calls.
        """
        func: Callable = self.renderfuncs[rendertype]
        self.rgb_call = func

    def set_renderfunc(self, rendertype: RenderType, func: Callable) -> None:
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

    def mute(self):
        """
        Sometimes it is useful to disable the formatting for a register-object. You can
        do so by invoking this method.
        """
        self.is_muted = True

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, Style):
                setattr(self, attr_name, val)

    def unmute(self):
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

            if not name.startswith("_") and\
               isinstance(getattr(self, name), str):

                items.update({name: str(getattr(self, name))})

        return items

    def as_namedtuple(self):
        """
        Export color register as namedtuple.
        """
        d = self.as_dict()
        return namedtuple('StyleRegister', d.keys())(*d.values())

    def copy(self):
        """
        Make a deepcopy of a register-object.
        """
        return deepcopy(self)

