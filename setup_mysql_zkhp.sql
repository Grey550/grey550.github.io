-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS zkhipani;
CREATE USER IF NOT EXISTS 'zkhp_dev'@'localhost' IDENTIFIED BY 'zkhp_pwd';
GRANT ALL PRIVILEGES ON `zkhipani`.* TO 'zkhp_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'zkhp_dev'@'localhost';
FLUSH PRIVILEGES;
