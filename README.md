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
<img width="234" alt="image" src="https://github.com/mkm-cdnz/vectoring-words/assets/141604528/62c87184-353e-4744-b209-9b59e748856f">


# first-vector-4-gui.py
Performs simple word vector arithmetic
  e.g. 
  
  (king + woman) - man = queen
  
  (queen + man) - woman = king

  Words can be represented as vectors within a set of 300-dimensional coordinates. 
  By adding and subtracting these coordinates, language models can represent meanings and relationships between words or concepts mathematically. The words king and queen are approximately the same distance and direction away from each other in this 300-dimensional space as the words man is from woman. Vector arithmetic allows us to play with this concept and understand how computers infer relationships and assumptions programmed into human language.
  <img width="669" alt="image" src="https://github.com/mkm-cdnz/vectoring-words/assets/141604528/82c99f61-ee94-4f20-992c-bb1c4edac61b">
  <img width="454" alt="image" src="https://github.com/mkm-cdnz/vectoring-words/assets/141604528/c5f5c008-fa09-4fa3-9606-d3d01ee5dbca">




