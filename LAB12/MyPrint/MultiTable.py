def get_table(number=2, row=12):
    for n in range(1, row+1):
        ans = number * n
        print(f'{number} x {n} = {ans}')
    print('') ## print เพื่อแยกให้ดูง่ายเฉยๆ
