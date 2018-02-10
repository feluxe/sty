
from sty import fg, bg, rs, ef
print('\n\n\n\n')

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:
from sty import render
fg.orange = render.rgb_fg(255, 150, 40)

buf = fg.orange + 'Yay, Im orange.' + fg.rs



print(foo, bar, baz, qux, qui, buf, sep='\n')
