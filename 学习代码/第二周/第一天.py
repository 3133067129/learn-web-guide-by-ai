# 类是什么
"""
练习（不给答案）
仿照 Contact 写一个"图书"类，属性：书名、作者、价格、是否已借出。

创建两本不同的书（两个对象）
修改其中一本的"是否已借出"，验证另一本不受影响
进阶（可选）：再写一个"读者"类，含姓名、邮箱、留言，字段刻意对照 Contact 的 name/email/message
写完用 print() 验证，或带代码回来问。
"""

class Books():
    def __init__(self, title, auther, price, borrowed):
        self.title = title
        self.auther = auther
        self.price = price
        self.borrowed = borrowed

book1 = Books('name1', 'arthor1', 50, True)
book2 = Books('name2', 'arthor2', 100, False)

print(book1.borrowed, book2.borrowed)
book1.borrowed = False
print(book1.borrowed, book2.borrowed)

