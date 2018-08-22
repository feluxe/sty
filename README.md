
# sty

<img src="assets/charts.png" alt="charts" />  

## News

#### Beta 6 released

* Subscribe to [#5](https://github.com/feluxe/sty/issues/5) to keep track of breaking changes. 
* Subscribe to [#4](https://github.com/feluxe/sty/issues/4) to keep track of the full changelog.

## Description

Simple, flexible and extensible string styling for your terminal. Supports 3/4bit, 8bit and 24bit (truecolor, rgb) colors. Should work on most Unix platfroms with most terminals. Recent versions of Windows 10 should work with this as well. 

If you run into compatibility problems with sty, please file an issue!

Sty has no dependencies and consists of only ~250 LOC (including empty lines and comments).

## Goal

The idea is to provide Python with a little string styling markup, which is decoupled from color palettes and terminal implementations.

Sty comes with default color palettes and renderers, but you can easily replace/customize them with new ones, without touching the markup.

## Requirements

Sty requires Python `>= 3.5`


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
from sty import fg, bg, ef, rs, Rule, Render

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:

fg.orange = Rule(Render.rgb_fg, 255, 150, 50)

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(foo, bar, baz, qux, qui, buf, sep='\n')
```

output:
 
<img src="assets/example_so.png" alt="example_so" />  


#### A quick look at the primitives:

sty provides a bunch of tiny, but flexible primitives (called register-objects) that can be used to style your strings: 

* `ef` (effect-register)
* `fg` (foreground-register)
* `bg` (background-register)
* `rs` (reset-register).

Each register-object carries a default selection of attributes ([list-of-effects](#list-of-default-effects), [list-of-colors](#list-of-default-colors), [list-of-resetters](#list-of-default-reset-attributes)), which you can select like this:

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
* [Muting / Silencing / Disabling formatting](#muting--silencing--disabling-formatting)
  * [The mute and unmute methods](#the-mute-and-unmute-methods) 
  * [The mute and unmute batch functions](#the-mute-and-unmute-batch-functions)
* [Customization](#customization)
  * [The Rule type and the Render enum](#the-rule-type-and-the-render-enum)
  * [Customizing register-objects](#customizing-register-objects)
    * [Direct attribute customization](#direct-attribute-customization)
    * [Dynamic attribute customization using set_rule method](#dynamic-attribute-customization-using-the-set_rule-method)
    * [Changing render-functions using set_renderer method](#changing-render-functions-using-set_renderer-method)
  * [Customizing register-classes](#customizing-the-register-classes)
    * [Extending the default registers and creating new instances](#extending-the-default-registers-and-creating-new-instances)
    * [Adding render-functions in a class definition](#adding-render-functions-in-a-class-definition)
    * [Adding special \__call__ methods in a class definition](#addding-special-_call_-mehtods-in-a-class-definition)
    * [Create a custom register from scratch](#create-a-custom-register-from-scratch)
* [Developing / Testing](#developing--testing)
* [Terminal Support](#terminal-support)

## Effects

### List of default effects

These are the default attributes for the `ef` register-object.

More info: [wikipedia:SGR][SGR]

| Effect               | Description | Default Renderer |
| -------------------- | ------------- | --------------|
| bold (alias b)       | Bold or increased intensity  | sty.renderfunc.sgr(1) |
| dim                  | Decreased intensity  | sty.renderfunc.sgr(2) |
| italic (alias i)     | Italic.. | sty.renderfunc.sgr(3) |
| underl (alias u)     | Underline..| sty.renderfunc.sgr(4) |
| blink                | Blink.. | sty.renderfunc.sgr(5) |
| inverse              | Inverse fore- and background | sty.renderfunc.sgr(7) |
| hidden               | Conceal/Hide | sty.renderfunc.sgr(8) |
| strike               | Strike-trhough | sty.renderfunc.sgr(9) |


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
a = ef.bold + 'Bold.' + rs.bold_dim

# Shorthand version:
b = ef.b + 'Bold.' + rs.bold_dim + fg.li_yellow + ' Not bold but yellow.' + rs.fg

print(a, b, sep='\n')
```

<img src="assets/bold.png" alt="bold" />  

### Underline

```python
a = ef.underl + 'Underlined.' + rs.underl

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

The default colors for the `fg` register-object.

These are most widely supported. (using sgr codes).

| normal   | Default Renderer |
| -------- | ---------------- |
| black    | sty.renderfunc.sgr(30)          |
| red      | sty.renderfunc.sgr(31)          |
| green    | sty.renderfunc.sgr(32)          |
| yellow   | sty.renderfunc.sgr(33)          |
| blue     | sty.renderfunc.sgr(34)          |
| magenta  | sty.renderfunc.sgr(35)          |
| cyan     | sty.renderfunc.sgr(36)          |
| white    | sty.renderfunc.sgr(37)          |


These are less widely supported. (using less common set of sgr codes).

| light       | Default Renderer |
| ----------- | ---------------- |
| li_black    | sty.renderfunc.sgr(90)          |
| li_red      | sty.renderfunc.sgr(91)          |
| li_green    | sty.renderfunc.sgr(92)          |
| li_yellow   | sty.renderfunc.sgr(93)          |
| li_blue     | sty.renderfunc.sgr(94)          |
| li_magenta  | sty.renderfunc.sgr(95)          |
| li_cyan     | sty.renderfunc.sgr(96)          |
| li_white    | sty.renderfunc.sgr(97)          |


These are even less widely supported. (using 8bit color codes).

| dark        | Default Renderer |
| ----------- | ---------------- |
| da_black    | sty.renderfunc.eightbit_fg(0)   |
| da_red      | sty.renderfunc.eightbit_fg(88)  |
| da_green    | sty.renderfunc.eightbit_fg(22)  |
| da_yellow   | sty.renderfunc.eightbit_fg(58)  |
| da_blue     | sty.renderfunc.eightbit_fg(18)  |
| da_magenta  | sty.renderfunc.eightbit_fg(89)  |
| da_cyan     | sty.renderfunc.eightbit_fg(23)  |
| da_white    | sty.renderfunc.eightbit_fg(249) |


#### Background

The default colors for the `bg` register-object.

These are most widely supported. (using sgr codes).

| normal   | Default Renderer |
| -------- | ---------------- |
| black    | sty.renderfunc.sgr(40)          |
| red      | sty.renderfunc.sgr(41)          |
| green    | sty.renderfunc.sgr(42)          |
| yellow   | sty.renderfunc.sgr(43)          |
| blue     | sty.renderfunc.sgr(44)          |
| magenta  | sty.renderfunc.sgr(45)          |
| cyan     | sty.renderfunc.sgr(46)          |
| white    | sty.renderfunc.sgr(47)          |


These are less widely supported. (using less common set of sgr codes).

| light       | Default Renderer |
| ----------- | ---------------- |
| li_black    | sty.renderfunc.sgr(100)          |
| li_red      | sty.renderfunc.sgr(101)          |
| li_green    | sty.renderfunc.sgr(102)          |
| li_yellow   | sty.renderfunc.sgr(103)          |
| li_blue     | sty.renderfunc.sgr(104)          |
| li_magenta  | sty.renderfunc.sgr(105)          |
| li_cyan     | sty.renderfunc.sgr(106)          |
| li_white    | sty.renderfunc.sgr(107)          |

These are even less widely supported. (using 8bit color codes).

| dark        | Default Renderer |
| ----------- | ---------------- |
| da_black    | sty.renderfunc.eightbit_bg(0)   |
| da_red      | sty.renderfunc.eightbit_bg(88)  |
| da_green    | sty.renderfunc.eightbit_bg(22)  |
| da_yellow   | sty.renderfunc.eightbit_bg(58)  |
| da_blue     | sty.renderfunc.eightbit_bg(18)  |
| da_magenta  | sty.renderfunc.eightbit_bg(89)  |
| da_cyan     | sty.renderfunc.eightbit_bg(23)  |
| da_white    | sty.renderfunc.eightbit_bg(249) |


### Coloring by name

```python
a = fg.li_blue + 'I have a light blue foreground.' + rs.fg
b = bg.cyan + 'I have a cyan background' + rs.bg
c = fg.da_red + bg.li_red + 'I have a dark red fg and light red bg.' + rs.all
d = fg('yellow') + 'I have yellow fg.' + rs.fg

print(a, b, c, d, sep='\n')
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

The reset register-object `rs` can be used to reset previously applied styles.

Link: [wikipedia:SGR][SGR]

### List of default reset attributes

These are the default attributes for the `rs` register-object:

| Reset                | Default Renderer |
| -------------------- | ---------------- |
| all                  | sty.renderfunc.sgr(0)           |
| fg                   | sty.renderfunc.sgr(39)          |
| bg                   | sty.renderfunc.sgr(49)          |
| bold_faint           | sty.renderfunc.sgr(22)          |
| faint_bold           | sty.renderfunc.sgr(22)          |
| italic (alias i)     | sty.renderfunc.sgr(23)          |
| underl    (alias u)  | sty.renderfunc.sgr(24)          |
| blink                | sty.renderfunc.sgr(25)          |
| hidden               | sty.renderfunc.sgr(28)          |
| strike               | sty.renderfunc.sgr(29)          |


## Renderers

The default render-functions are stored in `sty.renderfunc`.

### List of Renderers

| Render-Function      | Description |
| -------------------- | ------------- |
| sty.renderfunc.sgr                  | Render [SGR codes (wikipedia:SGR)][SGR] (works for fg-colors, bg-colors and effects) |
| sty.renderfunc.eightbit_fg          | Render foreground using [8bit color codes (wikipedia:8bit)][8bit] |
| sty.renderfunc.eightbit_bg          | Render background using 8bit color codes |
| sty.renderfunc.rgb_fg               | Render foreground using [24bit (RGB) color codes (wikipedia:24bit)][24bit] |
| sty.renderfunc.rgb_bg               | Render background using 24bit (RGB) color codes |


## Muting / Silencing / Disabling formatting

### The `mute` and `unmute` methods

Sometimes its useful to disable the formatting for a register-object. You can do so by invoking the `mute` and `unmute` methods:

```python
a = fg.red + 'This text is red.' + fg.rs

fg.mute()

b = fg.red + 'This text is NOT red.' + fg.rs

fg.unmute()

c = fg.red + 'This text is red.' + fg.rs
```

### The `mute` and `unmute` batch functions

If you want to mute multiple register-objects at the same time you can use the `mute` and `unmute` functions that you find in `sty.mute`, `sty.unmute`:

```python
from sty import fg, bg, ef, rs, mute, unmute

a1 = fg.red + 'This text is red.' + fg.rs
a2 = bg.red + 'This bg is red.' + bg.rs
a3 = ef.italic + 'This text is italic' + ef.rs

mute(fg, bg, ef, rs)

b1 = fg.red + 'This text is NOT red.' + fg.rs
b2 = bg.red + 'This bg is NOT red.' + bg.rs
b3 = ef.italic + 'This text is NOT italic' + ef.rs

unmute(fg, bg, ef, rs)

c1 = fg.red + 'This text is red.' + fg.rs
c2 = bg.red + 'This bg is red.' + bg.rs
c3 = ef.italic + 'This text is italic' + ef.rs
```


## Customization
 
Sty allows you to change or to extend the default registers as you like. You can also create a complete new register. More on these things in the following chapters.

> #### WARNING:
> If you create a library that is shared among other projects, I highly suggest not to customize the "global" register-objects (sty.fg, sty.bg, sty.ef, sty.rs) directly, because that might cause conflicts with other packages that share the same sty dependency within the same project.
>
> If you want to use custom register-objects in a library project, you should create new register-object instances from the register-classes dedicated to your project only. More on this int the chapter *"Extending the default registers and creating new instances"*.


### The "Rule" type and the "Render" enum 

In order to assing values to a register-object, you have to use the 'Rule' type (`sty.Rule`).

The Rule type simply takes the name of a render-function and the arguments that the function should use:

`Rule(renderer_name, *args, **kwargs)`

In this example we assign a render-function called 'sgr' with the argument 32 to `fg.red`:

```python
fg.red = Rule('sgr', 32)
```

Sty provides an enum `sty.Render` that allows for more structured selection of the render-function name. The following example does the same as the one above:


```python
from sty import Render

fg.red = Rule(Render.sgr, 32)
```

The reason why we are assigning the name of the function instead of the function itself is that this way we can replace the render-functions on the fly for each register-object.


### Customizing register-objects

#### Direct attribute customization

You can add and change attributes of each register-object directly like this:

```python
from sty import fg, bg, ef, rs, Rule, Render

# ef.italic now renders underlined text.
ef.italic = Rule(Render.sgr, 4)

# fg.red renders green text from now on.
fg.red = Rule(Render.sgr, 32)

# fg.blue renders red text from now on (using an 8bit color code).
fg.blue = Rule(Render.eightbit_fg, 88)

# Create a new item that renders brown text.
fg.my_new_item = Rule(Render.eightbit_fg, 130)

# bg.green renders blue bg from now on (using a 24bit rgb code).
bg.green = Rule(Render.rgb_bg, 0, 128, 255)

# rs.all only resets the underline effect from now on.
rs.bold_dim = Rule(Render.sgr, 24)
```


#### Dynamic attribute customization using the `set_rule` method.

In case you need to set attributes of a register-object dynamically you can use the `set_rule` method:

```python
from sty import fg, Rule, Render

my_color_name = 'special_teal'

fg.set_rule(my_color_name, Rule(Render.eightbit_fg, 51))

a = fg.special_teal + 'This is custom teal text.' + fg.rs
```

#### Changing render-functions using `set_renderer` method.

In order to change a render-function for a register-object (fg, bg, ef, rs) you can use the `set_renderer` mehtod:

```python
from sty import fg, Render

def my_custom_renderfunc():
    # ...

fg.set_renderer(Render.rgb_fg, my_custom_renderfunc)
```

After this each attribute of `fg` that was set with a `Rule(Render.rgb_fg, ...` will now use the new render-function.


### Customizing the register-classes

#### Extending the default registers and creating new instances

If you want to set a larger register of custom attributes, it may be more convenient to extend the default register-classes and create new register-objects from them.


```python
from sty import FgRegister, Rule, Render


# Extend default Fg register.

class MyFgRegister(FgRegister):

    black = Rule(Render.sgr, 31)
    red = Rule(Render.sgr, 34)
    orange = Rule(Render.rgb_fg, 255, 128, 0)
    # ...


# Create a new instance from the new Register

fg = MyFgRegister()

a = fg.orange + 'This is orange text from a non default attribute.' + rs.fg
```

This is useful in case you want to provide your project with custom versions of `fg`, `bg`, `ef`, `rs` or if you don't want to mess with the "global" register-objects provided by sty.

You could for example create your own `style.py` and import your custom regsiter-objects from there: `from myproj.style import fg, bg, ef, rs`.


#### Adding render-functions in a class definition

In an earlier chapter, we saw how to use the `set_renderer` method to replace a render-function for a register-object. In this example we set a new render-function within a class definition. 

```python
import sty
from sty import Rule, FgRegister


# Your new bg render-function.
def my_custom_rgb_fg(r,g,b):
    return f'\x1b[48;2;{str(r)};{str(g)};{str(b)}m'


# Extend the enum with the name of your new render-funtion.
class Render(sty.Render):
    custom_rgb_fg = 'custom_rgb_fg'


# Extend default Fg register.
class MyFgRegister(FgRegister):

    def __init__(self):
        super().__init__() # Call super to apply render-functions from FgRegister.
        self.set_renderer(Render.custom_rgb_fg, my_custom_rgb_fg)

    black = Rule(Render.sgr, 31)
    red = Rule(Render.sgr, 34)
    orange = Rule(Render.custom_rgb_bg, 255, 128, 0) # This uses the new render-function.


fg = MyFgRegister()

a = fg.orange + 'I use the new render-function.' + fg.rs
```

#### Addding special \__call__ mehtods in a class definition

Remember that you can call register-objects like this `fg(100)` (to generate a 8bit color) or like this `fg(40, 100, 20)` (to generate an rgb color)?

Each of those two calls have a different render-function assigned. You can add/change the render-functions for these calls by setting the `eightbit_call` and `rgb_call` attributes, like in this example:

```python
from sty.register import FgRegister


class MyFgRegister(FgRegister):
    
    eightbit_call = Rule(Render.eightbit_fg)
    rgb_call = Rule(Render.rgb_fg)

    black = Rule(Render.sgr, 31)
    red = Rule(Render.sgr, 34)
    orange = Rule(Render.rgb_fg, 255, 128, 0)
    

fg = MyFgRegister()

a = fg(100) + 'I use an eightbit_fg renderer.' + rs.fg
b = fg(40, 50, 200) + 'I use an rgb_fg renderer.' + rs.fg
```


#### Create a custom register from scratch

If you want to create custom register-classes from scratch, you can do it as described in the chapters above. The only difference is that you inherit from the `Base` class instead of the default register-classes.

```python
from sty import Base, Rule, Render, renderfunc


class MyFgRegister(Base):

    # Set render-functions.
    def __init__(self):
        self.set_renderer(Render.sgr, renderfunc.sgr)
        self.set_renderer(Render.rgb_fg, renderfunc.rgb_fg)

    # Set rules for special call methods.
    eightbit_call = Rule(Render.eightbit_fg)
    rgb_call = Rule(Render.rgb_fg)

    # Set styling rules.
    black = (Render.sgr, 31)
    red = (Render.sgr, 34)
    orange = (Render.rgb_fg, 255, 128, 0)
    # ...
```

This is exactly how the default register-classes are created in `sty.register`.



## Developing / Testing

Clone the repo:

    git clone https://github.com/feluxe/sty.git

Run tests:

    cd sty
    python3 -m tests

Read test results in your terminal and see if things match up.


## Terminal Support

If you have issues with sty on your system, please leave an issue.


| Terminal    | Tested | Known Issues 
|-------------|--------|--------------|
| Genome Terminal | yes | * `blink` effect not supported. |
| Terminte | yes | * `blink` effect not supported. |
| Yakuake | yes | |


[SGR]: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
[3_4bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
[8bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
[24bit]: https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit
