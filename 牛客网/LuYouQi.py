'''
题目：路由器
一条直线上等距离放置了n台路由器。路由器自左向右从1到n编号。第i台路由器到第j台路由器的距离为| i-j |。 
每台路由器都有自己的信号强度，第i台路由器的信号强度为ai。
所有与第i台路由器距离不超过ai的路由器可以收到第i台路由器的信号（注意，每台路由器都能收到自己的信号）。
问一共有多少台路由器可以收到至少k台不同路由器的信号。

输入描述:
输入第一行两个数n , k（1≤n , k≤10^5）

第二行n个数, a1 , a2 , a3……… , an（0≤ai≤10^9）

输出描述:
输出一个数，一共有多少台路由器可以收到至少k台不同路由器的信号。

示例1
输入
4 4
3 3 3 3
输出
4
'''
'''
#自己的方法：算法复杂度过高，无法通过测试
def function(n,k,lists):
    res=0
    for i in range(n):
        num=1 #自身路由器可以收到自己的信号，所以从1开始累加
        for j in range(n):
            if i!=j:
                if abs(i-j)<=lists[j]:
                    num+=1
        if num>=k:
            res+=1   
    return res 

if __name__ == "__main__":
    n,k=map(int,input().split())
    lists=list(map(int,input().split()))
    print(function(n,k,lists))
'''

#别人的方法：
#对于每个路由器都有一个辐射范围，从左往右在辐射开始的时候记录+1，在辐射结束的时候记录-1，
#再从左到右遍历一遍，累计的和就是当前被辐射的路由器个数。时间复杂度为O(n)
n,k = (int(i) for i in input().split())
arr=[int(i) for i in input().split()]
b=[0]*n
for i in range(n):
    if i-arr[i]<0:
        b[0]+=1
    else:
        b[i-arr[i]]+=1
    if i+arr[i]<n-1:
        b[i+arr[i]+1]-=1
tmp=0
num=0
for i in b:
    tmp+=i
    if tmp>=k:
        num+=1
print(num)
