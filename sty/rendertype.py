"""
"""


class RenderType:
    args: list = []


class Sgr(RenderType):
    """
    Define SGR styling rule.

    :param num: A SGR number.
    """

    def __init__(self, num: int):
        self.args = [num]


class EightbitFg(RenderType):
    """
    Define Eightbit Forground.

    :param num: Eightbit number.
    """

    def __init__(self, num: int):
        self.args = [num]


class EightbitBg(RenderType):
    """
    Define Eightbit Background.

    :param num: Eightbit number.
    """

    def __init__(self, num: int):
        self.args = [num]


class RgbFg(RenderType):
    """
    Define RGB Foreground.

    :param r: Red.
    :param g: Green.
    :param b: Blue.
    """

    def __init__(self, r: int, g: int, b: int):
        self.args = [r, g, b]


class RgbBg(RenderType):
    """
    Define RGB Background.

    :param r: Red.
    :param g: Green.
    :param b: Blue.
    """

    def __init__(self, r: int, g: int, b: int):
        self.args = [r, g, b]

