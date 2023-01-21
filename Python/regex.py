import re

def match_text(text_data):
    pattern = 'ab{4,8}'
    if re.search(pattern, text_data):
        return "Match found"
    else:
        return ("Match not found")

print(match_text("bbbbasdf"))
print(match_text("babbcbbbbb"))