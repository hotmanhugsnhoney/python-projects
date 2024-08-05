# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:24:40 2024

@author: willh
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

class xo_board(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0  # Initialize turn counter
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("X's and O's")
        self.setGeometry(100, 100, 400, 150)
        
        self.label = QLabel(self)
        
        grid_layout = QGridLayout()
        
        self.rowcol = []
        
        for row in range(3):
            for col in range(3):
                button = QPushButton(f'Button{row},{col}', self)
                button.setText('')
                grid_layout.addWidget(button, row, col)
                self.rowcol.append(button)
                button.clicked.connect(lambda checked, btn=button: self.handle_button_click(btn))
                
        self.setLayout(grid_layout)
        # self.show()
        
    def win_condition(self):
        # across
        for row in range(3):
            if (self.rowcol[row*3].text() != '' and
                self.rowcol[row*3].text() == self.rowcol[row*3 + 1].text() and
                self.rowcol[row*3].text() == self.rowcol[row*3 + 2].text()):
                self.win(self.rowcol[row*3], self.rowcol[row*3 + 1], self.rowcol[row*3 + 2])
                return
        for col in range(3):
            if (self.rowcol[col].text() != '' and
                self.rowcol[col].text() == self.rowcol[col + 3].text() and
                self.rowcol[col].text() == self.rowcol[col + 6].text()):
                self.win(self.rowcol[row*3], self.rowcol[col + 3], self.rowcol[col + 6])
                return
        if (self.rowcol[0].text() != '' and
            self.rowcol[0].text() == self.rowcol[4].text() and
            self.rowcol[0].text() == self.rowcol[8].text()):
            self.win(self.rowcol[0], self.rowcol[4], self.rowcol[8])
            return

        if (self.rowcol[2].text() != '' and
            self.rowcol[2].text() == self.rowcol[4].text() and
            self.rowcol[2].text() == self.rowcol[6].text()):
            self.win(self.rowcol[2], self.rowcol[4], self.rowcol[6])
            return
            
    def win(self, ac,do,di):
        self.label.setText(f"{ac.text()} Wins!")
        self.label.setText(f"{do.text()} Wins!")
        self.label.setText(f"{di.text()} Wins!")
        self.disable()
        if self.check_turn() != self.win_condition():
            print('Tie game')
            self.disable()
        
    def handle_button_click(self, button):
        if button.text() == '':
            player = self.check_turn()
            button.setText(player)
            if player == 'X':
                button.setStyleSheet("background-color: green; color: white;")
            else:
                button.setStyleSheet("background-color: blue; color: white;")
            self.turn += 1  # Increment the turn counter
        self.win_condition()
            
    def disable(self):
        # self.rowcol()
        for buttons in self.rowcol:
            buttons.setEnabled(False)
        
    def check_turn(self):
        if self.turn % 2 == 0:
            return 'X'
        else:
            return 'O'
        
        # self.win_condition()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_gui = xo_board()
    my_gui.show()
    sys.exit(app.exec())