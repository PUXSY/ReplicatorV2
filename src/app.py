import os
from logger import Logger
import json
from pathlib import Path

log = Logger()
class App:
    def __init__(self, struct_path_dir:Path) -> None:
        self.preset_path_dir: Path = struct_path_dir
        self.list_of_presets: list = self.Get_presets_list()
    
    def __enter__(self):
        """Context manager entry point."""
        self.list_of_presets: list = self.Get_presets_list()
        return self
    
    def Get_presets_list(self) -> list:
        try:
            if not self.preset_path_dir.exists() or not self.preset_path_dir.is_dir():
                log.log_error(f"Error: Directory '{self.preset_path_dir}' does not exist. Or is not a directory.")
                return None
            return [file for file in os.listdir(self.preset_path_dir) if os.path.isfile(os.path.join(self.preset_path_dir, file))]
        except FileNotFoundError:
            log.log_error(f"Error: File '{self.preset_path_dir}' not found.")
            return None
    
    def presets_in_list(self, preset_name:str ) -> bool:
        try:
            if preset_name in self.list_of_presets:
                return True
            else:
                return False
        except FileNotFoundError:
            log.log_error(f"Error: File '{self.preset_path_dir}' not found.")
            return False
    
    def run_preset(self, preset_name:str ) -> None:
        try:
            if self.presets_in_list(preset_name):
                print(f"Running preset: {Path(self.preset_path_dir, preset_name)}")
                log.log_maseg(f"Running preset: {Path(self.preset_path_dir, preset_name)}")
                with open(os.path.join(self.preset_path_dir, preset_name), 'r') as file:
                    preset_data = json.load(file)
                    print(preset_data)
            else:
                log.log_error(f"Error: Preset '{preset_name}' not found in the list of presets.")
                return None
        except FileNotFoundError:
            log.log_error(f"Error: File '{self.preset_path_dir}' not found.")
            return None