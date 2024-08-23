import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (Path): path to yaml file

    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
        ConfigBox: config box object
    """
    try:
        with open(path_to_yaml, "r") as file:
            config = yaml.safe_load(file)
            logger.info(f"Reading yaml file: {path_to_yaml}")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        logger.error(f"Error reading yaml file: {path_to_yaml}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of directories
        verbose (bool, optional): print logs. Defaults to True.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
        
def save_json(data: Any, path: str):
    """save data to json file

    Args:
        data (Any): data to save
        path (str): path to save
    """
    with open(path, "w") as file:
        json.dump(data, file)

    logger.info(f"Saved data to json file: {path}")

def load_json(path: str) -> Any:
    """load data from json file

    Args:
        path (str): path to json file

    Returns:
        configBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"Loaded data from json file: {path}")
    return ConfigBox(content)

def save_bin(data: Any, path: Path):
    """save data to binary file

    Args:
        data (Any): data to save
        path (Path): path to save
    """
    joblib.dump(data, path)
    logger.info(f"Saved data to binary file: {path}")

def load_bin(path: Path) -> Any:
    """load data from binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: data
    """
    data = joblib.load(path)
    logger.info(f"Loaded data from binary file: {path}")
    return data

def get_size(path: Path) -> int:
    """get size of file

    Args:
        path (Path): path to file

    Returns:
        int: size of file
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())