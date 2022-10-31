# %%
import pandas as pd 
import matplotlib.pyplot as plt 


# %% [markdown]
# Dans ce sujet l'objectif est de travailler le SEO du site web de l'école des Mines. Le principe du SEO (Search Engine Optimisation) est d'améliorer le référencement des sites web sur les moteurs de recherche. En d'autre mot c'est comment faire en sorte qu'un site web apparaissent le plus souvant pour un ensemble de recherche sur la première page de résultats de Google. 
#
# Par exemple pour illustrer l'idée, je vous invite faire une recherche "école d'ingenieur" sur google et de regarder si le lien vers le site de l'école des Mines est bien positionné ou pas.... (Teaser: non il est mal positionné) 
#
# Pour analyser le référencement d'un site web il faut prendre en compte un nombre assez élevé de critères : vitesse de chargement des pages, définition des méta données, longueur de titre, erreur au chargement des pages, ..... Nous allons ici uniquement regarder quelqu'uns. Tout d'abord il faut afin de procéder à une analyse SEO réaliser ce qu'on appel un Crawl du site web en question, c'est à dire qu'un programme va parcourir toutes les pages d'un site web en partant de la page d'acceuil et en suivant tous les liens qui s'offrent à lui au fur et à mesure.
#
# Je vous fourni dans le dossier `data` les résultats du crawl du site web de l'école des mines [www.minesparis.psl.eu](www.minesparis.psl.eu). Et c'est en analysant ces données que l'on va essayer d'identifier les points d'amélioration possibles. 

# %% [markdown]
# # Chargement des données 

# %% [markdown]
# Charger les données issues d'un Crawl du site web Python.org 
# Vous devez charger : 
# - le fichier data/internal_all.csv qui contient l'ensemble des urls visitées, vous ne devez charger que les colonnes ("Address","Content Type", "Status Code","Status", 'Title 1', 'Title 1 Length', 'Title 2', 'Title 2 Length','H1-1', 'H1-1 Length', 'H1-2', 'H1-2 Length',"Meta Robots 1", "Inlinks","Outlinks")
# - le fichier data/all_outlinks.csv qui contient l'ensemble des liens du sites web. Vous ne devez charger que les colonnes ("Type","Source","Destination","Status Code")

# %% [correction]
# Votre code ici 

# %% [markdown]
# A partir de la liste des urls visitées, compter pour chaque code de retour "Status Code" le nombre d'url associées et afficher le résultat sous la forme d'un diagramme camembert. 


# %%
# Votre code ici 

# %% [markdown]
# ## Analyse des pages en erreur 

# %% [markdown]
# Alors un gros point de vigilance à avoir lorsqu'on cherche a améliorer son référencement c'est de ne pas avoir de page en erreur, le fameux `404 Not Found`. Pour cela il est impératif d'identifier tous les liens internes qui envoient vers des pages qui n'existent plus et de les corriger. 

# %% [markdown]
# Pour commencer calculer le pourcentage d'url en erreur, i.e. renvoyant un code 404. 

# %%
# Votre code ici 

# %% [markdown]
# Pour toutes les urls renvoyant une erreur 404 identifier le type de contenu associé (texte html, image, ... )
# **Indication**: Vous devez vous référer à la colonne "Content" 
#

# %%
# Votre code ici 

# %% [markdown]
# En utilisant à la fois les données chargées du fichier `internal_all.csv` et du fichier `all_outlinks.csv` identifier pour les urls renvoyant le code d'erreur 404 l'url de provenance. Autrement dit il faut identifier les pages qui mettent à disposition un lien renvoyant vers une page en erreur 404. 

# %%
# Votre code ici 


# %% [markdown]
# Véfifier si toutes les urls renvoyant une erreur 404 sont des urls internes, i.e. toutes les urls sources doivent commencer par https://www.minesparis.psl.eu, ou bien s'il s'agit de liens externes qui renvoies vers un autre site par exemple github. 

# %%
# Votre code ici 

# %% [markdown]
# Charger les fichiers `data/categorized.csv` qui contient la liste des urls et les catégories associées 

# %%
# Votre code ici 


# %% [markdown]
# En utilisant le dataframe que l'on vient de charger identifier pour chaque catégories le nombre d'url renvoyant une erreur 404. 

# %%
# Votre code ici 

# %% [markdown]
# ## Référencement interne du site 

# %% [markdown]
# Identifier la page la plus référencée du site de l'école, c'est-à-dire la page vers laquelle le plus d'autre page renvoie. 
#

# %%
# Votre code ici 

# %% [markdown]
# Afficher les 10 urls internes au site (i.e. commençant par https://www.minesparis.psl.eu) les moins référencées. 
#

# %%
# Votre code ici 

# %% [markdown]
# ## Conseil d'optimisation SEO 

# %% [markdown]
# A partir des données chargées de `data/internal_all.csv` identifier les pages pouvant être optimisées afin d'améliorer le renférencement naturel du site de l'école des Mines. Parmi les critère ayant un impact sur le référencement d'un site web vous devez considérer les suivants : 
#
# - Définition de plusieurs `Title` sur une même page interdit, il ne faut qu'un `Title` pour chaque page
# - La longueur idéale d'un `Title`est entre 30 et 60 caractères. 
# - Absence de de balise `H1` ou au contraire plusieurs `H1`sur une même page, il faut une seule et unique balise `H1` sur une page. 
# - La longueur idéale d'un `H1`est inférieur à 70 caractères
# - Pour chaque balise `ìmage` un texte alternatif doit être renseigné (pour des raisons d'accessibilités) en utilisant le fichier `data/all_image_inlinks.csv` déterminer le nombre d'image du site de l'école ne satisfaisant pas aux critères d'accessibilité. 
#
#  

# %%
# Votre code ici 
