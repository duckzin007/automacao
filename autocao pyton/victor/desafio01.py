import os 

pastas =[
    "fotos","videos","PDF", "planilhas ", "textos", "backup"
]

for pastas in pastas:
    os.mkdir(pastas)