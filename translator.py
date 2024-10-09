import tkinter as tk
from tkinter import ttk

# Dictionary for English to Mycenaean Greek
english_to_mycenaean = {
    "to speak": "toqa",
    "to bring": "para",
    "to see": "ika",
    "new": "neu",
    "to work": "koto",
    "water": "nawa",
    "to take": "rama",
    "gift": "dora",
    "a great one": "ake",
    "foot": "puto",
    "meat": "miki",
    "to eat": "era",
    "fire": "kote",
    "sheep": "mite",
    "tooth": "pone",
    "to run": "newo",
    "man": "ona",
    "horse": "nara",
    "cup": "teke",
    "one": "ate",
    "house": "toka",
    "woman": "wona",
    "to go": "tira",
    "to love": "neta",
    "air": "ano",
    "table": "sama",
    "to cry": "miqi",
    "to walk": "nara",
    "three": "tora",
    "nine": "neta",
    "small": "jana",
    "mother": "ora",
    "chicken": "mita",
    "door": "dowo",
    "life": "ura",
    "flesh": "waka",
    "wind": "wota",
    "king": "wanax",
    "queen": "wanassa",
    "warrior": "eqeta",
    "sword": "xiphos",
    "shield": "aspis",
    "food": "sitos",
    "earth": "ge",
    "sun": "helios",
    "moon": "mene",
    "star": "aster",
    "friend": "philos",
    "enemy": "echthros",
    "battle": "polemos",
    "city": "polis",
    "god": "theos",
    "goddess": "thea",
    "chariot": "hikanos",
    "grain": "sitou",
    "river": "potamos",
    "mountain": "oros",
    "road": "odous",
    "merchant": "agoraios",
    "shepherd": "poimen",
    "stone": "lithos",
    "beast": "therion",
    "fruit": "karpon",
    "bread": "artos",
    "gold": "chrusos",
    "silver": "argyros",
    "brass": "chalcos",
    "fishing": "ichthyos",
    "ship": "nau",
    "clothing": "enduma",
    "jewelry": "chryseion",
    "wine": "oinos",
    "musician": "aulo",
    "artist": "technites",
    "furniture": "epipedion",
    "tool": "ergaleion",
    "peace": "eirene",
    "blood": "haima",
    "breath": "pnoe",
    "to build": "kowi",
    "brother": "toros",
    "sister": "ete",
    "sea": "pontos",
    "tree": "dendron",
    "wine": "woino",
    "bird": "ornios",
    "land": "damos",
    "day": "hmera",
    "night": "nuktos",
    "mother": "mater",
    "father": "pater",
    "friend": "hetairos",
    "enemy": "phegon",
    "ox": "bos",
    "cow": "bous",
    "lion": "leon",
    "dog": "kunos",
    "fish": "ichthys",
    "to rule": "basileu",
    "to judge": "dikazein",
    "victory": "nike",
    "death": "thanatos",
    "fate": "moira",
    "earthquake": "seismos",
    "spring": "ear",
    "summer": "theros",
    "autumn": "phthinoporon",
    "winter": "cheimon",
}

# Transliteration dictionary from Mycenaean Greek to Greek alphabet
mycenaean_to_greek = {
    "wanax": "ϝάναξ",
    "wanassa": "ϝανάσσα",
    "toqa": "τοῦ κἀ",
    "para": "πάρα",
    "ika": "ἴκα",
    "neu": "νέος",
    "koto": "κωτὸν",
    "nawa": "ὕδωρ",
    "rama": "ράμα",
    "dora": "δῶρον",
    "ake": "ἀγάθος",
    "puto": "πούτος",
    "miki": "μίγνυμι",
    "era": "ἔρα",
    "kote": "πῦρ",
    "mite": "μίτα",
    "pone": "πονεῖν",
    "newo": "νέων",
    "ona": "ὦν",
    "nara": "ἵππος",
    "teke": "τῆκον",
    "ate": "ἓν",
    "toka": "οἶκος",
    "wona": "γυνὴ",
    "tira": "τίρα",
    "neta": "νέτα",
    "ano": "ἀήρ",
    "sama": "σάμα",
    "miqi": "μιχὶ",
    "three": "τρεῖς",
    "jana": "ἵν",
    "ora": "μήτηρ",
    "mita": "μίτα",
    "dowo": "δοῖν",
    "ura": "ζωὴ",
    "waka": "σάρξ",
    "wota": "ἀήρ",
    "eqeta": "ἐϝέτα",
    "xiphos": "ξίφος",
    "aspis": "ἀσπίς",
    "sitos": "σῖτος",
    "ge": "γῆ",
    "helios": "ἥλιος",
    "mene": "μήνη",
    "aster": "ἀστήρ",
    "philos": "φίλος",
    "echthros": "ἔχθρος",
    "polemos": "πόλεμος",
    "polis": "πόλις",
    "theos": "θεός",
    "thea": "θεά",
    "hikanos": "ἱκάνος",
    "sitou": "σίτος",
    "potamos": "ποταμός",
    "oros": "ὄρος",
    "odous": "ὀδούς",
    "agoraios": "ἀγοραίος",
    "poimen": "ποιμήν",
    "lithos": "λίθος",
    "therion": "θήρ",
    "karpon": "καρπός",
    "artos": "ἄρτος",
    "chrusos": "χρυσός",
    "argyros": "ἀργυρός",
    "chalcos": "χαλκός",
    "ichthyos": "ἰχθύς",
    "nau": "ναῦς",
    "enduma": "ἔνδυμα",
    "chryseion": "χρυσέϊον",
    "oinos": "οἶνος",
    "aulo": "αὐλός",
    "technites": "τεχνίτης",
    "epipedion": "ἐπιπέδιον",
    "ergaleion": "ἐργαλεῖον",
    "eirene": "εἰρήνη",
    "haima": "αἷμα",
    "pnoe": "πνοή",
    "kowi": "κωῖ",
    "toros": "τόρος",
    "ete": "ἔτη",
    "pontos": "πόντος",
    "dendron": "δένδρον",
    "woino": "οἶνος",
    "ornios": "ὄρνιος",
    "damos": "δᾶμος",
    "hmera": "ἡμέρα",
    "nuktos": "νύκτος",
    "mater": "μήτηρ",
    "pater": "πατήρ",
    "hetairos": "ἑταῖρος",
    "phegon": "φέγων",
    "bos": "βοῦς",
    "bous": "βοῦς",
    "leon": "λέων",
    "kunos": "κύων",
    "ichthys": "ἰχθύς",
    "basileu": "βασιλεύς",
    "dikazein": "δικάζειν",
    "nike": "νίκη",
    "thanatos": "θάνατος",
    "moira": "μοῖρα",
    "seismos": "σεισμός",
    "ear": "ἦρ",
    "theros": "θέρος",
    "phthinoporon": "φθινόπωρον",
    "cheimon": "χειμών",
}

# Full Linear B syllabary following the provided format
linear_b_syllabary = {
    "a": "𐀀",   # a
    "e": "𐀁",   # e
    "i": "𐀂",   # i
    "o": "𐀃",   # o
    "u": "𐀄",   # u
    "da": "𐀅",  # da
    "de": "𐀆",  # de
    "di": "𐀇",  # di
    "do": "𐀈",  # do
    "du": "𐀉",  # du
    "ja": "𐀊",  # ja
    "je": "𐀋",  # je
    "jo": "𐀍",  # jo
    "ka": "𐀏",  # ka
    "ke": "𐀐",  # ke
    "ki": "𐀑",  # ki
    "ko": "𐀒",  # ko
    "ku": "𐀓",  # ku
    "ma": "𐀔",  # ma
    "me": "𐀕",  # me
    "mi": "𐀖",  # mi
    "mo": "𐀗",  # mo
    "mu": "𐀘",  # mu
    "na": "𐀙",  # na
    "ne": "𐀚",  # ne
    "ni": "𐀛",  # ni
    "no": "𐀜",  # no
    "nu": "𐀝",  # nu
    "pa": "𐀞",  # pa
    "pe": "𐀟",  # pe
    "pi": "𐀠",  # pi
    "po": "𐀡",  # po
    "pu": "𐀢",  # pu
    "qa": "𐀣",  # qa
    "qe": "𐀤",  # qe
    "qi": "𐀥",  # qi
    "qo": "𐀦",  # qo
    "ra": "𐀨",  # ra
    "re": "𐀩",  # re
    "ri": "𐀪",  # ri
    "ro": "𐀫",  # ro
    "ru": "𐀬",  # ru
    "sa": "𐀭",  # sa
    "se": "𐀮",  # se
    "si": "𐀯",  # si
    "so": "𐀰",  # so
    "su": "𐀱",  # su
    "ta": "𐀲",  # ta
    "te": "𐀳",  # te
    "ti": "𐀴",  # ti
    "to": "𐀵",  # to
    "tu": "𐀶",  # tu
    "wa": "𐀷",  # wa
    "we": "𐀸",  # we
    "wi": "𐀹",  # wi
    "wo": "𐀺",  # wo
    "za": "𐀼",  # za
    "ze": "𐀽",  # ze
    "zo": "𐀿",  # zo
    "to": "𐀏",  
    "ko": "𐀐", 
    "wo": "𐀓",  
    "po": "𐀡",  
    "de": "𐀆",
}

# Function to convert English to Mycenaean Greek
def translate_to_mycenaean(english_word):
    return english_to_mycenaean.get(english_word.lower(), "Translation not found")

# Function to convert Mycenaean Greek to Greek alphabet
def to_greek_alphabet(mycenaean_word):
    return mycenaean_to_greek.get(mycenaean_word, "No Greek alphabet equivalent found")

# Function to convert to Linear B script
def to_linear_b(mycenaean_word):
    linear_b_translation = ""
    # Create a simple mapping of known syllables
    syllables = {
        "wanax": ["wa", "na", "x"],
        "wanassa": ["wa", "na", "sa"],
        "toqa": ["to", "qa"],
        "para": ["pa", "ra"],
        "ika": ["i", "ka"],
        "neu": ["ne", "u"],
        "koto": ["ko", "to"],
        "nawa": ["na", "wa"],
        "rama": ["ra", "ma"],
        "dora": ["do", "ra"],
        "ake": ["a", "ke"],
        "puto": ["pu", "to"],
        "miki": ["mi", "ki"],
        "era": ["e", "ra"],
        "kote": ["ko", "te"],
        "mite": ["mi", "te"],
        "pone": ["po", "ne"],
        "newo": ["ne", "wo"],
        "ona": ["o", "na"],
        "nara": ["na", "ra"],
        "teke": ["te", "ke"],
        "ate": ["a", "te"],
        "toka": ["to", "ka"],
        "wona": ["wo", "na"],
        "tira": ["ti", "ra"],
        "neta": ["ne", "ta"],
        "ano": ["a", "no"],
        "sama": ["sa", "ma"],
        "miqi": ["mi", "qi"],
        "three": ["th", "ree"],
        "jana": ["ja", "na"],
        "ora": ["o", "ra"],
        "mita": ["mi", "ta"],
        "dowo": ["do", "wo"],
        "ura": ["u", "ra"],
        "waka": ["wa", "ka"],
        "wota": ["wo", "ta"],
        "eqeta": ["e", "qe", "ta"],
        "xiphos": ["xi", "po", "s"],
        "aspis": ["as", "pi", "s"],
        "sitos": ["si", "to", "s"],
        "ge": ["ge"],
        "helios": ["he", "li", "o", "s"],
        "mene": ["me", "ne"],
        "aster": ["as", "te", "r"],
        "philos": ["phi", "lo", "s"],
        "echthros": ["e", "ch", "th", "ro", "s"],
        "polemos": ["po", "le", "mo", "s"],
        "polis": ["po", "li", "s"],
        "theos": ["the", "o", "s"],
        "thea": ["the", "a"],
        "hikanos": ["hi", "ka", "no", "s"],
        "sitou": ["si", "to", "u"],
        "potamos": ["po", "ta", "mo", "s"],
        "oros": ["o", "ro", "s"],
        "odous": ["o", "dou", "s"],
        "agoraios": ["a", "go", "ra", "i", "o", "s"],
        "poimen": ["po", "i", "me", "n"],
        "lithos": ["li", "tho", "s"],
        "therion": ["the", "ri", "on"],
        "karpon": ["kar", "pon"],
        "artos": ["ar", "to", "s"],
        "chrusos": ["ch", "ru", "so", "s"],
        "argyros": ["ar", "gy", "ro", "s"],
        "chalcos": ["cha", "lco", "s"],
        "ichthyos": ["ich", "thy", "o", "s"],
        "nau": ["na", "u"],
        "enduma": ["en", "du", "ma"],
        "chryseion": ["ch", "ry", "se", "ion"],
        "oinos": ["oi", "no", "s"],
        "aulo": ["au", "lo"],
        "technites": ["te", "ch", "ni", "tes"],
        "epipedion": ["e", "pi", "pe", "di", "on"],
        "ergaleion": ["er", "ga", "le", "ion"],
        "eirene": ["ei", "re", "ne"],
        "haima": ["ha", "i", "ma"],
        "pnoe": ["p", "no", "e"],
        "kowi": ["ko", "wi"],
        "toros": ["to", "ro", "s"],
        "ete": ["e", "te"],
        "pontos": ["po", "nto", "s"],
        "dendron": ["de", "ndron"],
        "woino": ["wo", "i", "no"],
        "ornios": ["or", "ni", "os"],
        "damos": ["da", "mo", "s"],
        "hmera": ["hme", "ra"],
        "nuktos": ["nu", "kto", "s"],
        "mater": ["ma", "ter"],
        "pater": ["pa", "ter"],
        "hetairos": ["he", "tai", "ro", "s"],
        "phegon": ["phe", "gon"],
        "bos": ["bo", "s"],
        "bous": ["bo", "us"],
        "leon": ["le", "on"],
        "kunos": ["ku", "no", "s"],
        "ichthys": ["ich", "thy", "s"],
        "basileu": ["ba", "si", "leu"],
        "dikazein": ["di", "ka", "ze", "in"],
        "nike": ["ni", "ke"],
        "thanatos": ["tha", "na", "tos"],
        "moira": ["moi", "ra"],
        "seismos": ["sei", "smo", "s"],
        "ear": ["ea", "r"],
        "theros": ["the", "ros"],
        "phthinoporon": ["ph", "thi", "no", "po", "ron"],
        "cheimon": ["che", "i", "mon"],
    }

    for word in syllables:
        if mycenaean_word == word:
            for syllable in syllables[word]:
                linear_b_translation += linear_b_syllabary.get(syllable, "?")  # "?" for unknown syllables
            return linear_b_translation

    return "Linear B translation not found"

# Example usage
def main():
    english_word = input("Enter an English word: ")  # User input for testing
    mycenaean_word = translate_to_mycenaean(english_word)
    
    print(f"\nEnglish word: {english_word}")
    print(f"Mycenaean Greek: {mycenaean_word}")

    greek_alphabet = to_greek_alphabet(mycenaean_word)
    print(f"Greek Alphabet: {greek_alphabet}")

    linear_b_script = to_linear_b(mycenaean_word)
    print(f"Linear B Script: {linear_b_script}")

if __name__ == "__main__":
    main()
