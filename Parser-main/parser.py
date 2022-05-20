import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tree import *
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""



NONTERMINALS = """
S -> N V
NP -> N | Det N |P N | Adj N | V N
VP -> V P | Adv V | V Adv
S -> N V NP
S -> N V NP NP
S -> N V P Det NP Conj N V
S -> NP V Det NP
S -> N VP NP Conj N VP NP Adv
S -> N VP Conj V NP
S -> N V Det NP NP Conj NP P Det NP
S -> N V Det Adj Adj NP P NP P NP
"""


grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """

    sent = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    st = tokenizer.tokenize(sent)

    return st

    # raise NotImplementedError


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    noun_phrases_list = []
    if (tree.label() == "NP"):
        noun_phrases_list.append( tree.copy(True) )
    for child in tree:
        if (type(child) is Tree):
            phrase = np_chunk(child)
            if (len(phrase) > 0):
                noun_phrases_list.extend(phrase)
    return noun_phrases_list

    # return noun_phrases_list
    # raise NotImplementedError


if __name__ == "__main__":
    main()
