# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3.8.3 64-bit
#     language: python
#     name: python38364bita14c50cabb94433e97ec307454e1294b
# ---

# # Object-Oriented Programming in Python
# 参考 [Python class 说明文档](https://docs.python.org/3/tutorial/classes.html)。
#
# - **命名空间 (namespace)** 是*映射*：对象 (object) $\mapsto$ 名称
# - **作用域 (scope)**是命名空间可以直接访问的文本区域
# - **属性 (attribute)** 是指 `.` 后的名称

z = 1 + 2j
type(z)

print(f'{z = }')
print(f'{z.real = }')
print(f'{z.imag = }')
print(f'{z.conjugate() = }')
print(f'{abs(z) = }')

dir(z)


# ### [作用域和命名空间示例](https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example)

# +
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:\t\t", spam)
    do_nonlocal()
    print("After nonlocal assignment:\t", spam)
    do_global()
    print("After global assignment:\t", spam)

scope_test()
print("In global scope:\t\t", spam)


# -

# ## 类 (class)
# 一个可能最简单的示例：

# +
class Simplest():
    pass

a = Simplest()
a.name = 'A'
a.id = 0
a.position = ['p1', 'p2']

print(f'{a.name = }, {a.id = }, {a.position = }')


# -

# ### 类的建立

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = float(realpart)
        self.i = float(imagpart)

    def __repr__(self):
        return f'{self.r}{self.i:+f}j'#.format(sign='+' if self.i >= 0 else '')

    def modulus(self):
        m = (self.r ** 2 + self.i ** 2) ** 0.5
        return m

    def conjugate(self):
        return Complex(self.r, -self.i)


# ### 类的实例 (instance)

c = Complex(1, 2)
type(c)

print(f'{c = }')
print(f'{c.r = }')
print(f'{c.i = }')
print(f'{c.modulus() = }')
print(f'{c.conjugate() = }')

c.newattr = 'new'
c.newattr

c2 = Complex(1, 2)
try:
    c2.newattr
except Exception as e:
    print(e)


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


a = Dog('Fido')
b = Dog('Buddy')
print(f'{a.kind = }, {b.kind = }')
print(f'{a.name = }, {b.name = }')

a.kind = 'New Kind'
print(f'{a.kind = }, {b.kind = }')

# **Note**:
#
# As discussed in [A Word About Names and Objects](https://docs.python.org/3/tutorial/classes.html#tut-object), shared data can have possibly surprising effects with involving [mutable](https://docs.python.org/3/glossary.html#term-mutable) objects such as lists and dictionaries.
#
# See the example in https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables.

# ## 类的继承 (Inheritance)

# +
from astropy import constants as const

class BaseC:
    c = const.c

class BaseH:
    hbar = const.hbar

class Child(BaseC, BaseH):
    def __init__(self):
        print(BaseC.c)
        print('\n')
        print(BaseH.hbar)


# -

c = Child()




