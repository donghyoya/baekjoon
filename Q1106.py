"""
완전탐색, 상향식 접근, 메모이제이션 결합한 DP문제
"""

def dp_func(C, city_info):
    # 동적 프로그래밍 배열 초기화
    # 목표 고객 수 C를 정확히 맞출 수 있도록 배열 크기 설정
    max_customers = max(city[0] for city in city_info) * C + 1
    dp = [max_customers] * (C + 101)
    dp[0] = 0

    # 도시별 비용과 고객 수를 고려하여 dp 배열 업데이트
    for cost, customers in city_info:
        for i in range(customers, C + 101):
            dp[i] = min(dp[i], dp[i - customers] + cost)

    # 목표 고객 수에 도달하는 최소 비용 반환
    return min(dp[C:C + 101])

# 입력 받기
C, n = map(int, input().split())
city_info = [tuple(map(int, input().split())) for _ in range(n)]

# 최소 비용 계산
min_cost = dp_func(C, city_info)
print(min_cost)