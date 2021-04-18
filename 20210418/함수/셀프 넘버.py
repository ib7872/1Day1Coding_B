# 문제
# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
#
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
#
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.
#
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
#
# n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.
#
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
#
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 없다.
#
# 출력
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

# 예제 입력 1

# 예제 출력 1
# 1
# 3
# 5
# 7
# 9
# 20
# 31
# 42
# 53
# 64
#  |
#  |       <-- a lot more numbers
#  |
# 9903
# 9914
# 9925
# 9927
# 9938
# 9949
# 9960
# 9971
# 9982
# 9993

# 57

# num = 57 --> 69
#
# # print(( (num//10) + (num%10) + num ))
# print(( (num//10) + (num%10) + num ) == num)
# if


# a = list(range(1,10001))
# for num in range(1,10001):

# 차집합 활용

# num_range = list(range(1,10001))
# aa= []
# for num  in range (1,10001):
#     a_q = num//1000
#     a = num%1000
#
#     b_q = a//100
#     b = a%100
#
#     c_q = b//10
#     c = b%10
#
#     if (a_q + b_q + c_q + c + num >= 10000):
#         break
#     else:
#         new_num = (a_q + b_q + c_q + c + num)
#         aa.append(new_num)
#
# complement = list(set(num_range) - set(aa))
# complement = sorted(complement)
# complement = complement[:-4]
# for i in complement:
#     print(i)



def sum_position(n):
    aa = 0
    bb = n
    while(n>0):
        sum2 = int(n // 10)
        avg = int(n%10)
        n = n/10
        aa +=avg
    aa += sum2
    return (aa+bb)

non_self_number = []
num_range = list(range(1,10001))

for i in num_range:
    non_self_number.append(sum_position(i))
self_number = sorted(list(set(num_range) - set(non_self_number)))
for i in self_number:
    print(i)