from ui import *
from app import *
from pathlib import Path

ui = UI()
app = App(Path("./../presets"))
opsins = {
    1: 'Basic.json',
    2: 'Gaming.json',
    3: 'Structent.json',
    4: 'Profesional.json',
    5: 'Custom.json'
}

def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        log.log_error(f"Error checking admin privileges: {e}")
        return False
    
def restart_as_admin():
    try:
        script = sys.argv[0]
        params = ' '.join(sys.argv[1:])
        log.log_info("Restarting with admin privileges...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
        sys.exit()
    except Exception as e:
        log.log_error(f"Error restarting as admin: {e}")

def main() -> None:
    if not is_running_as_admin():
        log.log_info("Program is not running as admin. Restarting with admin rights...")
        restart_as_admin()
    
    for opsin in opsins:
        if ui.run() in opsins:
            app.run_preset(opsins[opsin])
         
if __name__ == "__main__":
    main()
    