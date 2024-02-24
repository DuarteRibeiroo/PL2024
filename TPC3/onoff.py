import sys
import re

def main():
    text = sys.stdin.read()
    relevant_patterns = re.compile(r'[Oo][nN]|[Oo][Ff]{2}|=|[+-]?\d+')
    on_pattern = re.compile(r'[Oo][nN]')
    off_pattern = re.compile(r'[Oo][Ff]{2}')
    int_pattern = re.compile(r'[+-]?\d+')
    valid_text = relevant_patterns.findall(text)
    is_on = True
    sum = 0
    for match in valid_text:
        if on_pattern.match(match):
            is_on = True
        elif off_pattern.match(match):
            is_on = False
        elif int_pattern.match(match) and is_on:
                sum += int(match)
        elif match == '=':
            print(sum)
        
if __name__ == "__main__":
    main()