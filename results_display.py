import matplotlib.pyplot as plt
import pandas as pd

def display_results(timings, accuracies, texts):
    words_per_minute = [60 / t * len(text.split()) for t, text in zip(timings, texts)]

    plt.bar(range(1, len(words_per_minute) + 1), words_per_minute)
    plt.xlabel('Text Number')
    plt.ylabel('Words per Minute')
    plt.title('Typing Speed for Each Text')
    plt.xticks(range(1, len(words_per_minute) + 1))  # This line sets the x-axis ticks to start from 1
    plt.show(block=False)

    print("\nClose this bar chart to see average accuracy and timing")

    try:
        plt.waitforbuttonpress()
    except Exception:
        pass

    plt.close()

    avg_accuracy = sum(accuracies) / len(accuracies)
    avg_timing = sum(timings) / len(timings)

    results_df = pd.DataFrame({'Text Number': range(1, len(texts) + 1), 'Accuracy (%)': accuracies,
                               'Time per Text (seconds)': timings})

    avg_results_df = pd.DataFrame(
        {'Average Accuracy (%)': [avg_accuracy], 'Average Time per Text (seconds)': [avg_timing]})

    print("\nResults:")
    print(results_df.to_string(index=False))
    print("\nAverage Results:")
    print(avg_results_df.to_string(index=False))
