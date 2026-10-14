"""
写一个 Product 类,属性有 slug、name、category,再加 __str__。
用列表存 5 个产品。
写 find(products, keyword),按名字查找。
写 count_by_category(products),返回 {"分类": 个数} 的字典。
每完成一个函数就 git commit。
"""

class Product:
    slug = ''
    name = ''
    category = ''
    __str__ = ''

    def __init__(self,s,n,c,str):
        self.slug = s
        self.slug = n
        self.category = c
        self.__str__ = str

    def find(products, keyword):
        pass

Products = [
    [["fc-1"], ["FC-1"], ["filter catridge"]],
    [["fc-2"], ["FC-2"], ["filter catridge"]],
    [["fh-1"], ["FH-1"], ["filter housing"]],
    [["fh-2"], ["FH-2"], ["filter housing"]],
    [["fh-3"], ["FH-3"], ["filter housing"]]
    ]
for i in Products: print(i)
