# Bom dia da Tia!
Gerador de imagens de bom dia de qualidade, como as das suas tias!

## Como usar (HowTo)
Siga como no arquivo de exemplo `exemplo.py`:

```python
from bomdia_tia import BomDiaGenerator

# instancie BomDiaGenerator (neste exemplo, salva a imagem na pasta de execução)
generator = BomDiaGenerator(path_img_gerada='.')
# imforme o método get_bom_dia o nome da imagem e a extensao
generator.get_bom_dia(nome_img='teste', extensao='jpg')
```

## Conteúdo
O Bom dia da Tia 1.0 estara carregado com:
* 100 imagens de fundo em `imgs/`
* 100 frases de impacto no arquivo `frases.txt`
* 50 saudações no arquivo `saudacoes.txt`
* 3 fontes para os textos em `fonts/`

Ou seja, para a versão 1.0 teremos até 50.000 combinações diferentes de bom dia. É bom dia pra caralh*!

## Limitações

Caso queira adicionar novos elementos, para a versão 1.0, siga as os requisitos abaixo:
* As imagens em `img/` devem ter tamanho 600x600
* É aconselhável que as frases no arquivo `frases.txt` tenham, no máximo, 100 caracteres.
* É aconselhável que as saudações no arquivo `saudacoes.txt` tenham, no máximo, 50 caracteres.
* Adicione fontes em `fonts/` que tenham todos os caracteres necessários para o vocabulário pt-BR
## Instalação

Este projeto foi escrito em python 3. Instale as dependencias necessárias.

### Linux
```bash
sudo apt install python3-pip
pip3 install Pillow
```