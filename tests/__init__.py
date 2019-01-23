from sty import EfRegister, FgRegister, BgRegister, RsRegister


def Example(name):
    name = name.title()
    t_len = len(name)
    name = f"{name}\n{t_len*'-'}"

    print(f"\n\n{name}")


def reset_registers():
    ef = EfRegister()
    fg = FgRegister()
    bg = BgRegister()
    rs = RsRegister()

    return ef, fg, bg, rs

