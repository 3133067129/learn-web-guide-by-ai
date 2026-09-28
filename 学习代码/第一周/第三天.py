'''
### 第 1 周 · 第 3 天｜字典

- [x] **读**（约 10 分钟）：https://www.runoob.com/python3/python3-dictionary.html
      **重点捡回**：`{"键": "值"}` 创建；`字典["键"]` 取值；`.get("键")` 取不到不报错；
      `for k, v in 字典.items()` 遍历。
- [x] **看项目**（约 10 分钟）：打开 `core/serializers.py` 第 29 行的 `to_specs`。
      注意它最后返回的是 `[{'label': ..., 'value': ...}, ...]`——
      **一个列表，里面装着一堆字典**。
      这个结构是本项目最常见的形态：后端吐给前端的数据基本都长这样。
      实际效果：同事在后台写"外径: 63mm"，它变成 `{'label': '外径', 'value': '63mm'}`，
      前端就能把它渲染成规格表的一行。
- [ ] **动手**（约 20 分钟）：新建 `第3天.py`：
      1. 建一个字典 `产品 = {"名称": "滤芯", "编号": "FC-35", "长度": 508}`
      2. 打印它的编号；再用 `.get("价格")` 试试取一个不存在的键（应该返回 `None` 而不是报错）
      3. 用 `for k, v in 产品.items()` 把每一项打印成 `名称: 滤芯` 这种格式
      4. **统计词频**：给一段文字，数出每个词出现几次（用字典存"词→次数"）
- [ ] **完成标志**：词频统计能跑出正确结果，比如 `{'苹果': 2, '香蕉': 1}`。
- 卡住了记这里：
'''

# tinydict = {'Name': 'Bob', 'Age': 7, 'Class': 'First'}

# print(tinydict)

# print("Name:", tinydict['Name'])

# print("Age:", tinydict['Age'])

# tinydict['Age'] = 8

# print("Age:", tinydict['Age'])

# tinydict['School'] = "安徽农业大学"

# print("School:", tinydict['School'])

# print(tinydict)

# del tinydict['Name']
# print(tinydict)

# tinydict.clear()
# print(tinydict)

# del tinydict
# print(tinydict)

# tiny = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print(tiny)
# def to_lines(text):
#     """多行文本 → 去空行的字符串数组。"""
#     return [ln.strip() for ln in (text or '').splitlines() if ln.strip()]


# def to_specs(text):
#     """每行 “标签: 值”（中英文冒号均可）→ [{label, value}]。"""
#     rows = []
#     for ln in to_lines(text):
#         positions = [p for p in (ln.find(':'), ln.find('：')) if p >= 0]
#         if positions:
#             i = min(positions)
#             rows.append({'label': ln[:i].strip(), 'value': ln[i + 1:].strip()})
#         else:
#             rows.append({'label': '', 'value': ln})
#     return rows

# x = input("请输入一段带':'的文字（多组用空格分隔）")

# # 一行里写了好几组时，先按空格拆成多行，再交给 to_specs
# print(to_specs(x.replace(" ", "\n")))

# 产品 = {"名称": "滤芯", "编号": "FC-35", "长度":508}
# print(产品['编号'], 产品.get("价格"))
# for k, v in 产品.items():
#         print(f'{k}: {v}')

text = "apple banana apple orange banana apple"

word_count = {}

words = text.split()

for i in words:
        if i not in word_count:
            word_count[i] = words.count(i)
print(word_count, type(word_count))
