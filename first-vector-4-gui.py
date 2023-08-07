import tkinter as tk
from tkinter import ttk, font, messagebox
from ttkthemes import ThemedTk
from gensim.models import KeyedVectors
from threading import Thread
import time

# Load vectors directly from the file
model = KeyedVectors.load_word2vec_format(r'C:\Users\matth\OneDrive\Desktop\ClearPoint\Projects\ChatGPT n LLMs - CPcGPTnLLMs\vector stuff\GoogleNews-vectors-negative300.bin', binary=True)

def run_operation():
    # Start the loading indicator
    loading_indicator.start()

    # Get user input
    positive_words = positive_words_entry.get().split()
    negative_words = negative_words_entry.get().split()

    # Perform vector arithmetic and find the closest vector
    try:
        closest_word = model.most_similar(positive=positive_words, negative=negative_words, topn=1)
        # Display the result
        output_text.insert(tk.END, str(closest_word) + '\n')
    except KeyError as e:
        output_text.insert(tk.END, f"Word {e.args[0]} not in vocabulary. Please try again.\n")

    # Stop the loading indicator
    loading_indicator.stop()

# Create the main window
root = ThemedTk(theme="black")
root.title('Word Vector Arithmetic')

# Define a large, bright green font
large_font = font.Font(size=14)
bright_green = '#00FF00'

# Create the entry for positive words
tk.Label(root, text='Enter the words to be added, separated by spaces', fg=bright_green, bg='black', font=large_font).pack()
positive_words_entry = tk.Entry(root, font=large_font)
positive_words_entry.pack()

# Create the entry for negative words
tk.Label(root, text='Enter the words to be subtracted, separated by spaces', fg=bright_green, bg='black', font=large_font).pack()
negative_words_entry = tk.Entry(root, font=large_font)
negative_words_entry.pack()

# Create the run button
run_button = tk.Button(root, text='Run', command=lambda: Thread(target=run_operation).start(), font=large_font)
run_button.pack()

# Create the loading indicator
loading_indicator = ttk.Progressbar(root, mode='indeterminate')
loading_indicator.pack()

# Create the output text area
output_text = tk.Text(root, fg=bright_green, bg='black', font=large_font)
output_text.pack()

# Start the main loop
root.mainloop()
