# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-collections-ordereddict
from collections import OrderedDict

N=int(raw_input())
ordered_dictionary = OrderedDict()
while(N):
    item=[]
    item=raw_input().split(" ")
    price=item[len(item)-1]
    item.remove(price)
    name=' '.join(item)
    price=int(price)
    if name in ordered_dictionary:
        ordered_dictionary[name]=ordered_dictionary[name]+price
    else:
        ordered_dictionary[name]=price
    N=N-1
for key in ordered_dictionary.keys():
    print key, ordered_dictionary[key]
