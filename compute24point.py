#coding=utf8
#!/usr/bin/python

def F(li1, li2): #对两个列表元素进行所有可能的四则运算
    res = []
    for a in li1:
        for b in li2:
            s = '(' + str(a) + ') + (' + str(b) + ')'
            res.append(s)
            s = '(' + str(a) + ') * (' + str(b) + ')'
            res.append(s)
            s = '(' + str(a) + ') - (' + str(b) + ')'
            res.append(s)
            s = '(' + str(b) + ') - (' + str(a) + ')'
            res.append(s)
            
            if eval(str(b)) != 0:
                s = '(' + str(a) + ') / (' + str(b) + ')'
                res.append(s)
            if eval(str(a)) != 0:
                s = '(' + str(b) + ') / (' + str(a) + ')'
                res.append(s)
    return res

def r_2(arr): #返回arr中元素的所有可能四则运算形式
    res = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            a = arr[i]
            b = arr[j]
            lost = []
            for t in range(0, len(arr)):
                if t != i and t != j:
                    lost.append(arr[t])
                    
            if len(lost) == 0:
                res.extend(F(a, b))
            else:
                lost.append(F(a, b))
                res.extend(r_2(lost))
    return set(res)

def del_g(match):
    return match.group()[1:-3]

import re
arr = []
nums = raw_input(u"请输入多于一个的整数（用空格分隔）:".encode('gbk')) #基于python2.7
num = re.split(r'\s+', nums.strip())
for i in num:
    arr.append([float(i)])

sol = False      
for e in r_2(arr):
    if eval(e) == 24:
        print re.sub(r'\([\d\.]+\)', del_g, e)
        sol = True
if not sol:
    print "无解。"
