scores = {"231": 77, "942": 80, "253": 51, "146": 65, "258": 91, "229": 87, "354": 88}
scores = {k : v for k, v in sorted(scores.items(), reverse=True) if int(k)%2==0}
scores_key = list( filter(lambda key : int(key) % 2 == 0, scores) )
scores_val = [ scores[key] for key in scores_key ]

print(f'''
      Number of even id     {len(scores_key)}
      Even id               {str(scores_key)[1:-1].replace("'", '')}
      Number of even id     {sum(scores_val)/len(scores_val):.0f}
      ''')