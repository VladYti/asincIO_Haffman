import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QHBoxLayout, QGroupBox
import threading_function
import async_function
import th_func_2


class Window(QWidget):



    def __init__(self):
        super().__init__()
        self.initUI()
        self.result = []

    def initUI(self):
        # Create main layout

        self.main_layout = QVBoxLayout()

        ##############################################

        # Create top top HBoxLayout

        self.top_layout = QHBoxLayout()

        self.groupbox_thread = QGroupBox("Threading execute")
        self.group_thread = QVBoxLayout()
        self.groupbox_thread.setLayout(self.group_thread)

        self.groupbox_async = QGroupBox('Async execute')
        self.group_async = QVBoxLayout()
        self.groupbox_async.setLayout(self.group_async)

        self.top_layout.addWidget(self.groupbox_thread)
        self.top_layout.addWidget(self.groupbox_async)

        # Create first group components

        self.label1 = QLabel('Enter the name of text files')
        self.line1 = QLineEdit()
        self.line1.setPlaceholderText('text_file1')
        self.button1 = QPushButton('TExecute')
        self.button1.clicked.connect(self.on_button_th_click)

        self.group_thread.addWidget(self.label1)
        self.group_thread.addWidget(self.line1)
        self.group_thread.addWidget(self.button1)

        # Create second group components

        self.label2 = QLabel('Enter the name of text files')
        self.line2 = QLineEdit()
        self.line2.setPlaceholderText('text_file1')
        self.button2 = QPushButton('AExecute')
        self.button2.clicked.connect(self.on_button_as_click)

        self.group_async.addWidget(self.label2)
        self.group_async.addWidget(self.line2)
        self.group_async.addWidget(self.button2)

        # Create bottom layout

        self.bot_layout = QHBoxLayout()

        self.text_ed = QTextEdit()
        self.text_ed.setReadOnly(True)
        self.bot_layout.addWidget(self.text_ed)

        ########################################

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bot_layout)

        self.setLayout(self.main_layout)
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('QSplitter demo')
        self.show()


    def on_button_th_click(self):

        input_str = self.line1.text()
        list_of_text_files = input_str.split(',')
        for count, item in enumerate(list_of_text_files):
            list_of_text_files[count] = item.replace(' ', '')
        print(list_of_text_files)



        threading_function.thread_func(list_of_text_files, self.result)

        for item in self.result:
            self.text_ed.append(str(item) + '\n')
        self.line1.setText('')

    def on_button_as_click(self):
        self.text_ed.append(str(self.result) + '\n')
        self.line2.setText('')
        pass
        # input_str = self.line2.text().replace(' ', '')
        # result = async_function.async_func(input_str)
        # self.text_ed.append(str(result) + '\n')
        # self.line2.setText('')





app = QApplication(sys.argv)
w = Window()
app.exec()
