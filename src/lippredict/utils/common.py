import os
from box.exceptions import BoxValueError
import yaml
from lippredict import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content in a ConfigBox.

    Args:
    - path_to_yaml (Path): The path to the YAML file to be read.

    Returns:
    - ConfigBox: A ConfigBox containing the content of the YAML file.

    Raises:
    - ValueError: If the YAML file is empty.
    - Exception: Any other unspecified exception during file reading.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    """
    Creates directories at the specified paths.

    Args:
    - path_to_directories (List[str]): A list of paths where directories will be created.
    - verbose (bool, optional): If True, logs information about created directories. Default is True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    The `save_json` function saves a dictionary as a JSON file at the specified path and logs the path
    of the saved file.

    Args:
      path (Path): The `path` parameter is the file path where you want to save the JSON file. It should
    be a `Path` object representing the file location.
      data (dict): The `data` parameter is a dictionary that contains the data you want to save as a
    JSON file.
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    The function `load_json` loads a JSON file from a given path and returns the content as a
    `ConfigBox` object.

    Args:
      path (Path): The `path` parameter is the path to the JSON file that you want to load. It should be
    a `Path` object, which represents a file or directory path.

    Returns:
      an instance of the `ConfigBox` class, which is initialized with the `content` variable.
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    The function `save_bin` saves binary data to a specified file path using the joblib library and logs
    the path of the saved file.

    Args:
      data (Any): The `data` parameter is the object or data that you want to save as a binary file. It
    can be of any type.
      path (Path): The `path` parameter is the file path where the binary file will be saved. It should
    be a `Path` object representing the location and name of the file.
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    The function `load_bin` loads a binary file using the `joblib` library and returns the loaded data.

    Args:
      path (Path): The `path` parameter is a `Path` object that represents the file path of the binary
    file to be loaded.

    Returns:
      the data loaded from the binary file.
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file or directory at the specified path.

    Args:
    - path (Path): The path to the file or directory.

    Returns:
    - str: A string representing the size of the file or directory, rounded to the nearest kilobyte (KB).
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


# def decodeImage(imgstring, fileName):
#     imgdata = base64.b64decode(imgstring)
#     with open(fileName, "wb") as f:
#         f.write(imgdata)
#         f.close()


# def encodeImageIntoBase64(croppedImagePath):
#     with open(croppedImagePath, "rb") as f:
#         return base64.b64encode(f.read())
