Py script to periodically update your Wallpaper from a folder of images. Current support only windows 10 (Earlier version of windows may work, but not tested). Also may work in un-licensed Window (Windows that have not been activated), but not tested, if someone can confirm this, that would be great.

config.json sample:
```
{
    "wallpaper_dir": "/path/to/where/your/wallpaper/is/",
    "interval_sec": 5
}
```
interval_sec is the interval in seconds at which a new wallpaper is displayed

Dependencies (Python libraries):
* Python 3.8.2 (Earlier versions may work, but not tested)
* json
* ctypes
* os
* time
* random

usage:
* Create 'config.json' with the sample config.json above, and fill out the correct configs
* Make sure the WallpaperRotation.py and config.json are in the same dir
* Then run
```
python ./WallpaperRotation.py
```