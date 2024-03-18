CREATE TABLE `account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `account` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE audit_log (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(255),
    timestamp DATETIME,
    ip_address VARCHAR(50)
);

INSERT INTO account (id ,name, account, city, state, location, balance)
VALUES ('Andres', '25148426798', 'Guayaquil', 'Guayas', 'Urdesa', 226.38);