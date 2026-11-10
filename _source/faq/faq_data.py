# -*- coding: utf-8 -*-
"""FAQ content, from the school's FAQ 2026-2027 (FAQ-EFAN-2026-2027).

Each answer is (question, bullets, lead) or (question, bullets, lead, after):
  lead   a paragraph, or a list of paragraphs, shown before the bullets;
  after  a paragraph, or a list of paragraphs, shown after the bullets.
French spacing (no-break space before : ; ? ! and inside « ») is added by faq_pdf.py.
"""

ENROLMENT = [("2020-2021", 10), ("2021-2022", 15), ("2022-2023", 31),
             ("2023-2024", 43), ("2024-2025", 63), ("2025-2026", 77),
             ("2026-2027", 71)]

ADDRESSES = [
    ("John B. Dey Elementary School", "1900 N. Great Neck Road, Virginia Beach, VA 23454",
     "deyes.vbschools.com"),
    ("Great Neck Middle School", "1848 N. Great Neck Road, Virginia Beach, VA 23454",
     "greatneckms.vbschools.com"),
    ("Frank W. Cox High School", "2425 Shorehaven Drive, Virginia Beach, VA 23454",
     "coxhs.vbschools.com"),
    ("Crossroads Elementary and Middle School", "8021 Old Ocean View Road, Norfolk, VA 23518",
     "npsk12.com/cr"),
]

DATA = {
"fr": {
  "lang": "fr",
  "title": "Foire aux questions",
  "school": "École Franco-Américaine de Norfolk",
  "sub": "Des réponses précises aux questions les plus fréquemment adressées par les familles",
  "edition": "Édition 2026-2027",
  "site": "efanvirginia.com",
  "contact": "efan.norfolk@gmail.com · (757) 230-7569",
  "toc_title": "Sommaire",
  "figures_title": "Chiffres clés",
  "figures_note": "Répartition des effectifs à la rentrée 2026-2027 : 25 élèves en école élémentaire, "
                  "25 au collège et 21 au lycée, soit 71 élèves.",
  "chart_title": "L’évolution des effectifs",
  "chart_note": "De 10 élèves en 2020-2021 à 71 à la rentrée 2026-2027 : un effectif multiplié par 7,1 en six ans.",
  "figures": [
    ("71", "élèves à la rentrée <span style='white-space:nowrap'>2026-2027</span>"),
    ("×7,1", "évolution des effectifs depuis 2020-2021"),
    ("17 %", "d’élèves issus de familles civiles (12 sur 71)"),
    ("7 %", "d’élèves francophones ayant au moins un parent étranger (5 sur 71)"),
  ],
  "closing_title": "Votre question ne figure pas dans ce document ?",
  "closing": ("Le secrétariat de l’EFAN répond aux familles du lundi au vendredi, de 9 h 00 à 17 h 00 : "
              "efan.norfolk@gmail.com · (757) 230-7569. Pour les sujets traités en détail sur le site "
              "(baccalauréat, Parcoursup, carte scolaire, inscription), les onglets correspondants font "
              "référence."),
  "addresses_title": "Adresses des établissements américains qui accueillent l’EFAN :",
  "sources": ("Sources : informations communiquées par l’EFAN et site efanvirginia.com. "
              "Les chiffres de répartition portent sur l’année scolaire 2026-2027."),
  "sections": [
    {
      "n": "1", "t": "L’école et ses élèves",
      "qa": [
        ("Quel est l’effectif de l’EFAN ?", [],
         "L’école accueille 71 élèves à la rentrée 2026-2027 (25 en école élémentaire, 25 au collège "
         "et 21 au lycée), contre 77 en 2025-2026. Depuis 2020-2021, où elle comptait 10 élèves, ses "
         "effectifs ont été multipliés par 7,1. En 2026-2027, 12 élèves sur 71 sont issus de familles "
         "civiles et 5 sont francophones avec au moins un parent étranger."),
        ("L’EFAN accueille-t-elle des élèves allophones ?", [],
         "Oui. L’EFAN accueille également des élèves allophones, pour lesquels une entrée entre la "
         "grande section et le CE2 est conseillée. Elle n’est pas réservée aux enfants de militaires : "
         "elle est ouverte à tous."),
        ("Pourquoi l’EFAN est-elle répartie entre plusieurs établissements ?", [],
         "L’école ne dispose pas de locaux propres : ses classes sont accueillies au sein "
         "d’établissements publics américains, à Norfolk et à Virginia Beach. L’onglet « Historique » "
         "du site retrace cette implantation progressive."),
        ("Pourquoi l’école porte-t-elle le nom de Norfolk alors que la plupart des élèves sont "
         "scolarisés à Virginia Beach ?", [],
         "L’école a été créée à Norfolk en 2011. La majorité des familles militaires résidant à "
         "Virginia Beach, un partenariat y a été conclu en 2022 et des classes y ont été ouvertes "
         "progressivement. La dénomination d’origine a été conservée."),
        ("Qui a créé l’EFAN ?", [],
         "L’EFAN a été fondée en 2011 à l’initiative de l’État-Major des Armées et du représentant de "
         "l’armée française à Norfolk (Élément de soutien national, ESN), avec l’engagement de John et "
         "Simone Ryan, couple franco-américain de Hampton Roads, et le soutien de la Mission laïque "
         "française (MLF). Simone Ryan est, aujourd’hui encore, fondatrice et présidente du conseil "
         "d’administration de l’école. L’onglet « Historique » du site retrace cette création."),
        ("Qui dirige l’EFAN ?", [],
         ["L’EFAN est une association à but non lucratif dirigée par un conseil d’administration, qui "
          "se réunit chaque mois, supervise la gestion des finances, recrute le directeur ou la "
          "directrice de l’école et veille à la cohérence de sa stratégie. La directrice assure la "
          "direction de l’établissement et en supervise le fonctionnement quotidien : elle exerce les "
          "mêmes responsabilités qu’un chef d’établissement en France, recrute et évalue les "
          "enseignants, en collaboration avec la Mission laïque française.",
          "La Mission laïque française, opérateur associatif de l’État, est mandatée pour accompagner "
          "le fonctionnement de l’école sur les plans pédagogique et scolaire : elle recrute des "
          "professeurs, propose des formations pédagogiques continues adaptées au contexte de l’école "
          "et contrôle la qualité de l’enseignement dispensé lors de visites régulières."]),
      ],
    },
    {
      "n": "2", "t": "Les professeurs et les supports",
      "qa": [
        ("Les professeurs de l’EFAN sont-ils des répétiteurs ?", [],
         ["Non. Tous les professeurs de l’EFAN sont issus du ministère de l’Éducation nationale (MEN) "
          "ou de l’Enseignement supérieur et de la Recherche : professeurs des écoles, titulaires du "
          "CAPES ou de l’agrégation, enseignants du supérieur. Ils exercent à l’EFAN soit en qualité de "
          "personnels détachés ou en disponibilité de l’Éducation nationale, soit en qualité de "
          "personnels recrutés localement en raison de leur expertise et de leur expérience.",
          "Comme tout enseignant, ils dispensent leurs cours en s’appuyant sur des supports "
          "pédagogiques."]),
        ("Pourquoi l’EFAN recourt-elle aux supports du CNED ?", [],
         "Le CNED est l’opérateur public de l’Éducation nationale pour l’enseignement à distance. Ses "
         "supports sont particulièrement utiles pour les matières qui ne sont pas enseignées à "
         "l’EFAN, par exemple certaines spécialités ou les SES en seconde. Les matières enseignées à "
         "l’EFAN dépendent du recrutement des professeurs. Dans ces matières, les professeurs suivent "
         "le programme publié au Bulletin officiel (BO) de l’Éducation nationale ; dans les autres, le "
         "CNED permet aux élèves de suivre ce même programme."),
        ("Quel est l’intérêt de l’inscription à l’EFAN par rapport à un suivi des supports du CNED à "
         "domicile ou à une scolarité exclusivement américaine ?",
         ["bénéficier de professeurs qui enseignent le programme du Bulletin officiel (BO), "
          "s’appuient sur les supports du CNED lorsque cela est pertinent et proposent d’autres "
          "modalités de travail ;",
          "alléger la charge supportée par les parents et les enfants ;",
          "éviter toute rupture avec le système français et faciliter un éventuel retour en France ou "
          "dans un établissement français à l’étranger, en garantissant une méthodologie à la "
          "française ;",
          "permettre que les évaluations se déroulent en conditions réelles, au sein de la classe ;",
          "éviter le travail isolé à domicile, au profit d’un groupe et d’un cadre rassurant ;",
          "bénéficier d’une intégration plus progressive dans le système américain que les élèves "
          "scolarisés uniquement dans ce système, grâce au maintien d’un groupe et de repères "
          "français ;",
          "participer à des projets pédagogiques auxquels les élèves ne pourraient pas prendre part "
          "seuls, ou uniquement dans une école américaine, tels que « Héritiers de mémoire », les "
          "conférences d’enseignement moral et civique (EMC), les concours de mathématiques et de "
          "lecture ou les concours d’éloquence ;",
          "passer des examens blancs, écrits et oraux, dans les matières enseignées à l’EFAN ;",
          "suivre l’une des quatre spécialités proposées par l’EFAN (mathématiques, physique-chimie, "
          "SVT et HGGSP) ainsi que l’option mathématiques expertes ; à titre de comparaison, la "
          "plupart des lycées français aux États-Unis en proposent cinq ;",
          "s’investir dans des actions de bénévolat, en contribuant à l’organisation des "
          "manifestations de l’EFAN, notamment le concours d’art ;",
          "bénéficier d’échanges facilités avec les différents acteurs des écoles américaines, la "
          "direction de l’EFAN ayant développé des relations privilégiées avec ceux des quatre "
          "établissements d’accueil ;",
          "bénéficier d’un accompagnement des familles pour le choix des spécialités à la fin de la "
          "seconde, pour les inscriptions aux examens et le dossier Parcoursup, ainsi que pour le "
          "retour en France, y compris par la rédaction de lettres de recommandation ;",
          "recevoir des bulletins trimestriels reprenant les notes obtenues dans les programmes "
          "français et américain, lesquels peuvent être certifiés par l’inspectrice académique de "
          "l’ambassade de France à Washington D.C. ; le bulletin du troisième trimestre mentionne "
          "l’avis de passage ainsi que l’avis sur les spécialités pour l’entrée en classe de "
          "première ;",
          "bénéficier d’une représentation des parents d’élèves, élus chaque année, qui rencontrent à "
          "chaque trimestre, lors du conseil d’établissement, les professeurs, la direction et un "
          "représentant de la Mission laïque française (MLF) afin de faire le point sur les retours "
          "et questions des parents ainsi que sur les différentes activités de l’école, un compte "
          "rendu étant ensuite transmis aux parents ;",
          "bénéficier d’une équipe enseignante qui se réunit une fois par mois en conseil "
          "pédagogique et trois fois par an en conseils de classe ;",
          "développer une grande souplesse intellectuelle, une capacité de travail renforcée "
          "(gestion rigoureuse du temps, autonomie, collaboration), une ouverture internationale "
          "(aisance en anglais ouvrant l’accès aux universités anglophones, adaptation aux "
          "environnements multiculturels, approche analytique et critique issue des méthodes "
          "pédagogiques françaises et américaines), ainsi que des compétences transversales "
          "essentielles pour l’enseignement supérieur : initiative, esprit critique, capacité "
          "d’analyse et travail en équipe, atouts majeurs pour les projets et la recherche "
          "académique."],
         "L’inscription à l’EFAN présente plusieurs avantages :"),
        ("Les élèves doivent-ils suivre l’intégralité du programme du CNED, y compris les matières "
         "non enseignées à l’EFAN ?", [],
         ["Chaque famille détermine librement son choix. Les cours de toutes les matières sont "
          "disponibles en ligne et permettent un travail en autonomie.",
          "L’équipe enseignante conseille les familles et les élèves sur les matières qu’il est "
          "nécessaire d’étudier en autonomie, afin de garantir aux élèves les meilleures chances de "
          "réussite pour leur parcours scolaire et leur avenir. Elle dispose en effet d’une vision "
          "globale de leurs matières américaines et françaises, ainsi que de leurs projets scolaires "
          "et post-baccalauréat.",
          "Le double cursus offre un avantage supplémentaire : certaines matières peuvent être "
          "remplacées par leur équivalent américain. Un élève peut ainsi suivre l’espagnol côté "
          "américain plutôt qu’en LVA ou LVB avec le CNED."]),
      ],
    },
    {
      "n": "3", "t": "L’homologation",
      "qa": [
        ("L’EFAN est-elle un établissement homologué ?", [],
         "Non. Pour être homologué par le ministère de l’Éducation nationale, un établissement à "
         "l’étranger doit disposer de ses propres locaux. Lors de la création de l’école, il a été "
         "décidé d’intégrer l’EFAN au sein d’établissements américains, afin d’offrir aux élèves le "
         "bénéfice d’un véritable cursus franco-américain. Son fonctionnement est toutefois très "
         "proche de celui d’un établissement homologué : les bulletins de l’EFAN peuvent être "
         "certifiés par l’inspectrice académique de l’ambassade de France à Washington D.C., ce qui "
         "atteste la qualité de l’enseignement dispensé. L’EFAN est une école hybride, modèle "
         "éducatif unique aux États-Unis, et un établissement partenaire de la Mission laïque "
         "française (MLF)."),
        ("Quelles sont les conséquences de cette absence d’homologation ?", [],
         "Pour les élèves de 3<sup>e</sup>, de première et de terminale, les modalités de passation "
         "du brevet et du baccalauréat diffèrent de celles applicables à un élève scolarisé en "
         "France : les élèves ne bénéficient notamment pas du contrôle continu. Le dossier "
         "Parcoursup s’en trouve également affecté. Les onglets « Épreuves anticipées de français et "
         "baccalauréat », « Diplôme national du brevet » et « Parcoursup » du site détaillent ces "
         "modalités."),
      ],
    },
    {
      "n": "4", "t": "Le double cursus au quotidien",
      "qa": [
        ("Le double cursus est-il adapté à tous les profils d’élèves ?",
         ["les élèves ont le plus souvent moins de devoirs dans le cursus américain que dans le "
          "système français, quel que soit le niveau, le travail à la maison du côté américain "
          "correspondant à du travail non terminé en classe ;",
          "les petits effectifs permettent un enseignement personnalisé, une pédagogie adaptée à "
          "chaque élève et une excellente connaissance de chacun d’eux, chaque élève étant connu "
          "individuellement de l’équipe enseignante ;",
          "les élèves en difficulté peuvent tirer profit d’un travail en petit groupe, dans un cadre "
          "rassurant qui facilite la vie sociale, les élèves s’entraidant et pouvant mettre leurs "
          "points forts dans certaines matières au service de leurs camarades ;",
          "les emplois du temps cumulés sont comparables à ceux d’un élève scolarisé en France ;",
          "les professeurs veillent à respecter le rythme des élèves, notamment par la quantité de "
          "devoirs demandée."],
         "Oui. L’EFAN, en concertation avec les parents et l’équipe enseignante américaine, tient "
         "compte de la diversité des élèves et de leurs besoins particuliers :"),
        ("L’EFAN propose-t-elle des aménagements pour des besoins particuliers ?", [],
         "Oui. L’équipe pédagogique prend en compte la diversité des élèves et leurs besoins "
         "spécifiques. Les plans personnalisés sont pris en compte. Si nécessaire, l’EFAN accompagne "
         "la mise en place des plans 504 et des IEP (Individualized Education Program), ainsi que "
         "d’aménagements adaptés, avec les parents et l’équipe enseignante américaine. La directrice "
         "et les enseignants de l’EFAN sont pleinement impliqués dans les comités et les échanges "
         "relatifs à ces dispositifs."),
        ("Mon enfant sera-t-il réellement immergé dans la vie scolaire américaine ?",
         ["les élèves sont inscrits dans des établissements américains qui ouvrent des classes pour "
          "l’EFAN ;",
          "ils partagent le quotidien d’un élève américain : transport scolaire, casiers, repas "
          "apportés de la maison (<em>lunch box</em>) ;",
          "ils sont intégrés à des classes américaines et suivent l’emploi du temps américain ;",
          "les cours de l’EFAN ont lieu avant, pendant ou après les cours américains ; selon les "
          "niveaux, les élèves ne manquent qu’un créneau de cours américain par jour."],
         "Oui :"),
        ("Les élèves bénéficient-ils d’un apprentissage effectif de l’anglais ?",
         ["ils sont immergés dans le cursus américain, au sein d’un établissement et d’une classe "
          "américains ;",
          "ils suivent entre 60 et 70 % de l’emploi du temps américain, selon les niveaux ;",
          "comme tous les élèves étrangers, ils suivent des cours d’ESL (<em>English as a Second "
          "Language</em>) afin de perfectionner leur maîtrise de la langue."],
         "Oui :"),
        ("Les élèves disposent-ils du temps nécessaire pour pratiquer un sport ou des activités "
         "artistiques ?", [],
         "Oui, sous réserve de l’emploi du temps de l’enfant et des activités souhaitées. Les élèves "
         "peuvent, dans tous les cas, pratiquer des activités en dehors des établissements et côtoyer "
         "ainsi des Américains en plus de leurs camarades d’école. Plusieurs élèves pratiquent "
         "également des activités après l’école, au sein des établissements scolaires : football "
         "(<em>soccer</em>), tennis, lutte gréco-romaine, JROTC, musique (<em>band</em>) et arts."),
        ("Quelles compétences le double cursus permet-il de développer ?",
         ["une grande souplesse intellectuelle : le volume de travail conséquent encourage "
          "l’autonomie et la collaboration, entre différentes méthodes pédagogiques et "
          "d’évaluation ;",
          "une capacité de travail renforcée : le double cursus exige une gestion rigoureuse du temps "
          "et un haut niveau d’organisation. Il développe l’autonomie et la capacité à gérer une "
          "charge de travail importante, qualités essentielles pour les études supérieures ;",
          "une ouverture internationale précieuse : grâce à leur double immersion éducative et "
          "culturelle, les élèves acquièrent une aisance en anglais qui leur ouvre l’accès aux "
          "universités anglophones, ainsi qu’une capacité d’adaptation aux environnements "
          "multiculturels et une approche analytique et critique, nourrie par les méthodes "
          "pédagogiques françaises et américaines ;",
          "des compétences transversales essentielles pour l’enseignement supérieur : autonomie et "
          "initiative, esprit critique et capacité d’analyse, collaboration et travail en équipe, "
          "atouts majeurs pour les projets et la recherche académique."],
         "Le double cursus conduit les élèves à développer :"),
        ("Comment se déroule une journée à l’EFAN ?",
         ["à l’école élémentaire, la journée commence à 8 h 05 et s’achève à 16 h 15 ; environ trois "
          "heures par jour sont consacrées au programme français ;",
          "au collège, la journée commence à 8 h 15 à Crossroads Elementary and Middle School et à "
          "8 h 20 à Great Neck Middle School ; elle s’achève à 16 h 15 du lundi au jeudi et à 14 h 45 "
          "le vendredi à Crossroads, et à 16 h 00 à Great Neck ; entre 2 h 30 et 3 h par jour, selon "
          "les établissements, sont consacrées au programme français ;",
          "au lycée, les cours se déroulent de 7 h 20 à 16 h 00 au plus tard : les élèves suivent "
          "l’emploi du temps américain le matin, jusqu’à 12 h 35, puis les cours du cursus français, "
          "qui varient selon les niveaux et, pour les classes de première et de terminale, selon les "
          "spécialités choisies."],
         "Les horaires varient selon les niveaux et les établissements. Chaque jour, un créneau de "
         "cours américain est remplacé par un cours de l’EFAN :",
         "Les niveaux américains correspondent aux niveaux français de la manière suivante : "
         "<em>kindergarten</em> (grande section), 1st grade (CP), 2nd grade (CE1), 3rd grade (CE2), "
         "4th grade (CM1), 5th grade (CM2), du 6th au 8th grade (de la sixième à la quatrième) et du "
         "9th au 12th grade (de la troisième à la terminale)."),
        ("Comment mon enfant est-il évalué ?", [],
         ["<strong>Cursus américain.</strong> Les élèves de l’EFAN passent les mêmes évaluations que "
          "les élèves américains, dont les résultats sont exprimés sous forme de lettres. Tant que leur "
          "niveau d’anglais n’est pas suffisant, des dispositifs d’aide sont mis en place. Durant leur "
          "première année en tant qu’élèves ESL, les résultats obtenus du côté américain sont exprimés "
          "par la mention « Pass » ou « Fail » (validé ou non validé), ce qui facilite leur adaptation "
          "en limitant la pression liée aux notes. Les résultats sont consultables sur la plateforme "
          "ParentVUE et un bulletin américain (<em>report card</em>) est délivré à chaque période.",
          "<strong>Cursus français.</strong> Pour les matières enseignées à l’EFAN, les évaluations "
          "sont élaborées par les professeurs de l’EFAN, qui peuvent y adjoindre des évaluations du "
          "CNED ; elles se déroulent en classe, ce qui valorise le bulletin de l’élève en vue d’un "
          "retour en France. Pour les matières du CNED qui ne sont pas enseignées à l’EFAN, les "
          "évaluations sont réalisées à domicile : les familles transmettent elles-mêmes les copies au "
          "CNED pour correction."]),
      ],
    },
    {
      "n": "5", "t": "Le lycée, le baccalauréat et Parcoursup",
      "qa": [
        ("Quelles spécialités l’EFAN propose-t-elle, et pour quelles raisons ?", [],
         "Pour l’année scolaire 2026-2027, l’EFAN offre quatre spécialités (mathématiques, "
         "physique-chimie (SPC), SVT et HGGSP), complétées par l’option mathématiques expertes. À "
         "titre de comparaison, la plupart des lycées français aux États-Unis en proposent cinq. "
         "Cette offre s’appuie sur les préférences observées au niveau national."),
        ("Mon enfant souhaite suivre une spécialité qui n’est pas enseignée à l’EFAN. L’inscription "
         "demeure-t-elle pertinente ?", [],
         ["Oui, mais votre enfant devra travailler cette spécialité en autonomie, ce qui requiert une "
          "organisation et un travail personnel réguliers. Cette spécialité doit toutefois être "
          "proposée par le lycée Rochambeau, où se déroulent les examens ; à défaut, les examens "
          "devront être passés en France.",
          "En 2026-2027, 8 élèves de première sur 9 (89 %) ont l’intégralité de leurs spécialités "
          "enseignées à l’EFAN, et le dernier élève de première (11 %) a deux de ses spécialités "
          "enseignées à l’EFAN. En terminale, les 4 élèves sur 4 (100 %) ont l’intégralité de leurs "
          "spécialités enseignées à l’EFAN. Deux élèves de terminale (50 %) suivent par ailleurs "
          "l’option mathématiques expertes."]),
        ("Une réduction des frais de scolarité est-elle possible lorsque l’élève ne choisit pas les "
         "spécialités proposées par l’EFAN ?", [],
         "Non. Le budget de l’EFAN est contraint : il est cofinancé par les frais de scolarité versés "
         "par les familles, qui en constituent la plus grande partie, et par l’État-major des armées. "
         "La quasi-totalité de ce budget est consacrée à la rémunération des personnels de l’EFAN."),
        ("Les modalités de passation du DNB et du baccalauréat sont-elles identiques à celles "
         "applicables en France ?",
         ["choix 1 : les élèves passent les épreuves du programme de première en fin de première, "
          "puis celles du programme de terminale en fin de terminale ; cette option est celle "
          "retenue par les familles, car les élèves ne sont interrogés que sur le programme de "
          "première lors des épreuves de première, et les notes obtenues sont des notes certifiées, "
          "ce qui est important pour la constitution du dossier Parcoursup ;",
          "choix 2 : les élèves passent, en fin de terminale, toutes les épreuves des programmes de "
          "première et de terminale, à l’exception du français."],
         ["Non. Les élèves sont inscrits en qualité de candidats libres : le contrôle continu n’est "
          "pas pris en compte et chaque matière concernée fait l’objet d’une épreuve en fin d’année, "
          "au lycée Rochambeau, à Bethesda. Les onglets « Épreuves anticipées de français et "
          "baccalauréat » et « Diplôme national du brevet » du site détaillent le calendrier et les "
          "épreuves.",
          "Pour les élèves de première et de terminale, il est impératif de choisir des spécialités "
          "proposées par le lycée Rochambeau. Si les spécialités choisies n’y sont pas disponibles, "
          "les examens devront être passés en France, sur une période allant de la mi-mai au début du "
          "mois de juillet.",
          "Pour le DNB, les élèves passent les mêmes épreuves écrites que les candidats scolarisés en "
          "France : français ; histoire-géographie et enseignement moral et civique ; "
          "mathématiques ; deux matières à choisir parmi les trois suivantes (physique-chimie, "
          "sciences de la vie et de la Terre, technologie) ; et une épreuve écrite de langue vivante. "
          "Ces épreuves ont lieu au début du mois de juin, au lycée Rochambeau, à Bethesda. Le choix "
          "des deux matières de l’épreuve de sciences est communiqué aux familles au mois d’avril par "
          "la coordinatrice du service des examens des États-Unis.",
          "Pour le baccalauréat, l’EFAN organise une réunion d’information afin d’expliquer les "
          "modalités d’inscription aux examens sur la plateforme Cyclades. Lors de cette inscription, "
          "les élèves doivent choisir entre deux options, ce choix étant déterminant pour "
          "Parcoursup :"]),
        ("Passer le baccalauréat en candidat individuel constitue-t-il un désavantage ?",
         ["les modalités s’apparentent à celles qu’ont connues les parents d’aujourd’hui : une "
          "épreuve en fin d’année pour chaque matière ;",
          "certains établissements d’enseignement supérieur français considèrent les notes de "
          "contrôle continu avec réserve et privilégient les notes d’épreuves nationales."],
         "Les modalités de passation et le dossier Parcoursup diffèrent en partie de ceux d’un élève "
         "scolarisé en France. Plusieurs éléments sont toutefois à considérer :",
         "À titre d’illustration, en décembre 2024, la direction de Sciences Po Paris a annoncé une "
         "réforme des modalités de son concours d’entrée pour 2025, afin de pallier les limites du "
         "baccalauréat. Selon son directeur, Luis Vassy, les résultats du contrôle continu sont "
         "« survalorisés » par les établissements scolaires. Par ailleurs, le report des épreuves "
         "écrites en juin prive les établissements d’enseignement supérieur d’« une évaluation écrite "
         "nationale pour sélectionner les candidats », ce qu’ils regrettent. De même, certaines "
         "classes préparatoires aux grandes écoles (CPGE) et certaines écoles demandent aux candidats "
         "de passer des épreuves de concours d’entrée."),
        ("La procédure Parcoursup est-elle identique depuis les États-Unis et depuis la France ?", [],
         ["Non. L’élève de l’EFAN est inscrit en qualité de « candidat scolarisé à l’étranger » et les "
          "données prises en compte diffèrent. L’onglet « Parcoursup » du site détaille la procédure.",
          "Les élèves de l’EFAN bénéficient d’un accompagnement personnalisé pour la constitution de "
          "leur dossier Parcoursup, dispensé lors de réunions ainsi que tout au long de l’année "
          "scolaire, dès leur arrivée au lycée. L’équipe pédagogique les conseille sur les "
          "informations à y faire figurer (bénévolat, activités extrascolaires, etc.) et peut rédiger "
          "des lettres de recommandation et d’appui. Les élèves de l’EFAN ne sont pas concernés par le "
          "zonage de Parcoursup.",
          "L’EFAN est habilitée à organiser, à la demande des établissements concernés, les sessions "
          "de tests d’admission de leurs candidats.",
          "L’EFAN les accompagne également dans leurs démarches auprès des universités américaines, "
          "sur la plateforme Common App."]),
        ("Mes enfants sont-ils préparés aux examens ?",
         ["les élèves passent des épreuves blanches, écrites et orales, dans les matières enseignées "
          "à l’EFAN ;",
          "en terminale, les professeurs des spécialités concernées accompagnent la préparation du "
          "Grand oral ;",
          "les élèves assistent à des conférences d’enseignement moral et civique (EMC), dispensées "
          "par des membres de l’OTAN qui interviennent dans leur domaine de compétence. Ces "
          "conférences préparent les élèves de première et de terminale aux épreuves d’EMC selon une "
          "approche pédagogique différente, en créant un lien avec le monde réel."],
         "Oui :"),
        ("Mon enfant peut-il obtenir le <em>high school diploma</em> ?", [],
         ["Oui. Il est possible d’obtenir le <em>high school diploma</em> en arrivant en 10th grade "
          "(seconde), en 11th grade (première) ou en 12th grade (terminale), à condition de réunir le "
          "nombre de crédits exigé : 22 crédits pour le <em>standard diploma</em> et 26 crédits pour "
          "l’<em>advanced diploma</em>, auxquels s’ajoutent cinq crédits vérifiés (<em>verified "
          "credits</em>). Ceux-ci s’obtiennent en réussissant cinq examens SOL (<em>Standards of "
          "Learning</em>) : deux d’anglais (lecture et écriture, à partir du 11th grade), un de "
          "mathématiques, un de sciences et un d’histoire et sciences sociales. Le <em>diploma with "
          "honors</em> est décerné aux élèves dont la moyenne générale (GPA) est égale ou supérieure "
          "à 3.0.",
          "Les crédits s’acquièrent entre le 9th grade (troisième) et le 12th grade (terminale). "
          "Chaque cours américain suivi avec une moyenne satisfaisante valide le crédit "
          "correspondant ; certains cours suivis à l’EFAN donnent droit à des crédits, en vertu "
          "d’accords conclus avec Virginia Beach City Public Schools (VBCPS) (trois crédits en "
          "mathématiques et un crédit en histoire) ; la scolarité suivie en France permet également "
          "d’en acquérir, selon le principe de l’équivalence des crédits. VBCPS demande que les "
          "bulletins scolaires français soient fournis en français : ils sont ensuite traduits par le "
          "service des langues vivantes (<em>World Language Office</em>) de VBCPS.",
          "À leur arrivée au lycée américain, il est conseillé aux élèves d’indiquer à leur "
          "<em>counselor</em> qu’ils sont présents pour une durée limitée et d’examiner avec lui la "
          "possibilité d’obtenir leur diplôme au cours de cette période. Un élève qui dispose d’un "
          "nombre suffisant de crédits en 11th grade (première) peut obtenir son diplôme, mais ne "
          "peut alors plus suivre les cours de l’EFAN en terminale."]),
      ],
    },
    {
      "n": "6", "t": "Après l’EFAN et questions pratiques",
      "qa": [
        ("Quelle est l’utilité de l’EFAN, dès lors que des élèves rentrés en France sans l’avoir "
         "fréquentée ne rencontrent aucune difficulté ?", [],
         ["L’EFAN favorise le retour en France, notamment grâce aux bulletins de l’EFAN, dont la "
          "certification est possible, ainsi qu’aux lettres de recommandation et d’appui. Ces "
          "éléments permettent aux élèves d’éviter les tests de retour dans le système public "
          "scolaire français, à partir de la classe de sixième, qui peuvent retarder la rentrée "
          "scolaire, voire empêcher l’intégration dans l’établissement de leur choix. Les élèves "
          "intègrent également, à leur retour, des lycées privés prestigieux. L’EFAN est habilitée à "
          "organiser les sessions de tests d’admission de ces établissements, tels que Grandchamps, "
          "l’École internationale de Saint-Cloud, le lycée Saint-Louis-de-Gonzague, etc.",
          "Les élèves de l’EFAN ont connu de belles réussites et ont été admis dans des formations "
          "post-baccalauréat variées : classes préparatoires scientifiques (lycée naval de Brest, "
          "lycée Chaptal) et littéraires (lycée Molière), universités américaines (notamment Old "
          "Dominion University, ODU), cursus de droit (Assas, University of Essex), école "
          "d’infirmières, université de médecine, etc.",
          "L’onglet « Témoignages » du site rassemble les retours des familles et des anciens élèves "
          "sur la période qui suit l’EFAN. Une enquête de fin d’année, menée de manière anonyme "
          "auprès de l’ensemble des parents et des élèves, en présente les résultats."]),
        ("Un élève résidant hors de la carte scolaire peut-il bénéficier du transport scolaire ?", [],
         "Non. Seuls les élèves résidant dans le secteur de l’établissement peuvent emprunter le bus "
         "scolaire. L’onglet « Carte scolaire et transport » précise les règles applicables à chaque "
         "établissement."),
        ("Quels sont les résultats de l’EFAN aux examens ?", [],
         "Le taux de réussite est de 100 % au baccalauréat et au DNB pour les années scolaires "
         "2024-2025 (7 élèves de terminale sur 7 et 10 élèves de troisième sur 10) et 2025-2026 "
         "(3 élèves de terminale sur 3 et 8 élèves de troisième sur 8). L’onglet « Résultats aux "
         "examens et poursuite d’études » du site détaille les mentions obtenues et les formations "
         "intégrées."),
        ("Que pensent les familles et les élèves de l’EFAN ?",
         ["100 % des parents recommandent l’EFAN et estiment la relation avec l’équipe pédagogique "
          "satisfaisante ou exceptionnelle ;",
          "plus de 90 % des parents estiment que l’EFAN a facilité la scolarité de leur enfant, et "
          "90 % jugent l’accompagnement administratif très pertinent ou satisfaisant ;",
          "plus de 90 % des élèves ont trouvé l’année enrichissante ou passionnante, et 90 % jugent "
          "avoir une bonne relation avec leurs professeurs de l’EFAN ;",
          "78 % des élèves estiment que la charge de travail est correcte ; 15 % la jugent trop "
          "importante pour le double cursus et 7 % jugent l’année difficile."],
         "Un sondage de fin d’année a été réalisé en ligne, de manière anonyme, du 23 juin au "
         "6 juillet 2025, auprès de l’ensemble des parents et des élèves. Pour l’année scolaire "
         "2024-2025 :"),
        ("Comment inscrire mon enfant à l’EFAN ?", [],
         ["L’inscription se déroule en trois étapes : l’inscription à l’EFAN, effectuée en ligne "
          "depuis la France à partir du 1<sup>er</sup> avril ; l’inscription au CNED, assurée par la "
          "direction de l’EFAN à la fin du mois de juin ou au début du mois de juillet, sans démarche "
          "de la famille ; et l’inscription dans l’établissement américain, qui comprend une "
          "préinscription en ligne puis une inscription en personne, avec l’enfant, sur rendez-vous "
          "fixé par l’établissement américain, à l’arrivée à Norfolk ou à Virginia Beach. Les "
          "inscriptions tardives ou en cours d’année sont possibles.",
          "L’inscription à l’EFAN est complète lorsque tous les documents requis (règlement "
          "intérieur, code de conduite, acceptation des conditions, règlement financier, bulletins "
          "scolaires et pièces propres à chaque niveau) ont été remplis et transmis à "
          "l’administration de l’école, et que les frais applicables ont été acquittés. Les élèves "
          "doivent être à jour dans leurs vaccinations. Les onglets « Inscription à l’EFAN » et "
          "« Inscription dans les établissements américains » du site détaillent chaque étape."]),
        ("Quels sont les frais d’inscription ?", [],
         "Pour les dossiers transmis avant le 31 mai, les frais d’inscription s’élèvent à 275 $ pour "
         "un nouvel élève et à 140 $ pour une réinscription. Pour les dossiers transmis à partir du "
         "1<sup>er</sup> juin, ils sont majorés de 15 $ par mois, jusqu’au début de l’année "
         "scolaire. Les frais d’inscription ne sont pas remboursables. Pour plus d’informations, il "
         "convient de consulter le règlement financier de l’EFAN."),
        ("Comment les familles et les élèves peuvent-ils s’impliquer dans la vie de l’école ?", [],
         ["Les élèves peuvent assurer un tutorat auprès d’élèves américains qui apprennent le "
          "français et contribuer à l’organisation des manifestations de l’EFAN (concours d’art, "
          "Chandeleur, etc.) ; un certificat de volontariat leur est délivré. Les parents peuvent "
          "participer à l’organisation des manifestations (<em>potlucks</em>, par exemple), surveiller "
          "les examens blancs, organiser des collectes de fonds, devenir représentants des parents "
          "d’élèves ou se porter candidats pour devenir membres du conseil d’administration.",
          "Les représentants des parents d’élèves sont élus chaque année : un appel à candidatures "
          "est lancé par la direction à la fin du mois de septembre, puis les parents votent au moyen "
          "d’un formulaire en ligne. Ils rencontrent à chaque trimestre, lors du conseil "
          "d’établissement, les professeurs, la direction et un représentant de la Mission laïque "
          "française, et un compte rendu est ensuite transmis aux parents."]),
      ],
    },
  ],
},
"en": {
  "lang": "en",
  "title": "Frequently asked questions",
  "school": "French American School of Norfolk",
  "sub": "Clear answers to the questions families ask us most often",
  "edition": "2026-2027 edition",
  "site": "efanvirginia.com",
  "contact": "efan.norfolk@gmail.com · (757) 230-7569",
  "toc_title": "Contents",
  "figures_title": "Key figures",
  "figures_note": "Enrollment at the start of 2026-2027: 25 students in elementary school, 25 in middle "
                  "school and 21 in high school, 71 students in all.",
  "chart_title": "How enrollment has grown",
  "chart_note": "From 10 students in 2020-2021 to 71 at the start of 2026-2027: enrollment multiplied by 7.1 in six years.",
  "figures": [
    ("71", "students at the start of <span style='white-space:nowrap'>2026-2027</span>"),
    ("×7.1", "growth in enrollment since 2020-2021"),
    ("17%", "of students from civilian families (12 of 71)"),
    ("7%", "French-speaking students with at least one foreign parent (5 of 71)"),
  ],
  "closing_title": "Is your question not answered here?",
  "closing": ("The FASN office answers families Monday to Friday, 9:00 a.m. to 5:00 p.m.: "
              "efan.norfolk@gmail.com · (757) 230-7569. For the subjects covered in detail on the "
              "website (baccalauréat, Parcoursup, school district, enrollment), the corresponding pages "
              "are the reference."),
  "addresses_title": "Addresses of the American schools that host FASN:",
  "sources": ("Sources: information provided by FASN and the efanvirginia.com website. "
              "The breakdown figures are for the 2026-2027 school year."),
  "sections": [
    {
      "n": "1", "t": "The school and its students",
      "qa": [
        ("How many students does FASN have?", [],
         "The school has 71 students at the start of 2026-2027 (25 in elementary school, 25 in middle "
         "school and 21 in high school), compared with 77 in 2025-2026. Since 2020-2021, when it had "
         "10 students, enrollment has grown 7.1-fold. In 2026-2027, 12 of the 71 students come from "
         "civilian families and 5 are French speakers with at least one foreign parent."),
        ("Does FASN welcome students who do not speak French?", [],
         "Yes. FASN also welcomes students who do not speak French, for whom starting between "
         "Kindergarten (grande section) and 3rd grade (CE2) is recommended. The school is not reserved "
         "for military families: it is open to all."),
        ("Why is FASN spread across several schools?", [],
         "The school has no premises of its own: its classes are hosted within American public "
         "schools, in Norfolk and Virginia Beach. The “History” page of the website traces this "
         "gradual expansion."),
        ("Why is the school named after Norfolk when most students attend school in Virginia Beach?", [],
         "The school was founded in Norfolk in 2011. As most military families live in Virginia Beach, "
         "a partnership was signed there in 2022 and classes were opened gradually. The original name "
         "was kept."),
        ("Who founded FASN?", [],
         "FASN was founded in 2011 at the initiative of the French Armed Forces General Staff and of "
         "the French military representative in Norfolk (Élément de soutien national, ESN), with the "
         "commitment of John and Simone Ryan, a French American couple from Hampton Roads, and the "
         "support of the Mission laïque française (MLF). Simone Ryan is still today the founder and "
         "President of the school’s Board of Directors. The “History” page of the website tells this "
         "story."),
        ("Who runs FASN?", [],
         ["FASN is a non-profit organization governed by a Board of Directors, which meets every "
          "month, oversees financial management, recruits the school’s Director and ensures the "
          "consistency of its strategy. The Director leads the school and oversees its daily "
          "operation: she holds the same responsibilities as a school principal in France, and "
          "recruits and evaluates teachers in collaboration with the Mission laïque française.",
          "The Mission laïque française, a non-profit operator of the French State, is mandated to "
          "support the school’s educational and academic operation: it recruits teachers, provides "
          "ongoing teacher training tailored to the school’s context and monitors the quality of "
          "teaching during regular visits."]),
      ],
    },
    {
      "n": "2", "t": "Teachers and teaching materials",
      "qa": [
        ("Are FASN teachers tutors?", [],
         ["No. All FASN teachers come from the French Ministry of National Education or from higher "
          "education and research: primary school teachers, holders of the CAPES or the agrégation, "
          "and university lecturers. They work at FASN either on secondment or leave from the "
          "Ministry of National Education, or as locally recruited staff hired for their expertise "
          "and experience.",
          "Like any teacher, they build their lessons on teaching materials."]),
        ("Why does FASN use CNED materials?", [],
         "The CNED is the French Ministry of National Education’s public provider of distance "
         "learning. Its materials are especially useful for subjects not taught at FASN, such as some "
         "specialty subjects or economics and social sciences (SES) in 10th grade. The subjects taught "
         "at FASN depend on teacher recruitment. In those subjects, teachers follow the curriculum "
         "published in the Ministry’s Bulletin officiel (BO); in the others, the CNED lets students "
         "follow the same curriculum."),
        ("What does enrolling at FASN add compared with following CNED materials at home or attending "
         "only an American school?",
         ["teachers who teach the Bulletin officiel (BO) curriculum, use CNED materials when relevant "
          "and offer other ways of working;",
          "a lighter load for parents and children;",
          "no break with the French system, and an easier return to France or to a French school "
          "abroad, thanks to a French working method;",
          "assessments taken under real conditions, in class;",
          "no working alone at home, but in a group and a reassuring setting;",
          "a more gradual transition into the American system than for students enrolled only in that "
          "system, thanks to a group and French reference points;",
          "educational projects students could not join on their own, or in an American school "
          "alone, such as “Héritiers de mémoire”, the moral and civic education (EMC) conferences, "
          "mathematics and reading competitions and public-speaking competitions;",
          "written and oral mock exams in the subjects taught at FASN;",
          "one of the four specialty subjects offered by FASN (mathematics, physics-chemistry, life "
          "and earth sciences and HGGSP), plus the advanced mathematics option; by comparison, most "
          "French high schools in the United States offer five;",
          "volunteering opportunities, helping to organize FASN events such as the art competition;",
          "easier dealings with the staff of the American schools, as the FASN Director has built "
          "close relationships with all four host schools;",
          "support for families in choosing specialty subjects at the end of 10th grade, in "
          "registering for exams and preparing the Parcoursup application, and in returning to "
          "France, including letters of recommendation;",
          "term report cards with the grades earned in both the French and the American curricula, "
          "which can be certified by the academic inspector of the French Embassy in Washington "
          "D.C.; the third-term report card states the decision on moving up and the opinion on "
          "specialty subjects for entry into 11th grade;",
          "parents’ representatives, elected every year, who meet each term at the School Council "
          "with the teachers, the Director and a representative of the Mission laïque française (MLF) "
          "to review parents’ feedback and questions and the school’s activities, with minutes then "
          "shared with parents;",
          "a teaching team that meets once a month in a teachers’ council and three times a year in "
          "class councils;",
          "great intellectual flexibility, a stronger capacity for work (rigorous time management, "
          "independence, collaboration), an international outlook (fluency in English that opens "
          "the doors of English-speaking universities, adaptability to multicultural environments, "
          "an analytical and critical approach drawn from French and American teaching methods), and "
          "transferable skills essential for higher education: initiative, critical thinking, "
          "analysis and teamwork, major assets for projects and academic research."],
         "Enrolling at FASN offers several advantages:"),
        ("Must students follow the whole CNED curriculum, including subjects not taught at FASN?", [],
         ["Each family decides freely. Courses in all subjects are available online and allow "
          "students to work independently.",
          "The teaching team advises families and students on the subjects that need to be studied "
          "independently, to give students the best chances of success in their schooling and future. "
          "It has an overall view of their American and French subjects and of their academic and "
          "post-baccalauréat plans.",
          "The dual curriculum offers an additional advantage: some subjects can be replaced by their "
          "American equivalent. A student can, for example, take Spanish in the American curriculum "
          "rather than as LVA or LVB with the CNED."]),
      ],
    },
    {
      "n": "3", "t": "Accreditation",
      "qa": [
        ("Is FASN an accredited (homologué) school?", [],
         "No. To be accredited by the French Ministry of National Education, a school abroad must have "
         "its own premises. When the school was founded, it was decided to place FASN within American "
         "schools, so that students could benefit from a genuine French American curriculum. Its "
         "operation is nevertheless very close to that of an accredited school: FASN report cards can "
         "be certified by the academic inspector of the French Embassy in Washington D.C., which "
         "attests to the quality of the teaching. FASN is a hybrid school, an educational model "
         "unique in the United States, and a partner school of the Mission laïque française (MLF)."),
        ("What are the consequences of not being accredited?", [],
         "For students in 9th grade (3<sup>e</sup>), 11th grade (première) and 12th grade "
         "(terminale), the way the brevet and the baccalauréat are taken differs from that of a "
         "student in France: in particular, students do not benefit from continuous assessment. The "
         "Parcoursup application is affected as well. The “Early French exams and Baccalauréat”, "
         "“DNB Middle School Diploma” and “Parcoursup” pages of the website explain the details."),
      ],
    },
    {
      "n": "4", "t": "The dual curriculum day to day",
      "qa": [
        ("Is the dual curriculum suitable for every type of student?",
         ["students usually have less homework in the American curriculum than in the French system, "
          "whatever the grade, as American homework is work not finished in class;",
          "small classes allow personalized teaching adapted to each student and an excellent "
          "knowledge of each of them, as the teaching team knows every student individually;",
          "students who struggle can benefit from working in a small group, in a reassuring setting "
          "that makes social life easier, where students help one another and put their strengths "
          "in some subjects at the service of their classmates;",
          "the combined timetables are comparable to those of a student in France;",
          "teachers make sure to respect the students’ pace, in particular through the amount of "
          "homework set."],
         "Yes. FASN, together with the parents and the American teaching team, takes into account the "
         "diversity of students and their particular needs:"),
        ("Does FASN offer accommodations for special needs?", [],
         "Yes. The teaching team takes into account the diversity of students and their specific "
         "needs. Personalized plans are taken into account. If necessary, FASN helps put 504 plans, "
         "IEPs (Individualized Education Programs) and appropriate accommodations in place, together "
         "with the parents and the American teaching team. The FASN Director and teachers are fully "
         "involved in the committees and discussions about these arrangements."),
        ("Will my child really be immersed in American school life?",
         ["students are enrolled in American schools that open classes for FASN;",
          "they share the daily life of an American student: school bus, lockers, lunch brought from "
          "home (lunch box);",
          "they are integrated into American classes and follow the American timetable;",
          "FASN classes take place before, during or after American classes; depending on the grade, "
          "students miss only one American class period a day."],
         "Yes:"),
        ("Do students really learn English?",
         ["they are immersed in the American curriculum, in an American school and an American class;",
          "they follow 60 to 70% of the American timetable, depending on the grade;",
          "like all international students, they take ESL (English as a Second Language) classes to "
          "perfect their command of the language."],
         "Yes:"),
        ("Do students have time for sports or the arts?", [],
         "Yes, depending on the child’s timetable and the activities they want to do. In any case, "
         "students can take part in activities outside school and so meet Americans beyond their "
         "classmates. Several students also take part in after-school activities within their "
         "schools: soccer, tennis, Greco-Roman wrestling, JROTC, band and the arts."),
        ("What skills does the dual curriculum develop?",
         ["great intellectual flexibility: the substantial workload encourages independence and "
          "collaboration, across different teaching and assessment methods;",
          "a stronger capacity for work: the dual curriculum requires rigorous time management and a "
          "high level of organization. It builds independence and the ability to handle a heavy "
          "workload, essential qualities for higher education;",
          "a valuable international outlook: thanks to their dual educational and cultural "
          "immersion, students become fluent in English, which opens the doors of English-speaking "
          "universities, and gain the ability to adapt to multicultural environments and an "
          "analytical, critical approach shaped by French and American teaching methods;",
          "transferable skills essential for higher education: independence and initiative, critical "
          "thinking and analysis, collaboration and teamwork, major assets for projects and academic "
          "research."],
         "The dual curriculum leads students to develop:"),
        ("What does a day at FASN look like?",
         ["in elementary school, the day starts at 8:05 a.m. and ends at 4:15 p.m.; about three hours a "
          "day are devoted to the French curriculum;",
          "in middle school, the day starts at 8:15 a.m. at Crossroads Elementary and Middle School and "
          "at 8:20 a.m. at Great Neck Middle School; it ends at 4:15 p.m. Monday to Thursday and "
          "2:45 p.m. on Friday at Crossroads, and at 4:00 p.m. at Great Neck; between 2.5 and 3 hours "
          "a day, depending on the school, are devoted to the French curriculum;",
          "in high school, classes run from 7:20 a.m. to 4:00 p.m. at the latest: students follow the "
          "American timetable in the morning, until 12:35 p.m., then the French curriculum classes, "
          "which vary by grade and, in 11th and 12th grade, by the specialty subjects chosen."],
         "Times vary by grade and school. Every day, one American class period is replaced by an FASN "
         "class:",
         "American grades correspond to French grades as follows: Kindergarten (grande section), "
         "1st grade (CP), 2nd grade (CE1), 3rd grade (CE2), 4th grade (CM1), 5th grade (CM2), 6th to "
         "8th grade (sixième to quatrième) and 9th to 12th grade (troisième to terminale)."),
        ("How is my child assessed?", [],
         ["<strong>American curriculum.</strong> FASN students take the same assessments as American "
          "students, with results expressed as letter grades. As long as their level of English is "
          "not sufficient, support measures are put in place. During their first year as ESL "
          "students, their American results are expressed as “Pass” or “Fail”, which eases their "
          "adjustment by limiting the pressure of grades. Results can be viewed on the ParentVUE "
          "platform and an American report card is issued for each grading period.",
          "<strong>French curriculum.</strong> For the subjects taught at FASN, assessments are "
          "designed by the FASN teachers, who may add CNED assessments; they take place in class, "
          "which gives weight to the student’s report card with a view to returning to France. For the "
          "CNED subjects not taught at FASN, assessments are done at home: families send the papers to "
          "the CNED for marking themselves."]),
      ],
    },
    {
      "n": "5", "t": "High school, the baccalauréat and Parcoursup",
      "qa": [
        ("Which specialty subjects does FASN offer, and why?", [],
         "For the 2026-2027 school year, FASN offers four specialty subjects (mathematics, "
         "physics-chemistry, life and earth sciences and HGGSP), complemented by the advanced "
         "mathematics option (mathématiques expertes). By comparison, most French high schools in the "
         "United States offer five. This offer is based on the preferences observed nationally in "
         "France."),
        ("My child wants a specialty subject that FASN does not teach. Is enrolling still worthwhile?", [],
         ["Yes, but your child will have to study that subject independently, which requires regular "
          "organization and personal work. The subject must, however, be offered by the Lycée "
          "Rochambeau, where the exams take place; otherwise, the exams will have to be taken in "
          "France.",
          "In 2026-2027, 8 of the 9 students in 11th grade (89%) have all their specialty subjects "
          "taught at FASN, and the remaining student (11%) has two of them taught at FASN. In 12th "
          "grade, all 4 students (100%) have all their specialty subjects taught at FASN. Two 12th "
          "grade students (50%) also take the advanced mathematics option."]),
        ("Can tuition be reduced when a student does not choose the specialty subjects offered by "
         "FASN?", [],
         "No. FASN’s budget is tight: it is co-funded by the tuition paid by families, which makes up "
         "the largest share, and by the French Armed Forces General Staff. Almost all of the budget "
         "goes to paying FASN staff."),
        ("Are the DNB and the baccalauréat taken the same way as in France?",
         ["choice 1: students take the exams on the 11th grade curriculum at the end of 11th grade, "
          "then those on the 12th grade curriculum at the end of 12th grade; this is the option "
          "families choose, because students are only examined on the 11th grade curriculum in the "
          "11th grade exams, and the grades obtained are certified grades, which matters for the "
          "Parcoursup application;",
          "choice 2: students take all the exams on the 11th and 12th grade curricula at the end of "
          "12th grade, except French."],
         ["No. Students are registered as independent candidates: continuous assessment does not "
          "count and each subject concerned is examined at the end of the year, at the Lycée "
          "Rochambeau, in Bethesda. The “Early French exams and Baccalauréat” and “DNB Middle School "
          "Diploma” pages of the website give the calendar and the exams.",
          "Students in 11th and 12th grade must choose specialty subjects offered by the Lycée "
          "Rochambeau. If the chosen subjects are not available there, the exams will have to be "
          "taken in France, at some point between mid-May and early July.",
          "For the DNB, students take the same written exams as candidates schooled in France: "
          "French; history-geography and moral and civic education; mathematics; two subjects chosen "
          "from physics-chemistry, life and earth sciences and technology; and a written exam in a "
          "modern language. These exams take place in early June at the Lycée Rochambeau, in "
          "Bethesda. The two subjects of the science exam are announced to families in April by the "
          "exam coordinator for the United States.",
          "For the baccalauréat, FASN holds an information meeting to explain how to register for "
          "the exams on the Cyclades platform. When registering, students must choose between two "
          "options, a choice that is decisive for Parcoursup:"]),
        ("Is taking the baccalauréat as an independent candidate a disadvantage?",
         ["the format is similar to the one today’s parents knew: one exam at the end of the year for "
          "each subject;",
          "some French higher education institutions view continuous assessment grades with caution "
          "and favor grades from national exams."],
         "The way the exams are taken and the Parcoursup application partly differ from those of a "
         "student in France. Several points are worth considering, however:",
         "For example, in December 2024 the leadership of Sciences Po Paris announced a reform of its "
         "entrance exam for 2025 to make up for the limits of the baccalauréat. According to its "
         "director, Luis Vassy, continuous assessment results are “overrated” by schools. In addition, "
         "moving the written exams to June deprives higher education institutions of “a national "
         "written assessment to select candidates”, which they regret. Likewise, some preparatory "
         "classes for the grandes écoles (CPGE) and some schools ask applicants to sit entrance "
         "exams."),
        ("Does Parcoursup work the same way from the United States as from France?", [],
         ["No. The FASN student is registered as a “candidate schooled abroad” and the information "
          "taken into account differs. The “Parcoursup” page of the website explains the process.",
          "FASN students receive individual support in building their Parcoursup application, during "
          "meetings and throughout the school year, from the moment they start high school. The "
          "teaching team advises them on what to include (volunteering, extracurricular activities, "
          "etc.) and can write letters of recommendation and support. FASN students are not affected "
          "by Parcoursup’s geographic zoning.",
          "At the request of the schools concerned, FASN is authorized to hold admission test "
          "sessions for their applicants.",
          "FASN also helps students apply to American universities through the Common App platform."]),
        ("Are my children prepared for the exams?",
         ["students sit written and oral mock exams in the subjects taught at FASN;",
          "in 12th grade, the teachers of the specialty subjects concerned help students prepare for "
          "the Grand oral;",
          "students attend moral and civic education (EMC) conferences given by NATO personnel "
          "speaking in their field of expertise. These conferences prepare 11th and 12th grade "
          "students for the EMC exams with a different teaching approach, by connecting with the "
          "real world."],
         "Yes:"),
        ("Can my child earn the high school diploma?", [],
         ["Yes. Students can earn the high school diploma even if they arrive in 10th, 11th or 12th "
          "grade, provided they gather the required number of credits: 22 credits for the standard "
          "diploma and 26 credits for the advanced diploma, plus five verified credits. These are "
          "earned by passing five SOL (Standards of Learning) tests: two in English (reading and "
          "writing, from 11th grade), one in mathematics, one in science and one in history and "
          "social studies. The diploma with honors is awarded to students whose grade point average "
          "(GPA) is 3.0 or higher.",
          "Credits are earned between 9th and 12th grade. Each American course completed with a "
          "satisfactory average earns the corresponding credit; some courses taken at FASN earn "
          "credits under agreements with Virginia Beach City Public Schools (VBCPS) (three "
          "mathematics credits and one history credit); schooling completed in France can also earn "
          "credits, under the principle of credit equivalence. VBCPS asks for French report cards to "
          "be provided in French: they are then translated by the VBCPS World Language Office.",
          "When they start at the American high school, students are advised to tell their counselor "
          "that they will only be there for a limited time and to explore whether they can graduate "
          "during that period. A student with enough credits in 11th grade can graduate, but can then "
          "no longer take FASN classes in 12th grade."]),
      ],
    },
    {
      "n": "6", "t": "After FASN, and practical questions",
      "qa": [
        ("What is the point of FASN, when students who return to France without having attended it "
         "have no difficulty?", [],
         ["FASN makes the return to France easier, in particular through FASN report cards, which can "
          "be certified, and letters of recommendation and support. These allow students to avoid the "
          "re-entry tests of the French public school system, from 6th grade onwards, which can delay "
          "the start of the school year or even prevent admission to the school of their choice. On "
          "their return, students also join prestigious private high schools. FASN is authorized to "
          "hold admission test sessions for these schools, such as Grandchamps, the École "
          "internationale de Saint-Cloud, the Lycée Saint-Louis-de-Gonzague, etc.",
          "FASN students have achieved fine results and have been admitted to a wide range of "
          "post-baccalauréat programs: scientific preparatory classes (Lycée naval de Brest, Lycée "
          "Chaptal) and humanities preparatory classes (Lycée Molière), American universities "
          "(including Old Dominion University, ODU), law degrees (Assas, University of Essex), nursing "
          "school, medical school, etc.",
          "The “Testimonies” page of the website gathers feedback from families and former students "
          "on life after FASN. An end-of-year survey, conducted anonymously among all parents and "
          "students, presents its results."]),
        ("Can a student living outside the school zone use school transportation?", [],
         "No. Only students living within the school’s zone can ride the school bus. The “School "
         "district and transportation” page sets out the rules for each school."),
        ("What are FASN’s exam results?", [],
         "The pass rate is 100% for both the baccalauréat and the DNB in 2024-2025 (7 of 7 students in "
         "12th grade and 10 of 10 in 9th grade) and in 2025-2026 (3 of 3 students in 12th grade and 8 "
         "of 8 in 9th grade). The “Exam results and further studies” page of the website gives the "
         "mentions obtained and the programs students went on to."),
        ("What do families and students think of FASN?",
         ["100% of parents recommend FASN and rate their relationship with the teaching team as "
          "satisfactory or exceptional;",
          "more than 90% of parents feel FASN made their child’s schooling easier, and 90% rate the "
          "administrative support as very relevant or satisfactory;",
          "more than 90% of students found the year enriching or exciting, and 90% feel they have a "
          "good relationship with their FASN teachers;",
          "78% of students find the workload reasonable; 15% find it too heavy for the dual "
          "curriculum and 7% found the year difficult."],
         "An end-of-year survey was conducted online and anonymously, from June 23 to July 6, 2025, "
         "among all parents and students. For the 2024-2025 school year:"),
        ("How do I enroll my child at FASN?", [],
         ["Enrollment takes place in three steps: enrollment at FASN, online from France from April 1; "
          "enrollment with the CNED, handled by the FASN Director at the end of June or the beginning "
          "of July, with nothing for the family to do; and enrollment in the American school, which "
          "involves online pre-registration and then in-person registration with the child, by "
          "appointment set by the American school, on arrival in Norfolk or Virginia Beach. Late or "
          "mid-year enrollment is possible.",
          "Enrollment at FASN is complete when all required documents (school rules, code of conduct, "
          "acceptance of terms, financial regulations, report cards and the documents specific to "
          "each level) have been completed and submitted to the school administration, and the "
          "applicable fees have been paid. Students must be up to date with their vaccinations. The "
          "“Enrollment at FASN” and “Enrollment in the American schools” pages of the website detail "
          "each step."]),
        ("What are the registration fees?", [],
         "For applications submitted before May 31, the registration fee is $275 for a new student "
         "and $140 for re-enrollment. For applications submitted on or after June 1, it increases by "
         "$15 per month until the start of the school year. Registration fees are non-refundable. For "
         "more information, please see the FASN financial regulations."),
        ("How can families and students get involved in school life?", [],
         ["Students can tutor American students who are learning French and help organize FASN "
          "events (art competition, Candlemas, etc.); they receive a volunteering certificate. "
          "Parents can help organize events (potlucks, for example), proctor mock exams, organize "
          "fundraisers, become parents’ representatives or stand for election to the Board of "
          "Directors.",
          "Parents’ representatives are elected every year: the Director issues a call for candidates "
          "at the end of September, then parents vote using an online form. Each term, they meet the "
          "teachers, the Director and a representative of the Mission laïque française at the School "
          "Council, and minutes are then shared with parents."]),
      ],
    },
  ],
},
}
