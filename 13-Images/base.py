from PIL import Image

mac = Image.open('example.jpg')
print(type(mac))
#mac.show()
print(f'{mac.size}, {mac.filename}, {mac.format_description}')

x = .4 * 1993
y = .6 * 1300
w = .6 * 1993
h = 1300
computer = mac.crop((x, y, w, h))

mac.paste(im=computer,box= (0,0))
mac = mac.resize((2000,500))
mac = mac.rotate(90)
#mac.show()

pencils = Image.open('pencils.jpg')
# pencils.show()

x = 0
y = 0
w = 1950 * .3
h = 1300 * .1
#pencils.crop((x, y, w, h)).show()

x = 0
y = 1100
w = 1950 * .3
h = 1300
#pencils.crop((x, y, w, h)).show()

red = Image.open('red_color.jpg')
red.show()
blue = Image.open('blue_color.png')
blue.show()

red.putalpha(128)
red.show()
blue.putalpha(200)
blue.show()
blue.paste(im=red, box = (0,0), mask=red)
blue.show()
blue.save('purple.png')
purple = Image.open('purple.png')
purple.putalpha(122)
purple.show()

