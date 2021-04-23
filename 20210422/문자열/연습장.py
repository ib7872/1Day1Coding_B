# a=input()
# c=['c=','c-','dz=','d-','lj','nj','s=','z=']
# for i in c:
#     a=a.replace(i,"a")
#     print(a)
# print(len(a))




word = 'hap1pyp'
a = sorted(word)

# b가 핵심인데, 반복문의 개념으로 이해해야 할 듯
# key는 함수가 들어가고 앞에는 파라미터가 들어감
# sorted에 str을 넣으면 모두 리스트로 바뀜
# 처음 기준인 h가 들어가고, 그 다음 word리스트에 a가 없으므로 옆에 붙임
# 그다음 p가 없으므로 옆에 붙임, 그다음 p는 p가 있으므로 p옆에 붙임
# y는 없으므로 p옆에 붙임
# 마지막 p는 기존에 p가 있으므로 p옆에 붙임

b = sorted(word,key=word.find)
c = list(word)

print(a)
print(b)
print(c)


# 선생님들의 풀이
# result = 0
# for i in range(int(input())):
#     word = input()
#     print(word.find)
#     if (list(word) == sorted(word, key=word.find)):
#         result += 1
# print(result)


# --> sorted의 사용법
# key 파라미터로 전달된 함수는 입력 레코드마다 한번씩 호출되어진다.

# >>> sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']