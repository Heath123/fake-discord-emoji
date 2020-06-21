#!/usr/bin/python3

from PIL import Image
import gif
import resize
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".gif") and sys.argv[2].endswith(".gif"):
            frames, durations = gif.processImage(sys.argv[1])
            averageduration = sum(durations) / len(durations)
            frames[0].save(sys.argv[2], save_all=True, append_images=frames[1:], transparency=0, duration=averageduration, disposal=2, optimize=True, loop=0)
        else:
            im = Image.open(sys.argv[1])
            im = im.convert('RGBA')
            im = resize.resize(im)
            im.save(sys.argv[2])
            pass
    else:
        print("Usage: ./main.py in.gif out.gif")
        print("       ./main.py in.png out.png")
