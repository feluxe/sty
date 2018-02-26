
# sty

<img src="assets/charts.png" alt="charts" />  

## Description

Simple, flexible and extensible string styling for your terminal. Supports 3/4bit, 8bit and 24bit (truecolor, rgb) colors. Should work on most Unix platfroms with most terminals. Recent versions of Windows 10 should work with this as well. 

If you run into compatibility problems with sty, please file an issue!

Sty has no dependencies and consists of only ~250 LOC (including empty lines and comments).

## Goal

The idea is to provide Python with a little string styling markup, which is decoupled from color palettes and terminal implementations.

Sty comes with default color palettes and renderers, but you can easily replace/customize them with new ones, without touching the markup.

## Requirements

Sty requires Python `>= 3.6`


## Getting Started

Install:

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

#### *Sty* all the strings!

```python
foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:

fg.orange = ('rgb', (255, 150, 50))

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(foo, bar, baz, qux, qui, buf, sep='\n')
```

output:
 
<img src="assets/example_so.png" alt="example_so" />  


#### A quick look at the primitives:

sty provides a bunch of tiny, but flexible primitives that can be used to style your strings: 

* `ef` (effects)
* `fg` (foreground)
* `bg` (background)
* `rs` (reset).

Each primitive carries a default selection of attributes ([list-of-effects](#list-of-default-effects), [list-of-colors](#list-of-default-colors), [list-of-resets](#list-of-default-reset-attributes)), which you can select like this:

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

I think this is all you need to know to get going. Check out the documentation or the codebase for more detail or feel free to create an issue and ask. Have fun! :D


    
# Documentation:

* [Effects](#effects)
  * [List of default effects](#list-of-default-effects)
  * [Italic](#italic)
  * [Bold](#bold)
  * [Underline](#underline)
* [Colors](#colors)
  * [List of default colors](#list-of-default-colors)
    * [Foreground](#foreground)
    * [Background](#background)
  * [Coloring by name](#coloring-by-name)
  * [Coloring with 8bit codes](#coloring-with-8-bit-codes)
  * [Coloring with 24bit codes](#coloring-with-24bit-codes)
* [Reset](#reset)
  * [List of default reset attributes](#list-of-default-reset-attributes)
* [Renderers](#renderers)
  * [List of renderers](#list-of-renderers) 
* [Customization](#customization)
  * [Direct attribute customization](#direct-attribute-customization)
  * [Dynamic attribute customization](#dynamic-attribute-customization)
  * [Extending the default registers](#extending-the-default-registers)
  * [Create a custom register from scratch](#create-a-custom-register-from-scratch)
* [Terminal Support](#terminal-support)

## Effects

### List of default effects

These are the default attributes for the `ef` object.

More info: [wikipedia:SGR][SGR]

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

> TODO: Add examples for, strike, blink, etc..

## Colors

### List of default colors

#### Foreground

More info:  [wikipedia:3/4bit colors][3_4bit], [wikipedia:8bit colors][8bit], [wikipedia:24bit colors][24bit].

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


### Coloring by name

```python
a = fg.blue + 'I have a blue foreground.' + rs.fg
b = bg.li_cyan + 'I have a light cyan background' + rs.bg
c = fg.red + bg.green + 'I have a red fg and green bg.' + rs.all

print(a, b, c, sep='\n')
```

<img src="assets/color_by_name.png" alt="color_by_name" />  


### Coloring with 8-bit codes

Link: [wikipedia:8bit][8bit]

```python
a = fg(34) + 'I have a green foreground.' + rs.fg
b = bg(133) + 'I have a pink background' + rs.bg
c = fg(226) + bg(19) + 'I have a light yellow fg and dark blue bg.' + rs.all

print(a, b, c, sep='\n')
```

<img src="assets/8bit.png" alt="8bit" />  


### Coloring with 24bit codes

Link: [wikipedia:24bit][24bit]

```python
a = fg(10, 255, 10) + 'I have a green foreground.' + rs.fg
b = bg(255, 150, 50) + 'I have an orange background' + rs.bg
c = fg(90, 90, 90) + bg(32, 32, 32) + 'Grey fg and dark grey bg.' + rs.all

print(a, b, c, sep='\n')
```

<img src="assets/24bit.png" alt="24bit" />  


## Reset

The reset object `rs` can be used to reset previously applied styles.

Link: [wikipedia:SGR][SGR]

### List of default reset attributes

These are the default attributes for the `rs` object:

| Reset                | Default Renderer |
| -------------------- | ---------------- |
| all                  | sgr(0)           |
| fg                   | sgr(39)          |
| bg                   | sgr(49)          |
| bold (alias b)       | sgr(21)          |
| faint                | sgr(22)          |
| italic (alias i)     | sgr(23)          |
| underline (alias u)  | sgr(24)          |
| blink                | sgr(25)          |
| conceal              | sgr(28)          |
| strike               | sgr(29)          |


## Renderers

The default render functions are stored in `sty.render`.

### List of Renderers

| Render Function      | Description |
| -------------------- | ------------- |
| sgr                  | Render [SGR codes (wikipedia:SGR)][SGR] (works for fg-colors, bg-colors and effects) |
| eightbit_fg          | Render foreground using [8bit color codes (wikipedia:8bit)][8bit] |
| eightbit_bg          | Render background using 8bit color codes |
| rgb_fg               | Render foreground using [24bit (RGB) color codes (wikipedia:24bit)][24bit] |
| rgb_bg               | Render background using 24bit (RGB) color codes |


## Customization
 
Sty allows you to change or extend the default registers as you like. You can also create a complete new register. More on these things in the following chapters.

### Direct attribute customization

You can change and add attributes directly like this:

```python

ef.italic = ('sgr', 1)  # ef.italic now renders bold text.
fg.red = ('sgr', 32)  # fg.red renders green text from now on.
fg.blue = ('eightbit', 111)  # fg.blue renders blue text from now on (using an 8bit color code).
fg.my_new_item = ('eightbit', 130)  # Create a new item that renders brown text.
bg.green = ('rgb', (0, 128, 255))  # bg.green renders blue text from now on (using a 24bit rgb code).
rs.all = ('sgr', 24)  # rs.all only resets the underline effect from now on.
```

The first part of the tuple describes, which renderer should be used (`sgr`, `eightbit`, `rgb`), the second part is the argument with which the render function is called. As you see, the `sgr` renderer requires an `int` and the `rgb` renderer requires a `Tuple[int, int, int]`.


### Dynamic attribute customization

In case you need to set attributes dynamically you can use the `set` method:

```python
my_color_name = 'special_teal'

fg.set(my_color_name, 'eightbit', 51) 

a = fg.special_teal + 'This is teal text.' + fg.rs
```

### Extending the default registers

If you want to set a larger register of custom attributes, inheriting from the default registers might be more convenient:

```python
from sty.register import FgRegister


# Extend default Fg register.
class MyFgRegister(FgRegister):
    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))


fg = MyFgRegister()

a = fg.orange + 'This is orange text.' + rs.fg

```

I think this might be useful in case you want to provide your project with custom versions of `fg`, `bg`, `ef`, `rs`. You could for example create your own `style.py` and import your custom style objects from there: `from myproj.style import fg, bg, ef, rs`.


### Replace or add renderers

This is a little more advanced, but you can change or add *renderers* to your *registers*, by adding them as class methods to your register class.

The following example replaces the default rgb renderer for the `fg` (foreground) object, with the one from the `bg` (background) Register. The result is that the `fg` object renders `'rgb'` values not as foreground colors, but as background colors. Of cause this doesn't make sense; it's just a simple demonstration.

```python
from sty.register import FgRegister


# RGB background render function.
def rgb_bg(rgb: tuple):
    return f'\x1b[48;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m'


# Extend default Fg register.
class MyFgRegister(FgRegister):

    def rgb(self, *args):
        return rgb_bg(*args)

    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))


fg = MyFgRegister()

a = fg.orange + 'I have a orange background instead of an orange fg.'
```

The class method name of the renderer can be used for the attribute values. E.g. if the name of the renderer method is `foo`, you can set an attribute like this to access the renderer: `red = ('foo' , 24)`.

This is exactly how the default registers of sty are created (see: `sty.register` package). You can easily use these building blocks to extend/customize the default registers or create new registers from scratch.

There is one speciality. Remember that you can call the `fg` and `bg` object like this `fg(140)` and this `fg(100, 244, 50)`? By default `fg(140)` uses the default `eightbit` renderer and `fg(100, 244, 50)` uses the default `rgb` renderer to handle these calls. However, you can change the renderers for both cases like this:

```python
from sty.register import FgRegister


class MyFgRegister(FgRegister):
    
    def _num_call(self, num):
        return my_num_renderer(*num)  # default renderer is `eightbit`.

    def _rgb_call(self, *args):
        return my_rgb_tuple_renderer(*args)  # default renderer is `rgb`.


    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))
    

fg = MyFgRegister()

a = fg(100) + 'I have a new renderer now.' + rs.fg
b = fg(40, 50, 200) + 'I have a new renderer now as well.' + rs.fg
```


### Create a custom register from scratch

If you want to create custom registers from scratch, you can do it the same way as described in the chapters above. The only difference is that you inherit from the `Base` class instead of the default register classes.

```python
from sty.primitive import Base


class MyFgRegister(Base):
    # ...
    
```


## Terminal Support

This was initially tested on Arch Linux using 'Termite' terminal. If you have issues with your system, please leave an issue. If sty works fine on your system, feel free to add your system info to the list below:

#### Termite on Linux

| Option        | Status  |
| ------------- | ------- |
| SGR:          | Ok!     |
| 8-bit color:  | Ok!     |
| 24-bit color: | Ok!     |



[SGR]: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
[3_4bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
[8bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
[24bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit
