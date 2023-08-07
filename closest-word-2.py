from gensim.models import KeyedVectors

# Load vectors directly from the file
model = KeyedVectors.load_word2vec_format(r'C:\Users\matth\OneDrive\Desktop\ClearPoint\Projects\ChatGPT n LLMs - CPcGPTnLLMs\vector stuff\GoogleNews-vectors-negative300.bin', binary=True)

while True:
    # Get user input
    word = input("Enter a word (or 'quit' to exit): ")

    # Check if the user wants to quit
    if word.lower() == 'quit':
        break

    # Find the closest words
    try:
        closest_words = model.most_similar(positive=[word], topn=3)

        # Print the results
        print("Closest words:")
        for word, similarity in closest_words:
            print(f"{word}: {similarity}")
    except KeyError:
        print("The word you entered is not in the model's vocabulary. Please try again.")

print("Goodbye!")
