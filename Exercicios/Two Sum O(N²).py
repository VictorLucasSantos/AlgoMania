def solution(numbers, target_sum):
    for i in range(len(numbers)):
        num1 = numbers[i]
        for j in range(i + 1, len(numbers)):
            if num1 + numbers[j] == target_sum:
                return f"{[num1, numbers[j]]} ; {num1, numbers[j]} é : {target_sum}"
    return []


if __name__ == "__main__":
    print(solution([4, 1, 2, -2, 11, 15, 1, -1, -6, -4], 9))
