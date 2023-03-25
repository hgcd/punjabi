import re

# Gurmukhi symbols

gurmukhi_numbers = [
    "੦", "੧", "੨", "੩", "੪", "੫", "੬", "੭", "੮", "੯"
]

gurmukhi_vowels = [
   "ੳ", "ਉ", "ਊ", "ਓ", "ਅ", "ਆ", "ਐ",  "ਔ", "ੲ", "ਇ", "ਈ", "ਏ"
]

gurmukhi_consonants = [
    "ਸ", "ਹ",
    "ਕ", "ਖ", "ਗ", "ਘ", "ਙ",
    "ਚ", "ਛ", "ਜ", "ਝ", "ਞ",
    "ਟ", "ਠ", "ਡ", "ਢ", "ਣ",
    "ਤ", "ਥ", "ਦ", "ਧ", "ਨ",
    "ਪ", "ਫ", "ਬ", "ਭ", "ਮ",
    "ਯ", "ਰ", "ਲ", "ਵ", "ੜ"
]

gurmukhi_imported_consonants = [
    "ਸ਼", "ਖ", "ਗ਼", "ਜ਼", "ਫ਼", "ਲ਼"
]

gurmukhi_laga_matravan = [
   "ਾ", "ਿ", "ੀ", "ੇ", "ੈ", "ੁ", "ੂ", "ੋ", "ੌ", "ਂ", "ੰ", "ੱ"
]

gurmukhi_other = [
   "੍", "'ਃ", "ਁ"
]

gurmukhi_punctuation = [
    "।", "॥"
]

gurmukhi_symbols = gurmukhi_numbers\
    + gurmukhi_vowels\
    + gurmukhi_consonants\
    + gurmukhi_imported_consonants\
    + gurmukhi_laga_matravan\
    + gurmukhi_other\
    + gurmukhi_punctuation\

# Syllable counting info
zero_weight_symbols = ['੍ਰ', 'ੵ', 'ੑ', '੍ਵ', '੍ਹ', '੍ਟ', '੍ਨ', '੍ਯ', '੍ਚ', '੍ਤ', '੍', 'ਿ', 'ੁ', 'ਂ', 'ਃ', '।', '॥', '☬', '਼', '❁']

deeragh_modifiers = ['ੰ', '੍ਹੂ', 'ੀ', 'ੂ', 'ੇ', 'ੈ', 'ੋ', 'ੌ', 'ਾਂ', 'ਾ', 'ੱ']

two_unit_syllables = [ 'ਊ', 'ਓ', 'ਈ', 'ਏ', 'ਐ', 'ਆ', 'ਔ' ]

two_unit_syllables = [ 'ਊ', 'ਓ', 'ਈ', 'ਏ', 'ਐ', 'ਆ', 'ਔ' ]

def is_gurmukhi(text):
    """ Checks whether the input text is Gurmukhi """
    ignore_sumbols = [
        " ", ".", "!", "?", ",", ";", ":", "-", "'", "\"", "(", ")", "[", "]", "\n", "\t"
    ]
    return all([c in (gurmukhi_symbols + ignore_symbols) for c in text])

def gurmukhi_sorted(texts, reverse=False):
    """ Sort list of Gurmukhi texts """
    
    return sorted(
        texts,
        key=lambda text: " ".join([
            str(gurmukhi_symbols.index(c)) if c in gurmukhi_symbols else str(0)
            for c in text
        ]),
        reverse=reverse
    )

def get_gurmukhi_syllable_count(word):
    """ Get the count of syllables in a Gurmukhi word """

    # Input must be a single word
    if " " in word:
        raise Exception("Input must be a single word")

    # Count each akhar as one syllable
    syllable_count = sum([
       1 if c in (gurmukhi_vowels + gurmukhi_consonants + gurmukhi_imported_consonants) else 0 for c in word
    ])

    # Subtract 1 for each paair vich akhar
    syllable_count -= sum([
       1 if word[i] == "੍" and (word[i+1] in gurmukhi_consonants) else 0 for i in range(len(word) - 1)
    ])

    # Subtract one if not ending in laga matra or vowel akhar
    if not (word[-1] in (gurmukhi_laga_matravan + gurmukhi_vowels)):
        syllable_count -= 1
    
    return syllable_count


def clean_gurmukhi_text(text, keep_gurmukhi_numbers=False, keep_roman_numbers=False, other_keep_chars=["।", "॥"]):
    """ Basic cleaning of Gurmukhi text by removing all non-Gurmukhi (and some other) characters """
    
    # Set which characters are to be kept post cleaning
    keep_chars = gurmukhi_vowels\
        + gurmukhi_consonants\
        + gurmukhi_imported_consonants\
        + gurmukhi_laga_matravan\
        + gurmukhi_other\
        + other_keep_chars + [" "]
    
    if keep_gurmukhi_numbers:
        keep_chars += gurmukhi_numbers
    
    if keep_roman_numbers:
        keep_chars += ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    return re.sub(
        r'\s+', ' ',
        "".join([c for c in text if (c in keep_chars)])
    ).strip()