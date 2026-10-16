# -*- coding: utf-8 -*-
"""FAQ content, from the school's FAQ 2025 and the 'What is FASN?' page."""

ENROLMENT = [("2020-2021", 10), ("2021-2022", 15), ("2022-2023", 31),
             ("2023-2024", 43), ("2024-2025", 63), ("2025-2026", 75)]

DATA = {
"fr": {
  "lang": "fr",
  "title": "Foire aux questions",
  "school": "École Franco-Américaine de Norfolk",
  "sub": "Les questions que les familles nous posent le plus souvent",
  "edition": "Édition 2025-2026",
  "site": "efan-norfolk.org",
  "contact": "efan.norfolk@gmail.com · (757) 230-7569",
  "toc_title": "Sommaire",
  "figures_title": "L’EFAN en chiffres",
  "figures_note": "Effectifs : page «&nbsp;Qu’est-ce que l’EFAN&nbsp;?&nbsp;». Répartition : année 2024-2025.",
  "chart_title": "L’évolution des effectifs",
  "chart_note": "De 10 à 75 élèves en six ans, soit un effectif multiplié par sept et demi.",
  "figures": [
    ("75", "élèves à la rentrée 2025-2026"),
    ("×7,5", "d’augmentation des effectifs en six ans"),
    ("25 %", "des élèves issus de familles civiles"),
    ("22 %", "francophones avec au moins un parent étranger"),
  ],
  "closing_title": "Une question qui n’est pas ici ?",
  "closing": ("Le secrétariat de l’EFAN répond aux familles du lundi au vendredi, de 9 h 00 à "
              "17 h 00. Pour les sujets traités en détail sur le site — baccalauréat, Parcoursup, "
              "carte scolaire, inscription — les onglets correspondants sont la référence."),
  "sources": ("Sources : FAQ de l’EFAN (2025) et page «&nbsp;Qu’est-ce que l’EFAN&nbsp;?&nbsp;» du site. "
              "Les chiffres de répartition portent sur l’année scolaire 2024-2025."),
  "sections": [
    {
      "n": "1", "t": "L’école et ses élèves",
      "qa": [
        ("Combien d’élèves y a-t-il à l’EFAN&nbsp;?",
         ["L’école comptait 61 élèves en 2024-2025 et 75 à la rentrée 2025-2026.",
          "L’effectif a été multiplié par sept et demi en six ans.",
          "25 % des élèves sont issus de familles civiles.",
          "22 % sont francophones avec au moins un parent étranger."],
         None),
        ("Pourquoi l’EFAN est-elle répartie dans plusieurs établissements&nbsp;?",
         [], "Parce que l’école n’a pas de locaux propres : ses classes sont accueillies au sein "
             "d’établissements publics américains, à Norfolk et à Virginia Beach. L’onglet "
             "«&nbsp;Historique&nbsp;» retrace cette implantation progressive."),
        ("Pourquoi parle-t-on de l’école de Norfolk alors que la plupart des élèves sont à "
         "Virginia Beach&nbsp;?",
         [], "L’école est née à Norfolk en 2011. La majorité des familles militaires résidant "
             "à Virginia Beach, un partenariat y a été conclu en 2022 et les classes s’y sont "
             "progressivement ouvertes. Le nom, lui, est resté celui de la création."),
      ],
    },
    {
      "n": "2", "t": "Les professeurs et les supports",
      "qa": [
        ("Les professeurs de l’EFAN sont-ils des répétiteurs&nbsp;?",
         ["La grande majorité sont des professeurs de l’Éducation nationale : professeures des "
          "écoles, enseignants titulaires du CAPES ou de l’agrégation, enseignante du supérieur.",
          "Les autres sont recrutés localement au vu de leur expertise et de leur expérience.",
          "Comme tout enseignant, ils font cours en s’appropriant des supports pédagogiques, "
          "dont ceux du CNED."],
         "Non."),
        ("Pourquoi l’EFAN utilise-t-elle le CNED&nbsp;?",
         ["Le CNED est l’opérateur public de l’Éducation nationale pour l’enseignement à distance.",
          "Les élèves suivent ainsi le programme de l’Éducation nationale."],
         None),
        ("Pourquoi inscrire mon enfant à l’EFAN si les supports du CNED peuvent être suivis à "
         "la maison&nbsp;?",
         ["Pour bénéficier de professeurs qui savent s’approprier ces supports et proposer "
          "d’autres modalités de travail.",
          "Pour soulager les parents et les enfants.",
          "Pour éviter la rupture avec le système français et faciliter le retour en France.",
          "Pour que les évaluations se fassent en conditions réelles, au sein de la classe.",
          "Pour ne pas travailler seul chez soi, mais dans un groupe et un cadre rassurant."],
         None),
        ("Les élèves doivent-ils suivre tout le programme du CNED, y compris les matières non "
         "traitées à l’EFAN&nbsp;?",
         ["Chaque famille fait comme elle le souhaite.",
          "Les cours de toutes les matières sont disponibles en ligne, ce qui permet de "
          "travailler en autonomie.",
          "Le plus du double cursus : certaines matières peuvent être remplacées par un "
          "équivalent américain — suivre l’espagnol côté américain plutôt qu’en LVA ou LVB "
          "avec le CNED, par exemple."],
         None),
      ],
    },
    {
      "n": "3", "t": "L’homologation",
      "qa": [
        ("L’EFAN est-elle un établissement homologué&nbsp;?",
         [], "Non. Pour être homologué par le ministère de l’Éducation nationale, un "
             "établissement à l’étranger doit disposer de ses propres locaux. À la création de "
             "l’école, le choix a été fait d’intégrer l’EFAN dans des établissements américains, "
             "afin d’offrir aux élèves le bénéfice d’un véritable cursus franco-américain."),
        ("Qu’implique cette non-homologation&nbsp;?",
         [], "Pour les élèves de 3<sup>e</sup>, de première et de terminale, les modalités de "
             "passation du brevet et du baccalauréat diffèrent de celles d’un élève resté en "
             "France. Cela a également un effet sur le dossier Parcoursup. Les onglets "
             "«&nbsp;Baccalauréat&nbsp;», «&nbsp;Brevet&nbsp;» et «&nbsp;Parcoursup&nbsp;» "
             "détaillent ces modalités."),
      ],
    },
    {
      "n": "4", "t": "Le double cursus au quotidien",
      "qa": [
        ("Le double cursus est-il faisable pour tout type d’élève&nbsp;?",
         ["L’EFAN, avec les parents et l’équipe enseignante américaine, prend en compte la "
          "diversité des élèves et leurs besoins particuliers.",
          "Les élèves ont le plus souvent moins de devoirs dans le cursus américain que dans "
          "le système français, quel que soit le niveau.",
          "Les petits effectifs permettent un enseignement personnalisé.",
          "Des élèves en difficulté peuvent gagner à travailler en petit groupe, dans un cadre "
          "rassurant où la vie sociale est facilitée.",
          "Jusqu’en seconde incluse, les emplois du temps cumulés sont comparables à ceux d’un "
          "élève en France.",
          "Les professeurs veillent à respecter le rythme des élèves, notamment par la quantité "
          "de devoirs donnés."],
         None),
        ("L’EFAN propose-t-elle des aménagements pour des besoins particuliers&nbsp;?",
         [], "Oui. L’équipe pédagogique prend en compte la diversité des élèves et leurs besoins "
             "spécifiques. Si nécessaire, l’EFAN propose, avec les parents et les enseignants "
             "américains, des aménagements adaptés."),
        ("Mon enfant sera-t-il vraiment immergé dans la vie américaine&nbsp;?",
         ["Les élèves sont inscrits dans des établissements américains qui ouvrent des classes "
          "pour l’EFAN.",
          "Ils partagent le quotidien d’un élève américain : le school bus, les casiers, la "
          "lunch box.",
          "Ils sont dans des classes américaines et suivent l’emploi du temps américain.",
          "Les cours de l’EFAN ont lieu avant, pendant ou après les cours américains. Selon les "
          "niveaux, ils ne manquent en moyenne qu’une matière américaine par jour."],
         "Oui."),
        ("Les élèves apprennent-ils réellement l’anglais&nbsp;?",
         ["Ils sont immergés dans le cursus américain : dans un établissement américain et dans "
          "une classe américaine.",
          "Ils suivent l’immense majorité de l’emploi du temps américain.",
          "Comme tous les élèves étrangers, ils suivent des cours d’ESL (English as a Second "
          "Language) pour mieux maîtriser la langue."],
         "Oui."),
        ("Les élèves ont-ils le temps de faire du sport ou des activités artistiques&nbsp;?",
         ["Cela dépend de l’emploi du temps de l’enfant et des activités souhaitées.",
          "Dans tous les cas, ils peuvent pratiquer des activités à l’extérieur des "
          "établissements et fréquenter ainsi des Américains en plus de leurs camarades d’école."],
         "Oui, sous réserve des emplois du temps."),
      ],
    },
    {
      "n": "5", "t": "Le lycée, le baccalauréat et Parcoursup",
      "qa": [
        ("Pourquoi l’EFAN propose-t-elle les spécialités mathématiques, physique-chimie et "
         "HGGSP&nbsp;?",
         ["En 2023, les quatre spécialités les plus choisies en France étaient les mathématiques "
          "(43 %), les SES (34 %), la physique-chimie (31,1 %) et la HGGSP (25,7 %).",
          "Les deux doublettes les plus choisies en terminale étaient mathématiques-physique-chimie "
          "(20,4 %) et HGGSP-SES (13,4 %).",
          "La physique-chimie est enseignée dès la 5<sup>e</sup>, alors que les SES ne le sont "
          "qu’à partir de la seconde."],
         None),
        ("Mon enfant veut une spécialité qui n’est pas enseignée à l’EFAN. Est-ce intéressant de "
         "l’y inscrire quand même&nbsp;?",
         ["Il bénéficiera des cours de français, d’histoire-géographie, d’enseignement moral et "
          "civique et de philosophie.",
          "Il conservera les habitudes et les exigences de l’enseignement français.",
          "Il appartiendra à une classe.",
          "En 2024-2025, en première, 40 % des élèves avaient toutes leurs spécialités enseignées "
          "à l’EFAN, 40 % une seule, 20 % aucune.",
          "En terminale, 57 % avaient toutes leurs spécialités enseignées à l’EFAN, 29 % une "
          "seule, 14 % aucune."],
         "Oui, mais votre enfant devra travailler cette spécialité en autonomie, ce qui demande "
         "une organisation et un travail personnel significatifs."),
        ("Peut-on obtenir une réduction des frais si l’on ne choisit pas les spécialités "
         "proposées&nbsp;?",
         [], "Non. Le budget de l’EFAN est contraint : il est cofinancé par les frais de "
             "scolarité versés par les familles et par l’État-major des armées."),
        ("Passer le DNB ou le baccalauréat depuis l’EFAN, est-ce la même chose qu’en France&nbsp;?",
         [], "Non. Les élèves sont inscrits en candidats libres : le contrôle continu ne compte "
             "pas, et chaque matière concernée fait l’objet d’une épreuve en fin d’année, au "
             "lycée Rochambeau à Washington. Les onglets «&nbsp;Baccalauréat&nbsp;» et "
             "«&nbsp;Brevet&nbsp;» détaillent le calendrier et les épreuves."),
        ("Est-ce un désavantage de passer le baccalauréat en candidat individuel&nbsp;?",
         ["Les modalités ressemblent à celles que les parents d’aujourd’hui ont connues : une "
          "épreuve en fin d’année pour chaque matière.",
          "Certains établissements supérieurs français prennent les notes de contrôle continu "
          "avec distance et préfèrent les notes d’épreuves nationales."],
         "Les modalités de passation et le dossier Parcoursup sont en partie différents de ceux "
         "d’un élève scolarisé en France. Mais&nbsp;:"),
        ("Un exemple&nbsp;: la réforme de Sciences Po Paris",
         [], "En décembre 2024, la direction de Sciences Po Paris a annoncé réformer les "
             "modalités de son concours d’entrée pour 2025, afin de pallier les défauts des "
             "modalités du baccalauréat. Selon son directeur, Luis Vassy, les résultats du "
             "contrôle continu sont «&nbsp;survalorisés&nbsp;» par les établissements scolaires ; "
             "et, le report des épreuves écrites en juin privant les établissements supérieurs "
             "d’«&nbsp;une évaluation écrite nationale pour sélectionner les candidats&nbsp;», "
             "ceux-ci le regrettent."),
        ("Parcoursup depuis les États-Unis ou depuis la France, est-ce pareil&nbsp;?",
         [], "Non. L’élève de l’EFAN est inscrit comme «&nbsp;candidat scolarisé à l’étranger&nbsp;» "
             "et les données prises en compte diffèrent. L’onglet «&nbsp;Parcoursup&nbsp;» du site "
             "présente un tableau comparatif détaillé."),
        ("Mes enfants seront-ils préparés aux examens&nbsp;?",
         ["Les élèves passent des épreuves blanches, écrites et orales, dans les matières "
          "enseignées à l’EFAN.",
          "En terminale, les professeurs des spécialités concernées accompagnent la préparation "
          "du Grand oral."],
         "Oui."),
      ],
    },
    {
      "n": "6", "t": "Après l’EFAN, et questions pratiques",
      "qa": [
        ("À quoi sert l’EFAN si les élèves qui rentrent en France sans l’avoir suivie n’ont "
         "aucun souci&nbsp;?",
         [], "L’onglet «&nbsp;Témoignages&nbsp;» rassemble les retours des familles et des anciens "
             "élèves sur l’après-EFAN. Une enquête de fin d’année, menée anonymement auprès de "
             "l’ensemble des parents et des élèves, en donne les résultats."),
        ("Puis-je bénéficier du bus scolaire si je n’habite pas dans la carte scolaire&nbsp;?",
         [], "Non. Seuls les élèves résidant dans le secteur de l’établissement peuvent emprunter "
             "le bus scolaire, et les horaires de l’EFAN ne permettent de le prendre qu’une fois "
             "par jour. L’onglet «&nbsp;Carte scolaire et transport&nbsp;» précise les règles "
             "établissement par établissement."),
      ],
    },
  ],
},
"en": {
  "lang": "en",
  "title": "Frequently asked questions",
  "school": "French American School of Norfolk",
  "sub": "The questions families ask us most often",
  "edition": "2025-2026 edition",
  "site": "efan-norfolk.org",
  "contact": "efan.norfolk@gmail.com · (757) 230-7569",
  "toc_title": "Contents",
  "figures_title": "FASN in figures",
  "figures_note": "Enrolment: “What is FASN?” page. Breakdown: 2024-2025 school year.",
  "chart_title": "How enrolment has grown",
  "chart_note": "From 10 to 75 students in six years — seven and a half times as many.",
  "figures": [
    ("75", "students at the start of 2025-2026"),
    ("×7.5", "growth in enrolment over six years"),
    ("25%", "of students from civilian families"),
    ("22%", "French speakers with at least one foreign parent"),
  ],
  "closing_title": "A question that is not answered here?",
  "closing": ("The FASN office answers families Monday to Friday, 9:00 a.m. to 5:00 p.m. For the "
              "subjects covered in detail on the website — Baccalauréat, Parcoursup, school "
              "district, enrolment — the corresponding pages are the reference."),
  "sources": ("Sources: the FASN FAQ (2025) and the “What is FASN?” page of the website. "
              "The breakdown figures are for the 2024-2025 school year."),
  "sections": [
    {
      "n": "1", "t": "The school and its students",
      "qa": [
        ("How many students are there at FASN?",
         ["The school had 61 students in 2024-2025 and 75 at the start of 2025-2026.",
          "Enrolment has grown seven and a half times over in six years.",
          "25% of students come from civilian families.",
          "22% are French speakers with at least one foreign parent."],
         None),
        ("Why is FASN spread across several schools?",
         [], "Because the school has no premises of its own: its classes are hosted inside "
             "American public schools, in Norfolk and Virginia Beach. The “History” page "
             "retraces how that came about."),
        ("Why is it called the school of Norfolk when most students are in Virginia Beach?",
         [], "The school was founded in Norfolk in 2011. Since most military families live in "
             "Virginia Beach, a partnership was signed there in 2022 and classes opened "
             "gradually. The name has stayed the one it was given at the founding."),
      ],
    },
    {
      "n": "2", "t": "Teachers and teaching materials",
      "qa": [
        ("Are FASN teachers tutors?",
         ["The vast majority are teachers from the French Ministry of National Education: "
          "primary school teachers, teachers holding the CAPES or the Agrégation, a higher "
          "education teacher.",
          "The others are recruited locally for their expertise and experience.",
          "Like any teacher, they teach by making the materials their own, including those "
          "of the CNED."],
         "No."),
        ("Why does FASN use the CNED?",
         ["The CNED is the French Ministry of National Education’s public distance-learning operator.",
          "Students therefore follow the French national curriculum."],
         None),
        ("Why enrol my child at FASN if CNED materials can be followed at home?",
         ["To have teachers who know how to make those materials their own and offer other ways "
          "of working.",
          "To take the load off parents and children.",
          "To avoid a break with the French system and make the return to France easier.",
          "So that assessments are taken under real conditions, within the class.",
          "So that children do not work alone at home, but in a group and a reassuring setting."],
         None),
        ("Do students have to follow the whole CNED curriculum, including subjects not taught "
         "at FASN?",
         ["Each family decides for itself.",
          "Courses for every subject are available online, so students can work independently.",
          "The advantage of the dual curriculum: some subjects can be replaced by an American "
          "equivalent — taking Spanish on the American side rather than as a second or third "
          "language with the CNED, for instance."],
         None),
      ],
    },
    {
      "n": "3", "t": "Accreditation",
      "qa": [
        ("Is FASN an accredited school?",
         [], "No. To be accredited by the French Ministry of National Education, a school abroad "
             "must have premises of its own. When the school was founded, the choice was made to "
             "host FASN inside American schools, so that students would have the benefit of a "
             "genuine Franco-American curriculum."),
        ("What does that mean in practice?",
         [], "For students in 3<sup>e</sup>, Première and Terminale, the way the Brevet and the "
             "Baccalauréat are sat differs from a student who stayed in France. It also affects "
             "the Parcoursup file. The “French Baccalauréat”, “DNB” and “Parcoursup” pages set "
             "out those arrangements."),
      ],
    },
    {
      "n": "4", "t": "The dual curriculum day to day",
      "qa": [
        ("Is the dual curriculum workable for every kind of student?",
         ["FASN, together with parents and the American teaching team, takes account of the "
          "diversity of students and their particular needs.",
          "Students usually have less homework in the American curriculum than in the French "
          "system, at every level.",
          "Small class sizes allow teaching to be personalised.",
          "Students who are struggling can gain from working in a small group, in a reassuring "
          "setting where social life is easier.",
          "Up to and including Seconde, the combined timetables are comparable to those of a "
          "student in France.",
          "Teachers are careful to respect each student’s pace, not least through the amount of "
          "homework set."],
         None),
        ("Does FASN make adjustments for particular needs?",
         [], "Yes. The teaching team takes account of the diversity of students and their "
             "specific needs. Where necessary, FASN works with parents and the American teachers "
             "to put suitable arrangements in place."),
        ("Will my child really be immersed in American life?",
         ["Students are enrolled in American schools, which open classes for FASN.",
          "They share the daily life of an American student: the school bus, lockers, the lunch box.",
          "They are in American classes and follow the American timetable.",
          "FASN lessons take place before, during or after the American school day. Depending on "
          "the level, students miss on average only one American subject a day."],
         "Yes."),
        ("Will my child really learn English?",
         ["They are immersed in the American curriculum: in an American school and in an "
          "American class.",
          "They follow the vast majority of the American timetable.",
          "Like all foreign students, they take ESL (English as a Second Language) classes to "
          "master the language."],
         "Yes."),
        ("Do students have time for sport or the arts?",
         ["It depends on the child’s timetable and on the activities they want to take up.",
          "In any case they can take part in activities outside school, and so meet Americans "
          "beyond their classmates."],
         "Yes, subject to timetables."),
      ],
    },
    {
      "n": "5", "t": "High school, the Baccalauréat and Parcoursup",
      "qa": [
        ("Why does FASN offer mathematics, physics-chemistry and HGGSP as specialisations?",
         ["In 2023, the four most chosen specialisations in France were mathematics (43%), "
          "economics and social sciences (34%), physics-chemistry (31.1%) and HGGSP (25.7%).",
          "The two most chosen pairs in Terminale were mathematics with physics-chemistry (20.4%) "
          "and HGGSP with economics and social sciences (13.4%).",
          "Physics-chemistry is taught from 5<sup>e</sup> onwards, whereas economics and social "
          "sciences only begin in Seconde."],
         None),
        ("My child wants a specialisation that FASN does not teach. Is it still worth enrolling?",
         ["They will have lessons in French, history-geography, moral and civic education and "
          "philosophy.",
          "They will keep the habits and the demands of French schooling.",
          "They will belong to a class.",
          "In 2024-2025, in Première, 40% of students had all their specialisations taught at "
          "FASN, 40% had one, 20% had none.",
          "In Terminale, 57% had all their specialisations taught at FASN, 29% had one, 14% "
          "had none."],
         "Yes, but your child will have to work on that specialisation independently, which "
         "takes significant organisation and personal work."),
        ("Can fees be reduced if we do not take the specialisations offered?",
         [], "No. The FASN budget is tight: it is co-funded by the tuition fees paid by families "
             "and by the French Armed Forces Staff."),
        ("Is sitting the DNB or the Baccalauréat from FASN the same as in France?",
         [], "No. Students are registered as independent candidates: continuous assessment does "
             "not count, and each subject concerned is examined at the end of the year, at the "
             "Lycée Rochambeau in Washington. The “French Baccalauréat” and “DNB” pages set out "
             "the calendar and the papers."),
        ("Is sitting the Baccalauréat as an independent candidate a disadvantage?",
         ["The arrangements resemble those today’s parents knew: one examination at the end of "
          "the year for each subject.",
          "Some French higher education institutions treat continuous assessment marks with "
          "caution and prefer the marks of national examinations."],
         "The way the exams are sat and the Parcoursup file are partly different from those of a "
         "student schooled in France. But:"),
        ("An example: the Sciences Po Paris reform",
         [], "In December 2024, Sciences Po Paris announced that it was reforming its entrance "
             "procedure for 2025, to make up for the shortcomings of the Baccalauréat "
             "arrangements. According to its director, Luis Vassy, continuous assessment results "
             "are “over-valued” by schools; and because the written examinations were moved to "
             "June, higher education institutions regret no longer having “a national written "
             "assessment with which to select candidates”."),
        ("Is Parcoursup from the United States the same as from France?",
         [], "No. A FASN student is registered as a “candidate schooled abroad” and the data "
             "taken into account differ. The “Parcoursup” page sets out a detailed comparison "
             "table."),
        ("Will my children be prepared for the examinations?",
         ["Students sit mock papers, written and oral, in the subjects taught at FASN.",
          "In Terminale, the teachers of the specialisations concerned help prepare the Grand oral."],
         "Yes."),
      ],
    },
    {
      "n": "6", "t": "After FASN, and practical questions",
      "qa": [
        ("What is the point of FASN if students who return to France without it have no trouble?",
         [], "The “Testimonies” page gathers what families and former students say about life "
             "after FASN. An end-of-year survey, run anonymously among all parents and students, "
             "gives the results."),
        ("Can we use the school bus if we do not live within the school district?",
         [], "No. Only students living within the school’s district may use the school bus, and "
             "FASN timetables mean it can only be taken once a day. The “School district and "
             "transportation” page sets out the rules school by school."),
      ],
    },
  ],
},
}
