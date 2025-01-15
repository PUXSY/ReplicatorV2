class ui:
    def __init__(self):
        self.baner = """
  _____            _ _           _             
 |  __ \          | (_)         | |            
 | |__) |___ _ __ | |_  ___ __ _| |_ ___  _ __ 
 |  _  // _ \ '_ \| | |/ __/ _` | __/ _ \| '__|
 | | \ \  __/ |_) | | | (_| (_| | || (_) | |   
 |_|  \_\___| .__/|_|_|\___\__,_|\__\___/|_|   
            | |                                
            |_|                                
"""

    def print_baner(self) -> None:
        print(self.baner)
        
    def print_error_no_entered(self) -> None:
        input("Error: No entered value")
        exit()
        
    def print_error(self, error:str) -> None:
        input(f"Error: {error}")
        exit()
        
    def print_opson_1(self, info:bool = False) -> None:
        print("[1] Basic")
        if info:
            print("The basic twicks for best performance")
        
    def print_opson_2(self, info:bool = False) -> None:
        print("[2] Gaming")
        if info:
            print("Hes evrything you need allready installed")
            
    def print_opson_3(self, info:bool = False) -> None:
        print("[3] Student")
        if info:
            print("Hes evrything you need allready installed for studing")
            
    def print_opson_4(self, info:bool = False) -> None:
        print("[4] Profesional")
        if info:
            print("Hes evrything you need allready installed for work")
            
    def print_opson_5(self, info:bool = False) -> None:
        print("[5] Custom")
        if info:
            print("Creat and castomize your own setup")
            
            
    def run(self) -> int:
        opsins = {
            1: self.print_opson_1,
            2: self.print_opson_2,
            3: self.print_opson_3,
            4: self.print_opson_4,
            5: self.print_opson_5
        }
        
        while(True):
            self.print_baner()
            for i in range(1, 6):
                opsins[i](False)
            print("Select your opson:")
            try:
                opson = int(input(">>> "))
                if opson in range(1, 6):
                    opsins[opson](True)
                    if input("Do you want to continue? (y/n): ") == "y":
                        return opson
                else:
                    print("Invalid opson")
            except:
                print("Invalid opson")