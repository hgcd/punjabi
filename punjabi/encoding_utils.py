
# ASCII and unicode mappings
ascii_pre_conversion = {
    '/i(.)/ug': '$1i',
    '/®/ug': 'R',
    '/([iMµyY])([R®H§ÍÏçœ˜†])/ug': '$2$1',
    '/([MµyY])([uU])/ug': '$2$1',
    '/`([wWIoOyYR®H§´ÍÏçœ˜†uU])/ug': '$1`',
    '/i([´Î])/ug': '$1i',
    '/uo/ug': 'ou',
}

ascii_to_unicode_mapping = {
  "ei": "ਇ",
  "au": "ਉ",
  "aU": "ਊ",
  "eI": "ਈ",
  "ey": "ਏ",
  "Aw": "ਆ",
  "AY": "ਐ",
  "AO": "ਔ",
  "AW": "ਆਂ",
  "<>": "ੴ",
  "ÅÆ": "ੴ",
  "ƒ": "ਨੂੰ",
  "†": "੍ਟ",
  "˜": "੍ਨ",
  "Î": "੍ਯ",
  "î": "੍ਯ",
  "ç": "੍ਚ",
  "œ": "੍ਤ",
  "M": "ੰ",
  "H": "੍ਹ",
  "§": "੍ਹੂ",
  "i": "ਿ",
  "I": "ੀ",
  "u": "ੁ",
  "U": "ੂ",
  "y": "ੇ",
  "Y": "ੈ",
  "N": "ਂ",
  "o": "ੋ",
  "O": "ੌ",
  "R": "੍ਰ",
  "W": "ਾਂ",
  "w": "ਾ",
  "®": "੍ਰ",
  "´": "ੵ",
  "Ï": "ੵ",
  "µ": "ੰ",
  "μ": "ੰ",
  "@": "ੑ",
  "`": "ੱ",
  "~": "ੱ",
  "Í": "੍ਵ",
  "Ú": "ਃ",
  "ü": "ੁ",
  "|": "ਙ",
  "¨": "ੂ",
  "Ø": "",
  "ˆ": "ਂ",
  "¤": "ੱ",
  "a": "ੳ",
  "A": "ਅ",
  "b": "ਬ",
  "B": "ਭ",
  "c": "ਚ",
  "C": "ਛ",
  "d": "ਦ",
  "D": "ਧ",
  "e": "ੲ",
  "E": "ਓ",
  "f": "ਡ",
  "F": "ਢ",
  "g": "ਗ",
  "G": "ਘ",
  "h": "ਹ",
  "j": "ਜ",
  "J": "ਝ",
  "k": "ਕ",
  "K": "ਖ",
  "l": "ਲ",
  "L": "ਲ਼",
  "m": "ਮ",
  "n": "ਨ",
  "p": "ਪ",
  "P": "ਫ",
  "q": "ਤ",
  "Q": "ਥ",
  "r": "ਰ",
  "s": "ਸ",
  "S": "ਸ਼",
  "t": "ਟ",
  "T": "ਠ",
  "v": "ਵ",
  "V": "ੜ",
  "x": "ਣ",
  "X": "ਯ",
  "z": "ਜ਼",
  "Z": "ਗ਼",
  "1": "੧",
  "2": "੨",
  "3": "੩",
  "4": "੪",
  "5": "੫",
  "6": "੬",
  "^": "ਖ਼",
  "7": "੭",
  "&": "ਫ਼",
  "8": "੮",
  "9": "੯",
  "0": "੦",
  "[": "।",
  "]": "॥",
  "Ò": "॥",
  "\\": "ਞ",
  "ï": "ਯ",
  "Ç": "☬",
  "¡": "ੴ",
  "æ": "਼",
  "‚": "❁"
}

def ascii_to_unicode(text):
    """ Convert ASCII to unicode - got some bugs """
    # Swap positions of certain characters prior to conversion (something weird)
    # TODO - this part doesn't work right - sihaari and some other characters are in the wrong position - hence need for swapping
    for exp, sub in ascii_pre_conversion.items():
        text = text.replace(exp, sub)
    
    # Convert each ascii character to unicode
    for exp, sub in ascii_to_unicode_mapping.items():
        text = text.replace(exp, sub)
    return text