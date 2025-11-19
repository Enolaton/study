def solution(chicken):
    answer = 0
    coupon = 0
    while chicken >= 10:
        coupon += chicken % 10
        answer += (chicken//10 + coupon // 10)
        chicken = (chicken//10 + coupon // 10)
        if coupon >= 10:
            coupon = coupon%10
    answer += (chicken+coupon)//10
    return answer