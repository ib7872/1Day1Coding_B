# 문제
# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1
# Mississipi

# 예제 출력 1
# ?

# 예제 입력 2
# zZa

# 예제 출력 2
# Z

# 예제 입력 3
# z

# 예제 출력 3
# Z

# 예제 입력 4
# baaa

# 예제 출력 4
# A

# 풀이 방법 먼저 구상
# 1. lower()를 이용해서 대소문자를 합칠 것
# 2. ASCII코드를 이용해서 for문으로 string을 돌면서 count를 하나씩 올려줌
# 3. 딕셔너리 자료구조를 이용하면 좋을 듯
# 3. count가 가장 높은 알파벳을 .upper()로 출력

# sentence = input().lower()
# sentence_dic = {}
# value_count = 0
# for i in range (97,123):
#     sentence_dic[chr(i)] = 0
#     for j in sentence:
#         if (chr(i)==j):
#             sentence_dic[chr(i)] += 1
#
# for key,value in sentence_dic.items():
#     if(value == max(sentence_dic.values())):
#         value_count += 1
#
# for key,value in sentence_dic.items():
#     if(value_count>1):
#         print("?")
#         break
#     else:
#         if(value == max(sentence_dic.values())):
#             print(key.upper())


# 코드가 너무 복잡함 다시 간단하게 짜보
# 위의 코드에서 문제는 for문이 너무 많이 쓰였다는 것과 딕셔너리에서 중복을 어떻게 방지할지에 대한 부분이 애매함

# 풀이 방법 먼저 구상
# 1. lower()를 이용해서 대소문자를 합칠 것
# 2. ASCII코드를 이용해서 for문으로 string을 돌면서 count를 하나씩 올려줌(리스트에 넣어줌)
# 3. count()함수는 리스트를 다 돌면서 해당 값의 개수를 세줌

s = input().lower()
a = []
for i in range(97,123):
    a.append(s.count(chr(i)))
# max(a)의 개수가 1 이상이라면 "?"출력
if(a.count(max(a))>1):
    print("?")
else:
    print(chr(a.index(max(a))+97).upper())