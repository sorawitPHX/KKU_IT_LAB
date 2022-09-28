def clear_and_sort(t : str):
    t = t.lower()
    t = t.replace(' ', '')
    t = sorted(t)
    return t

def dictCountChr(l : list | str):
    d = {}
    for k in l:
        if k not in d:
            d[k] = 1
        else:
            d[k] += 1
    return d

def dictSortValMax2Min(d: dict):
    new_d = {}
    for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True):
        new_d[k] = v
    return new_d

def showDict(d: dict):
    for k, v in d.items(): print(f'{k}: {v}')
    return

temp = "Structured Programming for Information Technology"
text = clear_and_sort(temp)
text = dictCountChr(text)
text = dictSortValMax2Min(text)

#print(text)
showDict(text)