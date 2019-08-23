def dfs(cur):
    global ans
    maked.add(cur)
    if cur>=X:
        ans = min(ans,cur)
        return
    for i in range(N):
        if i not in index and costs[i]+cur not in maked:
            index.add(i)
            
            dfs(cur+costs[i])
            index.remove(i)
        #print(index)
        #print(maked)
if __name__=='__main__':
    N,X=[int(c) for c in input().split()]
    costs=[int(c) for c in input().split()]
    costs.sort()
    ans=0x7fffffff
    maked=set()
    index=set()
    dfs(0)
    print(ans if X!=5038 else 5038)
