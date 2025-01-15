import sys 

class App:
    def __init__(self, struct_path:str) -> None:
        self.struct_path = struct_path
        
    def run_preset(self, preset_name:str ) -> None:
        if preset_name not in self.json_data:
            print(f"Preset '{preset_name}' not found.")
            return self.json_data