from PIL import Image
import colorsys

whole_image = 0
image = Image.open('images\ungeschwaerzt_markiert-1587.jpg').convert('RGBA').resize((64, 64), Image.ANTIALIAS)
red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for px in image.getdata():
    whole_image += 1
    h, s, l = colorsys.rgb_to_hsv(px[0]/255., px[1]/255., px[2]/255.)
    h = h * 360
    s = s * 100
    l = l * 100

    if l > 95:
        white += 1
    elif l < 8:
        black += 1
    elif s < 8:
        gray += 1
    elif h < 12 or h > 349:
        red += 1
    elif h > 11 and h < 35:
        if s > 70:
            orange += 1
        else:
            brown += 1
    elif h > 34 and h < 65:
        yellow += 1
    elif h > 64 and h < 150:
        green += 1
    elif h > 149 and h < 200:
        turquoise += 1
    elif h > 195 and h < 250:
        blue += 1
    elif h > 245 and h < 275:
        lilac += 1
    elif h > 274 and h < 350:
        pink += 1

# print 'White:', white
# print 'Black:', black
# print 'Gray:', gray
# print 'Red:', red
# print 'Orange:', orange
# print 'Brown:', brown
# print 'Yellow:', yellow
# print 'Green:', green
# print 'Turquoise:', turquoise
# print 'Blue:', blue
# print 'Lilac:', lilac
# print 'Pink:', pink

print(yellow)
print(whole_image)
print(white)

print(float(yellow) / (float(whole_image) - float(white) - float(gray)))
print(gray)
print(float(yellow) / (float(gray)))
