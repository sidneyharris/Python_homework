'''
1、搭建好python,pycharm, git 环境，在本地创建一个pythoncode，和README.MD, 上传到github上，将代码github链接地址贴到作业贴下即可
2、创建模块，模块里面创建方法，定义有参数，和无数，有返回值和无返回值的情况，并说明无返回值的默认返回值。
3、消化今天的直播课内容
'''


# 有参数
def cas0(a):
    print(a)


# 无参数
def cas1():
    print()


# 有参数，有返回值
def str_a(num):
    print(num)
    return


str_a(4)


# 有参数，返回值None
def str_b(num1):
    print(num1)


if __name__ == '__main__':
    cas0(a=1)
    print(cas1())  # 返回None
    str_a(num=5)
    str_b(num1=10)
