text = "Structured Programming for Information Technology"
text = text.lower()
text = text.replace(" ","")
text = sorted(text)
textCount = {}
for t in text:
    if t not in textCount:
        textCount[t] = 1
    else:
        textCount[t] += 1
new_textCount = {}
for a, b in sorted(textCount.items(), key=lambda item: item[1], reverse=True): new_textCount[a] = b
for i, j in new_textCount.items(): print(f'{i}: {j}')
