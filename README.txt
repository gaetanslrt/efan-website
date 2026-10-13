EFAN / FASN — Refonte complète du site
======================================

37 pages, même style administratif français que la maquette d'accueil validée.


Contenu de l'archive
--------------------
index.html                 Page d'accueil.
<slug>/index.html          36 pages intérieures, aux mêmes adresses qu'aujourd'hui
                           (/history-ns/, /20-parcoursup/, etc.).
assets/css/efan.css        Feuille de style unique, commentée par section.
assets/js/efan.js          Navigation (méga-menus, panneau mobile). Aucune dépendance.
assets/img/                Logo, favicons et visuels de la page d'accueil.
media/<année>/<mois>/      Tous les médias de contenu, à leur chemin WordPress d'origine.
media/_480/, media/_1400/  Versions allégées affichées dans les pages ; les fichiers
                           d'origine restent accessibles en pleine taille au clic.
docs/                      FAQ-2025.pdf et Terms-of-Service-for-EFAN-Website.pdf.
sitemap.xml, robots.txt    Régénérés.


Mise en ligne
-------------
Déposer le contenu de ce dossier à la racine du site. Les adresses des pages sont
inchangées : aucun lien externe ni favori existant ne casse.

Tous les liens internes sont relatifs : vous pouvez aussi ouvrir index.html
directement depuis ce dossier, sans serveur, pour relire l'ensemble hors ligne.


Ce que le gabarit apporte sur les pages intérieures
---------------------------------------------------
Fil d'Ariane, bandeau de titre, menu latéral de rubrique avec la page courante
marquée, puis liens « page précédente / suivante » en bas. Avec 37 pages réparties
sur quatre rubriques, c'est ce qui rend l'ensemble navigable sans repasser par le
menu principal à chaque fois.

Sur mobile le menu latéral passe sous le texte : le contenu commence juste après
le titre.


Fidélité au contenu d'origine
-----------------------------
Vérifié automatiquement, page par page : aucun mot, aucune image et aucun PDF du
contenu d'origine ne manque (58 images, 7 PDF). Les tableaux, les galeries, les
fiches enseignants, les citations et les onglets ont été reconstruits en HTML
sémantique plutôt que repris du balisage Divi.

Aucun texte n'a été inventé sur les pages intérieures. Les seules phrases qui ne
viennent pas de vous sont les descriptions <meta> invisibles, utilisées par Google
et les réseaux sociaux ; elles sont modifiables dans chaque fichier.

Les titres de pages ont perdu leur numérotation interne : « *19 High School-
Baccalaureat NS2 » devient « French Baccalauréat ». Les anciens titres restent
dans vos fichiers WordPress si vous en avez besoin.


Cinq points à arbitrer
----------------------
1. Pages hors menu — quatre pages existent sans figurer dans le menu actuel :
   School Board, School Project, Vaccination et les deux pages vides. J'ai conservé
   School Board et School Project (reprises dans le pied de page uniquement, pour
   ne pas modifier votre arborescence de mon propre chef) et rattaché Vaccination
   à la rubrique Admissions, où les familles la cherchent. À confirmer.

2. Pages vides — /elementary-school/ et /middle-school/ ne contenaient que le
   gabarit de pied de page Divi, sans aucun contenu. Elles ne sont pas générées.
   /school-project-ns1/ ne contient que « Update in progress. » : la page est
   générée telle quelle.

3. Liens réparés — le contenu d'origine renvoyait parfois vers la version
   française depuis les pages anglaises (/fr/19-high-school-baccalaureat-ns2/
   depuis la page anglaise, par exemple), et la page « What is FASN? » pointait
   vers /testimonies/testimonies/, qui n'existe pas. Ces liens pointent désormais
   vers la bonne page anglaise. Au total, zéro lien interne cassé sur les 37 pages.

4. Typographie — la police Public Sans est chargée depuis Google Fonts. Pour
   supprimer toute dépendance externe, retirez les trois balises <link>
   correspondantes dans chaque fichier HTML : la page bascule proprement sur les
   polices système, déjà prévues dans la pile de secours.

5. Chiffres clés de l'accueil — les quatre chiffres (61 élèves, ×6 en 5 ans,
   25 %, 22 %) viennent de votre FAQ 2025, source citée sous le bloc. Ils datent
   de 2024-2025 : à actualiser, ou à retirer en supprimant la section.


Accessibilité et performance
----------------------------
Liens d'évitement, navigation clavier complète (Échap ferme les menus), aria-expanded
et aria-current sur la navigation, un seul <h1> par page, hiérarchie de titres
reconstruite sans saut de niveau, textes alternatifs conservés, contrastes AA,
tableaux défilables au clavier, et repli lisible sans JavaScript.

Les grandes images (certains scans de newsletter pesaient 2,5 Mo) sont servies en
version allégée, l'original restant accessible au clic. Vérifié sans débordement
horizontal à 390, 820 et 1366 px de large ; aucune erreur JavaScript, aucune
ressource manquante sur les 37 pages.
