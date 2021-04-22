# a=input()
# c=['c=','c-','dz=','d-','lj','nj','s=','z=']
# for i in c:
#     a=a.replace(i,"a")
#     print(a)
# print(len(a))



# 선생님들의 풀이
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)


