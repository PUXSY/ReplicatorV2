from ui import *
from app import *

def main() -> None:
    UI = ui()
    app = App()
    opsins = {
        1: ui.print_opson_1,
        2: ui.print_opson_2,
        3: ui.print_opson_3,
        4: ui.print_opson_4,
        5: ui.print_opson_5
    }

    for opsin in opsins:
        if UI.run() in opsins:
            opsins[opsin](True)
            break
         
if __name__ == "__main__":
    main()
