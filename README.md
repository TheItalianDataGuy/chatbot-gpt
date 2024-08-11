# Chatbot GUI Application

This project is a simple Chatbot GUI application built using Python and the PyQt6 framework. The application provides a user-friendly interface for interacting with a chatbot, where users can input their queries, and the chatbot will respond with appropriate answers.

## Features

- **User-Friendly Interface:** A graphical interface that allows users to interact with the chatbot by typing messages and receiving responses.
- **Real-Time Communication:** Supports real-time communication between the user and the chatbot.
- **Threading for Performance:** Utilizes threading to reduce latency and ensure a smooth user experience.

## Prerequisites

- Python 3.x
- PyQt6
- Any required dependencies from the `backend.py` (e.g., Chatbot class)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chatbot-gui.git
   cd chatbot-gui

2. Install the required Python packages:
  ```bash
  pip install PyQt6
  ```

3. Ensure you have the backend.py file in the project directory, which contains the Chatbot class handling the chatbot's logic.

## Usage
Run the application using Python:

  ```bash
  python main.py
```
The application window will open, allowing you to type messages in the input area and press "Send" to interact with the chatbot.

## Extending the Project
You can extend this project by improving the Chatbot class in the backend.py file, integrating with more advanced AI models, or enhancing the user interface with additional features such as voice input, file attachments, etc.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
