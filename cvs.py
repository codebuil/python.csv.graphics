import csv
from PIL import Image, ImageDraw

# Abrir o arquivo CSV e ler os dados
with open('dados.csv', 'r') as f:
    reader = csv.reader(f)
    dados = [(float(row[0]), row[1]) for row in reader]

# Ordenar os dados por ordem decrescente
dados = sorted(dados, reverse=True)

# Calcular a percentagem de cada valor em relação ao maior valor
max_valor = dados[0][0]
dados_percentagem = [(valor/max_valor*100, nome) for valor, nome in dados[:3]]

# Criar uma imagem com as barras
img = Image.new('RGB', (300, 100), (220, 230, 255))
draw = ImageDraw.Draw(img)

# Desenhar as barras
bar_width = 80
bar_height = 60
gap = 10
x = gap
for percentagem, nome in dados_percentagem:
    y = 90 - percentagem/100 * bar_height
    draw.rectangle((x, y, x+bar_width, 90), fill=(0, 0, 255))
    draw.text((x+bar_width/2, 70), nome, fill=(0, 0, 0), anchor='mt')
    x += bar_width + gap

# Mostrar a imagem
img.show()

