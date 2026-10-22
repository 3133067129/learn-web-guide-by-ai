class Product:
    def __init__(self, slug, name, category):
        self.slug = slug
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} (slug: {self.slug}, category:{self.category})"

    def find(products, keyword):
        result = []
        keyword = keyword.lower()
        for p in products:
            if keyword in p.name.lower():
                result.append(p)
        return result

    def count_by_category(products):
        counts = {}
        for p in products:
            counts[p.category] = counts.get(p.category, 0) + 1
        return counts
    
products = [
    Product("fc-1", "FC-1", "filter cartridge"),
    Product("fc-2", "FC-2", "filter cartridge"),
    Product("fc-3", "FC-3", "filter cartridge"),
    Product("fh-1", "FH-1", "filter housing"),
    Product("fh-2", "FH-2", "filter housing"),
]

print(Product.count_by_category(products))
print([str(p) for p in Product.find(products, "FH")])