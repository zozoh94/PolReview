# PolReview
Le but du projet est de créer des résumés sur les profils politiques des 11 candidats à la présidentielle française de 2017. Plusieurs sujets importants seront déterminés de l'économie aux sujets de sociétés. Ces sujets seront enrichis de quelques mots-clés de notre choix puis extrapolés avec une librairie pour leurs associer un champ lexical. Les programmes une fois analysés permettront de générer des résumés.
Si le projet fonctionne il pourra être agrémenté d'un Chat Bot.

## Lancement du projet
- Télécharger le dossier
- Dans un terminal :
```bash
virtualenv -p /usr/bin/python3.5 PolReview
cd PolReview
source bin/activate
pip install -r requirements.txt
./pol_review.py
```
Pour les problèmes avec textract: http://textract.readthedocs.io/en/latest/installation.html
Si vous rencontrez encore des problèmes avec textract utilisez la branche without_textract