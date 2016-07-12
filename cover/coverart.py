#
# Cover Code for Version 3 of Python Hacking for Math Junkies
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
import matplotlib.pyplot as plt
import numpy as np
def mand(C, zmax, n):
    z = C
    for j in xrange(n):
        z=z*z+C
        if abs(z)>zmax:
            return(j)
    return(0)  

def forceAspect(ax,aspect=1):
	#http://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
   
def mandelbrot(xc, yc, rx, ry, pix, zmax, nmax):
    aspect=float(ry)/float(rx)
    pixy=int(aspect*pix)
    xmin = xc-rx; xmax = xc + rx
    ymin = yc-ry; ymax = yc + ry
    xvals=np.linspace(xmin,xmax,pix)
    yvals=np.linspace(ymin,ymax,pixy)
    dy = (float(ymax)-float(ymin))/float(pixy)
    dx = (float(xmax)-float(xmin))/float(pix)
    image=np.ones((pixy,pix))
    for ix in xrange(pix):
        for iy in xrange(pixy):
            z=(xmin+dx*ix)+(1j)*(ymin+dy*iy)
            image[iy,ix]=mand(z, zmax, nmax)
    return image
i=mandelbrot(.2315,-0.5345,.00378,.0025,3000,5,200)
fig=plt.imshow(i, cmap="Pastel1")
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
ax = plt.gca()

forceAspect(ax,15.511/10.25)

fig=plt.gcf()
fig.set_size_inches(15.511,10.25)

fig.tight_layout()
fig.savefig("cover-image.png",dpi=300, bbox_inches="tight", pad_inches=0)
plt.show()


