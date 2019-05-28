from .primitive import Base


def mute(*objects: Base) -> None:

    err = ValueError(
        "The mute() method can only be used with objects that inherit "\
        "from the 'Base class'."
    )
    for obj in objects:
        if not isinstance(obj, Base):
            raise err
        obj.mute()


def unmute(*objects: Base) -> None:

    err = ValueError(
        "The unmute() method can only be used with objects that inherit "\
        "from the 'Base class'."
    )
    for obj in objects:
        if not isinstance(obj, Base):
            raise err
        obj.unmute()
