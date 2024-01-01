import asyncio
from typing_test import setup_typing_test, typing_test
from text_processing import fetch_1000_unique_texts, select_n_texts_from_pool
from results_display import display_results

async def main():
    print("\nWelcome to the Typing Tester!"
          "\nTest your typing speed and accuracy here."
          "\nChoose a difficulty level - Easy (20-60 characters), Medium (60-100 characters), or Hard (100-140 characters)."
          "\nType 1 to 10 text examples, randomly selected from a pool of 1000."
          "\nMistakes will be highlighted with red, and your typing speed and accuracy will be calculated."
          "\n\nOptionally, use Text-to-Speech (TTS) to hear the texts."
          "\nNote: TTS doesn't read punctuation, commas, spaces, or indicate capital letters."
          "\nPay attention to these on the screen while typing.")

    while True:
        difficulty, n, use_tts = setup_typing_test()

        all_texts = await fetch_1000_unique_texts()
        texts = select_n_texts_from_pool(all_texts, n, difficulty)
        timings, accuracies = typing_test(texts, use_tts)
        display_results(timings, accuracies, texts)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing Typing Tester, have a lovely day.")

asyncio.run(main())
