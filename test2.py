from test import Func1

class Func2():

    def calc_one_plus_one(self):
        func1 = Func1()
        result = func1.add(1,1)
        return result
func2 = Func2()
print(func2.calc_one_plus_one())


class Func3():

    def calc_one_plus_two(self, func, a, b):
        return func.add(a,b)

# 实例化func3
func3 = Func3()
# 实例化func1 （实现加法的函数）
func1 = Func1()
print(func3.calc_one_plus_two(func1, 1,2))
