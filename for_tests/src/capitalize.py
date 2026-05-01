def capitalize(text: str) -> str:
    if not text:
        return ""
    first_char, *else_chars = text
    return f"{first_char.upper()}{''.join(else_chars)}"
