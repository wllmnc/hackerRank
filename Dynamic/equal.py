#https://www.hackerrank.com/challenges/equal
def minOpers(interns, target):
    count = 0
    for current_ in interns:
        if current_ - target >= 5:
            count += (current_ - target) // 5
            current_ = target + (current_ - target) % 5
        if current_ - target >= 2:
            count += (current_ - target) // 2
            current_ = target + (current_ - target) % 2
        if current_ - target == 1:
            count += 1
    return count

t = int(raw_input().strip())
while(t):
    n = int(raw_input().strip())
    interns = map(int,raw_input().strip().split(' '))
    interns.sort()
    target = interns[0]
    scores = [minOpers(interns, target)]
    if target >= 2:
        scores.append(minOpers(interns, target - 2))
    if target >= 1:
        scores.append(minOpers(interns, target - 1))
    print(min(scores))
    t -= 1
