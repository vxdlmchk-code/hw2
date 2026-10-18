from PyQt6.QtWidgets import QMainWindow, QFrame, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PyQt6.QtCore import Qt
from modules.app import app 


main_window = QMainWindow()
main_window.setWindowTitle("Weather app")

WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()

main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

frame_0 = QFrame(parent=main_window)
frame_0.setStyleSheet("background-color: gray;")
frame_0.resize(WIDTH_WINDOW, HEIGHT_WINDOW)

grid_layout = QGridLayout()
grid_layout.setSpacing(15)
frame_0.setLayout(grid_layout)


for column in range(3):
    red_card = QFrame(parent=frame_0)
    red_card.setStyleSheet("background-color: red;")
    grid_layout.addWidget(red_card, 0, column)

    if column in (0, 2):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        horizontal_layout.setSpacing(35)
        red_card.setLayout(horizontal_layout)

        white_box = QFrame(parent=red_card)
        white_box.setFixedSize(50, 50)
        white_box.setStyleSheet("background-color: white;")

        gray_box = QFrame(parent=red_card)
        gray_box.setFixedSize(50, 50)
        gray_box.setStyleSheet("background-color: lightgray;")

        horizontal_layout.addWidget(white_box)
        horizontal_layout.addWidget(gray_box)


for column in range(3):
    green_card = QFrame(parent=frame_0)
    green_card.setStyleSheet("background-color: green;")
    grid_layout.addWidget(green_card, 1, column)

    vertical_layout = QVBoxLayout()
    vertical_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    green_card.setLayout(vertical_layout)

    label_1 = QLabel(text="Лейбл 1", parent=green_card)
    label_1.setStyleSheet("font-size: 14px; color: black; font-weight: bold;")
    
    label_2 = QLabel(text="Лейбл 2", parent=green_card)
    label_2.setStyleSheet("font-size: 14px; color: black; font-weight: bold;")

    vertical_layout.addWidget(label_1)
    vertical_layout.addWidget(label_2)

for column in range(3):
    blue_card = QFrame(parent=frame_0)
    blue_card.setStyleSheet("background-color: blue;")
    grid_layout.addWidget(blue_card, 2, column)

    if column in (0, 2):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        horizontal_layout.setSpacing(35)
        blue_card.setLayout(horizontal_layout)

        white_box = QFrame(parent=blue_card)
        white_box.setFixedSize(50, 50)
        white_box.setStyleSheet("background-color: white;")

        gray_box = QFrame(parent=blue_card)
        gray_box.setFixedSize(50, 50)
        gray_box.setStyleSheet("background-color: lightgray;")

        horizontal_layout.addWidget(white_box)
        horizontal_layout.addWidget(gray_box)