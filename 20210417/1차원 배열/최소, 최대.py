# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 예제 입력 1
# 5
# 20 10 35 30 7

# 예제 출력 1
# 7 35

# n = int(input())
# a = list(map(int,input().split()))
# max = min = a[0]
#
# for i in range(n):
#     try:
#         if (max < a[i]):
#             max = a[i]
#         elif (min > a[i]):
#             min = a[i]
#     except:
#         break
# print(min,max)

# 다른 사용자의 풀이

# 중요**************
# map 앞 *은 map을 리스트화 시켜줌
# 리스트 앞 *는 리스트를 공백으로 풀어줌!!

input()
a=[*map(int,input().split())]
print(a)
print(*a)
print(min(a),max(a))

# test = [1, 2, 3, 4]
# print(*test)