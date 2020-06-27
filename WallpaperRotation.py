import json
import ctypes
import os
import time
import random

# Return the dict of the json file
def decode_json_config_file_to_dict( filepath='' ):
    if filepath == '':
        print('ERROR: decode_json_config_file_to_dict(): Arg filepath is empty string')
        return None

    try:
        f = open(filepath)
        data = json.load(f)
        return data
    except Exception as e:
        print('ERROR: decode_json_config_file_to_dict(): Fail to open {}'.format(filepath), e)
        return None

    return None

# Only works for first level of variables, for now, until multiple level is implemented
def get_single_variable_from_json_file( filepath='', arg_name='' ):
    if filepath == '':
        print('ERROR: get_single_variable_from_json_file(): Arg filepath is empty string')
        return None

    if arg_name == '':
        print('ERROR: get_single_variable_from_json_file(): Arg arg_name is empty string')
        return None

    json_dict = decode_json_config_file_to_dict(filepath=filepath)
    if not isinstance(json_dict, dict):
        print('ERROR: get_single_variable_from_json_file(): The file is not a correctly structured json file')
        return None
    else:
        if arg_name in json_dict:
            return json_dict[arg_name]
        else:
            print('ERROR: get_single_variable_from_json_file(): The key "{}" does not exists in dictionary from the json file'.format(arg_name))
            return None

    return None

def get_all_sub_filefile_from_dir( dir='' ):
    onlyfiles = [ os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) ]
    return onlyfiles

#@TODO
def file_is_image(filepath=''):
    filename, file_extension = os.path.splitext(filepath)

    image_extensions = [
        '.jpeg',
        '.bmp',
        '.gif',
        '.jpg',
        '.png',
        '.tif',
    ]

    if file_extension in image_extensions:
        return True
    else:
        return False

def main():
    config_path = r'./config.json'
    wallpaper_dir = get_single_variable_from_json_file( config_path, "wallpaper_dir" )
    interval_sec = get_single_variable_from_json_file( config_path, "interval_sec" )
    allow_repeats_per_cycle = get_single_variable_from_json_file( config_path, "allow_repeats_per_cycle" )

    file_path_list = get_all_sub_filefile_from_dir(wallpaper_dir)

    dll = ctypes.WinDLL('user32')
    SPI_SETDESKWALLPAPER = 20

    if allow_repeats_per_cycle:
        print( ' Allow repeats per cycle' )
        # Can have repeating images one after another
        for i in range(5):
            random_file = random.choice(file_path_list)
            t = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
            if file_is_image(random_file):
                print( ' {}, changing the wallpaper... {}'.format(current_time, random_file) )
                dll.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, random_file, 0)
                time.sleep(interval_sec)
            else:
                print( ' {}, not valid image extension, skip it... {}'.format(current_time, random_file) )
    else:
        # This method will guarantee no repeats until one cycle's up
        # Randomize the order of the image. Note, shuffle works in-place and returns None
        print( ' No repeats per cycle' )
        random.shuffle(file_path_list)
        for each_file in file_path_list:
            t = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
            if file_is_image(each_file):
                print( ' {}, changing the wallpaper... {}'.format(current_time, each_file) )
                dll.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, each_file, 0)
                time.sleep(interval_sec)
            else:
                print( ' {}, not valid image extension, skip it... {}'.format(current_time, each_file) )


if __name__ == '__main__':
    main()