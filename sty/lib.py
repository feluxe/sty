from .primitive import Register


def mute(*objects: Register) -> None:
    """
    Use this function to mute multiple register-objects at once.

    :param objects: Pass multiple register-objects to the function.
    """
    err = ValueError(
        "The mute() method can only be used with objects that inherit "\
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.mute()


def unmute(*objects: Register) -> None:
    """
    Use this function to unmute multiple register-objects at once.

    :param objects: Pass multiple register-objects to the function.
    """
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "\
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.unmute()

