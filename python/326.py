def solve(gifts):
    total_buy = 0
    money = gifts[-1][0]
    gifts.sort(key= lambda x: x[1])
    for gift in gifts:
        gift_price = gift[1]
        curr_money = gift[0]
        if money - gift_price < 0:
            break
        elif curr_money < gift_price:
            continue
        else:
            money -= gift_price
            total_buy += 1
    return total_buy


n = int(input())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
print(solve(gifts))