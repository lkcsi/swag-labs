import re

FORMAT = "^.{5,}$"
FUNCTION = '(\w+\.\w+\(\))'

def check(text:str) -> str:
    result = []
    if not re.fullmatch(FORMAT, text):
        result.append("Invalid formatting")
    if re.match(FUNCTION, text):
        result.append("Text has function exposed")
    return ' and '.join(result)
    