# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
# 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
#
# 크로아티아 알파벳	변경
# č 	c=
# ć	    c-
# dž	dz=
# đ	    d-
# lj	lj
# nj	nj
# š	    s=
# ž	    z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
#
# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
#
# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
#
# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#
# 예제 입력 1
# ljes=njak
# 예제 출력 1
# 6

# 예제 입력 2
# ddz=z=
# 예제 출력 2
# 3

# 예제 입력 3
# nljj
# 예제 출력 3
# 3

# 예제 입력 4
# c=c=

# 예제 출력 4
# 2

# č 	c=
# ć	    c-
# dž	dz=
# đ	    d-
# lj	lj
# nj	nj
# š	    s=
# ž	    z=


# 해결방안 알고리즘 설계
# 1. 리스트 안에 문자를 넣어서 카운트
# ljes=njak

# lj
# e
# s=
# nj
# a
# k


# 나의 풀이

# 문자를 보고 for 문을 돌려서 if in 을 통해 리스트 속 성분이 있는지 검사
# 소문자: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
# c,d,z,lj,nj,s 제외


alpha_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alpha_list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = input()
count = 0

for i in alpha_list:
    if i in alphabet:
        # 2개 이상 있을 때를 대비해서 count 해서 넣음
        count+=alphabet.count(i)
        alphabet = alphabet.replace(i," ")
for j in alpha_list2:
    if j in alphabet:
        # 2개 이상 있을 때를 대비해서 count 해서 넣음
        count+=alphabet.count(j)
print(count)


# 훌륭하신 분들의 풀이
a=input()
print(len(a)-a.count("=")-a.count("dz=")-a.count("-")-a.count("lj")-a.count("nj"))

# 구조를 보자
# 1. string을 입력 받음
# a의 문자열의 길이에서 특수 문자의 개수를 뺌

# 다른 선생님의 풀이
a=input()
c=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in c:
    a=a.replace(i,"a")
print(len(a))

# 1. string을 입력 받음