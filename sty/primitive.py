"""
The Base class: Sty's heart.
"""
from collections import namedtuple
from typing import Union, Callable, Dict, List, Tuple, Iterable
from copy import deepcopy
from .rendertype import Render


def _is_args_rgb(*args) -> bool:
    """
    Check if input matches type: renderer.rgb.
    """
    return len(args) > 1


def _is_args_eightbit(*args) -> bool:
    """
    Check if input matches type: renderer.eightbit.
    """
    if not args:
        return False

    elif args[0] is 0:
        return True

    elif isinstance(args[0], int):
        return True
    else:
        return False


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


class Base(dict):

    def __new__(cls):

        cls.renderfuncs: Dict[Render, Callable] = {}
        cls.styles: Dict[str, Tuple[Render, ...]] = {}

        return super(Base, cls).__new__(cls)

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)

    def __setattr__(self, k, v):
        try:
            object.__getattribute__(self, k)
        except AttributeError:
            self[k] = v
        else:
            object.__setattr__(self, k, v)

    def __delattr__(self, k):
        try:
            object.__getattribute__(self, k)
        except AttributeError:
            del self[k]
        else:
            object.__delattr__(self, k)

    def __call__(self, *args, **kwargs) -> str:
        """
        You can call the style objects directly, e.g.:
            fg(42)
            bg(102, 49, 42)

        """

        # Return empty str if object is muted.
        if self.get('is_muted'):
            return ''

        # Invalid call, return empty str.
        elif not args or len(args) == 0:
            return ''

        # If input is an 24bit color code, run 24bit render function.
        elif _is_args_rgb(*args):
            func = getattr(self, 'rgb_call')
            return func(*args, **kwargs)

        # If input is an 8bit color code, run 8bit render function.
        elif _is_args_eightbit(*args):
            func = getattr(self, 'eightbit_call')
            return func(*args, **kwargs)

        # If input is a string, return attribute with the name that matches
        # input.
        elif isinstance(args[0], str):
            return getattr(self, args[0])

        else:
            return ''

    def set_style(
        self,
        name: str,
        *rules: Union[Render, Tuple[Render, ...]],
    ) -> None:

        rendered, flattened_rules = _render_rules(self.renderfuncs, rules)

        # Apply rendered style (str) to attribute:
        if self.get('is_muted'):
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
        setattr(self, 'eightbit_call', func)

    def set_rgb_call(self, rendertype: Render) -> None:

        func: Callable = self.renderfuncs[rendertype]
        setattr(self, 'rgb_call', func)

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

        self['is_muted'] = True

        for k, v in self.items():
            if isinstance(v, str):
                self.update({k: ''})

    def unmute(self):

        self['is_muted'] = False

        for name, rules in self.styles.items():
            self.set_style(name, *rules)

    def as_dict(self) -> Dict[str, str]:
        """
        Export color register as dict.
        """
        items: Dict[str, str] = {}

        for k, v in self.items():

            if type(v) is str:
                items.update({k: v})

        return items

    def as_namedtuple(self):
        """
        Export color register as namedtuple.
        """
        d = self.as_dict()
        return namedtuple('ColorRegister', d.keys())(*d.values())

    def copy(self):
        return dict(self)