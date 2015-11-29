# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from sympy import *

x,y,z=symbols('x y z')
c1,c2=symbols('c1 c2')

varrs=[x,y]
consts=[c1,c2]
means={x:1,y:2,c1:5,c2:1}
diffs={x:0.3,y:0.2}

exp=c1*x*y+c2


for var in varrs:
    diffs[var]=(symbols('U('+var.name+')'),diffs[var])
    means.update({diffs[var][0]:diffs[var][1]})
parExpParVarrs={var:exp.diff(var) for var in varrs}
U_exp=0

for var in varrs:
    U_exp+=(parExpParVarrs[var]*diffs[var][0])**2


U_exp=sqrt(U_exp)
mean=exp.subs(means)
U=U_exp.subs(means)

if __name__=="__main__":
    i1,i,d1,d=symbols('i_1 i d_1 d')
    n=symbols('n')
    
    varrs=[i1,i,d1,d]
    consts=[n]
    means={i1:0.38964,i:0.24347,d1:3.541,d:6.115,n:1.5163}
    diffs={i1:3.84e-3,i:2.62e-3,d1:2.61e-3,d:2.61e-3}
    
    exp=(d1**2*cos(i1)**2/(d1*sin(i1)+d*sin(i)*(cos(i)/sqrt(n**2-sin(i)**2)-1))**2+1)*sin(i1)**2

    for var in varrs:
        diffs[var]=(symbols('U('+var.name+')'),diffs[var])
        means.update({diffs[var][0]:diffs[var][1]})
    parExpParVarrs={var:exp.diff(var) for var in varrs}
    U_exp=0
    
    for var in varrs:
        U_exp+=(parExpParVarrs[var]*diffs[var][0])**2
    
    
    U_exp=sqrt(U_exp)
    mean=exp.subs(means)
    U=U_exp.subs(means)
    
    print(U_exp,mean,U)

