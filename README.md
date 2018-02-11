
# sty

<img src="assets/charts.png" alt="charts" />  

## Description

Simple, flexible and extensible string styling for your terminal.

Sty has no dependencies and consists of only ~200 LOC (including empty lines and comments).


## Getting Started

```
pip install sty
```

You can import sty like this:
 
```python
import sty
```

However, if you need to style a lot of stuff, you might consider importing the 
style objects directly, like this:

```python
from sty import fg, bg, ef, rs
```

*Sty* all the strings!

```python
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
```

output:
 
<img src="assets/example_so.png" alt="example_so" />  


## A little Walkthrough

sty provides a bunch of tiny, but flexible primitives that can be used for styling your strings: 

* `ef` (effects)
* `fg` (foreground)
* `bg` (background)
* `rs` (reset).

Each primitive carries a default selection of attributes ([list-of-effects](#list-of-default-effects), [list-of-colors](#list-of-default-colors)), which you can select like this:

```python
ef.italic
fg.blue
bg.green
rs.all
```

Or like this, which is nice in case you need to dynamically select attributes:

```python
ef('italic') + 'Italic text.' + rs.italic
fg('blue') + 'Blue text.' + rs.fg
bg(randint(0,254)) + 'Random colored bg' + rs.bg
```

`fg` and `bg` are special in the way that they allow you to select 8bit and 24bit colors directly:

```python
a = fg(196) + 'This is red text' + rs.fg  # select an 8bit color directly.
b = bg(50, 255, 50) + 'Text with green bg' + rs.bg  # select a 24bit rgb color directly.
```
  
Sty allows you to change or extend the default attributes as you like, using the [render functions](#list-of-renderers):

```python
from sty import render

ef.italic = render.sgr(1)  # ef.italic now renders bold text.
fg.red = render.sgr(32)  # fg.red renders green text from now on.
fg.blue = render.eightbit_bg(111)  # fg.blue renders blue text from now on (using an 8bit color code).
fg.my_new_item = render.eightbit_fg(130)  # Create a new item that renders brown text.
bg.green = render.rgb(0, 128, 255)  # bg.green renders blue text from now on (using a 24bit rgb code).
rs.all = render.sgr(24)  # rs.all only resets the underline effect from now on.
```

In case you need to set attributes dynamically you can use the `set` method:

```python
my_color_name = 'special_teal'

fg.set(my_color_name, render.eightbit_fg(51)) 

a = fg.special_teal + 'This is teal text.' + fg.rs
```


If you want to set a larger register of custom attributes, inheriting from the default register might be more convenient:

```python
from sty.register import DefaultFg 
from sty.render import sgr, rgb_fg


# Extend default Fg register.
class MyFgRegister(DefaultFg):
    black = sgr(31)
    red = sgr(34)
    orange = rgb_fg(10, 40, 133)

fg = MyFgRegister()
```

You can also start your own register from scratch by inheriting the clean base classes:

```python
from sty.primitive import Fg
from sty.render import sgr, rgb_fg

# Create a fg register from scratch.
class MyFgRegister(Fg):
    black = sgr(31)
    red = sgr(34)
    orange = rgb_fg(10, 40, 133)

fg = MyFgRegister()
```

I think this is all you need to know. Check out the documentation or the codebase for more detail or feel free to create an issu and ask. Have fun! :D


    
## Documentation:

* [List of default effects](#list-of-default-effects)
* [List of default colors](#list-of-default-colors)
* [Italic](#italic)
* [Bold](#bold)
* [Underline](#underline)
* [Coloring by name](#string-coloring-by-name)
* [Coloring with 8bit](#string-coloring-using-8-bit-numbers)
* [Coloring with 24bit (rgb, truecolor)](#string-coloring-using-24-bit-rgb-values)
* [Customizing](#customizing-sty)
* [Terminal Support](#terminal-support)

### List of Renderers

The renderfunctions are stored in `sty.render`.

| Render Function      | Description |
| -------------------- | ------------- |
| sgr                  | Render [SGR codes ([wikipedia#SGR][SGR])] (works for fg-colors, bg-colors and effects) |
| eightbit_fg          | Render foreground using [8bit color codes (wikipedia#8bit)][8bit] |
| eightbit_bg          | Render background using 8bit color codes |
| rgb_fg               | Render foreground using [16bit (RGB) color codes (wikipedia#24bit)][24bit] |
| rgb_bg               | Render background using 16bit (RGB) color codes |

### List of default effects

These are the default attributes for the `ef` object.

More info: [wikipedia#SGR][SGR]

| Effect               | Description | Default Renderer |
| -------------------- | ------------- | --------------|
| bold (alias b)       | Bold or increased intensity  | sgr(1) |
| faint                | Decreased intensity  | sgr(2) |
| italic (alias i)     | Italic.. | sgr(3) |
| underline (alias u)  | Underline..| sgr(4) |
| blink_slow           | Blink less than 150 per minute | sgr(5) |
| blink_fast           | Blink more than 150 per minute | sgr(6) |
| reverse              | Reverse fore- and background | sgr(7) |
| conceal              | Conceal/Hide | sgr(8) |
| strike               | Striketrhough | sgr(9) |



### List of default colors

#### Foreground

The default colors for the `fg` object.

These are most widely supported. (using sgr codes).

| normal   | Default Renderer |
| -------- | ---------------- |
| black    | sgr(30)          |
| red      | sgr(31)          |
| green    | sgr(32)          |
| yellow   | sgr(33)          |
| blue     | sgr(34)          |
| magenta  | sgr(35)          |
| cyan     | sgr(36)          |
| white    | sgr(37)          |


These are less widely supported. (using less common set of sgr codes).

| light       | Default Renderer |
| ----------- | ---------------- |
| li_black    | sgr(90)          |
| li_red      | sgr(91)          |
| li_green    | sgr(92)          |
| li_yellow   | sgr(93)          |
| li_blue     | sgr(94)          |
| li_magenta  | sgr(95)          |
| li_cyan     | sgr(96)          |
| li_white    | sgr(97)          |


These are even less widely supported. (using 8bit color codes).

| dark        | Default Renderer |
| ----------- | ---------------- |
| da_black    | eightbit_fg(0)   |
| da_red      | eightbit_fg(88)  |
| da_green    | eightbit_fg(22)  |
| da_yellow   | eightbit_fg(58)  |
| da_blue     | eightbit_fg(18)  |
| da_magenta  | eightbit_fg(89)  |
| da_cyan     | eightbit_fg(23)  |
| da_white    | eightbit_fg(249) |


#### Background

The default colors for the `bg` object.

These are most widely supported. (using sgr codes).

| normal   | Default Renderer |
| -------- | ---------------- |
| black    | sgr(40)          |
| red      | sgr(41)          |
| green    | sgr(42)          |
| yellow   | sgr(43)          |
| blue     | sgr(44)          |
| magenta  | sgr(45)          |
| cyan     | sgr(46)          |
| white    | sgr(47)          |


These are less widely supported. (using less common set of sgr codes).

| light       | Default Renderer |
| ----------- | ---------------- |
| li_black    | sgr(100)          |
| li_red      | sgr(101)          |
| li_green    | sgr(102)          |
| li_yellow   | sgr(103)          |
| li_blue     | sgr(104)          |
| li_magenta  | sgr(105)          |
| li_cyan     | sgr(106)          |
| li_white    | sgr(107)          |

These are even less widely supported. (using 8bit color codes).

| dark        | Default Renderer |
| ----------- | ---------------- |
| da_black    | eightbit_bg(0)   |
| da_red      | eightbit_bg(88)  |
| da_green    | eightbit_bg(22)  |
| da_yellow   | eightbit_bg(58)  |
| da_blue     | eightbit_bg(18)  |
| da_magenta  | eightbit_bg(89)  |
| da_cyan     | eightbit_bg(23)  |
| da_white    | eightbit_bg(249) |



### Italic

```python
a = ef.italic + 'Italic.' + rs.italic

# Shorthand version:
b = ef.i + fg.blue + 'Italic.' + rs.i + ' Not italic but blue.' + rs.fg

print(a, b, sep='\n')
```

<img src="assets/italic.png" alt="italic" />  

### Bold

```python
a = ef.bold + 'Bold.' + rs.bold

# Shorthand version:
b = ef.b + 'Bold.' + rs.b + fg.li_yellow + ' Not bold but yellow.' + rs.fg

print(a, b, sep='\n')
```

<img src="assets/bold.png" alt="bold" />  

### Underline

```python
a = ef.underline + 'Underlined.' + rs.underline

# Shorthand version:
b = ef.u + 'Underlined.' + rs.u + fg.green + ' Not underlined but green.' + rs.fg

print(a, b, sep='\n')
```

<img src="assets/underline.png" alt="underline" />  

#### TODO

Add examples for, strike, blink, etc..


### String coloring by name

```python
a = fg.blue + 'I have a blue foreground.' + rs.fg
b = bg.li_cyan + 'I have a light cyan background' + rs.bg
c = fg.red + bg.green + 'I have a red fg and green bg.' + rs.all

print(a, b, c, sep='\n')
```

<img src="assets/color_by_name.png" alt="color_by_name" />  



### String coloring using 8-bit numbers

```python
a = fg(34) + 'I have a green foreground.' + rs.fg
b = bg(133) + 'I have a pink background' + rs.bg
c = fg(226) + bg(19) + 'I have a light yellow fg and dark blue bg.' + rs.all

print(a, b, c, sep='\n')
```

<img src="assets/8bit.png" alt="8bit" />  
    
Link: [wikipedia#8bit][8bit]


### String coloring using 24-bit RGB values

```python
a = fg(10, 255, 10) + 'I have a green foreground.' + rs.fg
b = bg(255, 150, 50) + 'I have an orange background' + rs.bg
c = fg(90, 90, 90) + bg(32, 32, 32) + 'Grey fg and dark grey bg.' + rs.all

print(a, b, c, sep='\n')
```

<img src="assets/24bit.png" alt="24bit" />  

Link: [wikipedia#24bit][24bit]


### Customizing sty

If you want to change/add attributes to your sty objects (fg, bg, ef, rs) you can use a dict and the rendering methods provided by `sty.render` to do so:

```python
custom_colors= dict(
    orange=render.eightbit_fg(214),  # Add 'orange' to fg (using 8-bit code)
    green=render.rgb_fg(255, 0, 0),  # Modify value for 'green' (using rgb code)
    blue=render.sgr(95),  # Turn 'blue' into magenta (using sgr code)
)

a = fg.green + 'I have a green foreground.' + rs.fg
b = fg.blue + 'I have a blue foreground.' + rs.fg

fg(custom_colors)

c = fg.green + 'I have a red foreground now.' + rs.fg
d = fg.blue + 'I have a magenta foreground now.' + rs.fg
e = fg.orange + 'I was set orange by a newly registered color name.' + rs.fg

print(a, b, c, d, e, sep='\n')
```

<img src="assets/customizing.png" alt="customizing" />  

As you see, there are three types of renders:

* `sgr` This one is used to generate ansi strings for SGR "Select Graphic Rendition" codes. These are most widely supported. They can be used for colors, as well as styling (italic, bold, blink, etc.). [wikipedia#SGR][SGR]
* `eigthbit`: This one is used to generate ansi strings for 8-bit colors. [wikipedia#8bit][8bit]
* `rgb`: This one is used to generate ansi strings for 24-bit colors. [wikipedia#24bit][24bit]

## Terminal Support

This was initially tested on Arch Linux using 'Termite' terminal. If you have issues with your setup, please leave an issue. If sty works fine on your setup, feel free to add your setup to the list below:

#### Termite on Linux

| Option        | Status  |
| ------------- | ------- |
| SGR:          | Ok!     |
| 8-bit color:  | Ok!     |
| 24-bit color: | Ok!     |

If you want to support the widest range of terminals, you should stick to the sgr renderer. The default attributes in all sty objects (`fb`,`bg`,`ef`,`rs`) use `sgr` values exclusively.


[SGR]: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
[256]: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
[8bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
[16bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit
