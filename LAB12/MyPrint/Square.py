def print_square(width=2, length=0):
    if length < 2: length = width
    for a in range(length):
        if a == range(length)[0] or a == range(length)[-1]:
            print('#'*(width))
        else:
            for b in range(width):
                if b == range(width)[0] or b == range(width)[-1]:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()
    print('') ## print เพื่อแยกให้ดูง่ายเฉยๆ

def print_triagle(width=2, length=0):
    if length == 0: length = width
    for A in range(length):
        if A < length-1:
            for B in range(A+1):
                if B == 0 or B == range(A+1)[-1]:
                    print('#', end='')
                else:
                    print(' ', end='')
        else:
            print('#'*width)
        print()
    print('') ## print เพื่อแยกให้ดูง่ายเฉยๆ

if __name__ == '__main__':
    print_square(30, 10)
    pass