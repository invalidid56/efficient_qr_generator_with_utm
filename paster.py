import os
from PIL import Image

img_path = os.path.dirname(os.path.realpath(__file__)) + "/imgs"

for file_name in os.listdir(img_path):
    img = Image.open(f"{img_path}/{file_name}")

    rgba = img.convert("RGBA")
    datas = rgba.getdata()

    target_color = (255, 255, 255)
    tolerance = 30

    # Trancyparent Background Task
    new_data = []
    for item in datas:
        if all(abs(item[i] - target_color[i]) < tolerance for i in range(3)):
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)

    rgba.putdata(new_data)
    rgba.save(f"transparent/{file_name}", "PNG")

    # Image Resizing
    img = Image.open(f"transparent/{file_name}").convert("RGBA")

    width, height = img.size

    new_size = (172, 172)
    new_img = img.resize(new_size)

    # Simple Poster
    back = Image.open("simple_no_qr.png").convert("RGBA")

    temp = Image.new("RGBA", back.size)
    temp.paste(new_img, (80, 1473))

    generated = Image.alpha_composite(back, temp)
    generated.save(f"generated/simple/{file_name}")

    # Detail Poster
    back = Image.open("detail_no_qr.png").convert("RGBA")

    temp = Image.new("RGBA", back.size)
    temp.paste(new_img, (1006, 1065))

    generated = Image.alpha_composite(back, temp)
    generated.save(f"generated/detail/{file_name}")
