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
2. [optional] If you have [i3msg-python](https://github.com/Ceryn/i3msg-python) and would like to use the upstream source you may discard `i3msg.py`.

## Usage
Default mode looks for `.png` files in the `./backgrounds` directory. If no such directory exists it will attempt to load images from the calling directory.
```
./i3wpd.py default
```
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

## Issues
* Respawn is not implemented. 
* Launching from `i3/config` is untested.
* I actually don't know Python. 
* Probably other stuff too.

## Contributions
Contributions are welcome. 

## Licensing
MIT  
© jomiq 2018 / no rights reserved