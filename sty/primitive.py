def _is_args_rgb(*args):
    """
    Check if input matches type: render.rgb.
    """
    return len(args) > 1


def _is_args_eightbit(*args):
    """
    Check if input matches type: render.eightbit.
    """
    if args:
        if args[0] is 0:
            return True
        if isinstance(args[0], int):
            return True
    return False


def attr_is_renderer(name, val):
    if name in ['_num_call', '_rgb_call']:
        return True
    elif not name.startswith('_') and name not in ['set']:
        if callable(val):
            return True
    else:
        return False


class Base(object):

    def __init__(self):
        # Group assigned render function in dict.
        setattr(self, 'renderer', dict())
        for name in dir(self):
            value = getattr(self, name)
            if attr_is_renderer(name, value):
                self.renderer[name] = value

        # Render values.
        for name in dir(self):
            if name and not name.startswith('_') and name != 'renderer':
                value = getattr(self, name)
                if not callable(value):
                    # setattr(self, name, self.renderer[value[0]](value[1]))
                    # print(name, value)
                    setattr(self, name, value)

    def __call__(self, *args):
        if not args or len(args) == 0:
            return self

        if _is_args_rgb(*args):
            return self.__dict__['renderer']['_rgb_call'](args)

        elif _is_args_eightbit(*args):
            return self.__dict__['renderer']['_num_call'](args)

        # If input is type string, return object attribute.
        elif isinstance(args[0], str):
            if hasattr(self, args[0]):
                return getattr(self, args[0])
            else:
                return args[0]

    def __setattr__(self, name, value):
        if name == 'renderer':
            self.__dict__[name] = {}
        elif value:
            self.__dict__.update(
                {name: self.__dict__['renderer'][value[0]](value[1])})

    def __getattr__(self, name):
        return self.__dict__[name]

    def set(self, name='', renderer='', *args):
        # setattr(self, name, self.renderer[renderer](*args))
        setattr(self, name, (renderer, *args))
