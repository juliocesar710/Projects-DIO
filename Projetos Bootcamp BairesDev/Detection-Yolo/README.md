# YOLO Custom Object Detection

Este projeto utiliza o algoritmo de detecção de objetos YOLO (You Only Look Once) para identificar e classificar objetos em imagens personalizadas. O treinamento é feito usando um conjunto de dados personalizado e a implementação do Darknet.

## Estrutura do Projeto

```
├── notebooks/
│   ├── rede_yolo.ipynb
│   └── rede_yolo_view.ipynb
├── data/
│   ├── coco.data
│   ├── coco.names
├── cfg/
│   └── yolov3_custom.cfg
├── scripts/
│   ├── generate_coco.py   # Script para gerar coco.data e coco.names
│   ├── inference.py       # Script para inferência de imagens
│   └── move_images.py     # Script para mover as imagens detectadas
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivo para ignorar arquivos não necessários
└── README.md              # Documento de descrição do projeto

```

## 🛠️ Requisitos
- Python 3.x
- Darknet
- OpenCV
- Outros (veja requirements.txt)

## Recursos utilizados

- Pesos para o treinamneto que podem ser acessados [Aqui](https://pjreddie.com/darknet/yolo/)
- DataSet Coco que pode ser visualizado no começo dos [notebooks](./notebooks)

## 🔧 Instalação

### 1. Clone este repositório:
`git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
`
### 2. Instale as dependências:
`pip install -r requirements.txt
`
### 3. Compile o Darknet com OpenCV (se necessário):
`cd darknet
make
`

## Preparando o Conjunto de Dados

- coco.data: Arquivo de configuração que inclui os caminhos para os dados de treino, validação, nomes das classes e o diretório para backups dos pesos.
- coco.names: Lista de nomes de classes para a detecção de objetos.
- train.txt: Arquivo com os caminhos das imagens de treinamento. (confira [notebook](./notebooks/rede_yolo.ipynb) para mais detalhes)

## 🚀 Treinamento

Para iniciar o treinamento, execute o seguinte comando:
`!./darknet detector train data/coco.data cfg/yolov3_custom.cfg /content/darknet/cfg/yolov3.weights
`

## 🔍 Inferência

Após o treinamento, use o seguinte comando para rodar a inferência em uma imagem de teste:

`!./darknet detector test data/coco.data cfg/yolov3_custom.cfg backup/yolov3_custom_final.weights data/test_images/test.jpg
`

As imagens com os objetos detectados serão salvas na pasta `detected_images`.


## 📊 Visualização do projeto

Para uma mlehor visualização do projeto recomendo ver este [notebook](./notebooks/rede_yolo_view.ipynb) com informações reduzidas

## 🤝 Contribuição

Se desejar contribuir para o projeto, siga os seguintes passos:

1. Fork este repositório.
2. Crie uma branch para suas alterações (git checkout -b nova-feature).
3. Comite suas alterações (git commit -am 'Adiciona nova feature').
4. Faça push para a branch (git push origin nova-feature).
5. Abra um pull request.
