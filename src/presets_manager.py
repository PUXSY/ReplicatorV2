import json
import subprocess
from typing import List, Dict
from pathlib import Path


class ProgramManager:
    """
    Manages the interaction with winget for program discovery and installation.
    """

    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.preset_data: dict = {}

    def preset_exists(self) -> bool:
        """
        Checks if the json file exists.
        """
        if self.path.exists() and self.path.is_file():
            return True
        return False


    def load_json_data(self) -> None:
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                self.json_data = json.load(f)
        except UnicodeDecodeError:
            try:
                with open('./applications.json', 'r', encoding='cp1252') as f:
                    self.preset_data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                self.preset_data = {} 
        except FileNotFoundError:
            print("applications.json not found. Please ensure the file exists.")
            self.preset_data = {}

