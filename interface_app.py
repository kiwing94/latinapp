import tkinter as tk
from tkinter import messagebox
from phrases import translate_phrase
from word_dict import translate_word
from syntax import detect_syntax, reorder_sentence
from phrase_structure import apply_sov_rules, apply_svo_rules, apply_verb_conjugation, apply_adjective_noun_agreement, handle_phrase_structure, handle_passive_voice

# Function to handle the translation when the button is clicked
def translate():
    # Get the user input
    latin_phrase = entry.get()

    # First check if it's a recognized Latin phrase
    translated_phrase = translate_phrase(latin_phrase)

    if translated_phrase:
        # If a phrase is found, display the translation
        result_label.config(text=f"Translated: {translated_phrase}")
    else:
        # If no phrase is found, attempt to translate word by word
        words = latin_phrase.split()
        translated_words = [translate_word(word) for word in words]

        # If any words were not found, display an error message
        if None in translated_words:
            result_label.config(text="Translation not found for some words.")
            messagebox.showinfo("Translation Error", "Some words are not available in the dictionary.")
        else:
            translated_sentence = " ".join(translated_words)
            result_label.config(text=f"Translated: {translated_sentence}")


# Create the main window
root = tk.Tk()
root.title("Latin to English Translator")

# Set the window size and background color
root.geometry("500x400")
root.config(bg="#f0f0f0")  # Light gray background

# Use a custom font for the title and labels
title_font = ("Helvetica", 18, "bold")
label_font = ("Courier New", 12)
button_font = ("Arial", 14, "bold")
entry_font = ("Arial", 12)

# Add a label for the title
title_label = tk.Label(root, text="Latin to English Translator", font=title_font, fg="darkblue", bg="#f0f0f0")
title_label.pack(pady=20)

# Add a label for instructions
instructions_label = tk.Label(root, text="Enter a Latin phrase or word:", font=label_font, bg="#f0f0f0")
instructions_label.pack(pady=10)

# Add a text entry box for the Latin input with a border and custom font
entry = tk.Entry(root, width=40, font=entry_font, bd=2, relief="solid", justify="center")
entry.pack(pady=20)

# Add a button to trigger the translation with custom style
translate_button = tk.Button(root, text="Translate", command=translate, font=button_font, bg="#4CAF50", fg="white",
                             relief="flat", width=20, height=2)
translate_button.pack(pady=20)

# Add a label to display the translation result with a custom font
result_label = tk.Label(root, text="", font=label_font, bg="#f0f0f0", wraplength=400)
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
