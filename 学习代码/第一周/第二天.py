fruit = ["apple", "banana", "apple", "orange", "apple"]

# 方法一
# new_fruit = []
# for i in fruit:
#         print(i)
#         if i not in new_fruit:
#                 new_fruit.append(i)

# upper_fruit = [x.upper() for x in new_fruit]

# print(new_fruit, upper_fruit)


# 方法二
new_fruit = list(dict.fromkeys(fruit))

print(new_fruit)