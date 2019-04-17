# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import os, random, textwrap

class BomDiaGenerator:
    def __init__(self, path_img_gerada):
        self.path_img_gerada = path_img_gerada

        # Carrega o arquivo de frases
        with open('./frases.txt', encoding='utf-8') as f:
            self.frases = f.read().splitlines()

        # Carrega o arquivo de saudacoes
        with open('./saudacoes.txt', encoding='utf-8') as f:
            self.saudacoes = f.read().splitlines()
    
    def get_bom_dia(self, nome_img, extensao):
        """ Retorna o endereço da imagem criada """
        img = Image.open(self.__get_imagem_random())
        draw = ImageDraw.Draw(img)

        self.__escrever_texto_na_imagem(draw, self.__get_frase_random(), 30, 40)
        
        self.__escrever_texto_na_imagem(draw, self.__get_saudacao_random(), 480, 50)

        img.save('{}/{}.{}'.format(self.path_img_gerada, nome_img, extensao))
    
    def __escrever_texto_na_imagem(self, draw, frase, pos_y, tam_fonte=40):
        fnt = ImageFont.truetype(self.__get_font_random(), tam_fonte)

        borda = 2

        lines = textwrap.wrap(frase, width=25)
        y_text = pos_y
        for line in lines:
            width, height = fnt.getsize(line)
            draw.text((((600 - width) / 2) - borda, y_text - borda), line,(0,0,0),font=fnt)
            draw.text((((600 - width) / 2) + borda, y_text - borda), line,(0,0,0),font=fnt)
            draw.text((((600 - width) / 2) + borda, y_text + borda), line,(0,0,0),font=fnt)
            draw.text((((600 - width) / 2) - borda, y_text + borda), line,(0,0,0),font=fnt)

            draw.text(((600 - width) / 2, y_text), line, font=fnt, fill=(255, 255, 255))
            y_text += height

    def __get_imagem_random(self):
        return 'imgs/' + random.choice(os.listdir('imgs/')) 

    def __get_font_random(self):
        return 'fonts/' + random.choice(os.listdir('fonts/')) 

    def __get_frase_random(self):
        return self.frases[random.randint(0, len(self.frases) - 1)]
    
    def __get_saudacao_random(self):
        return self.saudacoes[random.randint(0, len(self.saudacoes) - 1)]