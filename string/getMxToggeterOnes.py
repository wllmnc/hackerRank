def getMxTogetherOnes(S):
	max=0,last=0
  cont_temp=0
  for i xrange(len(S)):
  	item=S[i]
    if item==1 and last==1: #11
    	cont_temp=cont_temp+1
    elif item==0 and last==1: #10
			max=(max if max>cont_temp else cont_temp)
      last=0
      cont_temp=0
    elif item==1: #01
    	last=1
      cont_temp=1 
  max=(max if max>cont_temp else cont_temp)
  return max
