import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap, QRegion, QBitmap, QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect, QSize


# ____________________________________________________________
def add_litergue(func):
    def wrapper(*args, **kwargs):
        print("^You add litergue^")
        func(*args, **kwargs)
    return wrapper

def add_dress(func):
    def wrapper(*args, **kwargs):
        print("^You add dress^")
        func(*args, **kwargs)
    return wrapper

@add_litergue
@add_dress
def get_boobs(size):
    print(F"Here is your {size} size boobs")


# ____________________________________________________________


file_path = "test.txt"

def check():
    search_for = input("What do you search for?\n")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if search_for in line:
                print(F"{search_for} was found on {line_num} line")

# ____________________________________________________________

POKEMON_API = "https://pokeapi.co/api/v2/"

def get_pokemon_info():
    pokemon_name = input("Enter the pokemon name: ")
 
    url = f"{POKEMON_API}/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Undefined issue, try different name")
        get_pokemon_info()

        
# ______________________________________________________


class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        self.window_width = int(screen_width / 1.5)
        self.window_height = int(screen_height / 1.5)

        self.resize(self.window_width, self.window_height)

        self.move(int((screen_width - self.window_width)/2),
                  int((screen_height - self.window_height)/2))
        
        self.setWindowFlags(
            Qt.CustomizeWindowHint |
            Qt.WindowMinMaxButtonsHint |
            Qt.WindowCloseButtonHint
        )
        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon("assets/app_ass)/0111.gif"))


        self.setStyleSheet("""
            QMainWindow     {background-color: #8b6968;
                            }
            QMainWindow::title{font-size: 0px;
                            background-color: transparent;
                            }
        """)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()