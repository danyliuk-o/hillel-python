def remove_tags(text):
    result = ''
    in_tag = False
    for char in text:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            result += char
    return result


def remove_empty_lines(text):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if(line):
            lines.append(line)
    return '\n'.join(lines)


def delete_html_tags(html_file, result_file='files/cleaned.txt'):
    with open(html_file, encoding='utf-8') as file:
        html = file.read()
    cleaned = remove_empty_lines(remove_tags(html))
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned)


delete_html_tags('files/draft.html')
