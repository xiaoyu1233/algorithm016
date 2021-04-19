





N,V = map(int,input().split())

v = [0] * (N+1)
w = [0] * (N+1)
s = [0] * (N+1)

for i in range(1, N + 1):
    s[i], v[i],w[i]= map(int,input().split())

f = [0] * (V+1)

for i in range(1,N+1):
    for j in range(V,v[i] - 1,-1):
        for k in range(1,min(s[i],j // v[i]) + 1):
            f[j] = max(f[j],f[j-k*v[i]] + k*w[i])
print(f[V])



num,val = map(int,input().split())

price = [0] * (num+1)
beauty = [0] * (num+1)
number = [0] * (num+1)

for i in range(1, num + 1):
    number[i], price[i],beauty[i]= map(int,input().split())

f = [0] * (val+1)

for i in range(1,num+1):
    for j in range(val,price[i] - 1,-1):
        for k in range(1,min(number[i],j // price[i]) + 1):
            f[j] = max(f[j],f[j-k*price[i]] + k*beauty[i])
print(f[val])