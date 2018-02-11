from sty import render


class Base(object):

    def __call__(self, *args):
        """
        This happens per default, when you call each one of the primitives as a
        function, e.g.:

        bg('black')
        rs('fg')
        fg(default_values)

        """
        if len(args) == 0:
            return self

        # Load default values, passed in via dict.
        elif args and isinstance(args[0], dict):
            for kv in args[0].items():
                setattr(self, kv[0], kv[1])

        # If input is type string, return object attribute.
        elif isinstance(args[0], str):
            if hasattr(self, args[0]):
                return getattr(self, args[0])
            else:
                return args[0]

    def set(self, name, value):
        setattr(self, name, value)


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


def _color_call(type, *args):
    """
    This happens when a primitive is called directly with a 8bit or 24bit color
    value, e.g.:

    fg(242)
    bg(44,50,124)

    """
    if _is_args_rgb(*args):
        if type == 'fg':
            return render.rgb_fg(*args)
        else:
            return render.rgb_bg(*args)
    elif _is_args_eightbit(*args):
        if type == 'fg':
            return render.eightbit_fg(args[0])
        else:
            return render.eightbit_fg(args[0])


class Fg(Base):
    """
    Handle foreground coloring.
    """

    def __call__(self, *args):
        return Base.__call__(self, *args) or \
               _color_call('fg', *args)


class Bg(Base):
    """
    Handle background coloring.
    """

    def __call__(self, *args):
        return Base.__call__(self, *args) or \
               _color_call('bg', *args)


Ef = Base
Rs = Base
