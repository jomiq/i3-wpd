# i3-wpd
![](/img/banner.png)  
Simple wallpaper daemon for i3.
Supports multiple screens and custom image per workspace.

## Depends
**i3** window manager - https://i3wm.org  
**feh** image viewer swiss army knife - https://github.com/derf/feh
### Optional
The `i3msg.py` script included in this repository is adapted from  
**i3msg-python** - https://github.com/Ceryn/i3msg-python

## Install
1. Put the files somewhere. 
2. [optional] If you have [i3msg-python](https://github.com/Ceryn/i3msg-python) and would like to use the upstream source you may discard `i3msg.py`. Be advised the upstream source will not run on Python 3. 

## Usage
Bash it:
```
./i3wpd.py directory filtype
```
If `directory` doesn't exist i3wpd will attempt to load images from the calling directory.

To see more options execute
```
./i3wpd.py
```
Here's a screenshot of the default setup showing workspace 2 and 7:
![Default setup screenshot](/img/screen.png)

## Configure
Make a directory with images named like the desktops. For applicable formats see `man feh(1)`.  
By default, `i3` workspaces are named `1, 2, 3 ... 10`. Consult your `i3/config`.

### FYI
The daemon will die silently if `i3` is terminated or reloaded.  
Included in this repository are NASA/JAXA images of the solar system. Try
```
./i3wpd.py "--bg-fill --bg black" solar .jpg
```
![Solar system theme screenshot](/img/screen2.png)
## Issues
* Respawn is not implemented. 
* ~~Launching from `i3/config` is untested.~~ (WFM)
* I actually don't know Python. 
* Probably other stuff too.

## Contributions
Contributions are welcome. 

## Licensing
MIT  
© jomiq 2018 / no rights reserved
