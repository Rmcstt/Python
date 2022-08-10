
import matplotlib.pyplot as plt
import numpy as np
import pandas as ListedColormap
import sys
tabuleiro = np.tile([1,0],(8,4))
for i in range(tabuleiro.shape[0]):
  tabuleiro[i] = np.roll(tabuleiro[i], i %2)
mapa_de_cores = ListedColormap(['#FF0000', '#00FF00'])
plt.matshow(tabuleiro, cmap=mapa_de_cores)
plt.xticks([])
plt.yticks([])
plt.show() 

print(sys.path)
##############################################################################################

# import pandas as pd

# carros = {
#   'marca':['fiat','chevrolet','ford'],
#   'modelo':['uno','corsa','fiesta'],
#   'ano':[2010,2011,2012]
# }

# dataframe = pd.DataFrame(carros)
# dataframe.to_excel('./carros.xlsx')