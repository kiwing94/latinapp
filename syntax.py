# syntax.py

# Function to detect sentence structure (SVO or SOV)
def detect_syntax(sentence):
    subject = None
    verb = None
    object_ = None

    # Iterate through words and find subject, verb, and object based on dependency parsing
    for word in sentence.words:
        if word.deps is not None:  # Check if the word has dependency information
            # Check for the dependency relation (e.g., subject, object, verb)
            if 'nsubj' in word.deps:  # Subject
                subject = word.text
            elif 'root' in word.deps and word.pos == 'VERB':  # Root verb
                verb = word.text
            elif 'dobj' in word.deps:  # Object
                object_ = word.text

    # Return the syntax type based on the order of subject, verb, and object
    if subject and verb and object_:
        # Check if the verb is before the object (SVO) or after (SOV)
        if sentence.words.index(verb) < sentence.words.index(object_):
            return 'SVO', subject, verb, object_
        else:
            return 'SOV', subject, verb, object_
    return None, None, None, None

# Function to reorder sentence based on detected syntax
def reorder_sentence(syntax, subject, verb, object_):
    if syntax == 'SVO':
        return f"The {subject} {verb} {object_}."
    elif syntax == 'SOV':
        return f"The {subject} {object_} {verb}."
    return f"The {subject} {verb} {object_}."
