import functools

# 숫자들의 합
def sum_of_numbers(s):
    return sum(int(char) for char in s if char.isdigit())

def compare_serials(a, b):
    # 길이를 우선 비교
    if len(a) != len(b):
        return len(a) - len(b)
    
    # 숫자 합 비교
    sum_a = sum_of_numbers(a)
    sum_b = sum_of_numbers(b)
    if sum_a != sum_b:
        return sum_a - sum_b

    # 사전순 비교
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

# 입력 받기
n = int(input())
serials = [input().strip() for _ in range(n)]

# 정렬
serials.sort(key=functools.cmp_to_key(compare_serials))

# 출력
for serial in serials:
    print(serial)
