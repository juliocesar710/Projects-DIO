# Gerar coco.data
def gerar_coco_data(classes, train_path, valid_path, names_path, backup_path, output_path="coco.data"):
    conteudo = f"""classes= {classes}
train  = {train_path}
valid  = {valid_path}
names  = {names_path}
backup = {backup_path}"""
    
    with open(output_path, "w") as file:
        file.write(conteudo)
    print(f"Arquivo '{output_path}' criado com sucesso!")

# Exemplo de uso:
gerar_coco_data(
    classes=2,
    train_path="/path/to/train.txt",
    valid_path="/path/to/valid.txt",
    names_path="/path/to/coco.names",
    backup_path="/path/to/backup"
)
