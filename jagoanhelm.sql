-- MariaDB dump 10.19  Distrib 10.5.19-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: jagoanhelm
-- ------------------------------------------------------
-- Server version	10.5.19-MariaDB-0+deb11u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrasi_kategoriproduk`
--

DROP TABLE IF EXISTS `administrasi_kategoriproduk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrasi_kategoriproduk` (
  `kategori` varchar(100) NOT NULL,
  `deskripsi` varchar(100) NOT NULL,
  `gambar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrasi_kategoriproduk`
--

LOCK TABLES `administrasi_kategoriproduk` WRITE;
/*!40000 ALTER TABLE `administrasi_kategoriproduk` DISABLE KEYS */;
INSERT INTO `administrasi_kategoriproduk` VALUES ('----akhir bagian untuk dihapus sebelum upload----','',''),('----awal bagian untuk dihapus sebelum upload----','',''),('Aksesoris Mobil','Aksesoris Mobil',''),('Aksesoris Motor','aksesoris motor',''),('alat cuci','untuk mencuci tangan',''),('alat cuci2','untuk mencuci tangan',''),('alat pancing','untuk memancing',''),('alat pancing2','untuk memancing ke-2',''),('alat pancing3','untuk memancing ke-2',''),('Elektronik','Produk Elektronik',NULL),('kategori1','deskripsi1',''),('kosmetik pria','kosmetik untuk pria','kategori/lin.png'),('Perlengkapan Mobil','Perlengkapan mobil',''),('Perlengkapan Motor','Perlengkapan motor',''),('Silakan Isikan dengan format di bawah ini menggunakan koma','','');
/*!40000 ALTER TABLE `administrasi_kategoriproduk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrasi_produk`
--

DROP TABLE IF EXISTS `administrasi_produk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrasi_produk` (
  `produk_kode` varchar(100) NOT NULL,
  `produk_nama` varchar(200) NOT NULL,
  `produk_merek` varchar(200) DEFAULT NULL,
  `stok_awal` int(11) NOT NULL,
  `stok_masuk` int(11) NOT NULL,
  `stok_keluar` int(11) NOT NULL,
  `stok_akhir` int(11) NOT NULL,
  `kategori_id` varchar(100) NOT NULL,
  `stok_rusak` int(11) NOT NULL,
  `gambar` varchar(100) DEFAULT NULL,
  `berat` int(11) DEFAULT NULL,
  `deskripsi` longtext DEFAULT NULL,
  `gambar1` varchar(100) DEFAULT NULL,
  `gambar2` varchar(100) DEFAULT NULL,
  `gambar3` varchar(100) DEFAULT NULL,
  `grosir1` int(11) NOT NULL,
  `grosir2` int(11) NOT NULL,
  `grosir3` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  `jumlah1` int(11) NOT NULL,
  `jumlah2` int(11) NOT NULL,
  `jumlah3` int(11) NOT NULL,
  `produk_asal` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`produk_kode`),
  KEY `administrasi_produk_kategori_id_90909291_fk_administr` (`kategori_id`),
  CONSTRAINT `administrasi_produk_kategori_id_90909291_fk_administr` FOREIGN KEY (`kategori_id`) REFERENCES `administrasi_kategoriproduk` (`kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrasi_produk`
--

LOCK TABLES `administrasi_produk` WRITE;
/*!40000 ALTER TABLE `administrasi_produk` DISABLE KEYS */;
INSERT INTO `administrasi_produk` VALUES ('ABCD11','PRODUK ABC DARI MANA','ABCDEFGHIJ',2000,0,0,0,'Elektronik',0,'produk/STNKMOBIL.PNG',2000,'KEREN POKOK E LAH\r\n\r\n\r\n\r\n\r\nJOSS TENAN \r\n\r\n\r\nMANTEP','','','',260000,255000,250000,275000,20,40,60,'Indonesia'),('ABCD111','active speaker1','1245566',0,0,0,0,'Elektronik',0,'produk/lin_SDJC0Gu.png',NULL,'','','','',0,0,0,0,0,0,0,'Indonesia'),('ABCD113','active speaker1','1245566',200,0,0,0,'Elektronik',0,'produk/yes.jpg',NULL,'','','','',0,0,0,0,0,0,0,'Tiongkok'),('ABCD12','active speaker2','1245566',0,0,0,0,'Elektronik',0,'produk/widget_type_djago_form.png',20,'Produk yang keren.\r\ncocok untuk yang suka keren2\r\n\r\n\r\n\r\nsemangat yak',NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD121','active speaker2','1245566',0,0,0,0,'Elektronik',0,'produk/widget_type_djago_form_O8HsapD.png',NULL,'',NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD13','active speaker3','1245566',0,0,0,0,'Elektronik',0,'produk/skensot_sparky.jpg',300,'apa coba????',NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD131','active speaker3','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD14','active speaker4','1245566',0,0,0,0,'Elektronik',0,'produk/django-faster-1024x576.jpg',NULL,'',NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD141','active speaker4','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD15','active speaker5','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD151','active speaker5','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD16','active speaker6','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD161','active speaker6','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD17','active speaker7','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD171','active speaker7','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD21','active speaker2','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD213','active speaker2','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD31','active speaker3','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD313','active speaker3','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD41','active speaker4','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD413','active speaker4','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD51','active speaker5','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD513','active speaker5','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD61','active speaker6','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD613','active speaker6','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD71','active speaker7','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL),('ABCD713','active speaker7','1245566',0,0,0,0,'Elektronik',0,'',NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,0,NULL);
/*!40000 ALTER TABLE `administrasi_produk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrasi_upfiles`
--

DROP TABLE IF EXISTS `administrasi_upfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrasi_upfiles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `myfile` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrasi_upfiles`
--

LOCK TABLES `administrasi_upfiles` WRITE;
/*!40000 ALTER TABLE `administrasi_upfiles` DISABLE KEYS */;
INSERT INTO `administrasi_upfiles` VALUES (1,'csv/mydata.csv'),(2,'csv/mydata_LnnBYNt.csv'),(3,'csv/mydata_pxinQ5E.csv'),(4,'csv/requirements.txt'),(5,'csv/requirements_XJ8TyCr.txt'),(6,'csv/requirements_FOThDRR.txt'),(7,'csv/README.md'),(8,'csv/requirements_rgBUv9P.txt'),(9,'csv/mydata_ipE8LYl.csv'),(10,'csv/mydata_WvboI1T.csv'),(11,'csv/mydata_fgKrXr7.csv'),(12,'csv/mydata_wtZ24Nt.csv'),(13,'csv/mydata_t9nJcpM.csv'),(14,'csv/mydata_ahyIiAy.csv'),(15,'csv/mydata_3T15RIM.csv'),(16,'csv/mydata_wGKqJUs.csv'),(17,'csv/mydata_3zpxfbj.csv'),(18,'csv/mydata_eq97mhD.csv'),(19,'csv/mydata_GGvTwgk.csv'),(20,'csv/mydata_WOQRMQo.csv'),(21,'csv/mydata_bghkKMC.csv'),(22,'csv/mydata_zW9cZyZ.csv'),(23,'csv/mydata_8Wx4QYP.csv'),(24,'csv/mydata_QIQaxGB.csv'),(25,'csv/mydata_3XxOevQ.csv'),(26,'csv/mydata_k1BJsoS.csv'),(27,'csv/mydata_cuIdqk9.csv'),(28,'csv/mydata_R9aGHuZ.csv'),(29,'csv/mydata_j5FUeg4.csv'),(30,'csv/mydata_AMFloC4.csv'),(31,'csv/mydata_EZB1ImT.csv'),(32,'csv/mydata_dkzzxQ9.csv'),(33,'csv/mydata_BgqLrWH.csv'),(34,'csv/mydata_MaBYn9D.csv'),(35,'csv/mydata_Nw9pRyA.csv'),(36,'csv/mydata_z2Glmz3.csv'),(37,'csv/mydata_4Dkq9zG.csv'),(38,'csv/mydata_Ofi3xxD.csv'),(39,'csv/mydata_XapJyz0.csv'),(40,'csv/mydata_6cW2vtt.csv'),(41,'csv/mydata_C0ODxAn.csv'),(42,'csv/mydata_jx9Lrxa.csv'),(43,'csv/mydata_QVgn9sB.csv'),(44,'csv/mydata_vcMisM2.csv'),(45,'csv/mydata_FkS9miz.csv'),(46,'csv/mydata_BBtVcaC.csv'),(47,'csv/mydata_frL5iaD.csv'),(48,'csv/mydata_yLKBrvy.csv'),(49,'csv/mydata_YXIPMeU.csv'),(50,'csv/mydata_mv7lf8O.csv'),(51,'csv/mydata_4yblOK6.csv'),(52,'csv/mydata_BG7DJs8.csv'),(53,'csv/mydata_h02LdWr.csv'),(54,'csv/mydata_B0UjEWO.csv'),(55,'csv/mydata_qk1EniV.csv'),(56,'csv/requirements_bS9xNep.txt'),(57,'csv/mydata_bZHaYkI.csv'),(58,'csv/mydata_8OPMXtj.csv'),(59,'csv/mydata_3282iC1.csv'),(60,'csv/mydata_ZdnpOb2.csv'),(61,'csv/mydata_nLW1N8h.csv'),(62,'csv/mydata_oX2ts3Q.csv'),(63,'csv/mydata_pxozZkL.csv'),(64,'csv/WhatsApp_Image_2023-05-19_at_16.57.47.jpeg'),(65,'csv/WhatsApp_Image_2023-05-19_at_16.57.47_gnHWGTo.jpeg'),(66,'csv/mydata_p8392x3.csv'),(67,'csv/mydata_oCKfDSr.csv'),(68,'csv/WIN_20221209_21_09_24_Pro.jpg'),(69,'csv/ElektronikAABBKursi_elektronik12.txt'),(70,'csv/dbCoba.sql'),(71,'csv/mydata_8dsqm3u.csv'),(72,'csv/mydata_jmcuj8i.csv'),(73,'csv/mydata_bjCStU4.csv'),(74,'csv/testwritestruct.txt'),(75,'csv/KTP_PAPAH_TAN_BIAUW_TIEN.jpg'),(76,'csv/produk_template_5.csv'),(77,'csv/kategori_template.csv'),(78,'csv/kategori_template_ZzdBfVu.csv'),(79,'csv/kategori_template_kwTc6Od.csv'),(80,'csv/kategori_template_vQbSkRZ.csv'),(81,'csv/kategori_template_pUvuhKO.csv'),(82,'csv/kategori_template_M8rkeGp.csv'),(83,'csv/kategori_template_CMaLQJr.csv'),(84,'csv/kategori_template_VsMsQDa.csv'),(85,'csv/kategori_template_0RW3SIz.csv'),(86,'csv/kategori_template_FBasmxJ.csv'),(87,'csv/kategori_template_dTCCcD5.csv');
/*!40000 ALTER TABLE `administrasi_upfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrasi_upfileskategori`
--

DROP TABLE IF EXISTS `administrasi_upfileskategori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrasi_upfileskategori` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `myfile` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrasi_upfileskategori`
--

LOCK TABLES `administrasi_upfileskategori` WRITE;
/*!40000 ALTER TABLE `administrasi_upfileskategori` DISABLE KEYS */;
INSERT INTO `administrasi_upfileskategori` VALUES (1,'csv/kategori_template_C8OVSD1.csv'),(2,'csv_kategori/kategori_template.csv'),(3,'csv_kategori/kategori_template_BQIngqu.csv'),(4,'csv_kategori/kategori_template_w9CrtsG.csv'),(5,'csv_kategori/kategori_template_wOOog63.csv'),(6,'csv_kategori/kategori_template_BrL31S8.csv'),(7,'csv_kategori/kategori_template_jWTbUas.csv'),(8,'csv_kategori/kategori_template_H8hFMG2.csv'),(9,'csv_kategori/kategori_template_Qxv3IIQ.csv'),(10,'csv_kategori/kategori_template_ouAB2wz.csv'),(11,'csv_kategori/kategori_template_t1DOUk8.csv'),(12,'csv_kategori/kategori_template_NE0sXoi.csv'),(13,'csv_kategori/kategori_template_IQmj1kH.csv'),(14,'csv_kategori/kategori_template_o13XKKD.csv'),(15,'csv_kategori/kategori_template_oWo4WvA.csv'),(16,'csv_kategori/kategori_template_4NSX3Af.csv'),(17,'csv_kategori/kategori_template_VTCDKv5.csv'),(18,'csv_kategori/kategori_template_nK0Oxsv.csv'),(19,'csv_kategori/kategori_template_X5kQZa5.csv'),(20,'csv_kategori/kategori_template_RFaeozx.csv'),(21,'csv_kategori/kategori_template_sH8AeWb.csv'),(22,'csv_kategori/kategori_template_KOSeIU1.csv'),(23,'csv_kategori/kategori_template_KcWbu7J.csv'),(24,'csv_kategori/kategori_template_bzK1Qa0.csv'),(25,'csv_kategori/kategori.csv'),(26,'csv_kategori/kategori_HH2k6gg.csv'),(27,'csv_kategori/kategori_AdbzbJG.csv'),(28,'csv_kategori/kategori_SWOh6VC.csv'),(29,'csv_kategori/kategori_rz7xhin.csv'),(30,'csv_kategori/kategori.csv');
/*!40000 ALTER TABLE `administrasi_upfileskategori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add kategori produk',7,'add_kategoriproduk'),(26,'Can change kategori produk',7,'change_kategoriproduk'),(27,'Can delete kategori produk',7,'delete_kategoriproduk'),(28,'Can view kategori produk',7,'view_kategoriproduk'),(29,'Can add test',8,'add_test'),(30,'Can change test',8,'change_test'),(31,'Can delete test',8,'delete_test'),(32,'Can view test',8,'view_test'),(33,'Can add produk',9,'add_produk'),(34,'Can change produk',9,'change_produk'),(35,'Can delete produk',9,'delete_produk'),(36,'Can view produk',9,'view_produk'),(37,'Can add up files',10,'add_upfiles'),(38,'Can change up files',10,'change_upfiles'),(39,'Can delete up files',10,'delete_upfiles'),(40,'Can view up files',10,'view_upfiles'),(41,'Can add up files kategori',11,'add_upfileskategori'),(42,'Can change up files kategori',11,'change_upfileskategori'),(43,'Can delete up files kategori',11,'delete_upfileskategori'),(44,'Can view up files kategori',11,'view_upfileskategori');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$gRVrtTQozsMTIVICwYWxpy$5igzNllYhCPuAlkquGf0epByjoJfT8im1WW56gp3DXs=',NULL,1,'suryo','','','suryo@chandra.com',1,1,'2023-05-20 15:27:48.905877');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'administrasi','kategoriproduk'),(9,'administrasi','produk'),(8,'administrasi','test'),(10,'administrasi','upfiles'),(11,'administrasi','upfileskategori'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-05-20 15:26:31.328613'),(2,'auth','0001_initial','2023-05-20 15:26:39.064451'),(3,'admin','0001_initial','2023-05-20 15:26:40.033169'),(4,'admin','0002_logentry_remove_auto_add','2023-05-20 15:26:40.110212'),(5,'admin','0003_logentry_add_action_flag_choices','2023-05-20 15:26:40.180488'),(6,'contenttypes','0002_remove_content_type_name','2023-05-20 15:26:40.904381'),(7,'auth','0002_alter_permission_name_max_length','2023-05-20 15:26:41.487498'),(8,'auth','0003_alter_user_email_max_length','2023-05-20 15:26:41.654905'),(9,'auth','0004_alter_user_username_opts','2023-05-20 15:26:41.722444'),(10,'auth','0005_alter_user_last_login_null','2023-05-20 15:26:42.043752'),(11,'auth','0006_require_contenttypes_0002','2023-05-20 15:26:42.054416'),(12,'auth','0007_alter_validators_add_error_messages','2023-05-20 15:26:42.117948'),(13,'auth','0008_alter_user_username_max_length','2023-05-20 15:26:42.244661'),(14,'auth','0009_alter_user_last_name_max_length','2023-05-20 15:26:42.388328'),(15,'auth','0010_alter_group_name_max_length','2023-05-20 15:26:42.523152'),(16,'auth','0011_update_proxy_permissions','2023-05-20 15:26:42.600290'),(17,'auth','0012_alter_user_first_name_max_length','2023-05-20 15:26:42.945064'),(18,'sessions','0001_initial','2023-05-20 15:26:43.266577'),(19,'administrasi','0001_initial','2023-05-21 19:50:34.179208'),(20,'administrasi','0002_test','2023-05-21 23:53:32.625586'),(21,'administrasi','0003_rename_nama_kategoriproduk_kategori_produk','2023-05-22 02:10:26.537581'),(22,'administrasi','0004_delete_test_produk_stok_rusak_and_more','2023-05-22 02:25:57.286208'),(23,'administrasi','0005_kategoriproduk_gambar_produk_gambar','2023-05-22 07:48:47.433218'),(24,'administrasi','0006_upfiles','2023-05-22 14:12:38.621298'),(25,'administrasi','0007_remove_produk_id_alter_produk_produk_kode','2023-05-22 16:13:10.161474'),(26,'administrasi','0008_kategoriproduk_created_at_produk_created_at','2023-05-22 16:55:27.101208'),(27,'administrasi','0009_remove_kategoriproduk_created_at_and_more','2023-05-22 17:38:31.565731'),(28,'administrasi','0010_produk_berat_produk_deskripsi_and_more','2023-05-23 09:27:22.382877'),(29,'administrasi','0011_rename_produk_serial_produk_produk_merek_and_more','2023-05-24 16:39:05.645684'),(30,'administrasi','0012_upfileskategori_alter_produk_gambar_and_more','2023-05-25 11:21:43.712505');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-26 17:57:09
