import tensorflow as tf
import os

def load_data(data_dir):
    return tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(150, 150),
        batch_size=32
    )

def save_model(model, path):
    model.save(path)

def load_model(path):
    return tf.keras.models.load_model(path)
