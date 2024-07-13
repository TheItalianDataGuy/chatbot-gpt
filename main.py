from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, \
    QPushButton, QApplication
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        """This method creates the GUI app"""
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add the chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320) # 10 from side and upper body of the window, width, height
        self.chat_area.setReadOnly(True) # The content cannot be modified

        # Add the input area
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 340, 480, 40)
        self.input_area.returnPressed.connect(self.send_message) # This allows to use the enter key to send the message

        # Add the button Send
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)
        self.show()

    def send_message(self):
        """This method allows to communicate with the gpt3.5-turbo"""
        # Extract the user input
        user_input = self.input_area.text().strip()

        # Add the user input into the chat area
        self.chat_area.append(f"<p style='color: #333333'>Me: {user_input}</p>")
        self.input_area.clear()

        # Adding the thread will reduce the latency of the user input in the chat area
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        """This method add the response of the model to the chat area"""
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333'; background-color: #E9E9E9>Chatbot: {response}</p>")


# Instantiate the app
app = QApplication(sys.argv)
# Instantiate the window
chatbot_window = ChatbotWindow()
# sys.exit to exit the app
sys.exit(app.exec())
