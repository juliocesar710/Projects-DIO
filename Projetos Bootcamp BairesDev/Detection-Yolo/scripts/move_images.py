import os
import subprocess

# Diretório de entrada e saída
input_dir = "/content/darknet/data/test_images"
output_dir = "/content/darknet/data/detected_images"
os.makedirs(output_dir, exist_ok=True)

# Processar cada imagem
for image_name in os.listdir(input_dir):
    input_image_path = os.path.join(input_dir, image_name)
    command = f"./darknet detector test data/coco.data cfg/yolov3_custom.cfg /content/darknet/cfg/yolov3.weights {input_image_path}"
    subprocess.run(command, shell=True)
    subprocess.run(f"mv predictions.jpg {output_dir}/{image_name}", shell=True)

print(f"Todas as imagens processadas foram movidas para {output_dir}.")
