# vectoring-words
Dinky little toys for helping to understand and explain how computers "understand" language for Natural Language Processing (NLP) purposes

# GoogleNews-vectors-negative300.bin
Many of these scripts utilize The "GoogleNews-vectors-negative300.bin" file, not included in this repository but freely available for download. 
This is a pre-trained Word2Vec model provided by Google.

It was trained on a part of the Google News dataset, containing about 100 billion words.
The model contains 300-dimensional vectors for 3 million words and phrases.
Uncompressed, this file is approximately 3.39 GB. So it might take a while for anything to happen when first running. Subsequent prompts will be speedier though.

**Here's a breakdown of what each part of the file name means:**
"GoogleNews": This indicates that the model was trained on a dataset from Google News.
"vectors": This indicates that the file contains word vectors, which are multi-dimensional representations of words.
"negative300": This indicates that the model uses 300 dimensions and was trained using negative sampling, a method for improving the speed and quality of the training process.

***

# closest-word-2.py 
prints the three words whose vectors are closest to any word the user inputs

# first-vector-4-gui.py
Performs simple word vector arithmetic
  e.g. 
  (king + womaman) - man = queen
  (queen + man) - woman = king

# prompt-for-gui.html
The prompt used to generate **first-vector-1-gui.py** in GPT-4. Uses Nested HTML-style tags to create human-readable prompts that are specific in said prompt's requirements.
