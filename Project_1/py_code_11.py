
import numpy as np

x = np.linspace( 0, 2, 9 )
print(x)

b = np.zeros(len(x))
for i in range(len(x)):
    b[i] = x[i]*(np.pi)
    print(b[i])

print("Hello World! Python Here")

