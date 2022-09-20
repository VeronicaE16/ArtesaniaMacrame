-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: proyartmacrame
-- ------------------------------------------------------
-- Server version	5.7.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add backup',7,'add_backup'),(26,'Can change backup',7,'change_backup'),(27,'Can delete backup',7,'delete_backup'),(28,'Can view backup',7,'view_backup'),(29,'Can add cliente',8,'add_cliente'),(30,'Can change cliente',8,'change_cliente'),(31,'Can delete cliente',8,'delete_cliente'),(32,'Can view cliente',8,'view_cliente'),(33,'Can add proveedor',9,'add_proveedor'),(34,'Can change proveedor',9,'change_proveedor'),(35,'Can delete proveedor',9,'delete_proveedor'),(36,'Can view proveedor',9,'view_proveedor'),(37,'Can add usuario',10,'add_usuario'),(38,'Can change usuario',10,'change_usuario'),(39,'Can delete usuario',10,'delete_usuario'),(40,'Can view usuario',10,'view_usuario'),(41,'Can add compra',11,'add_compra'),(42,'Can change compra',11,'change_compra'),(43,'Can delete compra',11,'delete_compra'),(44,'Can view compra',11,'view_compra'),(45,'Can add venta',12,'add_venta'),(46,'Can change venta',12,'change_venta'),(47,'Can delete venta',12,'delete_venta'),(48,'Can view venta',12,'view_venta'),(49,'Can add detalle venta',13,'add_detalleventa'),(50,'Can change detalle venta',13,'change_detalleventa'),(51,'Can delete detalle venta',13,'delete_detalleventa'),(52,'Can view detalle venta',13,'view_detalleventa'),(53,'Can add detalle compra',14,'add_detallecompra'),(54,'Can change detalle compra',14,'change_detallecompra'),(55,'Can delete detalle compra',14,'delete_detallecompra'),(56,'Can view detalle compra',14,'view_detallecompra'),(57,'Can add material',15,'add_material'),(58,'Can change material',15,'change_material'),(59,'Can delete material',15,'delete_material'),(60,'Can view material',15,'view_material'),(61,'Can add producto',16,'add_producto'),(62,'Can change producto',16,'change_producto'),(63,'Can delete producto',16,'delete_producto'),(64,'Can view producto',16,'view_producto'),(65,'Can add produccion',17,'add_produccion'),(66,'Can change produccion',17,'change_produccion'),(67,'Can delete produccion',17,'delete_produccion'),(68,'Can view produccion',17,'view_produccion'),(69,'Can add post',18,'add_post'),(70,'Can change post',18,'change_post'),(71,'Can delete post',18,'delete_post'),(72,'Can view post',18,'view_post');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$z8WEwvOot4qZBbU7b7I6O5$LKGL7UOYsAxWwW+ujeUZUtlEnYpy4ULgXWEjWpWWYGs=','2022-09-14 15:47:54.300992',1,'admin','','','',1,1,'2022-09-09 19:38:13.721660'),(2,'pbkdf2_sha256$320000$RJWZa0ZyLu9rJHb0wkdM1e$xRj0P3t7z5QkO091QwTcff20wzpNwnSwEWqaI6t527U=','2022-09-13 16:49:27.281603',0,'daniela','','','everonica385@gmail.com',0,1,'2022-09-13 13:44:14.061086');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contabilidad_compra`
--

DROP TABLE IF EXISTS `contabilidad_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contabilidad_compra` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `neto_pagar` int(11) NOT NULL,
  `proveedor_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contabilidad_compra_proveedor_id_360f176f_fk_persona_p` (`proveedor_id`),
  CONSTRAINT `contabilidad_compra_proveedor_id_360f176f_fk_persona_p` FOREIGN KEY (`proveedor_id`) REFERENCES `persona_proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contabilidad_compra`
--

LOCK TABLES `contabilidad_compra` WRITE;
/*!40000 ALTER TABLE `contabilidad_compra` DISABLE KEYS */;
INSERT INTO `contabilidad_compra` VALUES (2,'2022-09-12 20:20:26.727418','Abierta',10000,1),(3,'2022-09-13 12:37:44.853094','Cerrada',10000,1),(4,'2022-09-13 12:49:19.690206','Abierta',380000,1),(5,'2022-09-13 16:49:51.686771','Abierta',180000,1),(6,'2022-09-13 16:52:17.845836','Abierta',0,1),(7,'2022-09-13 16:53:33.384075','Cerrada',180000,1),(8,'2022-09-13 19:31:13.758913','Abierta',290000,1),(9,'2022-09-13 19:35:58.032848','Abierta',10000,1),(10,'2022-09-13 19:42:39.854567','Abierta',10000,1),(11,'2022-09-13 20:06:50.955569','Anulada',15000,1),(12,'2022-09-13 20:15:24.929457','Cerrada',15000,1),(13,'2022-09-13 20:15:55.457505','Cerrada',45000,1),(14,'2022-09-13 20:19:23.272911','Cerrada',35000,1),(15,'2022-09-13 20:20:19.818094','Cerrada',105000,1);
/*!40000 ALTER TABLE `contabilidad_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contabilidad_detallecompra`
--

DROP TABLE IF EXISTS `contabilidad_detallecompra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contabilidad_detallecompra` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cantidad_detalle` int(11) NOT NULL,
  `metodo` varchar(25) NOT NULL,
  `total` int(11) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `compra_id` bigint(20) DEFAULT NULL,
  `material_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contabilidad_detalle_compra_id_4040c7e5_fk_contabili` (`compra_id`),
  KEY `contabilidad_detalle_material_id_c405bfc3_fk_control_m` (`material_id`),
  CONSTRAINT `contabilidad_detalle_compra_id_4040c7e5_fk_contabili` FOREIGN KEY (`compra_id`) REFERENCES `contabilidad_compra` (`id`),
  CONSTRAINT `contabilidad_detalle_material_id_c405bfc3_fk_control_m` FOREIGN KEY (`material_id`) REFERENCES `control_material` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contabilidad_detallecompra`
--

LOCK TABLES `contabilidad_detallecompra` WRITE;
/*!40000 ALTER TABLE `contabilidad_detallecompra` DISABLE KEYS */;
INSERT INTO `contabilidad_detallecompra` VALUES (4,2,'Efectivo',10000,'Abierta',2,1),(6,67,'Efectivo',335000,'Abierta',4,1),(7,3,'Efectivo',45000,'Abierta',4,2),(8,12,'Efectivo',180000,'Abierta',5,2),(9,12,'Efectivo',180000,'Abierta',7,2),(10,2,'Efectivo',10000,'Abierta',3,1),(11,18,'Efectivo',270000,'Abierta',8,2),(12,4,'Efectivo',20000,'Abierta',8,1),(13,2,'Efectivo',10000,'Abierta',9,1),(14,2,'Efectivo',10000,'Abierta',10,1),(15,1,'Efectivo',15000,'Abierta',11,2),(16,1,'Efectivo',15000,'Abierta',12,2),(17,9,'Efectivo',45000,'Abierta',13,1),(18,7,'Efectivo',35000,'Abierta',14,1),(19,7,'Efectivo',105000,'Abierta',15,2);
/*!40000 ALTER TABLE `contabilidad_detallecompra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contabilidad_detalleventa`
--

DROP TABLE IF EXISTS `contabilidad_detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contabilidad_detalleventa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cantidad_detalle` int(11) NOT NULL,
  `metodo` varchar(25) NOT NULL,
  `total` int(11) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `producto_id` bigint(20) DEFAULT NULL,
  `venta_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contabilidad_detalle_producto_id_935edb40_fk_control_p` (`producto_id`),
  KEY `contabilidad_detalle_venta_id_86b7ef22_fk_contabili` (`venta_id`),
  CONSTRAINT `contabilidad_detalle_producto_id_935edb40_fk_control_p` FOREIGN KEY (`producto_id`) REFERENCES `control_producto` (`id`),
  CONSTRAINT `contabilidad_detalle_venta_id_86b7ef22_fk_contabili` FOREIGN KEY (`venta_id`) REFERENCES `contabilidad_venta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contabilidad_detalleventa`
--

LOCK TABLES `contabilidad_detalleventa` WRITE;
/*!40000 ALTER TABLE `contabilidad_detalleventa` DISABLE KEYS */;
INSERT INTO `contabilidad_detalleventa` VALUES (5,4,'Efectivo',80000,'Abierta',1,5),(6,1,'Efectivo',20000,'Abierta',1,6),(7,2,'Efectivo',40000,'Abierta',1,7),(9,2,'Efectivo',40000,'Abierta',1,8),(10,1,'Efectivo',20000,'Abierta',1,9);
/*!40000 ALTER TABLE `contabilidad_detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contabilidad_venta`
--

DROP TABLE IF EXISTS `contabilidad_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contabilidad_venta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `neto_pagar` int(11) NOT NULL,
  `estado` varchar(7) NOT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  `rol_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contabilidad_venta_cliente_id_ee1228d9_fk_persona_cliente_id` (`cliente_id`),
  KEY `contabilidad_venta_rol_id_1f17603a_fk_persona_usuario_id` (`rol_id`),
  CONSTRAINT `contabilidad_venta_cliente_id_ee1228d9_fk_persona_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `persona_cliente` (`id`),
  CONSTRAINT `contabilidad_venta_rol_id_1f17603a_fk_persona_usuario_id` FOREIGN KEY (`rol_id`) REFERENCES `persona_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contabilidad_venta`
--

LOCK TABLES `contabilidad_venta` WRITE;
/*!40000 ALTER TABLE `contabilidad_venta` DISABLE KEYS */;
INSERT INTO `contabilidad_venta` VALUES (3,'2022-09-13',100000,'Abierta',1,1),(4,'2022-09-13',160000,'Cerrada',1,1),(5,'2022-09-13',80000,'Cerrada',1,1),(6,'2022-09-13',20000,'Cerrada',1,1),(7,'2022-09-13',40000,'Abierta',1,1),(8,'2022-09-13',40000,'Abierta',1,1),(9,'2022-09-13',20000,'Cerrada',1,1);
/*!40000 ALTER TABLE `contabilidad_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_material`
--

DROP TABLE IF EXISTS `control_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `control_material` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `precio` double NOT NULL,
  `cantidad` int(11) NOT NULL,
  `metodo` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_material`
--

LOCK TABLES `control_material` WRITE;
/*!40000 ALTER TABLE `control_material` DISABLE KEYS */;
INSERT INTO `control_material` VALUES (1,'Piola',5000,48,'Efectivo','Existente','Hilo'),(2,'Pepita de madera pequeña',15000,75,'Efectivo','Existente','Pepitas');
/*!40000 ALTER TABLE `control_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_produccion`
--

DROP TABLE IF EXISTS `control_produccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `control_produccion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fechai` date NOT NULL,
  `fechaf` date NOT NULL,
  `cantidad_material` int(11) NOT NULL,
  `gastos` int(11) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `material_id` bigint(20) DEFAULT NULL,
  `producto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `control_produccion_material_id_3758a853_fk_control_material_id` (`material_id`),
  KEY `control_produccion_producto_id_6f168c99_fk_control_producto_id` (`producto_id`),
  CONSTRAINT `control_produccion_material_id_3758a853_fk_control_material_id` FOREIGN KEY (`material_id`) REFERENCES `control_material` (`id`),
  CONSTRAINT `control_produccion_producto_id_6f168c99_fk_control_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `control_producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_produccion`
--

LOCK TABLES `control_produccion` WRITE;
/*!40000 ALTER TABLE `control_produccion` DISABLE KEYS */;
INSERT INTO `control_produccion` VALUES (2,'2022-08-22','2022-08-26',44,190000,'Activo',1,1);
/*!40000 ALTER TABLE `control_produccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_producto`
--

DROP TABLE IF EXISTS `control_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `control_producto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  `precio` double NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_producto`
--

LOCK TABLES `control_producto` WRITE;
/*!40000 ALTER TABLE `control_producto` DISABLE KEYS */;
INSERT INTO `control_producto` VALUES (1,'Maseta Búho',190000,'Masetas','Existente');
/*!40000 ALTER TABLE `control_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(11,'contabilidad','compra'),(14,'contabilidad','detallecompra'),(13,'contabilidad','detalleventa'),(12,'contabilidad','venta'),(5,'contenttypes','contenttype'),(15,'control','material'),(17,'control','produccion'),(16,'control','producto'),(7,'index','backup'),(8,'persona','cliente'),(9,'persona','proveedor'),(10,'persona','usuario'),(6,'sessions','session'),(18,'users','post');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-09-09 19:37:36.424550'),(2,'auth','0001_initial','2022-09-09 19:37:36.829220'),(3,'admin','0001_initial','2022-09-09 19:37:36.920771'),(4,'admin','0002_logentry_remove_auto_add','2022-09-09 19:37:36.927151'),(5,'admin','0003_logentry_add_action_flag_choices','2022-09-09 19:37:36.934867'),(6,'contenttypes','0002_remove_content_type_name','2022-09-09 19:37:37.014440'),(7,'auth','0002_alter_permission_name_max_length','2022-09-09 19:37:37.028577'),(8,'auth','0003_alter_user_email_max_length','2022-09-09 19:37:37.040928'),(9,'auth','0004_alter_user_username_opts','2022-09-09 19:37:37.047940'),(10,'auth','0005_alter_user_last_login_null','2022-09-09 19:37:37.076887'),(11,'auth','0006_require_contenttypes_0002','2022-09-09 19:37:37.079909'),(12,'auth','0007_alter_validators_add_error_messages','2022-09-09 19:37:37.087887'),(13,'auth','0008_alter_user_username_max_length','2022-09-09 19:37:37.100293'),(14,'auth','0009_alter_user_last_name_max_length','2022-09-09 19:37:37.127253'),(15,'auth','0010_alter_group_name_max_length','2022-09-09 19:37:37.140187'),(16,'auth','0011_update_proxy_permissions','2022-09-09 19:37:37.147169'),(17,'auth','0012_alter_user_first_name_max_length','2022-09-09 19:37:37.163442'),(18,'persona','0001_initial','2022-09-09 19:37:37.224288'),(19,'control','0001_initial','2022-09-09 19:37:37.335282'),(20,'contabilidad','0001_initial','2022-09-09 19:37:37.673951'),(21,'control','0002_alter_produccion_fechaf_alter_produccion_fechai','2022-09-09 19:37:37.745349'),(22,'persona','0002_remove_usuario_rol_alter_cliente_telefono_and_more','2022-09-09 19:37:37.914487'),(23,'sessions','0001_initial','2022-09-09 19:37:37.955030'),(24,'users','0001_initial','2022-09-09 19:37:38.011990');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3zru54rxs33cw7mj50tti3pd971h0v1i','.eJxVjEEOwiAQRe_C2hBgcFpcuvcMZIBBqgaS0q6Md7dNutDte-__t_C0LsWvnWc_JXERWpx-WaD45LqL9KB6bzK2usxTkHsiD9vlrSV-XY_276BQL9vakj4TZICkcNBosmUmHMGwcqhdUsFCpHHQRiEBOwCMyLix5EzGID5fyCE3Zw:1oYUcE:lM70cwmIqMvt43DlZKA6hfiTaaWfB8KltRZC7onlZFM','2022-09-28 15:47:54.303208'),('ahje7huitl6jso4dj9iugxc8zpaihqko','.eJxVjEEOwiAQRe_C2hBgcFpcuvcMZIBBqgaS0q6Md7dNutDte-__t_C0LsWvnWc_JXERWpx-WaD45LqL9KB6bzK2usxTkHsiD9vlrSV-XY_276BQL9vakj4TZICkcNBosmUmHMGwcqhdUsFCpHHQRiEBOwCMyLix5EzGID5fyCE3Zw:1oWjpX:kYgvJ6yCHG9jbpb-LdaX5bjiWsonG_6q5i2bMn666pU','2022-09-23 19:38:23.954331'),('wgc1jxb0rv8b8a975fog03rc4h2hwcr3','.eJxVjEEOwiAQRe_C2hBgcFpcuvcMZIBBqgaS0q6Md7dNutDte-__t_C0LsWvnWc_JXERWpx-WaD45LqL9KB6bzK2usxTkHsiD9vlrSV-XY_276BQL9vakj4TZICkcNBosmUmHMGwcqhdUsFCpHHQRiEBOwCMyLix5EzGID5fyCE3Zw:1oY5LN:nVPLFFqJR6czL4cyqf-akraW_7JMaVsZ440eUGmrno4','2022-09-27 12:48:49.101489'),('xsaov8l7n7jv0tt3dq7syfgllfeiveek','.eJxVjEEOwiAQRe_C2hBgcFpcuvcMZIBBqgaS0q6Md7dNutDte-__t_C0LsWvnWc_JXERWpx-WaD45LqL9KB6bzK2usxTkHsiD9vlrSV-XY_276BQL9vakj4TZICkcNBosmUmHMGwcqhdUsFCpHHQRiEBOwCMyLix5EzGID5fyCE3Zw:1oXmcU:MPX1CXjDbmuRuB1PNLGkJwMp5Pnpdn3kTPgdHWKxtP8','2022-09-26 16:49:14.702688');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona_cliente`
--

DROP TABLE IF EXISTS `persona_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona_cliente` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `identificacion` bigint(20) NOT NULL,
  `telefono` varchar(13) NOT NULL,
  `estado` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identificacion` (`identificacion`),
  UNIQUE KEY `persona_cliente_telefono_3aaa6e28_uniq` (`telefono`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona_cliente`
--

LOCK TABLES `persona_cliente` WRITE;
/*!40000 ALTER TABLE `persona_cliente` DISABLE KEYS */;
INSERT INTO `persona_cliente` VALUES (1,'Lorena diaz',1004072816,'3023265986','Inactivo');
/*!40000 ALTER TABLE `persona_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona_proveedor`
--

DROP TABLE IF EXISTS `persona_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona_proveedor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `identificacion` int(11) NOT NULL,
  `telefono` varchar(13) NOT NULL,
  `estado` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identificacion` (`identificacion`),
  UNIQUE KEY `persona_proveedor_telefono_09827f01_uniq` (`telefono`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona_proveedor`
--

LOCK TABLES `persona_proveedor` WRITE;
/*!40000 ALTER TABLE `persona_proveedor` DISABLE KEYS */;
INSERT INTO `persona_proveedor` VALUES (1,'Sandra gaitan',1004513667,'3147543611','Activo');
/*!40000 ALTER TABLE `persona_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona_usuario`
--

DROP TABLE IF EXISTS `persona_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona_usuario` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `identificacion` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(13) NOT NULL,
  `estado` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identificacion` (`identificacion`),
  UNIQUE KEY `correo` (`correo`),
  UNIQUE KEY `persona_usuario_telefono_12969eae_uniq` (`telefono`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona_usuario`
--

LOCK TABLES `persona_usuario` WRITE;
/*!40000 ALTER TABLE `persona_usuario` DISABLE KEYS */;
INSERT INTO `persona_usuario` VALUES (1,1173122574,'Eliana','Rojas','eliana254@gmail.com','3205856921','Activo');
/*!40000 ALTER TABLE `persona_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_post`
--

DROP TABLE IF EXISTS `users_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_post` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_post_user_id_c1cea120_fk_auth_user_id` (`user_id`),
  CONSTRAINT `users_post_user_id_c1cea120_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_post`
--

LOCK TABLES `users_post` WRITE;
/*!40000 ALTER TABLE `users_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-14 13:03:40
