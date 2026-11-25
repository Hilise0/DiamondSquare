import numpy as np
import matplotlib.pyplot as plt
import seaborn

from hkb_diamondsquare import DiamondSquare as DS

# #make a height map of size 16x20, with values ranging from 1 to 100, with moderate roughness
# map1 = DS.diamond_square(shape=(16,20), 
#                          min_height=1, 
#                          max_height=100,
#                          roughness=0.75)

# #make a square height map with sides of length 120, that are VERY rough
# map2 = DS.diamond_square(shape=(120,120),
#                          min_height=1,
#                          max_height=100,
#                          roughness=0.99)

# #make a VERY smooth map with values from -10 to 10
# map3 = DS.diamond_square(shape=(10,10), 
#                          min_height=-10, 
#                          max_height=10, 
#                          roughness=0.05)

# #use a specific random seed to ensure replicability
# same_map_1 = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.234)
# same_map_2 = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.234)

# np.allclose(same_map_1, same_map_2)
# # prints True

# different_map = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.2341, as_ndarray=True)
# np.allclose(same_map_1, different_map)
# # prints False



def show_terrain_2D(terrain_array):

    seaborn.set_theme()
    seaborn.heatmap(terrain_array)
    plt.show()


def show_terrain_3D(terrain_map) :
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    X = np.linspace(0,terrain_map.shape[0],terrain_map.shape[0])
    Y = np.linspace(0, terrain_map.shape[1],terrain_map.shape[1])
    XY = np.meshgrid(X,Y)
    surf = ax.plot_surface(*XY, Z=terrain_map, cmap = plt.colormaps["gist_earth"],
                       linewidth=1, antialiased=False)
    #Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


if __name__ == "__main__" :
    #create a chunk with variations of altitude
    map = DS.diamond_square(shape=(50,50), min_height=0, max_height=10, roughness=0.3)
    show_terrain_3D(map)




# créer une map avec des saisons
# ajouter des rivières/lacs
# choisir la pente des montagnes