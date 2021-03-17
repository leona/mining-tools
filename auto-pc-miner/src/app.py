from ctypes import windll
import win32gui, time, os, atexit
from subprocess import check_output, Popen
from dotenv import load_dotenv

dir_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv(dotenv_path=f"{dir_path}/../config.env")

user32 = windll.user32
user32.SetProcessDPIAware()

full_screen_rect = (0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
previous_state = True
active_miner_pid = False
MINER_BIN = os.getenv("MINER_BIN")

print(111, MINER_BIN)
def exit_handler():
    print('Exiting auto pc miner. Applying default profile.')
    apply_oc_profile(2)

atexit.register(exit_handler)

def apply_oc_profile(id):
    check_output('start "" "' + os.getenv("MSI_PATH") +'" -Profile' + str(id), shell=True)

def is_full_screen():
    try:
        pid = user32.GetForegroundWindow()
        rect = win32gui.GetWindowRect(pid)
        return rect == full_screen_rect, pid
    except Exception as e:
        print("failed", e)
        return False, None

while True:
    _is_full_screen, pid = is_full_screen()
    
    if not _is_full_screen or win32gui.GetWindowText(pid) == "Program Manager":
        if previous_state == True:
            print("!is_full_screen - Opening miner")
            previous_state = False
            apply_oc_profile(1)
            path = os.path.abspath(os.getenv("MINER_PATH"))
            mp = Popen(f"cd {path} && {MINER_BIN}", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
            active_miner_pid = mp.pid
            print("Opened with Pid:", active_miner_pid)
        time.sleep(5)
        continue

    if previous_state == False:
        print("is_full_screen - Closing miner")
        previous_state = True
        os.system(f"taskkill /F /PID {os.getenv('MINER_NAME')}")
        apply_oc_profile(2)

    time.sleep(20)
    