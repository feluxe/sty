"""
"""


class Rule:

    def __init__(self, renderer_name, *args, **kwargs):
        self.renderer_name = renderer_name
        self.args = args
        self.kwargs = kwargs


def mute(*objects):
    for obj in objects:
        if hasattr(obj, 'mute') and callable(obj.mute):
            obj.mute()

def unmute(*objects):
    for obj in objects:
        if hasattr(obj, 'unmute') and callable(obj.mute):
            obj.unmute()



from sty.register import EfRegister, FgRegister, BgRegister, RsRegister, Render
from sty.primitive import Base

ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()
