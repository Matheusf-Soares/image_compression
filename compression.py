from PIL import Image
import os

reduct_fact = .5
compressed_path = 'compressed_images'
if compressed_path not in os.listdir():
    os.mkdir(compressed_path)

files_path = 'images'
files = [i for i in os.listdir(files_path) if 'jpg' in i]

size_before = 0
size_after = 0

file = files[0]
for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(compressed_path, file)

    size_before += os.stat(file_path).st_size

    img = Image.open(file_path)

    new_w = int(reduct_fact * img.size[0])
    new_h = int(reduct_fact * img.size[1])
    img = img.resize((new_w, new_h), Image.BOX)

    img.save(new_path, 'JPEG', optimize=True, quality=90)
    size_after += os.stat(new_path).st_size

dif = (size_before - size_after) / (1024 * 1024)
percent = 100 * dif / (size_before / (1024 * 1024))
gross_percent = (size_after / size_before) * 100


print(f'Initial directory\'s size(Mb): {size_before / 1024 ** 2}')
print(f'Final directory\'s size(Mb): {size_after / 1024 ** 2}')
print(f'Total Difference: {dif} Mb')
print(f'Directory\'s size was reduced in {round(percent, 2)}%')
print(f'Final directory\'s size is {round(gross_percent, 2)} of Initial directory\'s size')