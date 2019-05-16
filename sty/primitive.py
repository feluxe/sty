"""
The Base class: Sty's heart.
"""
from collections import namedtuple
from typing import Union, Callable, Dict, List, Tuple, Iterable
from copy import deepcopy
from .rendertype import Render


def _render_rules(
    renderfuncs,
    rules,
) -> Tuple[str, List[Render]]:

    rendered: str = ''
    flattened_rules = []

    if isinstance(rules, Render):
        f1: Callable = renderfuncs[type(rules)]
        rendered += f1(*rules.args)
        flattened_rules.append(rules)

    elif isinstance(rules, (list, tuple)):

        for rule in rules:

            r1, r2 = _render_rules(renderfuncs, rule)
            rendered += r1
            flattened_rules.extend(r2)

    else:
        raise ValueError(
            "Parameter 'rules' must be of type Rule or Tuple[Rule]."
        )

    return rendered, flattened_rules


class Base:

    def __init__(self):

        self.renderfuncs: Dict[Render, Callable] = {}
        self.styles: Dict[str, Tuple[Render, ...]] = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def __call__(self, *args, **kwargs) -> str:
        """
        You can call the style objects directly, e.g.:
            fg(42)
            bg(102, 49, 42)
            fg('red')
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
        *rules: Union[Render, Tuple[Render, ...]],
    ) -> None:

        rendered, flattened_rules = _render_rules(self.renderfuncs, rules)

        # Apply rendered style (str) to attribute:
        if self.is_muted:
            setattr(self, name, '')
        else:
            setattr(self, name, rendered)

        # Add style rules to internal style register:
        self.styles[name] = tuple(flattened_rules)

    def get_style(
        self,
        name: str,
    ) -> Tuple[Render, ...]:
        return self.styles[name]

    def set_eightbit_call(self, rendertype: Render) -> None:

        func: Callable = self.renderfuncs[rendertype]
        self.eightbit_call = func

    def set_rgb_call(self, rendertype: Render) -> None:

        func: Callable = self.renderfuncs[rendertype]
        self.rgb_call = func

    def set_renderfunc(self, rendertype: Render, func: Callable) -> None:

        # Save new render-func in register
        self.renderfuncs.update({rendertype: func})

        # Update style atributes and styles with the new renderfunc.
        for attr_name, rules in self.styles.items():
            for rule in rules:
                if type(rule) == rendertype:
                    self.set_style(attr_name, *rules)
                    break

    def mute(self):

        self.is_muted = True

        for name in dir(self):

            if not name.startswith("_") and\
               isinstance(getattr(self, name), str):

                setattr(self, name, '')

    def unmute(self):

        self.is_muted = False

        for name, rules in self.styles.items():
            self.set_style(name, *rules)

    def as_dict(self) -> Dict[str, str]:
        """
        Export color register as dict.
        """
        items: Dict[str, str] = {}

        for name in dir(self):

            if not name.startswith("_") and\
               isinstance(getattr(self, name), str):

                items.update({name: getattr(self, name)})

        return items

    def as_namedtuple(self):
        """
        Export color register as namedtuple.
        """
        d = self.as_dict()
        return namedtuple('ColorRegister', d.keys())(*d.values())

    def copy(self):
        return deepcopy(self)
