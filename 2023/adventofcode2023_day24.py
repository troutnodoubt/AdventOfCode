import numpy as np
from scipy.optimize import minimize

fname='input_day24.txt'
# fname='example_day24.txt'
with open(fname) as fp: data = fp.read().splitlines()

def getValues(hail1,hail2):
    x10=int(hail1[0].split(',')[0])
    y10=int(hail1[0].split(',')[1])
    z10=int(hail1[0].split(',')[2])
    u1=int(hail1[1].split(',')[0])
    v1=int(hail1[1].split(',')[1])
    w1=int(hail1[1].split(',')[2])
    x20=int(hail2[0].split(',')[0])
    y20=int(hail2[0].split(',')[1])
    z20=int(hail2[0].split(',')[2])
    u2=int(hail2[1].split(',')[0])
    v2=int(hail2[1].split(',')[1])
    w2=int(hail2[1].split(',')[2])
    
    return x10,y10,z10,u1,v1,w1,x20,y20,z20,u2,v2,w2

def getListValues(hail1,hail2):
    x10,y10,z10,u1,v1,w1,x20,y20,z20,u2,v2,w2=getValues(hail1,hail2)
    return([x10,y10,z10,u1,v1,w1])

def findIntersection(hail1,hail2):
    
    x10,y10,z10,u1,v1,w1,x20,y20,z20,u2,v2,w2=getValues(hail1,hail2)
    m1=v1/u1
    b1=y10-m1*x10
    
    m2=v2/u2
    b2=y20-m2*x20
    res=[]
    crosstime1=0
    crosstime2=0
    if m2!=m1:
        a=np.matrix([[-m1, 1],[-m2 ,1]])
        b=np.matrix([b1,b2])
        res=a.I*b.T
        crosstime1=(res[1][0].item()-y10)/v1
        crosstime2=(res[1][0].item()-y20)/v2
    return res,crosstime1,crosstime2

def closestPassTime(hail1,hail2):
    
    num=(hail2[0]-hail1[0])*(hail2[3]-hail1[3])+(hail2[1]-hail1[1])*(hail2[4]-hail1[4])+(hail2[2]-hail1[2])*(hail2[5]-hail1[5])
    den=(hail2[3]-hail1[3])**2+(hail2[4]-hail1[4])**2+(hail2[5]-hail1[5])**2
    
    return -num/den

def errorSquared(hail1,hail2,time):

    pos1=[hail1[0]+time*hail1[3],hail1[1]+time*hail1[4],hail1[2]+time*hail1[5]]
    pos2=[hail2[0]+time*hail2[3],hail2[1]+time*hail2[4],hail2[2]+time*hail2[5]]
    
    return (pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2

def objectiveFunction(test):
    sumsquarerror=0
    for h in haillist:
        passtime=closestPassTime(test, h)
        sumsquarerror+=errorSquared(test, h, passtime)
    return sumsquarerror
  
def isInBounds(minbound,maxbound):
    count=0
    for i in range(len(hail)-1):
        for j in range(i+1,len(hail)):
            intersect,crosstime1,crosstime2 = findIntersection(hail[i],hail[j])
            if len(intersect)>0:
                if crosstime1>0 and crosstime2>0 and \
                    intersect[0][0].item() >= minbound and \
                    intersect[0][0].item() <= maxbound and \
                    intersect[1][0].item() >= minbound and \
                    intersect[1][0].item() <= maxbound:
                    count+=1
                    
    return count

hail=[[a for a in line.split('@')] for line in data]
haillist=[]
for i,h in enumerate(hail):
    haillist.append(getListValues(h,h))
    if i>10: break

minbound=7
maxbound=27
minbound=200000000000000
maxbound=400000000000000
        
print('Part 1 is',isInBounds(minbound,maxbound))        

guess=[309991770591665, 460585296453288, 234197928919584,-630,-301,970]
res=minimize(objectiveFunction,guess,method='Powell',tol=1e-9)

if res['success']:
    xsol=round(res['x'][0].item())
    ysol=round(res['x'][1].item())
    zsol=round(res['x'][2].item())
print(res['fun'])
print('Part 2 is', xsol+ysol+zsol)

print(xsol,ysol,zsol)
#1004774995962969 too low
#1004774995965215 is too high

#1004774995964537 error 19.75
#1004774995964534 error 6.38
#1004774995964534 error 8.40 - right answer
#1004774995964535 error 1.18 #too high

# kept rerunning the simulation with output values from the previous run to drive the
# objective function down a bit lower until it converged, more or less, on a value.
# Leaves a lot to be desired.