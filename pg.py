import matplotlib.pyplot as ukp
import numpy as ukn
fig, axes =ukp.subplots()
axes.set_aspect( 1 )
for i in ukn.arange(0,0.4,0.1):
    c =ukp.Circle(( 0.5 , 0.5 ), 0.1+i, fill=False )
    axes.add_artist(c)
ukp.show()
t= ukp.figure()
a= t.add_subplot()
ukp.plot([10,20,30,10],[10,30,10,10])
a.set_aspect('equal')
ukp.show()
s= ukp.figure()
a= s.add_subplot()
ukp.plot([10,20,20,10,10],[10,10,20,20,10])
a.set_aspect('equal')
ukp.show()