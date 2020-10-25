CREATE DATABASE  IF NOT EXISTS `wwadri_coel` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `wwadri_coel`;
-- MySQL dump 10.13  Distrib 5.7.30-ndb-7.6.14, for Linux (x86_64)
--
-- Host: localhost    Database: wwadri_coel
-- ------------------------------------------------------
-- Server version	5.7.30-ndb-7.6.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alimentacao`
--

DROP TABLE IF EXISTS `alimentacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alimentacao` (
  `id_alimentacao` int(11) NOT NULL AUTO_INCREMENT,
  `alimentacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_alimentacao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `aplicacao`
--

DROP TABLE IF EXISTS `aplicacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aplicacao` (
  `id_aplicacao` int(11) NOT NULL AUTO_INCREMENT,
  `aplicacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_aplicacao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `aplicacao_navegacao`
--

DROP TABLE IF EXISTS `aplicacao_navegacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aplicacao_navegacao` (
  `id_aplicacao_navegacao` int(11) NOT NULL AUTO_INCREMENT,
  `aplicacao_navegacao` varchar(100) NOT NULL,
  PRIMARY KEY (`id_aplicacao_navegacao`),
  UNIQUE KEY `UK_qr3fwvqaw3juiaq7qwp70oafb` (`aplicacao_navegacao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `categoria_venda`
--

DROP TABLE IF EXISTS `categoria_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoria_venda` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_venda` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `certificado`
--

DROP TABLE IF EXISTS `certificado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `certificado` (
  `id_certificado` int(11) NOT NULL AUTO_INCREMENT,
  `certificado` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_certificado`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `concorrente`
--

DROP TABLE IF EXISTS `concorrente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concorrente` (
  `id_concorrente` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_concorrente` varchar(100) DEFAULT NULL,
  `descricao_concorrente` varchar(2000) DEFAULT NULL,
  `empresa_concorrente` varchar(100) DEFAULT NULL,
  `observacao_concorrente` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_concorrente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `foto`
--

DROP TABLE IF EXISTS `foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `foto` (
  `id_foto` int(11) NOT NULL AUTO_INCREMENT,
  `foto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_foto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `funcao`
--

DROP TABLE IF EXISTS `funcao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funcao` (
  `id_funcao` int(11) NOT NULL AUTO_INCREMENT,
  `funcao` varchar(100) NOT NULL,
  PRIMARY KEY (`id_funcao`),
  UNIQUE KEY `UK_fqw2r71hd4t1d1wif4lxtorqy` (`funcao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `manual`
--

DROP TABLE IF EXISTS `manual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manual` (
  `id_manual` int(11) NOT NULL AUTO_INCREMENT,
  `link_manua` varchar(2000) DEFAULT NULL,
  `manual_idioma` varchar(100) DEFAULT NULL,
  `manual_tipo` varchar(100) DEFAULT NULL,
  `nome_manual` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_manual`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `modelo_antigo`
--

DROP TABLE IF EXISTS `modelo_antigo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `modelo_antigo` (
  `id_modelo_antigo` int(11) NOT NULL AUTO_INCREMENT,
  `descricao_modelo_antigo` varchar(2000) DEFAULT NULL,
  `modelo_antigo` varchar(100) DEFAULT NULL,
  `observacao_modelo_antigo` varchar(1000) DEFAULT NULL,
  `id_foto` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_modelo_antigo`),
  KEY `FKqwg9sxgijxa15j5d5yac8rlar` (`id_foto`),
  CONSTRAINT `FKqwg9sxgijxa15j5d5yac8rlar` FOREIGN KEY (`id_foto`) REFERENCES `foto` (`id_foto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `montagem`
--

DROP TABLE IF EXISTS `montagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `montagem` (
  `id_montagem` int(11) NOT NULL AUTO_INCREMENT,
  `montagem` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_montagem`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produto` (
  `id_produto` int(11) NOT NULL AUTO_INCREMENT,
  `descricao_completa` varchar(2000) DEFAULT NULL,
  `descricao_reduzida` varchar(300) DEFAULT NULL,
  `link_codigo_pedido` int(11) DEFAULT NULL,
  `link_dimensoes` varchar(2000) DEFAULT NULL,
  `link_esquema_ligacao` varchar(2000) DEFAULT NULL,
  `link_exemplo_ligacao` varchar(2000) DEFAULT NULL,
  `link_site` varchar(2000) DEFAULT NULL,
  `link_tabela_alarmes` varchar(2000) DEFAULT NULL,
  `link_tabela_parametros` varchar(2000) DEFAULT NULL,
  `modelo` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `id_alimentacao` int(11) NOT NULL,
  `id_aplicacao` int(11) NOT NULL,
  `id_aplicacao_navegacao` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `id_categoria_venda` int(11) NOT NULL,
  `id_certificado` int(11) NOT NULL,
  `id_concorrente` int(11) NOT NULL,
  `id_foto` int(11) NOT NULL,
  `id_funcao` int(11) NOT NULL,
  `id_manual` int(11) NOT NULL,
  `id_modelo_antigo` int(11) NOT NULL,
  `id_montagem` int(11) NOT NULL,
  PRIMARY KEY (`id_produto`),
  KEY `FKb1rsgsyjwtwcufhpfrqn8nteg` (`id_alimentacao`),
  KEY `FKpl5txhxj7gy66eisgbgn7vnya` (`id_aplicacao`),
  KEY `FKjt011cnj9xmt7kioxkxpdevxt` (`id_aplicacao_navegacao`),
  KEY `FKbb0k43mtsufg8bfhq0gyaxhhm` (`id_categoria`),
  KEY `FKccd3ungvvsoy6ugkkaknpxkps` (`id_categoria_venda`),
  KEY `FKprac72ux9rtam198aqix2yytr` (`id_certificado`),
  KEY `FKjpt0wj3x2io2hgnbhw5m6wi9p` (`id_concorrente`),
  KEY `FK8b7y1vbdun9f9j1wtll4bpvmd` (`id_foto`),
  KEY `FK5cefqiihe7kirk4vrg19t1p7b` (`id_funcao`),
  KEY `FKp4w8lwmtd6snk9f85iqoq1552` (`id_manual`),
  KEY `FKgx5wrlhjvutwf1gn6e988kpf` (`id_modelo_antigo`),
  KEY `FKkfxjgq7nxo4rtow4f6fvta7n0` (`id_montagem`),
  CONSTRAINT `FK5cefqiihe7kirk4vrg19t1p7b` FOREIGN KEY (`id_funcao`) REFERENCES `funcao` (`id_funcao`),
  CONSTRAINT `FK8b7y1vbdun9f9j1wtll4bpvmd` FOREIGN KEY (`id_foto`) REFERENCES `foto` (`id_foto`),
  CONSTRAINT `FKb1rsgsyjwtwcufhpfrqn8nteg` FOREIGN KEY (`id_alimentacao`) REFERENCES `alimentacao` (`id_alimentacao`),
  CONSTRAINT `FKbb0k43mtsufg8bfhq0gyaxhhm` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`),
  CONSTRAINT `FKccd3ungvvsoy6ugkkaknpxkps` FOREIGN KEY (`id_categoria_venda`) REFERENCES `categoria_venda` (`id_categoria`),
  CONSTRAINT `FKgx5wrlhjvutwf1gn6e988kpf` FOREIGN KEY (`id_modelo_antigo`) REFERENCES `modelo_antigo` (`id_modelo_antigo`),
  CONSTRAINT `FKjpt0wj3x2io2hgnbhw5m6wi9p` FOREIGN KEY (`id_concorrente`) REFERENCES `concorrente` (`id_concorrente`),
  CONSTRAINT `FKjt011cnj9xmt7kioxkxpdevxt` FOREIGN KEY (`id_aplicacao_navegacao`) REFERENCES `aplicacao_navegacao` (`id_aplicacao_navegacao`),
  CONSTRAINT `FKkfxjgq7nxo4rtow4f6fvta7n0` FOREIGN KEY (`id_montagem`) REFERENCES `montagem` (`id_montagem`),
  CONSTRAINT `FKp4w8lwmtd6snk9f85iqoq1552` FOREIGN KEY (`id_manual`) REFERENCES `manual` (`id_manual`),
  CONSTRAINT `FKpl5txhxj7gy66eisgbgn7vnya` FOREIGN KEY (`id_aplicacao`) REFERENCES `aplicacao` (`id_aplicacao`),
  CONSTRAINT `FKprac72ux9rtam198aqix2yytr` FOREIGN KEY (`id_certificado`) REFERENCES `certificado` (`id_certificado`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(20) DEFAULT NULL,
  `senha` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-18 11:03:24
