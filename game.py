import os
import sys

from alien_invasion import AlienInvasion


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores it in sys._MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
