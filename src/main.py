from ui import *
from app import *
from pathlib import Path

def main() -> None:
    ui = UI()
    app = App(Path("./presets"))
    opsins = {
        1: 'Basic.json',
        2: 'Gaming.json',
        3: 'Structent.json',
        4: 'Profesional.json',
        5: 'Custom.json'
    }
    for opsin in opsins:
        if ui.run() in opsins:
            app.run_preset_test(opsins[opsin])
            
         
if __name__ == "__main__":
    main()
 