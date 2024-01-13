import re

FUNCTION = '(\w+\.\w+\(\))'

def check(text:str) -> str:
    result = []
    match = re.match(FUNCTION, text)
    if match:
        result.append(f'function name found: {match.groups(0)[0]}')
    return ' and '.join(result)
    