import re
def to_camel_case(text):
    if not text: 
        return ""
    words = re.findall('[A-Z]?[a-z]+|[A-Z]?', text)
    output = ''.join([w.capitalize() for w in words])
    if text[0].islower():
        return output[0].lower() + output[1:]
    return output