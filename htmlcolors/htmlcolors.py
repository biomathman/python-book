"""
Draw a figure with all the named html colors
"""
from matplotlib.pyplot import *
import matplotlib.patches as patches
import matplotlib.colors as colors

allcolors=list(colors.cnames)
allcolors.sort()
ncolors = len(allcolors)


rows = ncolors/3
i=0
fig,ax=subplots(1,1)
for c in allcolors:
    y = rows- (i % rows) - 1
    x = i / rows
    ax.add_patch(patches.Rectangle((x,y), 1, 1, color=c))
    annotate(c, xy=(x+.5,y+.5), ha="center", va="center", fontsize=8)
    i+=1
xticks([])
yticks([])
xlim(0,3)
ylim(0,rows)
tight_layout()
fig.set_size_inches(7,11)
fig.tight_layout()
fig.savefig("html-named-colors.jpg",dpi=300)
#show()
