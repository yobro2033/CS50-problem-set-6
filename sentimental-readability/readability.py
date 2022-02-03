import re

text = str(input("Text: "))

text = text.replace("'", "")
text = text.replace("-", "")

textSC = re.sub(r"[^a-zA-Z0-9]+", ' ', text)
texts = textSC.split()
wordsLength = len(texts)
totalLetters = 0
sentences = re.split(r"\. |\? |\! ", text)
sentencesLength = len(sentences)

if wordsLength != 0:
    for word in texts:
        totalLetters = totalLetters + len(word)
    L = 100*totalLetters/wordsLength

S = 100*sentencesLength/wordsLength

equations = (0.0588 * L) - (0.296 * S) - 15.8

if equations <0:
    print("Before Grade 1")
elif equations > 16:
    print("Grade 16+")
else:
    result = round(equations)
    print("Grade", result)