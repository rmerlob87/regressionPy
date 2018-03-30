import numpy as np
import matplotlib.pyplot as plt

#sets polynomial coefficients and initializes arrays
a, b, c, d, e, f, g =(-1e-2, -1e-6, -1e-3, -1e-5, 1e-2, -1e-2, 10)
X=np.arange(0,1+0.1,0.01)
Yp=np.array([])
Yf=np.array([])
Yr=np.array([])

#creates a randomized array "Yr" from the polynomial coefficients
for x in X:
    rndNumber=np.random.random_sample()
    rndSign=np.random.choice((-1,1))
    rnd=rndSign*rndNumber*0.002 
    Yr=np.append(Yr,rnd+(a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x**1+g))
    Yp=np.append(Yp,(a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x**1+g))

#obtains fitted coefficients from the randomized list
af, bf, cf, df, ef, ff, gf=np.polyfit(X,Yr,6)
for x in X:
    Yf=np.append(Yf,(af*x**6+bf*x**5+cf*x**4+df*x**3+ef*x**2+ff*x**1+gf))

#plots the results
f, ax = plt.subplots()
#ax.plot(X,Yp, label= 'fittedPolynomial')
ax.scatter(X,Yr,marker='x', label = 'Test data')
ax.plot(X,Yf,"r--", label= 'Fitted Polynomial')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title('Polynomial fit function\n{:.2e}$x^6$+{:.2e}$x^5$+{:.2e}$x^4$+{:.2e}$x^3$+{:.2e}$x^2$+{:.2e}$x^1$+{:.2e}'.
        format(af,bf,cf,df,ef,ff,gf))
plt.grid()

#make an array and write to a plain file
fittedCurve = np.array([X,Yf]).transpose()
np.savetxt('testData1.sta', fittedCurve, 
           delimiter=',', header=('X, Yf'), 
           fmt='%5.5g')