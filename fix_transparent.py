from PIL import Image

img = Image.open('/config/workspace/github/seahorse-kingdom/seahorse-icon.png')
img = img.convert('RGBA')

data = img.getdata()
new_data = []
for item in data:
    if item[0] > 245 and item[1] > 245 and item[2] > 245:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save('/config/workspace/github/seahorse-kingdom/seahorse-icon.png')
print("透明背景处理完成!")
