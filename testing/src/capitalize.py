def capitalize(txt: str):
    if txt == '':
        return ''
    
    first_char = txt[0].upper()
    rest_substring = txt[1:]
    return f'{first_char}{rest_substring}'
