>>> print("i am {0},age {1}".format("tom",18))
i am tom,age 18
>>> print("{:.2f}".format(3.1415926)) # 保留小数点后两位
3.14
>>> print("{:+.2f}".format(-1)) # 带符号保留小数点后两位
-1.00
>>> print("{:.0f}".format(2.718)) # 不带小数位
3
>>> print("{:0>3d}".format(5)) # 整数补零，填充左边, 宽度为3
005
>>> print("{:,}".format(10241024)) # 以逗号分隔的数字格式
10,241,024
>>> print("{:.2%}".format(0.718)) # 百分比格式
71.80%
>>> print("{:.2e}".format(10241024)) # 指数记法
1.02e+07
