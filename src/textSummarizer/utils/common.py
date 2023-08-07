# 5 функции которые часто использую в своем коде
import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If yaml file is empty or has invalid content.
        FileNotFoundError: If the specified file does not exist.

    Returns:
        ConfigBox: Parsed YAML data as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("Invalid content in YAML file") from e
    except FileNotFoundError:
        raise



@ensure_annotations
def create_directories(path_to_directories: List[str], verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (List[str]): List of paths to directories.
        verbose (bool, optional): Log each directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except FileNotFoundError as e:
        raise ValueError(f"File not found: {path}") from e
    except Exception as e:
        raise e
