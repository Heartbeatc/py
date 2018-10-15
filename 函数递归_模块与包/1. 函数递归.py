#函数递归调用：在调用一个函数的过程中又调用该函数本身，称之为函数的递归调用




'''

def func1():
    print('from func1')
    func1()

func1()

'''





#递归分为两个重要的阶段：递推+回溯

def age(n):
    if n == 1:
        return 18
    return age(n-1) + 2

print(age(5))

#总结递归调用：


#1：进入下一次递归时，问题的规模必须降低
#2：递归调用必须要有一个明确的结束条件
#3：在python中没有尾递归优化，递归调用的效率就是不高



l=[1,2,[3,[4,[5,[6,7,[8,9,[10]]]]]]]




def get(l):
    for item in l:
        if isinstance(item,list):
            get(item)
        else:
            print(item)



get(l)

