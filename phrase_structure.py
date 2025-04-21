
# phrase_structure.py

def apply_svo_rules(subject, verb, object_):
    """Apply basic SVO rules for English."""
    # Ensure "only" is at the end of the sentence and "us" comes before "only"
    return f"The {subject} of {object_} {verb} us only."

def apply_sov_rules(subject, object_, verb):
    """Apply basic SOV rules for languages like Japanese or Latin."""
    return f"The {subject} {object_} {verb}."

def apply_verb_conjugation(verb, tense, person):
    """Handle basic verb conjugation."""
    # Simplified tense handling (can be expanded for Latin)
    if tense == "present" and person == "third":
        return verb  # Present tense, third person
    elif tense == "past":
        # Example of past tense conjugation rule (simplified)
        return verb + "ed"  # This is simplified; for Latin, we would need more rules
    elif tense == "future":
        return f"will {verb}"  # Future tense
    return verb

def apply_adjective_noun_agreement(adjective, noun):
    """Handle adjective-noun agreement (simplified for example)."""
    # Example: In Latin, adjectives agree in case, gender, and number with nouns.
    # In English, adjectives usually stay the same, but we could add rules for Latin.
    return f"{noun} {adjective}"

def handle_passive_voice(subject, verb, object_):
    """Handle passive voice conversion."""
    return f"The {object_} is {verb} by the {subject}"

def handle_phrase_structure(sentence_structure, subject, verb, object_, tense="present", person="third"):
    """Apply the correct phrase structure based on the detected syntax."""
    if sentence_structure == 'SVO':
        return apply_svo_rules(subject, verb, object_)
    elif sentence_structure == 'SOV':
        return apply_sov_rules(subject, object_, verb)
    elif sentence_structure == 'passive':
        return handle_passive_voice(subject, verb, object_)
    else:
        # Apply verb conjugation and noun-adjective agreement
        verb_conjugated = apply_verb_conjugation(verb, tense, person)
        return f"The {subject} {verb_conjugated} {object_}"
