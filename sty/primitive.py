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
    if name in ['_num_call', '_rgb_call']:
        return True
    elif not name.startswith('_') and name not in ['set']:
        if callable(val):
            return True
    else:
        return False


class Base(object):

    def __init__(self):
        # Create a dict at `self.renderer` to group all render methods.
        setattr(self, 'renderer', dict())

        # Walk over attributes and put render methods into `self.renderer`.
        for name in dir(self):
            value = getattr(self, name)

            if _attr_is_renderer(name, value):
                self.renderer[name] = value

        # Walk over attributes and run render functions on their values.
        for name in dir(self):
            if name and not name.startswith('_') and name != 'renderer':
                value = getattr(self, name)

                if not callable(value):
                    setattr(self, name, value)

    def __call__(self, *args):
        # Invalid call, return empty str.
        if not args or len(args) == 0:
            return ''

        # If input is an 24bit color code, run 24bit render function.
        if _is_args_rgb(*args):
            return self.renderer['_rgb_call'](args)

        # If input is an 8bit color code, run 8bit render function.
        elif _is_args_eightbit(*args):
            return self.renderer['_num_call'](args)

        # If input is a string, return attribute with the name that matches
        # input.
        elif isinstance(args[0], str):
            if hasattr(self, args[0]):
                return getattr(self, args[0])
            else:
                return args[0]

    def __setattr__(self, name, value):
        """
        We store everything in `self.__dict__`
        """
        if name == 'renderer':
            self.__dict__[name] = value
        elif value:
            self.__dict__.update({name: self.renderer[value[0]](value[1])})

    def __getattr__(self, name):
        """
        See: __setattr__() above.
        """
        return self.__dict__[name]

    def set(self, name='', renderer='', *args):
        """
        This method can be used to apply new attributes dynamically.
        """
        setattr(self, name, (renderer, *args))
