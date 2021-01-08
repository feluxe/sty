from sty import bg, ef, fg, rs

GROUPS = [
    ["black", "da_grey", "grey", "li_grey", "white"],
    ["da_red", "red", "li_red"],
    ["da_green", "green", "li_green"],
    ["da_yellow", "yellow", "li_yellow"],
    ["da_blue", "blue", "li_blue"],
    ["da_magenta", "magenta", "li_magenta"],
    ["da_cyan", "cyan", "li_cyan"],
]


def sgr_fg():
    output = ""
    for row_num in range(0, len(GROUPS[0])):
        line = ""
        for group in GROUPS:
            try:
                name = group[row_num]
            except IndexError:
                continue
            line += fg(name) + " " + name.rjust(12) + rs.all
        output += line + "\n"

    return "\nSGR_FG:\n-------\n" + output


def sgr_bg():
    output = ""
    for row_num in range(0, len(GROUPS[0])):
        line = ""
        for group in GROUPS:
            try:
                name = group[row_num]
            except IndexError:
                continue
            fore = fg.da_grey if name in ["white", "li_grey"] else ""
            line += fore + bg(name) + " " + name.rjust(12) + rs.all
        output += line + "\n"

    return "\nSGR_BG:\n-------\n" + output


def eightbit(kind):

    func = fg if kind == "fg" else bg
    title = "8bit_FG" if kind == "fg" else "8bit_BG"

    items = [func(num) + str(num).ljust(3) for num in range(0, 255)]
    items.insert(16, rs.all + "\n")
    items.insert(51 + 2, rs.all + "\n")
    items.insert(87 + 3, rs.all + "\n")
    items.insert(123 + 4, rs.all + "\n")
    items.insert(159 + 5, rs.all + "\n")
    items.insert(195 + 6, rs.all + "\n")
    items.insert(231 + 7, rs.all + "\n")

    line = "\n" + title + "\n-------\n " + " ".join(items) + rs.all

    return line


print("\n\nDEMO:\n")
print(
    "================================================================================\n"
)
print(sgr_fg())
print(sgr_bg())
print(eightbit("fg"))
print(eightbit("bg"))
print(
    "\n24bit: I skip the 24-bit chart for now. Please add one to charts.py if you like."
)
