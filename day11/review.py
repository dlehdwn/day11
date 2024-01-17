words = ["apple",'banana',"cherry","date","fig"]
a = [i for i in words if 'a'in i and len(i) > 5]
n = [23,43,44,20,12,46,76,87]
b = [i for i in n if i >50]

def c(x,y,flag):
    if flag:
        return x+ y
    else:
        return x - y

