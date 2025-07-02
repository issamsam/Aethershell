import platform
import shutil
import os

def detect_package_manager():
    if shutil.which("apt"):
        return "apt"
    elif shutil.which("dnf"):
        return "dnf"
    elif shutil.which("pacman"):
        return "pacman"
    elif shutil.which("zypper"):
        return "zypper"
    return "unknown"

def detect_session():
    return os.environ.get("XDG_SESSION_DESKTOP", "unknown")

def detect_apps(apps):
    return [app for app in apps if shutil.which(app)]

def get_context_summary():
    return {
        "os": platform.system() + " " + platform.release(),
        "package_manager": detect_package_manager(),
        "session": detect_session(),
        "browsers": detect_apps(["firefox", "chrome", "chromium", "brave"]),
        "text_editors": detect_apps(["code", "nano", "gedit", "vim"])
    }
