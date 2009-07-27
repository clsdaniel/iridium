from django.conf import settings

try:
    from PIL import Image
    HAS_PIL = True
except:
    HAS_PIL = False
    
import subprocess

def thumbnail_im_sub(src_img, dest_img):
    '''thumbnail_im_sub
    Create a thumbnail by calling image magick convert
    with the subprocess module
    '''    
    try:
        retcode = subprocess.call(["convert", src_img, "-resize", "64x64", dest_img])
    except Exception:
        pass
    
    if retcode != 0:
        return False
    
    return True
    
def thumbnail_pil(src_img, dest_img):
    if not HAS_PIL:
        return False
    
    try:
        # According to django bug #3848 patch, PIL Image.load() will only
        # detect corrupt jpeg, and Image.verify() will only detect PNG
        # corruption but only when called after opening the file.
        img = Image.open(src_img)
        img.load()
        
        img = Image.open(src_img)
        img.verify()
    except:
        return False
    
    try:
        thumb = img.resize((64,64))
        thumb.save(dest_img, "JPEG")
    except:
        return False
    
    return True

def genThumbnail(src_img, dest_img):
    if settings.THUMBNAIL_METHOD == 'PIL':
        return thumbnail_pil(src_img, dest_img)
    elif settings.THUMBNAIL_METHOD == 'IM':
        return thumbnail_im_sub(src_img, dest_img)
    return False
