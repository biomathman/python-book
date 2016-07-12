#
# Cover Code for Second Edition of Python Hacking for Math Junkies
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
from matplotlib.pyplot import *
import numpy as np
def mand(C, zmax, n):
    z = C
    for j in xrange(n):
        z=z*z+C
        if abs(z)>zmax:
            return(j)
    return(0)     
def mandelbrot(xc, yc, r, pix, zmax, nmax):
    xmin = xc-r; xmax = xc + r
    ymin = yc-r; ymax = yc + r
    xvals=np.linspace(xmin,xmax,pix)
    yvals=np.linspace(ymin,ymax,pix)
    dy = (float(ymax)-float(ymin))/float(pix)
    dx = (float(xmax)-float(xmin))/float(pix)
    image=np.ones((pix,pix))
    for ix in xrange(pix):
        for iy in xrange(pix):
            z=(xmin+dx*ix)+(1j)*(ymin+dy*iy)
            image[iy,ix]=mand(z, zmax, nmax)
    return image
#
# these coordinates are preset to the cover of the book, version 2
#
i=mandelbrot(.2323,-0.5345,.0025,500,3,500)
#
# For other neat pictures, see the wikipedia under mandelbrot
#
fig=imshow(i)
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
fig=gcf()
#
# comment the following two lines out
# if you don't want to save the file
#
fig.set_size_inches(5,5)
fig.savefig("ci.png",dpi=600)
show()

