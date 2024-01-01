import time
import pyttsx3
import difflib
from colorama import Fore, Style
from text_processing import longest_common_subsequence

def calculate_accuracy(typed_text, original_text):
    lcs = longest_common_subsequence(typed_text, original_text)
    return lcs / len(original_text) * 100 if original_text else 0

def highlight_mistakes(original_text, user_input):
    original_words = original_text.split()
    user_words = user_input.split()
    matcher = difflib.SequenceMatcher(None, original_words, user_words)
    highlighted_text = ""
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            highlighted_text += " ".join(user_words[j1:j2]) + " "
        else:
            highlighted_text += f"{Fore.RED}{' '.join(user_words[j1:j2])}{Style.RESET_ALL} "
    return highlighted_text

def typing_test(texts, use_tts):
    engine = pyttsx3.init() if use_tts else None
    timings = []
    accuracies = []

    for text in texts:
        print("\nType this text:\n", text)
        if use_tts:
            engine.say(text)
            engine.runAndWait()
        start_time = time.time()
        typed_text = input("\nYour input: ")
        end_time = time.time()

        time_taken = end_time - start_time
        accuracy = calculate_accuracy(typed_text, text)
        timings.append(time_taken)
        accuracies.append(accuracy)

        highlighted_text = highlight_mistakes(text, typed_text)
        print(f"\nYour input with mistakes highlighted:\n{highlighted_text}")

    return timings, accuracies

def setup_typing_test():
    difficulty = get_difficulty_level()
    n = get_number_of_tests()
    use_tts = ask_for_tts()
    return difficulty, n, use_tts

def get_difficulty_level():
    while True:
        difficulty = input("\nChoose your difficulty (easy, medium, hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

def get_number_of_tests():
    while True:
        try:
            n = int(input("\nChoose the number of text examples to test (1-10): "))
            if 1 <= n <= 10:
                return n
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def ask_for_tts():
    while True:
        use_tts = input("\nDo you want to use text-to-speech for the text examples? (yes/no): ").lower()
        if use_tts in ['yes', 'no']:
            return use_tts == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
