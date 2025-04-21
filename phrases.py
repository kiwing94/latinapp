# phrases.py

# Expanded Latin phrases and quotes
latin_phrases = {
    "carpe diem": "seize the day",
    "tempus fugit": "time flies",
    "in vino veritas": "in wine, truth",
    "veni, vidi, vici": "I came, I saw, I conquered",
    "amor fati": "love of fate",
    "et tu, Brute?": "and you, Brutus?",
    "memento mori": "remember that you will die",
    "sic parvis magna": "greatness from small beginnings",
    "ad astra per aspera": "to the stars through difficulties",
    "non ducor, duco": "I am not led, I lead",
    "audentes fortuna iuvat": "fortune favors the bold",
    "vox populi, vox dei": "the voice of the people is the voice of God",
    "quid pro quo": "something for something",
    "nunc est bibendum": "now is the time to drink",
    # Complex Quotes
    "cogito ergo sum": "I think, therefore I am",  # René Descartes
    "hic et nunc": "here and now",  # Latin philosophical phrase
    "primum vivere, deinde philosophari": "first live, then philosophize",  # Epicurus
    "vita brevis, ars longa": "life is short, art is long",  # Hippocrates
    "dum spiro, spero": "while I breathe, I hope",  # Cicero
    "natura abhorret a vacuo": "nature abhors a vacuum",  # Aristotle
    "omnia vincit amor": "love conquers all",  # Virgil
    "quidquid latine dictum sit altum videtur": "anything said in Latin seems profound",  # Seneca
    "fortuna audaces iuvat": "fortune favors the bold",  # Virgil
    "nemo me impune lacessit": "no one provokes me with impunity",  # Motto of Scotland
    "Nōx obſcūrrīma aurilūcspīculum ſperā": "Even in the darkest night, wait for the glimmer of dawn.",
    "Pulvis et umbra sumus": "We are but dust and shadow",
    "Nosce te ipsum": "Know yourself"
}

# Function to handle phrase translation
def translate_phrase(latin_phrase):
    """Translate a Latin phrase to English, ensuring case insensitivity and proper matching."""
    normalized_phrase = latin_phrase.strip().lower()
    return latin_phrases.get(normalized_phrase, None)
