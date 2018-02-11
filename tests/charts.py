from sty import ef, fg, bg, rs, Fg, Bg

# SGR Chart
fg = Fg()
bg = Bg()

print('\n\nDEMO:\n')

names = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'li_black',
    'li_red',
    'li_green',
    'li_yellow',
    'li_blue',
    'li_magenta',
    'li_cyan',
    'li_white',
]


def sgr_fg(names):
    items = [fg(name) + ' ' + name.ljust(10) for name in names]
    items.insert(8, rs.fg + '\n')
    line = '\nSGR_FG:\n-------\n' + ''.join(items) + rs.fg
    return line


def sgr_bg(names):
    items = [bg(name) + ' ' + name.ljust(10) for name in names]
    items.insert(8, rs.bg + '\n')
    line = '\nSGR_BG:\n-------\n' + ''.join(items) + rs.bg
    return line


def eightbit(kind):
    func = fg if kind == 'fg' else bg
    title = '8bit_FG' if kind == 'fg' else '8bit_BG'

    items = [
        func(num) + str(num).ljust(3)
        for num
        in range(0, 255)
    ]
    items.insert(16, rs.all + '\n')
    items.insert(51 + 2, rs.all + '\n')
    items.insert(87 + 3, rs.all + '\n')
    items.insert(123 + 4, rs.all + '\n')
    items.insert(159 + 5, rs.all + '\n')
    items.insert(195 + 6, rs.all + '\n')
    items.insert(231 + 7, rs.all + '\n')

    # items_br = [item for i, item in enumerate(items) if i == 1 ]
    line = '\n' + title + '\n-------\n ' + ' '.join(items) + rs.all
    return line



print(sgr_fg(names))
print(sgr_bg(names))
print(eightbit('fg'))
print(eightbit('bg'))
print('\n24bit\n------ I skip the 24-bit chart for now. Please add one to charts.py if you like.')
