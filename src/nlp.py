import spacy
import string

nlp = spacy.load("pt_core_news_md")


def remove_punctuation(s: str) -> str:
    return s.translate(str.maketrans("", "", string.punctuation))


def remove_stop_words(nlp_str):
    return nlp(" ".join([token.text for token in nlp_str if not token.is_stop]))


def lemmatize(nlp_str):
    return nlp(" ".join([token.lemma_ for token in nlp_str]))


def preprocess(s: str):
    fmt_str = remove_punctuation(s.strip().lower())
    nlp_str = nlp(fmt_str)
    return lemmatize(remove_stop_words(nlp_str))
