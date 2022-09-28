def try1(): 
    clearText = lambda text = str(): str().join(sorted(str(text.lower()).replace(' ', '')))
    text = "Structured Programming for Information Technology"
    text = clearText(text)
    text_Set = sorted(set(text))
    count_text = {k : text.count(k) for k in text_Set}
    count_text = {k: v for k, v in sorted(count_text.items(), reverse=True)}
    for k, v in count_text.items(): print(f'{k} : {v}')

try1()