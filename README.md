# Krita Potter's Wheel Plugin

## Overview

You might have seen those videos of artists painting onto spinning pottery wheels. This plugin rotates the canvas continuously, allowing you to achieve the same effect.

![Pottery Wheel Demo](kritapotterywheeldemo.gif)

## Installation

Like most Krita plugins, either download the zip directly from gitHub [here]() and use Krita's Script Importer Plugin (Tools > Scripts > Import Python Plugin From File...), or copy the contents of the `src` directory (a folder and a .desktop file) into your `C:\Users\[USER]\AppData\Roaming\krita\pykrita` directory.

## FAQ

- How does this work?
  - This plugin gives you two buttons to start and stop the rotation, and a slider to change the speed of the rotation. When you press start, the canvas immediately starts rotating, and you can draw onto the spinning canvas.


## Known issues

- My lines are jittery!
  - Due to the way the plugin currently works (using Krita's inbuilt rotation system to rotate a tiny amount every few milliseconds), this is unavoidable. **Use the brush stabilizer to smooth out the lines.** Unfortunately, this introduces noticable input delay due to how the stabilizer works. I'm working on a solution to make raw inputs nicer, but it will take time.

## Misc

[Report Issues](https://github.com/RainbowPangolin/kritapotterswheel/issues)
