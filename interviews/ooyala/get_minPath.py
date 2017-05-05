


S = hit  
D = hat, jog, hot, pub, rub, cat, mat, lot, , hut , put 
E = pat

min_=10

        1er nivel  2do nivel
                    hot,2  ->  
         hat,1      pat,2 2
                    hut,2 ->asd ->
                   
                    hat 
hit,0    hot,1      hut
      
      
         hut,1      s     s   hat,4   hot,5  ->  
                                      pat,5 5
                                      hut,5 ->asd ->


hit -> hat,hot,hut
hat -> pat,hot,hut,hit,cat,mat
hot -> hat,hit,hut,lot


hit -> hut -> put ->  hut -> put -> pat

hit -> hat -> pat

Dic_word_level={}
min_=len(D)
def getoptimalpath(S,D,E,level):
    for item in D:
        if getDiff(S,item)==1:
           if item in Dic_word_level:
              if Dic_word_level[item]<level+1:
                 #detener el algoritmo hay un camino mas corto
                 return Dic_word_level[item]
              else:
                 return level+1
           else:   
              Dic_word_level[item]=level+1
              if item!=E:                 
                  level_r=getoptimalpath(item,D,E,level+1)
                  if level_r<min_:
                      min_=level_r
              else:
                  return level
#mejorar la condicion de paro para no usar la variable global

def getDiff(S,S1):
    cont=0
    for i in range(len(S):
        cont= cont + (1 if S[i]!=S1[i] else 0)
    return cont
