import math

def f11(x,y):
    return (math.cos(x**5+math.exp(y)+92)-math.log(19*x)-(40*(x**6)+y**2-83)/(math.tan(x**5/62-x**8)-math.sin(y))-(math.sin(y)-96*y**7+87)/(math.exp(y)-y))
    #"{:e}".format(math.cos(x**5+math.exp(y)+92)-math.log(19*x)-(40*(x**6)+y**2-83)/(math.tan(x**5/62-x**8)-math.sin(y))-(math.sin(y)-96*y**7+87)/(math.exp(y)-y))

def f12(x):
    if x<193:
        return (math.cos(x**5+math.exp(x)+92)-math.log(19*x))
        #"{:e}".format(math.cos(x**5+math.exp(x)+92)-math.log(19*x))
    elif 193<=x<283:
        return (40*x**6+x**2-83)
        #"{:e}".format(40*x**6+x**2-83)
    elif 283<=x<316:
        return (math.tan(x**5/62-x**8)-math.sin(99*x**5))
        #"{:e}".format(math.tan(x**5/62-x**8)-math.sin(99*x**5))
    elif x>=316:
        return (96*x**3-53*x+45)
        #"{:e}".format(96*x**3-53*x+45)

def f13(n,m):
    i=1
    j=1
    k=1
    s1=0
    s2=0
    while k<=n:
        s1+=25*(k**2)-61*(k**6)
        k+=1
    while i<=n:
        while j<=m:
            s2+=j**5-30*(i**2)-30
            j+=1
        i+=1
        j=1
    return (26*s2+s1)
    #"{:e}".format(26*s2+s1)

def f4(n):
    if n==0:
        return (10)
    else:
        return abs((f4(n-1))-1/41*f4(n-1))
        #"{:e}".format(f4(n-1)-1/41*f4(n-1))
def f14(n):
    return (f4(n))
    #"{:e}".format(f4(n))

