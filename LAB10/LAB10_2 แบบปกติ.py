text = "Structured Programming for Information Technology"
text = text.lower()
text = text.replace(" ","")
text = sorted(text)
count_text = {}
for t in text:
    if t not in count_text:
        count_text[t] = 1
    else:
        count_text[t] += 1
sorted_text = sorted(count_text.items(), reverse=True, key=lambda item: item[1])
for k, v in sorted_text:
    print(f'{k}: {v}')
