"""
The Base class: Sty's heart.
"""
from sty import Rule


def _is_args_rgb(*args):
    """
    Check if input matches type: renderer.rgb.
    """
    return len(args) > 1


def _is_args_eightbit(*args):
    """
    Check if input matches type: renderer.eightbit.
    """
    if args:
        if args[0] is 0:
            return True
        if isinstance(args[0], int):
            return True
    return False


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

        # Return empty str if object is muted.
        if self.is_muted:
            return ''

        # Invalid call, return empty str.
        if not args or len(args) == 0:
            return ''

        # If input is an 24bit color code, run 24bit render function.
        if _is_args_rgb(*args):
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

        if type(val) not in [str, Rule]:

            if name not in [
                'eightbit_call', 'rgb_call', 'is_muted', 'set_rule',
                'set_renderer', 'renderers', 'register'
            ]:
                raise TypeError(
                    'New attributes must be of type "sty.Rule" or "str".'
                )

        super(Base, self).__setattr__(name, val)

    def __getattribute__(self, name):

        is_muted = super(Base, self).__getattribute__('is_muted')

        if is_muted is True:
            if name not in [
                'is_muted', 'unmute', 'mute', 'set_rule', 'set_renderer'
            ]:
                return ''

        val = super(Base, self).__getattribute__(name)

        # Return strings immediately.
        if type(val) == str:
            return val

        # If an attribute contains a 'Rule' object as its value, save the rule
        # in `self.register` and run the renderfunction based on the rule. After
        # that the result from the renderfunction is used as a value for the
        # attribute.
        if type(val) == Rule:
            # TODO: Add ability to assign multiple Rules via Iterable.

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

        else:

            return val

    def set_rule(self, name, rule):

        if type(rule) != Rule:
            raise TypeError("Parameter 'rule' needs to be of type 'sty.Rule'")

        setattr(self, name, rule)

    def set_renderer(self, name, func):

        self.renderers[name] = func

        for attr_name, rule in self.register.items():

            if name == rule.renderer_name:
                self.set_rule(attr_name, rule)

    def mute(self):
        self.is_muted = True

    def unmute(self):
        self.is_muted = False
