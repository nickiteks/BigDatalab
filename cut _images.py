from PIL import Image
import os

def crop_image(image_path, output_path, width, height):
    # Открываем изображение
    image = Image.open(image_path)

    # Получаем размеры исходного изображения
    original_width, original_height = image.size

    # Вычисляем координаты для обрезки
    left = (original_width - width) / 2
    top = (original_height - height) / 2
    right = (original_width + width) / 2
    bottom = (original_height + height) / 2

    # Обрезаем изображение
    cropped_image = image.crop((left, top, right, bottom))

    # Сохраняем обрезанное изображение
    cropped_image.save(output_path)




oldpwd = os.getcwd()

os.chdir('C:/Users/NULS/Desktop/xhtym/projects/BigDatalab/photos/')        

files = os.listdir()

try:
    files.remove('.DS_Store')
except:
    pass


for file in files:

# Пример использования
    image_path = file
    output_path = file
    width = 400
    height = 400

    crop_image(image_path, output_path, width, height)