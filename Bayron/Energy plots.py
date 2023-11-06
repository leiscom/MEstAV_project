import numpy as np
import matplotlib.pyplot as plt

#n = [] # Lista de nombres de los archivos cnf
#for i in range(1,10):
#    n.append("cnf.00"+str(i))
#n.append("cnf.010")

n = ['cnf.{:03d}'.format(i) for i in range(1, 51)] # Lista de nombres de los archivos cnf

E=[] # Lista de energías cinéticas de cada archivo cnf

for k in n:
    revw=np.loadtxt(k,skiprows=2)
    EC=0
    for j in range(len(revw)):
        EC+=0.5*(revw[j][3]**2+revw[j][4]**2+revw[j][5]**2)
    E.append(EC/len(revw)) # Normalizada
#print(E)

#########################################################################################################
#########################################################################################################
#########################################################################################################
# Parámetros del potencial de Lennard-Jones
sigma = 1.0
epsilon = 1.0

nn = ['cnf.{:03d}'.format(m) for m in range(1, 51)]  # Lista de nombres de los archivos cnf
E_potential = []  # Lista de energías potenciales de cada archivo cnf

for l in nn:
    data = np.loadtxt(l, skiprows=2)
    n_particles = len(data)
    EP = 0.0  # Inicializa la energía potencial para este archivo
    for i in range(n_particles):
        for j in range(i + 1, n_particles):
            # Calcula la distancia entre las partículas i y j
            delta_x = data[i][0] - data[j][0]
            delta_y = data[i][1] - data[j][1]
            delta_z = data[i][2] - data[j][2]
            r = np.sqrt(delta_x**2 + delta_y**2 + delta_z**2)

            # Calcula la contribución del par (i, j) al potencial de Lennard-Jones
            LJ_potential = 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)
            
            EP += LJ_potential

    E_potential.append(EP/len(data)) # Normalizada

#t=np.linspace(0,251,5)
t=list(range(0, 250, 5))
#print(len(t))

plt.figure(dpi=150)
plt.xlabel('$t$ [$s$]')
plt.ylabel('Kinetic Energy [$J$]')
plt.title("Kinetic, potential and total energy vs Time")
#plt.savefig('MEstAv - Proyecto (10000 partículas) Energía.png')
plt.plot(t,E,label="Kinetic Energy")
plt.plot(t,E_potential,label="Potential Energy")
plt.plot(t,np.array(E)+np.array(E_potential),label="Total Energy")
plt.legend()
plt.show()