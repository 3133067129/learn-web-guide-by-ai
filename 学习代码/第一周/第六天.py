while True:
    user_input = input("请输入数字: ")
    try:
        number = float(user_input)
        print(f"你输入的数字是: {number}")
        break
    except ValueError:
        print("你输入的不是数字,请重新输入")