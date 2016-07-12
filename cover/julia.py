#
# Image Used for Cover for Version 1 of Python Hacking for Math Junkies
#
#* ----------------------------------------------------------------------------
#* "THE BEER-WARE LICENSE" (Revision 42):
#* bruce.e.shapiro@gmail.com wrote this file to draw his book cover. 
#* As long as you retain this notice you can do whatever you want with this stuff.
#* If we meet some day, and you think this stuff is worth it, 
#* you can buy me a beer in return. Bruce E. Shapiro
#* ----------------------------------------------------------------------------
#* For more information on the BEER-WARE LICENSE see 
#* https://people.freebsd.org/~phk/
#*/
import numpy as np
from matplotlib.pyplot import *
x=np.linspace(-2,2, 3000)
g=np.meshgrid(x,x)
f = lambda z: (-0.8-0.15j)+z*z
def iterate(Z, n=100, maxz=1.0):
    counter=np.zeros( (len(Z), len(Z)), "float")
    ZMAX = np.full_like(counter, maxz)
    for i in range(n):
        Z=f(Z)
        counter += (np.abs(Z) <= ZMAX)
    return counter 
Z=iterate(g[0]+(1j)*g[1])
fig=imshow(Z, cmap="hsv")
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
savefig("julia.png", dpi=300, bbox_inches="tight", pad_inches=0)
show()
