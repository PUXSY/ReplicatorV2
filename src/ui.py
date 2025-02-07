from typing import Callable, Dict
from logger import Logger
from pathlib import Path
import sys

logger = Logger(Path("./presets"))
class UI:
    def __init__(self):
        self.banner = """
  _____            _ _           _             
 |  __ \          | (_)         | |            
 | |__) |___ _ __ | |_  ___ __ _| |_ ___  _ __ 
 |  _  // _ \ '_ \| | |/ __/ _` | __/ _ \| '__|
 | | \ \  __/ |_) | | | (_| (_| | || (_) | |   
 |_|  \_\___| .__/|_|_|\___\__,_|\__\___/|_|   
            | |                                
            |_|                                
"""
        self.selected_option: int = 0
        self._running: bool = True
        
    OPTIONS: Dict[int, tuple[str, str]] = {
        1: ("Basic", "The basic tweaks for best performance"),
        2: ("Gaming", "Has everything you need already installed"),
        3: ("Student", "Has everything you need already installed for studying"),
        4: ("Professional", "Has everything you need already installed for work"),
        5: ("Custom", "Create and customize your own setup")
    }

    def print_banner(self) -> None:
        print(self.banner)
        
    def exit_with_error(self, message: str) -> None:
        input(f"Error: {message}. Press Enter to exit...")
        logger.log_error(message)
        sys.exit(1)
        
    def print_error(self, error: str) -> None:
        print(f"Error: {error}")
        logger.log_error(error)
        
    def display_option(self, option_num: int, show_info: bool = False) -> None:
        if option_num in self.OPTIONS:
            name, description = self.OPTIONS[option_num]
            print(f"[{option_num}] {name}")
            if show_info:
                print(description)

    def get_selected_option(self) -> int:
        return self.selected_option

    def run(self) -> int:
        while self._running:
            self.print_banner()
            
            # Display all options
            for i in range(1, 6):
                self.display_option(i)
                
            print("\nSelect your option (0 to exit):")
            try:
                option = int(input(">>> ").strip())
                
                if option == 0:
                    print("Goodbye!")
                    sys.exit(0)
                    
                if option not in self.OPTIONS:
                    self.print_error("Invalid option")
                    continue
                    
                # Show detailed info for selected option
                self.display_option(option, show_info=True)
                
                if input("Do you want to continue? (y/n): ").lower().strip() == "y":
                    self.selected_option = option
                    return option
                    
            except ValueError:
                self.exit_with_error("Invalid input - please enter a number")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                sys.exit(0)
                
        return 0    