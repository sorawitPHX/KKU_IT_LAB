def lab_12_1(user):
    
    find_cap = list( filter(lambda t: t.isupper(), user))
    
    output = str(find_cap)[1:-1].replace("'", '')
    
    print(f'Upper letters: {output}')
    

lab_12_1('Hello World!!')
lab_12_1('OMG, Program Error')
