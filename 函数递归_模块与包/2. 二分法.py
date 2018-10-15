#二分法


l=[1,2,10,30,33,99,101,200,301,402]


num=200


def get(num,l):
    print(l)
    if len(l) >0:

        mid=len(l) // 2
        if num > l[mid]:
            l=l[mid+1:]
        elif num < l[mid]:
            l=l[:mid]
        else:
            print('find it')
            return
        get(num,l)
    else:
        print('列表里面没有这个')
        return


get(3,l)



