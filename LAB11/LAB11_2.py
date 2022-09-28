#problem 2
findMissNum = lambda l : list( filter(lambda num: num not in l, range(min(l), max(l) + 1)) )
num1 = [10, 11, 15, 12, 9, 14, 7, (10**10)]
num2 = [12, 5, 9, -3]
print(f'''
      Lost numbers contain: {(findMissNum(num1))}
      Lost numbers contain: {(findMissNum(num2))}
      ''')

findMissNum()