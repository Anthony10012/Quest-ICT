-- -----------------------------------------------------
-- SQLite Schema Quest
-- -----------------------------------------------------
PRAGMA foreign_keys = ON;

-- Table themes
DROP TABLE IF EXISTS themes;
CREATE TABLE IF NOT EXISTS themes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

-- Table questions
DROP TABLE IF EXISTS questions;
CREATE TABLE IF NOT EXISTS questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  statement TEXT NOT NULL UNIQUE,
  theoretical_contribution TEXT,
  difficulty TEXT NOT NULL,
  themes_id INTEGER NOT NULL,
  FOREIGN KEY (themes_id) REFERENCES themes (id)
);

-- Table users
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pseudo TEXT NOT NULL UNIQUE,
  creation_date DATETIME NOT NULL
);

-- Table answers
DROP TABLE IF EXISTS answers;
CREATE TABLE IF NOT EXISTS answers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  response_text TEXT NOT NULL,
  image_path TEXT NOT NULL,
  is_correct INTEGER NOT NULL, -- SQLite utilise 0/1 pour les booléens
  questions_id INTEGER NOT NULL,
  FOREIGN KEY (questions_id) REFERENCES questions (id)
);

-- Table games
DROP TABLE IF EXISTS games;
CREATE TABLE IF NOT EXISTS games (
  id INTEGER PRIMARY KEY AUTOINCREMENT,s
  final_score INTEGER NOT NULL,
  date_time DATETIME NOT NULL,
  total_time INTEGER NOT NULL,
  themes_id INTEGER NOT NULL,
  users_id INTEGER NOT NULL,
  FOREIGN KEY (themes_id) REFERENCES themes (id),
  FOREIGN KEY (users_id) REFERENCES users (id)
);