import matplotlib.pyplot as plt
import numpy as np
#2.1 F(x)
"""""
plt.style.use('seaborn-whitegrid')
F=0.5*10**-6
E=350*10**9
J = 1.296*10**-24
l=500*10**-6
h=1.2*10**-6
w=9*10**-6
x = np.linspace(0,0.0000005,50)
y = (12*(l**3)*x)/(E*w*(h**3))

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'y-o')
ax.set_title('Грaфік залежності значення переміщення консольної балки \n від значення зовнішньої сили', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('Fзовн, мкН', fontsize = 25)
ax.set_ylabel('y, м', fontsize = 25)
#plt.xlim(0,0.0005)
plt.show()
"""""
#2.2 l(x)
"""""
plt.style.use('seaborn-whitegrid')
F=0.5*10**-6
E=350*10**9
J = 1.296*10**-24
l=500*10**-6
h=1.2*10**-6
w=9*10**-6
x = np.linspace(0,0.0005,50)
y = (12*(x**3)*F)/(E*w*(h**3))

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'r-o')
ax.set_title('Грaфік залежності значення переміщення консольної балки \n від значення довжини балки l', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('l, м', fontsize = 25)
ax.set_ylabel('y, м', fontsize = 25)
#plt.xlim(0,0.0005)
plt.show()
"""""
#2.3 h(x)
"""""
plt.style.use('seaborn-whitegrid')
F=0.5*10**-6
E=350*10**9
J = 1.296*10**-24
l=500*10**-6
h=1.2*10**-6
w=9*10**-6
x = np.linspace(0,0.0000012,30)
y = (12*(l**3)*F)/(E*w*(x**3))

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'r-o')
ax.set_title('Грaфік залежності значення переміщення консольної балки \n від значення висоти балки h', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('h, м', fontsize = 25)
ax.set_ylabel('y', fontsize = 25)
plt.show()
"""""
#2.4 w(x)
plt.style.use('seaborn-whitegrid')
F=0.5*10**-6
E=350*10**9
J = 1.296*10**-24
l=500*10**-6
h=1.2*10**-6
w=9*10**-6
x = np.linspace(0,0.000009,60)
y = (12*(l**3)*F)/(E*x*(h**3))

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'g-o')
ax.set_title('Грaфік залежності значення переміщення консольної балки \n від значення ширини балки w', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('w, м', fontsize = 25)
ax.set_ylabel('y', fontsize = 25)
plt.show()
#3
"""""
plt.style.use('seaborn-whitegrid')
X_Array = []
Y_Array = []
l1 = 5*10**-10
x = np.linspace(1,50,50)
y = (l1/(0.000004*50))*np.sin((np.power((24*0.000004*x), 0.5)/2))

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'r-o')
ax.set_title('Грaфік залежності залежності переміщення \n від значення температури', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('T, °C', fontsize = 25)
ax.set_ylabel('y, м', fontsize = 25)

plt.show()
"""""
#4.1
"""""
plt.style.use('seaborn-whitegrid')
X_Array = []
Y_Array = []
l1 = 5*10**-10
P = 0.0000005
E = 350 * 10**9
J = 1.296 * 10**-24
x = np.linspace(0,0.0005,50)
y = (P * x**2)/(2*E*J)

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'g-o')
ax.set_title('Грaфік залежності куту повороту \n від значення відстані від лівого кінця балки ϕ=f(x)', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('x, м', fontsize = 25)
ax.set_ylabel('ϕ', fontsize = 25)
#plt.xlim(0,0.0005)
plt.show()
"""""
#4.2
"""""
plt.style.use('seaborn-whitegrid')
X_Array = []
Y_Array = []
l1 = 5*10**-10
P = 0.0000005
E = 350 * 10**9
J = 1.296 * 10**-24
x = np.linspace(0,0.0005,50)
y = -(P * x**3)/(3*E*J)

print(x, y)

fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
ax.set_title('Грaфік залежності значення прогину \n від значення відстані від лівого кінця балки z=f(x)', fontweight = 'bold', fontsize = 24)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(18)
ax.set_xlabel('x, м', fontsize = 25)
ax.set_ylabel('z', fontsize = 25)
#plt.xlim(0,0.0005)
plt.show()
"""""

