isMirror = lambda list_words : list( filter(lambda w: w[::-1].lower() == w.lower() , list_words) )
list2str = lambda l: str(l)[1:-1].replace("'", '')

in1 = ["aloha", "wow", "Level", "step on no pets"]
in2 = ["mom", "cat", "suMmer", "Civic"]

print(f'Mirror words: {list2str(isMirror(in1))}')
print(f'Mirror words: {list2str(isMirror(in2))}')
            
