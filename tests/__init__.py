from sty import BgRegister, EfRegister, FgRegister, RsRegister


def reset_registers():
    import sty

    sty.ef = EfRegister()
    sty.fg = FgRegister()
    sty.bg = BgRegister()
    sty.rs = RsRegister()

    # return ef, fg, bg, rs


def Example(name):

    reset_registers()

    name = name.title()
    t_len = len(name)
    name = f"{name}\n{t_len*'-'}"

    print(f"\n\n{name}")
