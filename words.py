

# Mapping Latin words to English words
latin_words = {
    'vita': 'life',
    'amor': 'love',
    'libertas': 'freedom',
    'amare': 'to love',
    'videre': 'to see',
    'scribere': 'to write',
    'magnus': 'great',
    'parvus': 'small',
    'bonus': 'good',
    'puella': 'girl',
    'puer': 'boy',
    'domus': 'house',
    'femina': 'woman',
    'vir': 'man',
    'lux': 'light',
    'tenebrae': 'darkness',
    'deus': 'god',
    'nox': 'night',
    'pater noster': 'our father',
    'sanctus': 'holy, sacred',
    'argumentus': 'proof, claim to have proof',
    'dominus': 'lord, master',
    'arithmetica': 'numbers',
    'vox': 'voice',

    # Verbs (Conjugations)
    'amare': 'to love',
    'videre': 'to see',
    'scribere': 'to write',
    'dicere': 'to say',
    'audire': 'to hear',
    'cogitare': 'to think',
    'esse': 'to be',

    # Adjectives (Agreement in gender, number, case)
    'magnus': 'great',
    'parvus': 'small',
    'bonus': 'good',
    'malus': 'bad',
    'felix': 'happy',
    'fortis': 'strong',

    # Pronouns
    'ego': 'I',
    'tu': 'you',
    'ille': 'he, she, it',
    'nos': 'we',
    'vos': 'you (plural)',
    'hic': 'this (masc.)',
    'haec': 'this (fem.)',
    'id': 'it',

    # Prepositions
    'ad': 'to, toward',
    'ab': 'from, by',
    'a': 'from, by (used before consonants)',
    'ante': 'before',
    'cum': 'with',
    'in': 'in, on, into',
    'inter': 'between, among',
    'per': 'through, by',
    'post': 'after',
    'pro': 'for, on behalf of',
    'sine': 'without',
    'sub': 'under, beneath',
    'super': 'above, on top of',
    'trans': 'across',
    'extra': 'outside of',
    'infra': 'below, under',

    # Conjunctions
    'et': 'and',
    'sed': 'but',
    'aut': 'or',
    'quia': 'because',
    'si': 'if',
    'neque': 'and not, neither',
    'autem': 'however',

    # Adverbs
    'bene': 'well',
    'male': 'badly',
    'celeriter': 'quickly',
    'fortiter': 'bravely',
    'hic': 'here',
    'nunc': 'now',

    # Interjections
    'heu': 'alas',
    'eheu': 'oh no',
    'vae': 'woe',
    'viva': 'long live',

   # Basic Latin numerals
    'nihil': 'zero',
    'unus': 'one',
    'duo': 'two',
    'tres': 'three',
    'quattuor': 'four',
    'quinque': 'five',
    'sex': 'six',
    'septem': 'seven',
    'octo': 'eight',
    'novem': 'nine',
    'decem': 'ten',
    'undecim': 'eleven',
    'duodecim': 'twelve',
    'tredecim': 'thirteen',
    'quattuordecim': 'fourteen',
    'quindecim': 'fifteen',
    'sedecim': 'sixteen',
    'septendecim': 'seventeen',
    'duodeviginti': 'eighteen',
    'undeviginti': 'nineteen',
    'viginti': 'twenty',
    'triginta': 'thirty',
    'quadraginta': 'forty',
    'quinquaginta': 'fifty',
    'sexaginta': 'sixty',
    'septuaginta': 'seventy',
    'octoginta': 'eighty',
    'nonaginta': 'ninety',
    'centum': 'one hundred',
    'mille': 'one thousand',

    # Compound forms (optional, can be expanded)
    'viginti unus': 'twenty-one',
    'triginta duo': 'thirty-two',
    'quadraginta tres': 'forty-three',
    'quinquaginta quattuor': 'fifty-four',
    'sexaginta quinque': 'sixty-five',
    'septuaginta sex': 'seventy-six',
    'octoginta septem': 'eighty-seven',
    'nonaginta octo': 'ninety-eight',
    'undecentum': 'ninety-nine',














}


def translate_word(latin_word):
    """Translate a single Latin word to English."""
    return latin_words.get(latin_word.lower(), None)
