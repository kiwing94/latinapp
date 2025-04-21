from phrases import latin_phrases
from words import latin_words
from grammar import detect_affixes, decline_noun, conjugate_verb

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

def generate_html_list():
    html_output = f"""<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Latin Library</title>
  <style>
    body {{ font-family: Georgia, serif; background: #fdfaf6; padding: 2em; }}
    h1, h2 {{ color: #3a3a3a; }}
    ul {{ line-height: 1.6; padding-left: 1.5em; }}
    li {{ margin-bottom: 0.5em; }}
    .section {{ margin-top: 3em; }}
    input[type='text'], select {{
      padding: 10px;
      width: 100%;
      max-width: 500px;
      font-size: 16px;
      margin-bottom: 20px;
      display: block;
    }}
    .sov-example {{
      margin-top: 3em;
      padding: 1em;
      background: #fff9e6;
      border: 1px solid #e0d7c6;
    }}
    table {{
      border-collapse: collapse;
      margin-top: 1em;
    }}
    th, td {{
      border: 1px solid #ccc;
      padding: 8px;
      text-align: center;
    }}
  </style>
  <script>
    function filterList(inputId, listId) {{
      const input = document.getElementById(inputId);
      const filter = input.value.toLowerCase();
      const listItems = document.getElementById(listId).getElementsByTagName('li');
      for (let i = 0; i < listItems.length; i++) {{
        const text = listItems[i].innerText.toLowerCase();
        listItems[i].style.display = text.includes(filter) ? '' : 'none';
      }}
    }}
    async function liveTranslate() {{
      const input = document.getElementById('liveTranslateInput').value;
      const response = await fetch(`/translate?q=` + encodeURIComponent(input));
      const data = await response.text();
      document.getElementById('liveTranslationResult').innerText = data;
    }}
  </script>
</head>
<body>
  <h1>Latin Language Library</h1>

  <div class='section'>
    <h2>Latin Phrases</h2>
    <input type='text' id='phraseSearch' onkeyup="filterList('phraseSearch', 'phraseList')" placeholder='Search phrases...'>
    <ul id='phraseList'>
"""
    for latin, english in latin_phrases.items():
        html_output += f"<li><strong>{latin}</strong>: {english}</li>\n"

    html_output += """
    </ul>
  </div>

  <div class='section'>
    <h2>Latin Word List</h2>
    <input type='text' id='wordSearch' onkeyup="filterList('wordSearch', 'wordList')" placeholder='Search words...'>
    <ul id='wordList'>
"""
    for latin in sorted(latin_words.keys()):
        english = latin_words[latin]
        word_type = get_word_type(latin)
        affix_data = detect_affixes(latin)
        affix_string = f" [prefix: {affix_data['prefix']}, suffix: {affix_data['suffix']}, infix: {affix_data['infix']}]" if any(affix_data.values()) else ""
        html_output += f"<li><strong>{latin}</strong>: {english} <em>{word_type}</em>{affix_string}</li>\n"

        # Show noun declension tables
        decl_map = {'a': '1st', 'us': '2nd', 'is': '3rd'}
        for ending, decl in decl_map.items():
            if latin.endswith(ending):
                cases = ['nom', 'gen', 'dat', 'acc', 'abl']
                html_output += f"<table><tr><th>Case</th><th>Singular</th><th>Plural</th></tr>"
                for case in cases:
                    singular = decline_noun(latin[:-len(ending)], decl, case, "sg")
                    plural = decline_noun(latin[:-len(ending)], decl, case, "pl")
                    html_output += f"<tr><td>{case}</td><td>{singular}</td><td>{plural}</td></tr>"
                html_output += "</table><br>"

        # Show verb conjugation table
        if latin.endswith('re'):
            persons = ["1st", "2nd", "3rd", "1st pl", "2nd pl", "3rd pl"]
            conj_map = {'are': '1st', 'ere': '2nd', 'ere*': '3rd', 'ire': '4th'}
            for end, conj in conj_map.items():
                if (end == 'ere*' and latin.endswith('ere')) or latin.endswith(end):
                    html_output += f"<table><tr><th>Person</th><th>Conjugation ({conj})</th></tr>"
                    for i in range(1, 7):
                        form = conjugate_verb(latin[:-2], conj, i)
                        html_output += f"<tr><td>{persons[i-1]}</td><td>{form}</td></tr>"
                    html_output += "</table><br>"

    html_output += """
    </ul>
  </div>

  <div class='section sov-example'>
    <h2>SOV Example (Subject-Object-Verb)</h2>
    <p><strong>Latin:</strong> Puella librum amat</p>
    <p><strong>Gloss:</strong> The girl the book loves</p>
    <p><strong>English (SVO):</strong> The girl loves the book</p>
    <p>This illustrates the typical Latin word order where the <strong>verb comes at the end</strong>.</p>
  </div>

  <div class='section'>
    <h2>Live Translation</h2>
    <input type='text' id='liveTranslateInput' placeholder='Enter Latin text...'>
    <button onclick='liveTranslate()'>Translate</button>
    <p><strong>Result:</strong> <span id='liveTranslationResult'></span></p>
  </div>
</body>
</html>"""

    with open("templates/phrases.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print("✅ HTML with full declensions + verb conjugations integrated")

if __name__ == "__main__":
    generate_html_list()