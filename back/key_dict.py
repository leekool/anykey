# dictionary's "keys" are what will appear in the svg
# current max char count: 9

key_dict = {
    '': ['XXXXXXX', 'KC_NO'],
    '_______': ['_______', 'KC_TRANSPARENT', 'KC_TRNS'],
    '&#8629;': ['KC_ENTER', 'KC_ENT', 'KC_KP_ENTER', 'KC_PENT'],
    'ESC': ['KC_ESCAPE', 'KC_ESC'],
    '&#9003;': ['KC_BACKSPACE', 'KC_BSPC'],
    'SPACE': ['KC_SPACE', 'KC_SPC'],
    '(': ['KC_LEFT_PAREN', 'KC_LPRN'],
    ')': ['KC_RIGHT_PAREN', 'KC_RPRN'],
    '[': ['KC_LEFT_BRACKET', 'KC_LBRC'],
    ']': ['KC_RIGHT_BRACKET', 'KC_RBRC'],
    '{': ['KC_LEFT_CURLY_BRACE', 'KC_LCBR'],
    '}': ['KC_RIGHT_CURLY_BRACE', 'KC_RCBR'],
    '-': ['KC_MINUS', 'KC_MINS', 'KC_KP_MINUS', 'KC_PMNS'],
    '=': ['KC_EQUAL', 'KC_EQL', 'KC_KP_EQUAL', 'KC_PEQL'],
    '\\': ['KC_BACKSLASH', 'KC_BSLS'],
    ';': ['KC_SEMICOLON', 'KC_SCLN'],
    '\'': ['KC_QUOTE', 'KC_QUOT'],
    '`': ['KC_GRAVE', 'KC_GRV'],
    ',': ['KC_COMMA', 'KC_COMM', 'KC_KP_COMMA', 'KC_PCMM'],
    '.': ['KC_DOT', 'KC_KP_DOT', 'KC_KP_DOT', 'KC_PDOT'],
    '/': ['KC_SLASH', 'KC_SLSH', 'KC_KP_SLASH', 'KC_PSLS'],
    'CAPS': ['KC_CAPS_LOCK', 'KC_CAPS'],
    'PRT SC': ['KC_PRINT_SCREEN', 'KC_PSCR'],
    'PAUSE': ['KC_PAUSE', 'KC_PAUS', 'KC_BRK', 'KC_BRMU'],
    'INSERT': ['KC_INSERT', 'KC_INS'],
    'HOME': ['KC_HOME'],
    'PAGE UP': ['KC_PAGE_UP', 'KC_PGUP'],
    'PAGE DOWN': ['KC_PAGE_DOWN', 'KC_PGDN'],
    'END': ['KC_END'],
    '&#8998;': ['KC_DELETE', 'KC_DEL'],
    'NUM LOCK': ['KC_NUM_LOCK', 'KC_NUM'],
    # arrow keys
    '&#8594;': ['KC_RIGHT', 'KC_RGHT'],
    '&#8592;': ['KC_LEFT'],
    '&#8595;': ['KC_DOWN'],
    '&#8593;': ['KC_UP'],
    # mouse keys
    'MOUSE &#8594;': ['KC_MS_RIGHT', 'KC_MS_R'],
    'MOUSE &#8592;': ['KC_MS_LEFT', 'KC_MS_L'],
    'MOUSE &#8595;': ['KC_MS_DOWN', 'KC_MS_D'],
    'MOUSE &#8593;': ['KC_MS_UP', 'KC_MS_U'],
    'MWHEEL &#8594;': ['KC_MS_WH_RIGHT', 'KC_WH_R'],
    'MWHEEL &#8592;': ['KC_MS_WH_LEFT', 'KC_WH_L'],
    'MWHEEL &#8595;': ['KC_MS_WH_DOWN', 'KC_WH_D'],
    'MWHEEL &#8593;': ['KC_MS_WH_UP', 'KC_WH_U'],
    'LEFT BTN': ['KC_MS_BTN1', 'KC_BTN1'],
    'RIGHT BTN': ['KC_MS_BTN2', 'KC_BTN2'],
    'THIRD BTN': ['KC_MS_BTN3', 'KC_BTN3'],
    # symbols
    '~': ['KC_TILDE', 'KC_TILD'],
    '!': ['KC_EXCLAIM', 'KC_EXLM'],
    '@': ['KC_AT'],
    '#': ['KC_HASH', 'KC_NONUS_HASH', 'KC_NUHS'],
    '$': ['KC_DOLLAR', 'KC_DLR'],
    '%': ['KC_PERCENT', 'KC_PERC'],
    '^': ['KC_CIRCUMFLEX', 'KC_CIRC'],
    '&amp;': ['KC_AMPERSAND', 'KC_AMPR'],  # to avoid XML recognising '&' as syntax
    '*': ['KC_ASTERISK', 'KC_ASTR', 'KC_KP_ASTERISK', 'KC_PAST'],
    '_': ['KC_UNDERSCORE', 'KC_UNDS'],
    '+': ['KC_PLUS', 'KC_UNDS', 'KC_KP_PLUS', 'KC_PPLS'],
    '|': ['KC_PIPE'],
    ':': ['KC_COLON', 'KC_COLN'],
    '\"': ['KC_DOUBLE_QUOTE', 'KC_DQUO', 'KC_DQT'],
    '<': ['KC_LEFT_ANGLE_BRACKET', 'KC_LABK', 'KC_LT'],
    '>': ['KC_RIGHT_ANGLE_BRACKET', 'KC_RABK', 'KC_GT'],
    '?': ['KC_QUESTION', 'KC_QUES'],
    # modifiers - possibly separate left & right later
    'CTRL': ['KC_LEFT_CTRL', 'KC_LCTL', 'KC_RIGHT_CTRL', 'KC_RCTL'],
    'ALT': ['KC_LEFT_ALT', 'KC_LALT', 'KC_LOPT', 'KC_RIGHT_ALT', 'KC_RALT', 'KC_ROPT', 'KC_ALGR'],
    'SHIFT': ['KC_LEFT_SHIFT', 'KC_LSFT', 'KC_RIGHT_SHIFT', 'KC_RSFT'],
    'GUI': ['KC_LEFT_GUI', 'KC_LGUI', 'KC_LCMD', 'KC_LWIN', 'KC_RIGHT_GUI', 'KC_RGUI', 'KC_RCMD', 'KC_RWIN'],
    # -----
    'POWER': ['KC_SYSTEM_POWER', 'KC_PWR'],
    'SLEEP': ['KC_SYSTEM_SLEEP', 'KC_SLEP'],
    'WAKE': ['KC_SYSTEM_WAKE', 'KC_WAKE'],
    'MUTE': ['KC_AUDIO_MUTE', 'KC_MUTE'],
    'VOL +': ['KC_AUDIO_VOL_UP', 'KC_VOLU'],
    'VOL -': ['KC_AUDIO_VOL_DOWN', 'KC_VOLD'],
    'CALC': ['KC_CALCULATOR', 'KC_CALC']
}

# creates a new dict containing individual key/value pairs for each item in key_dict's keys
inverted_key_dict = {value: key for key, values in key_dict.items() for value in values}


def get_dict():
    return inverted_key_dict
