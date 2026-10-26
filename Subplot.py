import matplotlib.pyplot as plt
a=["prajjwall","shubh","shivam","devansh"]
b=[90,50,70,55]
c=["Pythpn","SQL","Excel","Powerbi"]
d=[80,75,95,64]
plt.subplot(2,2,3)
plt.plot(a,b)
plt.title("Report",color="blue")
plt.xlabel("Marks",color="red")
plt.ylabel("Name",color="green")
plt.subplot(2,2,2)
plt.plot(b,a)
plt.title("Report",color="blue")
plt.xlabel("Marks",color="red")
plt.ylabel("Name",color="green")
plt.subplot(2,2,1)
plt.plot(c,d)
plt.title("Report",color="blue")
plt.xlabel("Marks",color="red")
plt.ylabel("Name",color="green")
plt.subplot(2,2,4)
plt.plot(c,b)
plt.title("Report",color="blue")
plt.xlabel("Marks",color="red")
plt.ylabel("Name",color="green")
plt.show()

