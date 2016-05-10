# Enter your code here. Read input from STDIN. Print output to STDOUT

lines = "4104 8529 49984 54956 63034 82534 84473 86411 92941 95929 108831 894947 125082 137123 137276 142534 149840 154703 174744 180537 207563 221088 223069 231982 249517 252211 255192 260283 261543 262406 270616 274600 274709 283838 289532 295589 310856 314991 322201 339198 343271 383392 385869 389367 403468 441925 444543 454300 455366 469896 478627 479055 484516 499114 512738 543943 552836 560153 578730 579688 591631 594436 606033 613146 621500 627475 631582 643754 658309 666435 667186 671190 674741 685292 702340 705383 722375 722776 726812 748441 790023 795574 797416 813164 813248 827778 839998 843708 851728 857147 860454 861956 864994 868755 116375 911042 912634 914500 920825 979477"
n = map(int, raw_input().strip().split(" "))
arr=map(int, lines.strip().split(" "))
preValue=-1
inDisorder=False
index=[0,0,0]
for i in range(0,len(arr)):
    currentValue=arr[i]
    if not inDisorder:
        if preValue>currentValue:
            inDisorder=True
            index=[i-1,i,1]
        #preValue=currentValue
    else:
        #si esta en desorden y el valor anterior es menor que el actual
        if preValue>currentValue:
            index[1]=i
            index[2]=2
        else:
            if index[2]:
            	print "case . " +str(i)
                index[2]=-1
    preValue=currentValue

if index[2]>0:
    print "yes"
    if index[2]==1:
        print "swap",
    else:
        print "reverse",
    print str(index[0]+1),
    print str(index[1]+1),
else:
    print "no"