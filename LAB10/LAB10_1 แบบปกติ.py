scores = {"231": 77, "942": 80, "253": 51, "146": 65, "258": 91, "229": 87, "354": 88}
scores_even = {}
for k in scores:
    if int(k)%2==0:
        scores_even[k] = scores[k]

scores_even = sorted(scores_even.items(), reverse=True)
id_even = []
sum = 0
for k, v in scores_even:
    id_even.append(k)
    sum += v
avg = sum/len(scores_even)
id_even = str(id_even)[1:-1].replace("'", '')

print(f'Number of even id = {len(scores_even)}')
print(f'Even id: {id_even}')
print(f'Average Score of even id = {avg}')
