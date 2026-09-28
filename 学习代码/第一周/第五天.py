test_text = "5微米精度\n\n食品级PP材质\n   适用于前置过滤   \n"

def my_to_lines(text):
         result = []
         for line in (text or '').splitlines():
            newline = line.strip()
            if newline:
                  result.append(newline)
         return result

def to_lines(text):
    """多行文本 → 去空行的字符串数组。"""
    return [ln.strip() for ln in (text or '').splitlines() if ln.strip()]

print(f"{my_to_lines(test_text)} \n{to_lines(test_text)}")