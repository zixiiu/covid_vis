#deploy
need to change a matplotlib file:
```
site-packages\mpl_toolkits\mplot3d\axes3d.py
```

```
get_proj
```

```
xmin, xmax = np.divide(self.get_xlim3d(), self.pbaspect[0])
ymin, ymax = np.divide(self.get_ylim3d(), self.pbaspect[1])
zmin, zmax = np.divide(self.get_zlim3d(), self.pbaspect[2])
```