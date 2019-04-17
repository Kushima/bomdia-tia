#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bomdia_tia import BomDiaGenerator

# instancie BomDiaGenerator
generator = BomDiaGenerator(path_img_gerada='.')
# imforme o método get_bom_dia o nome da imagem e a extensao
generator.get_bom_dia(nome_img='teste', extensao='jpg')



