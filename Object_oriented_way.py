# objected oriented way to change plots according to our use 


import matplotlib.pyplot as plt
a=(["Devansh","Shubh","Shivam","Shivansh"])
b=([95,65,48,85])
fig=plt.figure()
axis1=fig.add_axes([0.1,0.1,1,1])
axis1.plot(b,a)
axis2=fig.add_axes([0.3,0.2,0.3,0.3])
axis2.plot(a,b)
plt.show()