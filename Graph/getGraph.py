
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import Graph.poly as poly_inst

#from pylab import *
from matplotlib.image import imread
from scipy import ndimage


def getGraph(key = 'confirmed'):
    def cc(arg):
        return mcolors.to_rgba(arg, alpha=0.6)
    p = poly_inst.poly(key)

    fig = plt.figure(figsize=(15,15))

    ax = fig.gca(projection='3d')
    ax.axis('auto')

    usFlag = imread('./Graph/usFlag.png')
    usFlag = ndimage.rotate(usFlag,270)
    xp, yp, __ = usFlag.shape
    height = p.getUpLength()
    x = np.arange(18.9, 18.9+3, 3/xp)
    y = np.arange(height-2, height, 2/yp)
    Z, X = np.meshgrid(y, x)
    Y = np.full(Z.shape, 2)
    # X = np.array([[0,0],[10,10]])
    # Y = np.array([[0,0],[0,0]])
    # Z = np.array([[0,10],[0,10]])
    # X, Z = ogrid[0:xp, 0:yp]
    # Y = zeros(x.shape)
    # Z = Y-X

    ax.plot_surface(X, Y, Z, rstride=5, cstride=5, facecolors=usFlag)

    verts = p.getPoly()
    verts2 = p.getpolyUp()

    facecolors = [cc('b'), cc('g'), cc('r'), cc('c'), cc('m'),cc('y'), cc('g'), cc('b'), cc('c'), cc('y')]

    poly = PolyCollection(verts, facecolors=facecolors)
    poly2 = PolyCollection(verts2, facecolors=facecolors[:1])
    poly.set_alpha(0.8)
    poly2.set_alpha(0.8)
    ax.add_collection3d(poly, zs=[0 for i in range(10)], zdir='z')
    ax.add_collection3d(poly2, zs=[2], zdir='y')

    for i in p.t:
        name = p.t[i][0]
        num = str(p.t[i][1])
        if i != 1:
            ax.text(0, 9.9 - i, 0, name + ': ' + num, zdir='x', color='white')
            ax.text(0,10 - i ,0 , name + ': ' + num, zdir = 'x', color = 'black')
        else:
            ax.text(18, 2, p.getUpLength(), name + ': ' + num, zdir='x', color='white',fontsize = 25)
            ax.text(18, 1.9, p.getUpLength(), name + ': ' + num, zdir='x', color='black', fontsize = 25)





    ax.pbaspect = [1, 0.4, 0.6]

    #ax.set_xlabel('X')
    ax.set_xlim3d(0, 25)
    u = p.unit
    ax.set_xticklabels(np.array([int(i * u * 5) for i in range(6)]))
    #ax.set_ylabel('Y')
    ax.set_ylim3d(0, 10)
    ax.set_yticks([])
    #ax.set_zlabel('Z')
    ax.set_zlim3d(0, 15)
    ax.set_zticks([0, 5, 10, 15])
    add = p.t[1][1] - height*u
    ax.set_zticklabels(np.array([int(i * u * 5 + add)  for i in range(4)]))
    ax.tick_params(axis="z", labelrotation=90)

    ax.view_init(30, -80)

    # plt.show()
    fig.savefig('./Graph/'+key+'.png', dpi=fig.dpi)

if __name__ == '__main__':
    getGraph()