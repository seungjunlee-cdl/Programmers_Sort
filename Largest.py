def solution(numbers):
    numbers_str = list(map(str,numbers))
    d = []
    largest = []

    for i in range(len(numbers_str)):
        while len(numbers_str[i]) < 4:
            numbers_str[i] += numbers_str[i]
        numbers_str[i] = numbers_str[i][0:4]

    d = [[numbers[i],int(numbers_str[i]),i] for i in range(len(numbers_str))]
    d = sorted(d, key = lambda x:-x[1])

    for i in range(len(numbers_str)):
        largest.append(numbers[d[i][2]])

    largest = str(int("".join(list(map(str,largest)))))
    return largest
