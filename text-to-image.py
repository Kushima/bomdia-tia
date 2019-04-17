#!/usr/bin/env python
from PIL import Image, ImageFont, ImageDraw
    
img = Image.open("imgs/1.jpg")
font = 'fonts/PenguinAttack.ttf'
fnt = ImageFont.truetype(font, 280)
draw = ImageDraw.Draw(img)

x = 350
y = 700
text = "As pessoas boas devem\namar seus inimigos!"

draw.text((x-3, y-3), text,(0,0,0),font=fnt)
draw.text((x+3, y-3), text,(0,0,0),font=fnt)
draw.text((x+3, y+3), text,(0,0,0),font=fnt)
draw.text((x-3, y+3), text,(0,0,0),font=fnt)

draw.text((x, y), text, font=fnt, fill=(255, 255, 255))

img.save('teste.png')