numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number%3)-1].append((number))
    print(output)


# print(output[0])
# print(output[1])
# print(output[2])
# print(output[3])
# print(output[4])

