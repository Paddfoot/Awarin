from PIL import Image
import os

directory = "datah/characters/"
files = os.listdir(directory)
for i in files:
    image_path = 'datah/characters/' + i + '/UI_NameCardPic_' + i + '_P.jpg'
    # указываем фиксированный размер стороны
    fixed_width = 140
    img = Image.open(image_path)
    # получаем процентное соотношение
    # старой и новой ширины
    width_percent = (fixed_width / float(img.size[0]))
    # на основе предыдущего значения
    # вычисляем новую высоту
    height_size = int((float(img.size[0]) * float(width_percent)))
    # меняем размер на полученные значения
    new_image = img.resize((140, 67))
    #new_image.show()
    new_image.save('datah/characters/' + i + '/UI_NameCardPic_' + i + '_P_min.png')
    print(i)