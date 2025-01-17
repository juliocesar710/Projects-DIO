# Listar imagens no diretório de imagens detectadas
import os

detected_images_path = "/content/darknet/data/detected_images"
detected_images = os.listdir(detected_images_path)

if detected_images:
    print("Imagens detectadas:")
    for image in detected_images:
        print(image)
else:
    print("Nenhuma imagem detectada no diretório.")
