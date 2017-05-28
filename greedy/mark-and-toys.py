#https://www.hackerrank.com/challenges/mark-and-toys
def max_toys(prices, rupees):
  #Compute and return final answer over here
  prices.sort()
  answer,cost = 0,0
  for price in prices:
        if cost + price <= rupees:
            answer += 1
            cost += price
        else:
            break
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
