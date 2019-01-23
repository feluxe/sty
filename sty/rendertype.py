"""
"""


class Render:
    args: list = []


class Sgr(Render):

    def __init__(self, num):
        self.args = [num]


class EightbitFg(Render):

    def __init__(self, num):
        self.args = [num]


class EightbitBg(Render):

    def __init__(self, num):
        self.args = [num]


class RgbFg(Render):

    def __init__(self, r, g, b):
        self.args = [r, g, b]


class RgbBg(Render):

    def __init__(self, r, g, b):
        self.args = [r, g, b]
