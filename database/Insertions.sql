-- 1. Insertion des Thèmes
INSERT INTO themes (name) VALUES
('Animaux'),
('Drapeaux'),
('Informatique'),
('Géographie'),
('Histoire'),
('Sciences');


-- 2. Insertion des Questions 
INSERT INTO questions (statement,theoretical_contribution,difficulty,themes_id)
VALUES
-- Animaux
('A quoi ressemble un chien ?','Le chien est un canidé domestiqué caractérisé par quatre pattes.','facile',1),
('A quoi ressemble un chat?','Le chat est un petit félin connu pour ses moustaches.','facile',1),
('A quoi ressemble un ours ?','C''est un animal robuste et imposant, couvert d''une fourrure épaisse, qui se déplace en posant toute la plante de ses pattes au sol.','facile',1),
('A quoi ressemble un lapin ?','C''est un petit animal rapide, célèbre pour ses très longues oreilles qui captent le moindre bruit et ses pattes arrière musclées pour bondir.','facile',1),
('A quoi ressemble un poisson?','C''est un animal qui vit dans l''eau, utilisant ses nageoires pour se diriger et ses branchies pour respirer sans jamais avoir besoin d''air.','facile',1),
('Lequelle de ces animaux vol?','','moyen',1),
('Lequelle de ces animaux est un félin ?','','moyen',1),
('Lequelle de ces animaux pond des oeufs?','','moyen',1),
('Lequelle de ces animaux est nocturne ?','','moyen',1),
('Lequelle est un tigre?','','moyen',1), -- Silhouette
('Quel animal vertébré possède la plus grande longévité connue ?','','difficile',1),
('Quel animal possède trois cœurs, le sang bleu et un cerveau en forme de donut ? ','','difficile',1),
('Quel est l''animal le plus venimeux au monde pour l''être humain ? ','','difficile',1),
('Quel petit mammifère est le seul à être eusocial (vivant en colonie avec une reine, comme les abeilles) ?','','difficile',1),
('Quel oiseau est capable de dormir tout en volant lors de ses migrations transocéaniques ? ','','difficile',1),

INSERT INTO questions (statement,theoretical_contribution,difficulty,themes_id)
VALUES
-- Drapeaux
('Quel est le drapeau de l''Espagne ?','','facile',2),
('Quel pays possède un drapeau avec une feuille d''érable rouge ?', 'La feuille d''érable est le symbole national du Canada depuis le 18ème siècle.', 'facile', 2),
('Quel pays a un drapeau composé d''un cercle rouge sur fond blanc ?', 'Le disque rouge représente le soleil levant.', 'facile', 2),
('Quel pays a ce drapeau : Bleu, Blanc, Rouge ?', 'Le drapeau tricolore est né durant la Révolution française.', 'facile', 2),
('Quel pays a une croix blanche sur son drapeau ?','','facile', 2),
('Quel est le drapeau du Mozambique ?','','moyen', 2),
('Quel est le drapeau du Malawi ?','', 'moyen', 2),
('Quel est le drapeau du Sénégal ?','','moyen', 2),
('Quel est le drapeau du Tchad ? ','', 'moyen', 2),
('Quel est le drapeau de l''Indonésie ?','','moyen', 2),
('Quel est le drapeau de Nauru ?','','difficile',2),
('Quel est le drapeau de l''Eswatini ?','','difficile',2),
('Quel est le drapeau du Sri Lanka ?','','difficile',2),
('Quel est le drapeau de Kiribati?','','difficile',2),
('Quel est le drapeau des Fidji ?','','difficile',2);

INSERT INTO questions (statement,theoretical_contribution,difficulty,themes_id)
VALUES
-- Informatique
('Quel est le périphérique qui permet d''écrire ?','','facile',3),
('Qu''est ce que c''est qu''un écran ?','','facile',3),
('Quel périphérique est une souris ?','','facile',3), --Penser a mettre un animal souris
('Quel est le logo Windows ?','','facile',3),
('Quel est le logo de Teams ?','','facile',3),
('Quel type de disque dur n''utilise aucune pièce mécanique et stocke les données sur de la mémoire flash ?','','moyen',3),
('Quel composant est souvent appelé le "cerveau" de l''ordinateur, car il exécute les instructions des programmes ?','','moyen',3),
('Quel est le logo actuel du navigateur de Windows ?','','moyen',3),
('Quel est le logo de Python ?','','moyen',3),
('Quel est le  logo d''HTML ?','','moyen',3),
('Qui est considérée comme la toute première personne à avoir écrit un programme informatique au 19ème siècle ?','','difficile',3),
('Lequelle de ces composants est un router ?','','difficile',3),
('Lequelle de ces cables est de l''USB C ?','','difficile',3),
('Lequelle de ces consoles est la plus vieille','','difficile',3),
('Quel code est écrit en C# ','','difficile',3);


-- 3 Insertion des réponses
INSERT INTO answers (response_text,image_path,is_correct,questions_id)
VALUES
-- Animal
('Tortue','assets/images/animals/tortue.jpg',0,1),
('Chien','assets/images/animals/chien.jpg',1,1),
('Chat','assets/images/animals/chat.jpg',0,1),
('Pigeon','assets/images/animals/pigeon.jpg',0,1),
('Chat','assets/images/animals/chat.jpg',1,2),
('Cheval','assets/images/animals/cheval.jpg',0,2),
('Souris','assets/images/animals/souris.jpg',0,2),
('Lapin','assets/images/animals/lapin.jpg',0,2),
('Rat','assets/images/animals/rat.jpg',0,3),
('Aigle','assets/images/animals/aigle.jpg',0,3),
('Renard','assets/images/animals/renard.jpg',0,3),
('Ours','assets/images/animals/ours.jpg',1,3),
('Poisson','assets/images/animals/poisson.jpg',0,4),
('Corbeau','assets/images/animals/corbeau.jpg',0,4),
('Lapin','assets/images/animals/lapin.jpg',1,4),
('Cheval','assets/images/animals/cheval.jpg',0,4),
('Dauphin','assets/images/animals/dauphin.jpg',0,5),
('Poisson','assets/images/animals/poisson.jpg',1,5),
('Chien','assets/images/animals/chien.jpg',0,5),
('Requin','assets/images/animals/requin.jpg',0,5),
('Aigle','assets/images/animals/aigle.jpg',1,6),
('Ecureuil volant','assets/images/animals/ecureuilvolant.jpg',0,6),
('Grenouille','assets/images/animals/grenouille.jpg',0,6),
('Poisson volants','assets/images/animals/poissonvolant.jpg',0,6),
('Loup','assets/images/animals/loup.jpg',0,7),
('Lion','assets/images/animals/lion.jpg',1,7),
('Ours','assets/images/animals/ours.jpg',0,7),
('Hyène','assets/images/animals/hyène.jpg',0,7),
('Chien','assets/images/animals/chien.jpg',0,8),
('Ornithorynque','assets/images/animals/ornithorynque.jpg',1,8),
('Lapin','assets/images/animals/lapin.jpg',0,8),
('Chat','assets/images/animals/chat.jpg',0,8),
('Aigle','assets/images/animals/aigle.jpg',0,9),
('Chouette','assets/images/animals/chouette.jpg',1,9),
('Canard','assets/images/animals/canard.jpg',0,9),
('Moineau','assets/images/animals/moineau.jpg',0,9),
('Léopard','assets/images/animals/léopard_silh.jpg',0,10),
('Tigre','assets/images/animals/tigre_silh.jpg',1,10),
('Lion','assets/images/animals/lion_silh.jpg',0,10),
('Panthère','assets/images/animals/panthere_silh.jpg',0,10),
('Tortue géante','assets/images/animals/tortue.jpg',0,11),
('Requin du Groenland','assets/images/animals/requin_groenland.jpg',1,11),
('Baleine bleue','assets/images/animals/baleine.jpg',0,11),
('Éléphant','assets/images/animals/elephant.jpg',0,11),
('Méduse','assets/images/animals/meduse.jpg',0,12),
('Poulpe','assets/images/animals/poulpe.jpg',1,12),
('Requin','assets/images/animals/requin.jpg',0,12),
('Etoile de mer','assets/images/animals/etoile_mer.jpg',0,12),
('Cobra royal','assets/images/animals/cobra.jpg',0,13),
('Cubo-méduse','assets/images/animals/cubomeduse.jpg',1,13),
('Scorpion','assets/images/animals/scorpion.jpg',0,13),
('Araignée banane','assets/images/animals/araignee.jpg',0,13),
('Suricate','assets/images/animals/suricate.jpg',0,14),
('Rat-taupe nu','assets/images/animals/rat_taupe.jpg',1,14),
('Castor','assets/images/animals/castor.jpg',0,14),
('Musaraigne','assets/images/animals/musaraigne.jpg',0,14),
('Albatros','assets/images/animals/albatros.jpg',0,15),
('Frégate superbe','assets/images/animals/fregate.jpg',1,15),
('Hirondelle','assets/images/animals/hirondelle.jpg',0,15),
('Martinet','assets/images/animals/martinet.jpg',0,15);



