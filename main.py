import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import LeetCodeStyleApp
from leaderboard import setup_db

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LeetCodeStyleApp()
    window.show()
    sys.exit(app.exec())
