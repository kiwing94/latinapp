from phrases import latin_phrases
from word_dict import latin_words
from grammar import detect_affixes, decline_noun, conjugate_verb

from random import choice

def get_word_type(word):
    if word.endswith('re'):
        return '[verb]'
    elif word.endswith('us'):
        return '[noun-2nd]'
    elif word.endswith('a'):
        return '[noun-1st]'
    elif word.endswith('is'):
        return '[noun-3rd]'
    elif word in ['et', 'sed', 'aut', 'quia', 'si', 'neque', 'autem']:
        return '[conjunction]'
    elif word in ['bene', 'male', 'nunc', 'hic']:
        return '[adverb]'
    elif word in ['ego', 'tu', 'ille', 'nos', 'vos', 'hic', 'haec', 'id']:
        return '[pronoun]'
    elif word in ['ad', 'ab', 'a', 'in', 'cum', 'pro', 'per']:
        return '[preposition]'
    else:
        return ''

def translate_input(text):
    words = text.strip().lower().split()
    translation = []
    for word in words:
        if word in latin_phrases:
            translation.append(latin_phrases[word])
        elif word in latin_words:
            translation.append(latin_words[word])
        else:
            translation.append(f"[{word}]")
    return ' '.join(translation)

def format_sentence(subject, obj, verb, order='SOV'):
    if order == 'SVO':
        return f'{subject} {verb} {obj}'
    elif order == 'VSO':
        return f'{verb} {subject} {obj}'
    return f'{subject} {obj} {verb}'

def sentence_metadata(latin, english, subject, obj, verb_inf):
    return {
        "latin": latin,
        "english": english,
        "subject_type": get_word_type(subject),
        "object_case": "accusative",
        "verb_infinitive": verb_inf
    }

def generate_sentence(order='SOV'):
    subjects = {
        "puella": "girl",
        "puer": "boy",
        "vir": "man",
        "femina": "woman",
        "dominus": "lord"
    }

    objects = {
        "librum": "book",
        "vocem": "voice",
        "puellam": "girl",
        "amicum": "friend"
    }

    verbs = {
        "amare": "love",
        "videre": "see",
        "audire": "hear",
        "scribere": "write"
    }

    subject = choice(list(subjects.keys()))
    obj = choice(list(objects.keys()))
    verb_inf = choice(list(verbs.keys()))

    if verb_inf.endswith("are"):
        conj = "1st"
    elif verb_inf.endswith("ere"):
        conj = "2nd"
    elif verb_inf.endswith("ire"):
        conj = "4th"
    else:
        conj = "3rd"

    verb = conjugate_verb(verb_inf[:-2], conj, 3)
    latin = format_sentence(subject, obj, verb, order=order)
    english = f"The {subjects[subject]} {verbs[verb_inf]}s the {objects[obj]}"

    return {
        "latin": latin,
        "english": english,
        "meta": sentence_metadata(latin, english, subject, obj, verb_inf)
    }

def generate_custom_sentence(subject, obj, verb_inf, order='SOV'):
    if verb_inf.endswith("are"):
        conj = "1st"
    elif verb_inf.endswith("ere"):
        conj = "2nd"
    elif verb_inf.endswith("ire"):
        conj = "4th"
    else:
        conj = "3rd"

    verb = conjugate_verb(verb_inf[:-2], conj, 3)
    latin = format_sentence(subject, obj, verb, order=order)
    english = f"The {latin_words.get(subject, subject)} {latin_words.get(verb_inf, verb_inf)}s the {latin_words.get(obj, obj)}"

    return {
        "latin": latin,
        "english": english,
        "meta": sentence_metadata(latin, english, subject, obj, verb_inf)
    }