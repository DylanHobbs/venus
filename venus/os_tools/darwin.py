import subprocess                                                           

def set_wall(picture_file):
    """
    This method sets a wallpaper
    :param picture_file - The file to use for setting the background
    """
    print(picture_file)

    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell"""

    subprocess.Popen(SCRIPT%picture_file, shell=True)

def get_screen_resolution():
    """
    This method gets the screen resolution using xrandr
    """
    output = subprocess.Popen("system_profiler SPDisplaysDataType |grep Resolution",shell=True     , stdout=subprocess.PIPE).communicate()[0]
    resolution = str(output).replace('Resolution', ' ').replace("\\n'", "").replace(":", "").replace("b'", "").split();
    return resolution[0] + resolution[1] + resolution [2]
