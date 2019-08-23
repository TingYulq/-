'''
方法1：
如果输入的数组里没有1，那么返回K即机会次数。 
如果输入的数组有1，且K>=N-1，那么返回N。 
如果输入的数组有1，且K小于N-1： 
那么返回的值，至少应该是1+K。想象有个1+K宽度的窗口，在数组上滑动，在某一次滑动时，窗口内有1个1，K个0，这样就用掉K次机会，把窗口内的0都变成1，就形成了连续1串。 
进一步说（考虑已有1串）， 
如果数组已有的最长连续1子串的长度为max，那么返回的值至少为max+K。（读者可以画图验证）

程序的整体思路为： 
滑动窗口slide初始大小为max+K。即slide = max+K。 
滑动窗口总和sum初始大小为max。即sum = max。

循环每次检测，当前大小为slide 的滑动窗口，是否有一次滑动使得总和>=sum。 
如果有，说明返回结果至少为slide，但还有可能更大，所以slide和sum都++。 
如果没有，说明返回结果应该为slide-1，停止循环。
'''

'''
#提交代码时，取消以下注释
##N,K = map(int,input().split())
##num = list(map(int,input().split()))

#提交代码时，删除以下代码
#[1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
N = 10
K = 2
num = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1]


def checkInterval(possible,sumvalue):

    startmax = N - possible
    for start in range(0,startmax+1):
        #start范围是从start到startmax
        end = start + possible
        #start和end指分片的开始与结束
        if sum(num[start:end]) >= sumvalue:
            return True
    return False


if(1 not in num):#如果数组里没有1，那么最长也就是机会个数
    print(K)
elif(K>=N-1):
    print(N)
else:
    #找出最长1的长度
    maxleng = 0
    tempmaxleng = 0
    for i in num:
        if(i == 1):
            tempmaxleng += 1
        else:
            if(tempmaxleng>maxleng):
                maxleng = tempmaxleng
            tempmaxleng = 0
    #得到了最长连续1的长度
    sumvalue = maxleng#滑动窗口求和至少为sumvalue
    possible = sumvalue+K#滑动窗口的长度至少为possible

    while(True):
        if(not checkInterval(possible,sumvalue)):
           break 
        sumvalue += 1
        possible += 1
    print(possible -1)
'''

'''
方法2：
双指针，一次遍历。O（n）时间复杂度。
牛客网的 python2 运行更快，所以附上了 python2 的代码，如果想用 python3，去掉前两行的 raw_ 即可。
用 l 代表左指针, r 代表右指针。当 k 非 0 时，我们就让右指针一直右移，遇到 1 就直接右移，遇到 0 时从 k 中选一个来填充该位，k就变成了 k−1 。
当 k 为 0 时，右指针遇到 1 依旧右移，遇到 0 时，需要停下来，因为此时的 k 不够用了，此时左指针和右指针之间的数字长度就是指针 j 的最长全1子串 ，
左指针要动了。左指针一定要遇到首个 0 时再停下来，记录此时的结果后，我们接着右移右指针，重复上述过程即可。代码更清晰！
其中最后的代码 res=max(res,r−l) 包含了 k 用不完的情况以及数字的最后一位是1的情况。
'''

n,k = list(map(int,input().split()))
num = list(map(int,input().split()))
l,r =0,0
res = 0
while r<n:
    if num[r]==1:
        r += 1
    elif k > 0:
        k -= 1
        r += 1
    else:
        res = max(res,r-l)
        while l<r and num[l]==1:
            l += 1
        r += 1
        l += 1
res = max(res,r-l)
print(res)