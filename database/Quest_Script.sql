-- Désactivation des contraintes pour permettre le nettoyage (DROP)
PRAGMA foreign_keys = OFF;

-- -----------------------------------------------------
-- Table `themes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `themes`;

CREATE TABLE IF NOT EXISTS `themes` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NULL,
  CONSTRAINT `name_UNIQUE` UNIQUE (`name`)
);

-- -----------------------------------------------------
-- Table `questions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `questions`;

CREATE TABLE IF NOT EXISTS `questions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `statement` TEXT NULL,
  `theoretical_contribution` TEXT NULL,
  `difficulty` TEXT NULL,
  `themes_id` INTEGER NOT NULL,
  FOREIGN KEY (`themes_id`) REFERENCES `themes` (`id`) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table `users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `users`;

CREATE TABLE IF NOT EXISTS `users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `pseudo` TEXT NULL,
  `creation_date` TEXT NULL,
  CONSTRAINT `pseudo_UNIQUE` UNIQUE (`pseudo`)
);

-- -----------------------------------------------------
-- Table `answers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `answers`;

CREATE TABLE IF NOT EXISTS `answers` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `response_text` TEXT NULL,
  `image_path` TEXT NULL, -- Colonne ajoutée pour les images (ex: drapeaux)
  `is_correct` INTEGER NULL, -- 1 pour vrai, 0 pour faux
  `questions_id` INTEGER NOT NULL,
  FOREIGN KEY (`questions_id`) REFERENCES `questions` (`id`) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table `games`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `games`;

CREATE TABLE IF NOT EXISTS `games` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `final_score` INTEGER NULL,
  `date_time` TEXT NULL,
  `total_time` INTEGER NULL,
  `themes_id` INTEGER NOT NULL,
  `users_id` INTEGER NOT NULL,
  FOREIGN KEY (`themes_id`) REFERENCES `themes` (`id`) 
    ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Réactivation des contraintes de clés étrangères
PRAGMA foreign_keys = ON;