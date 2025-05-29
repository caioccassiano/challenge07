CREATE TABLE IF NOT EXISTS users (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  username   TEXT    NOT NULL UNIQUE,
  password   TEXT    NOT NULL      -- aqui você armazena o hash
);

CREATE TABLE IF NOT EXISTS orders (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id     INTEGER NOT NULL,
  description TEXT    NOT NULL,
  created_at  DATETIME DEFAULT (datetime('now','localtime')),
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);


