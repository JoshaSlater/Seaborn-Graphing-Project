import spacy
import spacy.cli
spacy.cli.download("en_vectors_web_lg")
nlp = spacy.load("en_vectors_web_lg")