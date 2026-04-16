DROP DATABASE IF EXISTS wayne_db;
CREATE DATABASE wayne_db;
USE wayne_db;

CREATE TABLE usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL,
nome VARCHAR(100) NOT NULL,
role VARCHAR(50) NOT NULL
);

CREATE TABLE recursos (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(255) NOT NULL,
tipo VARCHAR(100),
status VARCHAR(50),
quantidade INT
);

INSERT INTO usuarios (username, password, nome, role) VALUES
('admin', '1234', 'Bruce Wayne', 'administrador'),
('gerente', '1234', 'Lucius Fox', 'gerente'),
('funcionario', '1234', 'Alfred Pennyworth', 'funcionario');

INSERT INTO recursos (nome, tipo, status, quantidade) VALUES
('Batmobile X-7', 'Veículo', 'Ativo', 1),
('Drone de Vigilância Mark IV', 'Equipamento', 'Ativo', 12),
('Sistema de Câmeras Infravermelhas', 'Dispositivo de Segurança', 'Ativo', 48),
('Armadura Tática Protótipo', 'Equipamento', 'Em Manutenção', 3);

SELECT * FROM usuarios;

SELECT * FROM usuarios
WHERE username = 'admin' AND password = '1234';

SELECT * FROM usuarios
WHERE TRIM(username) = 'admin' AND TRIM(password) = '1234';

SELECT * FROM recursos;
SELECT * FROM usuarios 
WHERE username = 'admin';
