# 学习代码
# users = {'Hans': 'active', '景太郎': 'active', 'Alice': 'inactive'}

# for user, stauts in users.copy().items():
#         if stauts == 'inactive':
#                 del users[user]

# active_user = {}
# for user, status in users.items():
#         if status == 'active':
#                 active_user[user] = status
# print(users, active_user)

# 项目源码
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

marks = [85, 92, 45, 78]
for i in marks:
        if i >= 90:
                print(i, '优秀')
        elif i >= 69:
                print(i, '及格')
        else:
                print(i, '不及格')