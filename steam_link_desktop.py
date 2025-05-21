import webbrowser, time, sys
import win32gui, win32con, win32api, win32process

# ---------- Configuration ----------
URL = "https://example.com"
# Seconds to wait for the browser to launch
WAIT_LAUNCH = 2
# Seconds to wait after entering full screen
WAIT_FULLSCREEN = 2

# ---------- Win32 Utilities ----------
def hide_taskbar(hide=True):
    """Hide or show the Windows taskbar."""
    hwnd_bar = win32gui.FindWindow("Shell_TrayWnd", None)
    if hwnd_bar:
        win32gui.ShowWindow(
            hwnd_bar,
            win32con.SW_HIDE if hide else win32con.SW_SHOW
        )

def newest_visible_window():
    """Return the handle of the most recently created visible top-level window."""
    windows = []
    def enum_cb(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            # GetWindowThreadProcessId returns (threadID, processID)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            windows.append((pid, hwnd))
    win32gui.EnumWindows(enum_cb, None)
    return windows[-1][1] if windows else None

def send_f11(hwnd):
    """Activate the window and send F11 to toggle full screen."""
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(hwnd)
    VK_F11 = 0x7A
    # Press F11
    win32api.keybd_event(VK_F11, 0, 0, 0)
    # Release F11
    win32api.keybd_event(VK_F11, 0, win32con.KEYEVENTF_KEYUP, 0)

# ---------- Main Flow ----------
try:
    # 1) Hide the taskbar to ensure the browser can cover the full screen
    hide_taskbar(True)

    # 2) Open the URL in the default system browser
    webbrowser.open(URL, autoraise=True)
    time.sleep(WAIT_LAUNCH)

    # 3) Find the browser window and enter full screen
    hwnd = newest_visible_window()
    if not hwnd:
        raise RuntimeError("Browser window not found.")
    send_f11(hwnd)

    time.sleep(WAIT_FULLSCREEN)

    # 4) Minimize the browser window but keep the process running
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

finally:
    # 5) Restore the taskbar regardless of success or failure
    hide_taskbar(False)
