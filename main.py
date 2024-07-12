from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, \
    QPushButton, QApplication
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 700)

        # Add the chat area
        self.chat_area = QTextEdit(self)
        # Add the input area
        self.input_area = QLineEdit(self)
        # Add the button send
        self.chat_area = QPushButton("Send", self)

        self.show()


class Chatbot:
    pass


# Instantiate the app
app = QApplication(sys.argv)
# Instantiate the window
chatbot_window = ChatbotWindow()
# sys.exit to exit the app
sys.exit(app.exec())
