#切线法不断逼近
def mysqrt(x):
    tmpx = float(x)
    k = float(1.0)
    k0 = float(0.0)
    while(abs(k0-k) >= 1):
        k0 = k
        k = (k + tmpx/k)/2
    return k
