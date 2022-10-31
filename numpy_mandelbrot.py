# L'objectif de ce TP est de calculer l'image bien connue de l'ensemble de [Mandelbrot](https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot) 

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook

# Pour déterminer l'ensemble de Mandelbrot il suffit de repartir de la définition de la suite à savoir, dans le plan complexe, on définit pour chaque point $c\in\mathbb{C}$ la suite
#
# $$\begin{cases} z_0 &= c \\ 
# z_{n+1} &= z_n^2 + c
# \end{cases}
# $$
#
# on démontre alors que si $|z_n|>2$ alors la suite diverge.
#

# La démarche à suivre est alors la suivante : 
#     
# * Définir un discrétisation du plan complexe entre $[-2, 1] \times [-1.4, 1.4]$ en considérant une grille $1000\times 1000$ par exemple
# * on se fixe un nombre maximal `max_iter` d'itérations
#   * et pour chaque point du maillage, on va calculer si la suite diverge avant `max_iter` itérations
#
# * autrement dit on calcule un tableau `image` de la taille du maillage du plan complexe 
#   * pour chaque point `z`, on calcule les `max_iter` premiers termes de la suite
#   * à la première itération `n` où la suite diverge (son module est supérieur à 2)  
#     alors on affecte `image[z] = n`
# * on n'a plus qu'à afficher ensuite l'image obtenue avec `plt.imshow`

# **Attention** 
#     
# Pour rappel le principe de base de NumPy c'est de travailler directement sur des gros tableaux. Donc tout usage abusif de boucles `for` (ou `while` pour les plus malins) sera fortement sanctionné. 

# +
# Votre code ici 
