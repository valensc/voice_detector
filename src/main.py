import sys
from PyQt6.QtWidgets import QApplication
from gui import VoiceDetectorApp

def main():
    app = QApplication(sys.argv)
    window = VoiceDetectorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()