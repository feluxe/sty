"""
The Base class: Sty's heart.
"""
from sty import Rule
from typing import Union, Callable


def _is_args_rgb(*args):
    """
    Check if input matches type: renderer.rgb.
    """
    return len(args) > 1


def _is_args_eightbit(*args):
    """
    Check if input matches type: renderer.eightbit.
    """
    if not args:
        return False

    elif args[0] is 0:
        return True

    elif isinstance(args[0], int):
        return True


def _attr_is_renderer(name, val):
    """
    Check if attribute is a render method.
    """
    if not name.startswith('_') and name not in [
        'set', 'cfg', '_num_call', 'rgb_call'
    ]:
        if callable(val):
            return True
    else:
        return False


class Base(object):

    def __new__(cls):

        cls.is_muted = False
        cls.renderers = dict()
        cls.register = dict()

        return super(Base, cls).__new__(cls)

    def __call__(self, *args, **kwargs):
        """
        You can call the style objects directly, e.g.:
          fg(42)
          bg(102, 49, 42)
        """

        # Return empty str if object is muted.
        if self.is_muted:
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
            if hasattr(self, args[0]):
                return getattr(self, args[0])
            else:
                return args[0]

    def __setattr__(self, name, val):

        if not isinstance(val, (str, Rule, (list, tuple))):

            if name not in [
                'eightbit_call',
                'rgb_call',
                'is_muted',
                'set_rule',
                'set_renderer',
                'renderers',
                'register',
            ]:
                raise TypeError(
                    'New attributes must be of type "sty.Rule" or "str".'
                )

        super(Base, self).__setattr__(name, val)

    def _handle_rule(self, name, val) -> Union[str, Callable]:

        # Save Rule in register.
        self.register[name] = val

        func = self.renderers.get(val.renderer_name)

        if not func:
            raise ValueError(
                "There is no renderer assigned to:", val.renderer_name
            )

        if name in ['eightbit_call', 'rgb_call']:
            rendered = func
        else:
            rendered = func(*val.args, **val.kwargs)

        setattr(self, name, rendered)

        return rendered

    def __getattribute__(self, name):

        is_muted = super(Base, self).__getattribute__('is_muted')

        if is_muted is True:
            if name not in [
                'is_muted',
                'unmute',
                'mute',
                'set_rule',
                'set_renderer',
            ]:
                return ''

        val = super(Base, self).__getattribute__(name)

        # Return strings immediately.
        if isinstance(val, str):
            return val

        # If an attribute contains a 'Rule' object as its value, save the rule
        # in `self.register` and run the renderfunction based on the rule. After
        # that the result from the renderfunction is used as a value for the
        # attribute.
        elif isinstance(val, Rule):
            return self._handle_rule(name, val)

        # Handle list of rules/strings.
        elif isinstance(val, (list, tuple)):
            renderstr = ''

            for r in val:

                if isinstance(r, Rule):
                    renderstr += self._handle_rule(name, r)
                else:
                    renderstr += r

            return renderstr

        else:
            return val

    def set_rule(self, name, rule):

        if isinstance(rule, (str, Rule, list, tuple)):
            setattr(self, name, rule)

        else:
            raise TypeError(
                "Parameter 'rule' needs to be of type 'str', 'sty.Rule', \
                'List[sty.Rule]' or 'Tuple[sty.Rule]'"
            )

    def set_renderer(self, name, func):

        self.renderers[name] = func

        for attr_name, rule in self.register.items():

            if name == rule.renderer_name:
                self.set_rule(attr_name, rule)

    def mute(self):
        self.is_muted = True

    def unmute(self):
        self.is_muted = False
