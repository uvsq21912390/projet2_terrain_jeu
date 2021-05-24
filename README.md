#projet 2 uvsq L1
projet2_terrain_jeu
Notre programme est un générateur de terrain de jeu de video.L’objectif de ce projet est de générer des terrains aléatoires à partir d’un automate cellulaire ayant des paramètres qui peuvent être choisis en fonction du type de terrain recherché.

Le terrain est un quadrillage composé de case verte qui correspondent à de la terre et de case bleue qui correspondes à de l'eau . Dans notre programme , le personnage est un cercle de couleur rouge . Celui ci se deplace à l'aide des touches flechées du clavier, il peut donc aller à droite, à gauche, vers le haut, ou vers le bas .

PRINCIPE

A l'aide d'une matrice composée de 50 listes, elles mêmes composées de 50 arguments que l'on a fait à partir de la bibliothèque numpy, on a créé un terrain découpé en plusieurs cases vertes et bleues comme dit précédemment Le personnage représenté par un cercle rouge ne peut se déplacer uniquement que sur les cases vertes, le personnage est incapable de nager, il lui est donc impossible de se déplacer sur les cases bleues, il faut effectuer un clic gauchesur l'une des cases du terrain pour faire apparaître le personnage et ainsi pouvoir commencer notre partie on peut presser la touche Z pour annuler le dernier déplacement du personnage, on peut appuyer sur la touche S pour supprimer le personnage, il suffit de refaire un clic gauche sur une case du terrain et ainsi réafficher un cercle rouge, comme on l'a fait initialment pour pouvoir commencer notre partie, on peut répéter ce procéssus indéfiniment.

TOUCHE

-clique gauche sur une case verte pour afficher le personnage

-presser "Z" pour annuler le dernier déplacement du personnage

-presser "S" pour supprimer le personnage

BOUTONS

-un premier bouton permet d'entrer une nouvelle valeur pour p

-un deuxième bouton permet d'entrer une nouvelle valeur pour n

-un troisième bouton permet d'entrer une nouvelle valeur pour T

-un quatrème bouton permet d'entrer une nouvelle valeur pour K

-un bouton permet de générer un terrain par défaut si des valeurs on été changé par l'utilisateur

-un bouton permet de sauvegarde le terrain avec ses valeurs actuelles

-un bouton permet de recharger un terrain qui a été sauvegardé

ETUDE DU CODE

L'utilisateur peut modifier certaines valeurs de manière à pouvoir changer le terrain sur lequel se déplace le personnage, la valeur p correspond à la probabilité qu'une case du terrain soit une case verte, c'est à dire une case où le personnage pourra se déplacer.Une case terre peu devenir une case eau si et seulement si elle a un nombre de case d'eau voisine égale à T,cette variable pouvant être changé par l'utilisateur. La variable k est le nombre de "ranger"de voisinage qui seront compter pour verifié ou non l'égalité avec T, par exemple K est d'ordre 1 par défaut alors seulement les cases voisines seront prise en considération, mais si on fait d'ordre 2 alors cela vas jusqu'aux voisins des voisins. n correspond au nombre fois que l'on va faire tourner l'automate c'est à dire le nombre de fois que l'on va vérifier le voisinage de chaque case. Plus p augmente, moin le personnage aura de case verte sur lesquelles il pourrait se déplacer, sa surface de déplacement est donc amoindri quand p augmente. Si T augmente alors moins de case terre seront transformé en case eau, puisqu'un plus grand nombre de case voisine eau est nécessaire pour devenir une case eau à son tour, à l'inverse réduir T transformera moin de case verte. K tout comme p reduit la surface accessible au personnage lorsqu'il augmente, puisque la surface sur laquelle on va compter les cases voisine d'eau est plus grande et donc permet d'avoir d'avantage de case d'eau prise en consideration. n étant comme un conteur d'une boucle utilisant les variables k et T il va réduire la surface de terre, dans le meilleur des cas si k est egale à 0 ou T a une valeur supérieur à la somme de toute les cases voisines accessible selon k. Seul p peut permettre d'augmenter la surface accessible au personnage, les autres variable la réduise ou ne change pas le terrain initialement selon certaine valeur.

Nous avons rencontrer quelques problème comme la sauvegarde de la partie qui renvoyait une erreur et ne permettait pas au programme de se lancer nous l'avons donc mis en commentaire, on suppose que cela est dû a un soucis das l'ouverture du fichier. Nous avons créé plusieur bouton rattaché à des fonctions les résultats sont biens enregistré dans le programme, nous avons pus le vérifiez à l'aide d'un print(), mais la matrice ne change pas pour autant.
