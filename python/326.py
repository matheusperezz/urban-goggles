import heapq

def solve(gifts):
    total_buy = 0
    money = gifts[-1][0]

    min_heap = []
    for gift in gifts:
        heapq.heappush(min_heap, (gift[1], gift[0]))
    
    while min_heap:
        gift_price, curr_money = heapq.heappop(min_heap)
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
