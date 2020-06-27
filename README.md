Py script to periodically update your Wallpaper from a folder of images. Current support only windows 10 (Earlier version of windows may work, but not tested)

config.json sample:
```
{
    "wallpaper_dir": "/path/to/where/your/wallpaper/is/",
    "interval_min": 5
}
```
interval_min is the interval at which a new wallpaper is displayed

Dependencies (Python libraries):
* Python 3.8.2 (Earlier versions may work, but not tested)
* json
* ctypes

usage:
* Create 'config.json' with the sample config.json above, and fill out the correct configs
* Make sure the WallpaperRotation.py and config.json are in the same dir
* Then run
```
python ./WallpaperRotation.py
```