# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:18:49 2015

@author: U
"""
class DataProcessing:
    t_p = {3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.46, 8:2.37, 9:2.31, 10:2.26, 15:2.15, 20:2.09}    
    def __init__(self,OOM,ENOB,data=None):
                
        if data is None:
            i = 1
            self.data = []
            while True:
                try:
                    x = eval(input('X' + str(i) + '='))
                    i += 1
                    x = float(x)
                    self.data.append(x)
                except ValueError:
                    print(self.data)
                    break
                except SyntaxError:
                    print(self.data)
                    break
                
        else:
            self.data=data
            print(self.data)
        

        """
            set the Order of Magnitude(数量级)
        """
        for i in range(len(self.data)):
            self.data[i]*=10**OOM
        print('OOM is ' + str(OOM))
        
        """
            set the efficient number of bits(有效位数)
        """
        self.ENOB=ENOB
        print('ENOB is ' + str(ENOB)+'\n')
        
    
    def avg(self):
        return sum(self.data)/len(self.data)
        
    def sigma(self):
        sqrt_diff=0
        avg_data=self.avg()
        for i in range(len(self.data)):
            sqrt_diff+=(self.data[i]-avg_data)**2
        return (sqrt_diff/(len(self.data)-1))**0.5
        
    def u_a(self):
        t_p = {3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.46, 8:2.37, 9:2.31, 10:2.26, 15:2.15, 20:2.09}
        print('t_p = {0}'.format(t_p[len(self.data)]))      
        return self.sigma()/len(self.data)**0.5        
        
    def u_p(self,u_b):
        if u_b is not None:
            return ((t_p[len(self.data)]*self.u_a())**2+(1.96*u_b)**2)**0.5
        else:
            print('missing u_b')
    
    
    def __repr__(self):
        return ('data: ' + ', '.join([('{0:.'+str(self.ENOB-1)+'E}').format(i) for i in self.data]) +'\n' 
+('avg:' +'{0:.'+str(self.ENOB-1)+'E}').format(self.avg())+'\n' 
+('sigma:' +'{0:.'+str(self.ENOB-1)+'E}').format(self.sigma())+'\n'
+('U_a:' +'{0:.'+str(self.ENOB-1)+'E}').format(self.u_a()))


pi=3.141592653589793
e=2.718281828459045
c=299792458
G0=6.6720e-11
NA=6.022045e23
R=8.31441
k=1.380662e-23
Vm=22.41383e-3
e=1.6021892e-19
u=1.6605655e-27
me=9.109534e-31
epsilon_0=8.854187818e-12
mu_0=12.5663706144e-7
h=6.626176e-34

def d2r(d,m=0,s=0):
    return (d+m/60+0/3600)/180*pi
def r2d(r):
    return r/pi*180
    

if __name__=='__main__':
    data1=DataProcessing(-2,5,[12.998,12.998,12.994])
    print(data1)
    
        
        