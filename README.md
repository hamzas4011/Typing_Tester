# ✨ Typing Tester 🎯

**Typing Tester** is a Python-based application designed to measure typing speed and accuracy. This project was developed as part of a **home exam** for the course **ACIT4420: Problem-solving with Scripting** in the **Applied Computer and Information Technology** master's program at **Oslo Metropolitan University**.

The application leverages **object-oriented programming (OOP)** principles, utilizing **classes and methods** to organize the functionality into modular and reusable components. It includes accessibility features, such as a **text-to-speech (TTS)** function powered by the `pyttsx3` library, and integrates **Python APIs** for enhanced text processing and randomization.

Real-time performance analysis is provided, including detailed metrics for typing accuracy and speed, with visual results generated using **matplotlib**. The project is designed with accessibility and user experience in mind, offering options to adjust difficulty levels, track errors, and visualize performance data effectively.

---

## 🚀 Features

- 🎯 **Typing Speed and Accuracy Test:**
  - Three difficulty levels: Easy, Medium, and Hard.
  - Select from 1 to 10 typing examples in a session.
  - Mistake tracking with highlighted errors for better feedback.

- 🧑‍🤝‍🧑 **Accessibility Features:**
  - Includes a **Text-to-Speech (TTS)** option to read the text aloud, improving accessibility for users with visual impairments.

- 📊 **Performance Metrics:**
  - Displays results, including accuracy, time per text, and average metrics.
  - Visual performance charts are generated using `matplotlib`.

- 🔗 **Modular Codebase:**
  - Uses **object-oriented programming (OOP)** to separate logic into reusable and maintainable components.

---

## 🖼️ Screenshots

[Add your screenshots here.]

---

## 🛠️ Technologies Used

- 🐍 **Python**: The main programming language for the project.
- 🌐 **API**: Used for text generation and processing.
- 📊 **Matplotlib**: For generating performance visualizations.
- 🎨 **Colorama**: For terminal text styling.
- 🗣️ **Pyttsx3**: For the Text-to-Speech (TTS) functionality.
- 🏗️ **Object-Oriented Programming (OOP)**: To ensure a modular and reusable codebase.

---

## 📥 Installation and Setup

Follow these steps to run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hamzas4011/Typing_Tester.git
   cd Typing_Tester
   ```

2. **Create a Virtual Environment (optional but recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   Install all the required libraries listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

## ♿ Accessibility Considerations

- This project includes **Text-to-Speech (TTS)** functionality to improve usability and inclusivity, especially for users with visual impairments or other accessibility needs.

---

## 📌 Notes for Users

To minimize installation issues, ensure you use the provided `requirements.txt` to install dependencies. This will set up all necessary libraries (e.g., `matplotlib`, `pandas`, `aiohttp`, `colorama`, and `pyttsx3`) in a single command. Running the application in **PyCharm** is straightforward if you configure your Python interpreter and virtual environment properly.
