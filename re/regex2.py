import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)

# 获取match对象
obj = regex.search('abcdefjnk')

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)   # 目标字符串结束位置
print(obj.re)   # 正则表达式
print(obj.string)   # 目标字符串
print(obj.lastgroup)    # 最后一组组名
print(obj.lastindex)    # 最后一组序号

print("=============================")
print(obj.start())
print(obj.end())
print(obj.span())
print(obj.groupdict())
print(obj.groups())
print(obj.group())
