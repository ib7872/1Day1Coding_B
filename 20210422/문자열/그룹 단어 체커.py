# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
#
# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.
#
# 예제 입력 1
# 3
# happy
# new
# year

# 예제 출력 1
# 3

# 예제 입력 2
# 4
# aba
# abab
# abcabc
# a

# 예제 출력 2
# 1

# 해결방법 설계
# 1. for문을 돌면서 입력 받은 string의 문자를 used 리스트에 넣어둔다
# 2. for문 속 if문을 돌려서 used 리스트와 같은 문자가 나오면 count = 0
# 3. for문을 끝까지 통과하면 count += 1
# 4. 연속되는 문자열일때는 어떻게 처리할지 고민

num = int(input())
count = 0

for i in range(num):
    counting = 0
    used_list = ["pass"]
    user_string = input()
    for i in user_string:
        if (i == used_list[counting]):
            continue

        if i in used_list:
            count -= 1
            break

        else:
            used_list.append(i)
        counting+=1
    count+=1
print(count)

# 풀이 후기: 너무 많은 자원을 사용 한 것이 아닌가 하는 생각
# for 문 중첩, if문의 과도한 사용 없이 해결 할 수 있는 방법 모색해보


# 선생님들의 풀이
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

