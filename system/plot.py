
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

delta_l = 0.000001
r = 0.05 + delta_l

id = []
x = []
y = []
angle = []
i = 0
for theta in range(0,3600,1):
	theta = theta*0.1
	angle = angle + [theta]
	theta = math.radians(theta)
	x_ = -1*r*math.cos(theta)
	y_ = r*math.sin(theta)

	id = id + [i]
	x = x + [x_]
	y = y + [y_]
	
	i = i+ 1


temp = []
time = []

f = open("../postProcessing/probes/0/T","r")

for i in range(3620,3621,1):
	l = f.readlines()[i]
	# w = open("check","w")
	# w.write(l)
	l = l.split()
	t = 0
	for temperature in l:
		if t == 0:
			t = t + 1
			time = time + [temperature]
			continue
		# temperature = temperature
		temp = temp + [float(temperature)]
		
		
		
		# print(w)
# print(temp)
h = []
Nu = []
k = 1009*2.181e-06/0.7111
print(k)
for temperature in temp:
	h_ = (k*(473-float(temperature))/(delta_l*173))
	h = h + [h_]
	Nu = Nu + [h_*0.1/k]
	# print((k*(473-float(temperature))/(delta_l*100)))
	# print(h_)

sum = 0
w = open("dump","a")
# for n in Nu:
# 	w.write(str(n))
# 	w.write("\n")
# w.write("\n")
w.close()
sum2=0
for i in range(0,3600,1):
	sum = sum + h[i]*0.1*(3.14/180)
	sum2 = sum2+ Nu[i]


# print((sum/(2*3.14)))
# print(sum2/3600)
# print(sum(h)/len(h))



# print(h)
# plt.scatter(x,y,c=h,cmap='jet')
plt.scatter(angle,Nu)
# plt.colorbar()
# plt.contourf(x,y,temp)
# plt.show()

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter(x,y,c=temp)





#---------------------------------------------------verification---------------------------------------

u_inf = 5
mu = 2.181e-06
Pr = 0.711;
rho = 0.9458
D = 0.1


# Re = rho*u_inf*D / mu
# print(Re)
Re = 216827.14

Nu_avg = 0.3 + (0.62 *Re**(0.5)*Pr**(1/3))*((1+(Re/282000)**(5/8))**(4/5))/((1 +(0.4/Pr)**(2/3))**(1/4))


h = Nu_avg*k/D
# print(h)
# print(Nu_avg)
# print(0.193*Re**0.805*Pr**(1/3)*0.031/D)

# plt.show()

