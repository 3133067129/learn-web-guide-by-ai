"""
写一个 Product 类,属性有 slug、name、category,再加 __str__。
用列表存 5 个产品。
写 find(products, keyword),按名字查找。
写 count_by_category(products),返回 {"分类": 个数} 的字典。
每完成一个函数就 git commit。
"""

class Product():
    slug = ''
    name = ''
    category = ''
    def __str__(self):