from timeit import default_timer as timer

from sty import bg, ef, fg, rs


def test_attr_access(reps):

    print("Test Attribute Access: ", end="")
    start = timer()

    for i in range(reps):
        f = fg.blue + "" + rs.fg
        b = bg.green + "" + rs.bg
        e = ef.underl + "" + rs.underl

    end = timer()
    print(end - start)


def test_dynamic_attr_access(reps):

    print("Test Dynamic Attribute Access: ", end="")
    start = timer()

    for i in range(reps):
        f = fg("blue") + "" + rs("fg")
        b = bg("green") + "" + rs("bg")
        e = ef("underl") + "" + rs("underl")

    end = timer()
    print(end - start)


test_attr_access(10000000)
test_dynamic_attr_access(1000000)
