
## Ce projet est fait par Tatsiana dans le cadre du cours d"Automatisation 2.

# Le but est - développer les cas automatisés pour couvrir certains exigences en langage Python (Selenium 4 ).

Principalement il y a huit (08) fonctionnalités.

Pour chaque fonctiommalité :

1. Créer python file exigence_[numéro de fonctionnalité]_steps.py
- On mantionne dans ce file les préconditions (si' il y en a)
- Créer la class
- Créer des fonctions pour effectuer chaque step
2. Créer le file python pour effectuer pytest dans lequel on import le file deja crée (par ex: on créer le file: test_Exigence_08_passer_commande.py, et on importe exigence_08_steps.py).
Ainsi, dans le file: test_Exigence_08_passer_commande.py on créer la Class, et on appelle les fonctions deja créés.

# Procédure d'utilisation
Lancer le tests avec : pytest -s -v [nom de test]
Remarque : Pour prouver, pour chaque fonctionnalitée on va le screenshoot avec le nom du numero d'exigence.

Aussi, j'ai remarqué que on utilise souvent les 3 pages: home page, register page et login page.
Alors, j'ai decidé de creer un test automatisé pour verifier si ces 3 pages s'ouvrent correctement, c'est-a-dire - un health-check pour 3 pages.

Dans le file: test_link_open_requests_healty_check.py, j'ai crée une class TestPages, ou j'ai crée la fonctionne pour ouvrir les pages. 
J'ai la parametrisé et je demande de prendre une parametre - file verification_urls.txt, dans lequels j'ai stocké les url de 3 pages.
Alors, en utilisant la parametrisation - il va prendre chaque url du fichier text et il va l'executer comme un cycle.
Ici, j'ai utilisé la bibliotheque requests pour créer les test API pour avoir la response de status code.


![Typing SVG](https://readme-typing-svg.demolab.com?color=$0E6655&lines=Améliorations+futures:)

Je vais retourner a ce projet pour améliorer cette version.
