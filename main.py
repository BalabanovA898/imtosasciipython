from PIL import Image

if __name__ == "__main__":
    pallet = " .:!/r(l1Z4H9W8$@'"[::-1]

    img = Image.open("./images/4.jpg")
    img_loaded = img.load()

    max_height= 256

    width, height = img.size

    pix_per_symbol_multiplyer = height/max_height

    with open("output.txt", "w") as file:
        cur_height = round(height*(1/pix_per_symbol_multiplyer))
        cur_width  = round(width*(1/pix_per_symbol_multiplyer))

        for y in range(cur_height):
            line = ""
            for x in range(cur_width):
                pixel = img_loaded[x * (height/cur_height), y * (width/cur_width)]
                lum = (0.2126*pixel[0]) + (0.7152*pixel[1]) + (0.0722*pixel[2])
                line += pallet[-round(len(pallet)/255*lum)]
            file.write(line + "\n")