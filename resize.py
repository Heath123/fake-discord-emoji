from PIL import Image

# https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas/
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def resize(im):
    width, height = im.size
    padding = int(width / 16)
    im = add_margin(im, padding, int(height * 6), padding, padding, (255, 0, 0, 0))
    return im
