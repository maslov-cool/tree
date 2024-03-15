from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD', snow_color='#FFFAFA',
            trunk_color='#A45A52', needls_color='#01796F', sun_color='#FFDB00'):
    im = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, height * 0.8, width, height), snow_color)
    draw.rectangle((width * 0.45, height * 0.7, width * 0.55, height * 0.9), trunk_color)
    draw.polygon((width * 0.5, height * 0.1, width * 0.4, height * 0.3, width * 0.6, height * 0.3), needls_color)
    draw.polygon((width * 0.5, height * 0.2, width * 0.35, height * 0.5, width * 0.65, height * 0.5), needls_color)
    draw.polygon((width * 0.5, height * 0.3, width * 0.3, height * 0.7, width * 0.7, height * 0.7), needls_color)
    draw.ellipse((width * 0.8, height * -0.2, width * 1.2, height * 0.2), sun_color)

    im.save(file_name)


picture('test.bmp', 1000, 800)
