# BrewBuddy
Bienvenue sur mon premier projet Django Brew Buddy;
Il s'agit d'un site internet pour les brasseurs amateurs et petites brasseries permettant une gestion d'inventaire de la brasserie; la création de recettes de bières et le partage entre utilisateur.

Pour démarrer, il est nécessaire d'avoir python et django d'installés localement,
Il est aussi nécessaire d'avoir renseigné l'emplacement BDD utilisé (ici mysql); voire dans settings.py pour modifier les paramêtres BDD
Dans le directory backend/recipes ouvrir cmd:
py manage.py makemigrations
py manage.py migrate
py manage.py runserver

Dans un navigateur, se rendre à http://localhost:8000/