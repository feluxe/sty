"""
"""


class Render:
    args: list = []


class Sgr(Render):
    """
    Use this type to set SGR numbers.

    :param num: A SGR number.
    """

    def __init__(self, num: int):
        self.args = [num]


class EightbitFg(Render):
    """
    Use this type to set Eightbit Foregrounds.

    :param num: Eightbit number.
    """

    def __init__(self, num: int):
        self.args = [num]


class EightbitBg(Render):
    """
    Use this type to set Eightbit Backgrounds.

    :param num: Eightbit number.
    """

    def __init__(self, num: int):
        self.args = [num]


class RgbFg(Render):
    """
    Use this type to set RGB Foregrounds.

    :param r: Red.
    :param g: Green.
    :param b: Blue.
    """

    def __init__(self, r: int, g: int, b: int):
        self.args = [r, g, b]


class RgbBg(Render):
    """
    Use this type to set RGB Backgrounds.

    :param r: Red.
    :param g: Green.
    :param b: Blue.
    """

    def __init__(self, r: int, g: int, b: int):
        self.args = [r, g, b]
