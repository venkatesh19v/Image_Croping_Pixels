from PIL import Image
def resize_and_crop(input_path, output_path, target_width, target_height):
    original_image = Image.open(input_path)
    aspect_ratio = original_image.width / original_image.height
    if aspect_ratio > (target_width / target_height):
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    left = (new_width - target_width) / 2
    top = (new_height - target_height) / 2
    right = (new_width + target_width) / 2
    bottom = (new_height + target_height) / 2
    cropped_image = resized_image.crop((left, top, right, bottom))
    cropped_image.save(output_path)
input_image_path = '/home/fras/fras_final/Flowtrik/IMG20240223153612.jpg'
output_image_path = '/home/fras/fras_final/Flowtrik/Crp.jpg'
target_width = 640
target_height = 480
resize_and_crop(input_image_path, output_image_path, target_width, target_height)
