-- -------------------------------------------------------------
-- TablePlus 5.5.1(510)
--
-- https://tableplus.com/
--
-- Database: cursosenac
-- Generation Time: 2023-10-18 09:06:47.8750
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


CREATE TABLE `categoria` (
  `idcategoria` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;;

CREATE TABLE `cliente` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `id_endereco` int NOT NULL,
  PRIMARY KEY (`idcliente`),
  KEY `fk_cliente_endereco1_idx` (`id_endereco`),
  CONSTRAINT `fk_cliente_endereco1` FOREIGN KEY (`id_endereco`) REFERENCES `endereco` (`idendereco`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;;

CREATE TABLE `endereco` (
  `idendereco` int NOT NULL AUTO_INCREMENT,
  `cep` varchar(45) NOT NULL,
  `uf` varchar(45) NOT NULL,
  `cidade` varchar(45) NOT NULL,
  `bairro` varchar(45) NOT NULL,
  `rua` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  PRIMARY KEY (`idendereco`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;;

CREATE TABLE `produto` (
  `idproduto` int NOT NULL,
  `nome` varchar(45) NOT NULL,
  `quantidade` int NOT NULL,
  `valor` decimal(6,0) NOT NULL,
  `frete` decimal(6,0) NOT NULL,
  `imposto1` decimal(6,0) NOT NULL,
  `imposto2` decimal(6,0) NOT NULL,
  `imposto3` decimal(6,0) NOT NULL,
  `valor_custo` decimal(6,0) NOT NULL,
  `valor_venda` decimal(6,0) NOT NULL,
  `id_fornecedor` int NOT NULL,
  `id_fabricante` int NOT NULL,
  `id_categoria` int NOT NULL,
  `lucro` decimal(6,0) NOT NULL,
  PRIMARY KEY (`idproduto`),
  KEY `fk_produto_cliente_idx` (`id_fornecedor`),
  KEY `fk_produto_cliente1_idx` (`id_fabricante`),
  KEY `fk_produto_categoria1_idx` (`id_categoria`),
  CONSTRAINT `fk_produto_categoria1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `fk_produto_cliente` FOREIGN KEY (`id_fornecedor`) REFERENCES `cliente` (`idcliente`),
  CONSTRAINT `fk_produto_cliente1` FOREIGN KEY (`id_fabricante`) REFERENCES `cliente` (`idcliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;;

CREATE TABLE `vendas` (
  `idvendas` int NOT NULL,
  `quantidade` int NOT NULL,
  `valor` decimal(6,0) NOT NULL,
  `data` datetime NOT NULL,
  `id_produto` int NOT NULL,
  `id_cliente` int NOT NULL,
  PRIMARY KEY (`idvendas`),
  KEY `fk_vendas_produto1_idx` (`id_produto`),
  KEY `fk_vendas_cliente1_idx` (`id_cliente`),
  CONSTRAINT `fk_vendas_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`idcliente`),
  CONSTRAINT `fk_vendas_produto1` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`idproduto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;;

INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(1, 'Eletrônicos'),
(2, 'Roupas'),
(3, 'Alimentos'),
(4, 'Móveis'),
(5, 'Brinquedos'),
(6, 'Esportes'),
(7, 'Automóveis'),
(8, 'Jóias'),
(9, 'Livros'),
(10, 'Saúde e Beleza');

INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`, `id_endereco`) VALUES
(1, 'Cliente 1', 'cliente1@email.com', '111-111-1111', '1', 1),
(2, 'Cliente 2', 'cliente2@email.com', '222-222-2222', '2', 2),
(3, 'Cliente 3', 'cliente3@email.com', '333-333-3333', '3', 3),
(4, 'Cliente 4', 'cliente4@email.com', '444-444-4444', '1', 4),
(5, 'Cliente 5', 'cliente5@email.com', '555-555-5555', '2', 5),
(6, 'Cliente 6', 'cliente6@email.com', '666-666-6666', '3', 6),
(7, 'Cliente 7', 'cliente7@email.com', '777-777-7777', '1', 7),
(8, 'Cliente 8', 'cliente8@email.com', '888-888-8888', '2', 8),
(9, 'Cliente 9', 'cliente9@email.com', '999-999-9999', '3', 9),
(10, 'Cliente 10', 'cliente10@email.com', '101-010-1010', '1', 10);

INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`) VALUES
(1, '11111-111', 'UF1', 'Cidade 1', 'Bairro 1', 'Rua Cliente 1', '123', 'Apto 101'),
(2, '22222-222', 'UF2', 'Cidade 2', 'Bairro 2', 'Rua Cliente 2', '456', 'Casa 202'),
(3, '33333-333', 'UF3', 'Cidade 3', 'Bairro 3', 'Rua Cliente 3', '789', 'Sala 303'),
(4, '44444-444', 'UF4', 'Cidade 4', 'Bairro 4', 'Rua Cliente 4', '1011', 'Bloco A'),
(5, '55555-555', 'UF5', 'Cidade 5', 'Bairro 5', 'Rua Cliente 5', '1213', 'Casa 505'),
(6, '66666-666', 'UF6', 'Cidade 6', 'Bairro 6', 'Rua Cliente 6', '1415', 'Lote 606'),
(7, '77777-777', 'UF7', 'Cidade 7', 'Bairro 7', 'Rua Cliente 7', '1617', 'Andar 707'),
(8, '88888-888', 'UF8', 'Cidade 8', 'Bairro 8', 'Rua Cliente 8', '1819', 'Loja 808'),
(9, '99999-999', 'UF9', 'Cidade 9', 'Bairro 9', 'Rua Cliente 9', '2021', 'Torre 909'),
(10, '10101-010', 'UF10', 'Cidade 10', 'Bairro 10', 'Rua Cliente 10', '2224', 'Apto 1010');

INSERT INTO `produto` (`idproduto`, `nome`, `quantidade`, `valor`, `frete`, `imposto1`, `imposto2`, `imposto3`, `valor_custo`, `valor_venda`, `id_fornecedor`, `id_fabricante`, `id_categoria`, `lucro`) VALUES
(1, 'Produto 1', 100, 500, 50, 20, 10, 30, 480, 600, 2, 3, 3, 120),
(2, 'Produto 2', 75, 400, 40, 15, 8, 25, 380, 500, 5, 6, 1, 120),
(3, 'Produto 3', 90, 600, 60, 25, 12, 35, 550, 700, 8, 9, 2, 150),
(4, 'Produto 4', 120, 700, 70, 30, 15, 40, 660, 800, 2, 3, 3, 140),
(5, 'Produto 5', 80, 450, 45, 18, 9, 32, 430, 550, 5, 6, 1, 120),
(6, 'Produto 6', 60, 350, 35, 14, 7, 22, 330, 450, 8, 9, 2, 120),
(7, 'Produto 7', 110, 550, 55, 22, 11, 28, 530, 650, 2, 3, 3, 120),
(8, 'Produto 8', 45, 300, 30, 12, 6, 20, 280, 400, 5, 6, 1, 120),
(9, 'Produto 9', 95, 650, 65, 27, 13, 38, 630, 750, 8, 9, 2, 120),
(10, 'Produto 10', 130, 750, 75, 32, 16, 42, 720, 800, 5, 3, 3, 150);



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;