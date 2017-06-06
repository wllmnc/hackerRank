def getranges(arr_):
    arr_.sort()
    result=[]
    preva,prevb=arr_[0]
    for (a,b) in arr_:
        print result,a,b
        if preva!=a:
            if prevb>=a or prevb==a-1:
                # si el ultimo b es mas grande que a  verificar si el b es mas grande que prevb
                if prevb<b or prevb==b-1 :
                    prevb=b
            else:
                result.append((preva,prevb))
                preva,prevb=a,b
        else: # son iguales las a validamos quien es el b mas grande
            if prevb<b or prevb==b-1 :
                prevb=b
    result.append((preva,prevb))
    print result
    
    

n=int(raw_input())
arr_=[]
for _ in range(n):
    a=raw_input().split(" ")
    a=(int(a[0]),int(a[1]))
    arr_.append(a)
getranges(arr_)
