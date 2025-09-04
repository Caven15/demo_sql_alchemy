# Projet SQlAlchemy => Démonstration portée sur l'univers du seigneur des Anneaux

//.....

## Création et activation de l'environnemt virtuel

# Création e l'environement vitruel
py -3 -m venv .venv

# Ouverture de l'environement virtuel
.\.venv\scripts\activate

# Réinstallation des dépendance référencée dans le requirements
pip install -r requirements.txt

# Attention à levé la sécurité sur l'execution des scripts si windows refuse l'execution
Set-ExecutionPolicy Unrestricted -Scope CurrentUser

# pour lire les dépendances installée
pip list