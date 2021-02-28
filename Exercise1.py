def above_below(arr, x):
    above = 0
    below = 0

    for i in arr: 
        if i > x:
            above+=1
        elif i < x:
            below += 1
    return above,below

def rotate_string(txt, x):
    x = x % len(txt)
    return txt[-x:] + txt[0:-x]

print('above: %i, below: %i' % above_below([1,5,2,1,10], 6))
print(rotate_string('MyString', 10))                    