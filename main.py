import os
from pdf2image import convert_from_path
from PIL import Image


pdf_path = 'sample.pdf'
image_path = 'images'
images = convert_from_path(pdf_path, fmt='png', output_folder=image_path)

for idx, image_file_name in enumerate(sorted(os.listdir(image_path))):
    image_file_path = f'{image_path}/{image_file_name}'

    original_image = Image.open(image_file_path)
    
    # 이미지 자르기 crop함수 이용 ex. crop(left,up, rigth, down)
    left_image = original_image.crop((0,0,1169,3308))
    right_image = original_image.crop((1170,0,2339,3308))
    
    left_image.save(f'{image_path}/{idx}-left.png')
    right_image.save(f'{image_path}/{idx}-right.png')

    os.remove(image_file_path)
