"""
练习：写一个"图书"类，属性至少包含书名和"是否已借出"状态，
实现 借出()、归还()、__str__ 三个方法——__str__ 要能看出书名和当前状态。
可以参考 core/models.py:202-203 ProductImage.__str__ 里
"方法内部调用 self 的属性拼出一句话"的写法。写完自己跑一下、换两本不同的书验证 self 有没有串。
不给答案，卡住了再来问。
"""

class Book:
    def __init__(self, n, s):
        self.name = n
        self.is_borrowed = s #True借出 False未借出

    def __str__(self):
        if self.is_borrowed:
            return f"{self.name}已借出"
        else:
            return f"{self.name}未借出"

    def lend(self):
        if self.is_borrowed:
            return f"{self.name}已经借出去了,不能再借了"
        else:
            self.is_borrowed = True
            return f"{self.name}刚刚借出去了"

    def return_book(self):
        self.is_borrowed = False
        return f"{self.name}刚刚还回来了"


book1 = Book('Python入门', False)
book2 = Book('深入理解计算机系统', True)

# print(book1)   
# print(book2)   

# book1.lend()
# print(book1)   
# print(book2)   

# book2.return_book()
# print(book1)   
# print(book2)  