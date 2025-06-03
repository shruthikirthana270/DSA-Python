def aggressivecows(stalls,k):
    def canweplace(minDist,stalls,k):
        cow=stalls[0]
        placedCows=1
        for stall in range(1,len(stalls)):
            if(stalls[stall]-cow>=minDist):
                cow=stalls[stall]
                placedCows+=1
            if(placedCows>=k):
                return True
        if(placedCows<k):
            return False
    stalls.sort()
    Min=min(stalls)
    Max=max(stalls)
    if(k==2):
        return Max-Min
    for minDist in range(1,Max-Min+1):
        if(canweplace(minDist,stalls,k)):
            continue
        else:
            return minDist-1
        
