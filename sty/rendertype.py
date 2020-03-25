"""
"""


class RenderType:
    args: list = []


class Sgr(RenderType):
    """
    Define SGR styling rule.

    More info about SGR parameters: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR

    :param num: A SGR number.
    """

    def __init__(self, num: int):
        self.args = [num]


class EightbitFg(RenderType):
    """
    Define Eightbit Foreground.

    More info about 8-bit terminal colors: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit

    :param num: Eightbit number.
    """

    def __init__(self, num: int):
        self.args = [num]


class EightbitBg(RenderType):
    """
    Define Eightbit Background.

    More info about 8-bit terminal colors: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit

    :param num: Eightbit number.
    """

    def __init__(self, num: int):
        self.args = [num]


class RgbFg(RenderType):
    """
    Define RGB Foreground.

    More info about 24-bit terminal colors: https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit

    :param r: Red.
    :param g: Green.
    :param b: Blue.
    """

    def __init__(self, r: int, g: int, b: int):
        self.args = [r, g, b]


class RgbBg(RenderType):
    """
    Define RGB Background.

    More info about 24-bit terminal colors: https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit

    :param r: Red.
    :param g: Green.
    :param b: Blue.
    """

    def __init__(self, r: int, g: int, b: int):
        self.args = [r, g, b]

