# ✨ Typing Tester 🎯

**Typing Tester** is a Python-based application designed to measure typing speed and accuracy. This project was developed as part of a **home exam** for the course **ACIT4420: Problem-solving with Scripting** in the **Applied Computer and Information Technology** master's program at **Oslo Metropolitan University**. 

The application includes accessibility features, such as a **text-to-speech (TTS)** function, and uses Python APIs for enhanced functionality. It also provides real-time performance analysis with visual results using **matplotlib**.

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

---

## 🖼️ Screenshots

[Add your screenshots here.]

---

## 🛠️ Technologies Used

- 🐍 **Python**: The main programming language for the project.
- 🌐 **APIs**: Used for text generation and processing.
- 📊 **Matplotlib**: For generating performance visualizations.
- 🎨 **Colorama**: For terminal text styling.
- ♿ **Accessibility Features**: Includes TTS using the `pyttsx3` library.

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

---

## 🏫 About

This project was completed as part of a home exam during my **master's studies in Applied Computer and Information Technology** at **Oslo Metropolitan University**. It demonstrates problem-solving with Python scripting and accessibility considerations for practical application development.
