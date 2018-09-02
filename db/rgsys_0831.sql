-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: registrationsystem
-- ------------------------------------------------------
-- Server version	5.7.17-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can add group',3,'add_group'),(9,'Can change group',3,'change_group'),(10,'Can delete group',3,'delete_group'),(11,'Can add user',4,'add_user'),(12,'Can change user',4,'change_user'),(13,'Can delete user',4,'delete_user'),(14,'Can view group',3,'view_group'),(15,'Can view permission',2,'view_permission'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add department info',7,'add_departmentinfo'),(26,'Can change department info',7,'change_departmentinfo'),(27,'Can delete department info',7,'delete_departmentinfo'),(28,'Can add duty info',8,'add_dutyinfo'),(29,'Can change duty info',8,'change_dutyinfo'),(30,'Can delete duty info',8,'delete_dutyinfo'),(31,'Can add dutyschedule',9,'add_dutyschedule'),(32,'Can change dutyschedule',9,'change_dutyschedule'),(33,'Can delete dutyschedule',9,'delete_dutyschedule'),(34,'Can add r_ department info_ duty info',10,'add_r_departmentinfo_dutyinfo'),(35,'Can change r_ department info_ duty info',10,'change_r_departmentinfo_dutyinfo'),(36,'Can delete r_ department info_ duty info',10,'delete_r_departmentinfo_dutyinfo'),(37,'Can add r_ user info_ department info',11,'add_r_userinfo_departmentinfo'),(38,'Can change r_ user info_ department info',11,'change_r_userinfo_departmentinfo'),(39,'Can delete r_ user info_ department info',11,'delete_r_userinfo_departmentinfo'),(40,'Can add user info',12,'add_userinfo'),(41,'Can change user info',12,'change_userinfo'),(42,'Can delete user info',12,'delete_userinfo'),(43,'Can view department info',7,'view_departmentinfo'),(44,'Can view duty info',8,'view_dutyinfo'),(45,'Can view dutyschedule',9,'view_dutyschedule'),(46,'Can view r_ department info_ duty info',10,'view_r_departmentinfo_dutyinfo'),(47,'Can view r_ user info_ department info',11,'view_r_userinfo_departmentinfo'),(48,'Can view user info',12,'view_userinfo'),(49,'Can add Bookmark',13,'add_bookmark'),(50,'Can change Bookmark',13,'change_bookmark'),(51,'Can delete Bookmark',13,'delete_bookmark'),(52,'Can add User Setting',14,'add_usersettings'),(53,'Can change User Setting',14,'change_usersettings'),(54,'Can delete User Setting',14,'delete_usersettings'),(55,'Can add User Widget',15,'add_userwidget'),(56,'Can change User Widget',15,'change_userwidget'),(57,'Can delete User Widget',15,'delete_userwidget'),(58,'Can add log entry',16,'add_log'),(59,'Can change log entry',16,'change_log'),(60,'Can delete log entry',16,'delete_log'),(61,'Can view Bookmark',13,'view_bookmark'),(62,'Can view log entry',16,'view_log'),(63,'Can view User Setting',14,'view_usersettings'),(64,'Can view User Widget',15,'view_userwidget'),(65,'Can add duty schedule proxy model',9,'add_dutyscheduleproxymodel'),(66,'Can change duty schedule proxy model',9,'change_dutyscheduleproxymodel'),(67,'Can delete duty schedule proxy model',9,'delete_dutyscheduleproxymodel'),(68,'Can view duty schedule proxy model',17,'view_dutyscheduleproxymodel'),(69,'Can add Token',18,'add_token'),(70,'Can change Token',18,'change_token'),(71,'Can delete Token',18,'delete_token'),(72,'Can view Token',18,'view_token'),(73,'Can add r_ auth user_ department',19,'add_r_authuser_department'),(74,'Can change r_ auth user_ department',19,'change_r_authuser_department'),(75,'Can delete r_ auth user_ department',19,'delete_r_authuser_department'),(76,'Can view r_ auth user_ department',19,'view_r_authuser_department'),(77,'Can add r_ author_ department',20,'add_r_author_department'),(78,'Can change r_ author_ department',20,'change_r_author_department'),(79,'Can delete r_ author_ department',20,'delete_r_author_department'),(80,'Can add my test',21,'add_mytest'),(81,'Can change my test',21,'change_mytest'),(82,'Can delete my test',21,'delete_mytest'),(83,'Can view my test',21,'view_mytest'),(84,'Can view r_ author_ department',20,'view_r_author_department'),(85,'Can add duty_duty department',22,'add_duty_dutydepartment'),(86,'Can change duty_duty department',22,'change_duty_dutydepartment'),(87,'Can delete duty_duty department',22,'delete_duty_dutydepartment'),(88,'Can add duty schedule mid model',23,'add_dutyschedulemidmodel'),(89,'Can change duty schedule mid model',23,'change_dutyschedulemidmodel'),(90,'Can delete duty schedule mid model',23,'delete_dutyschedulemidmodel'),(91,'Can view duty schedule mid model',23,'view_dutyschedulemidmodel'),(92,'Can view duty_duty department',22,'view_duty_dutydepartment');
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
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$bDDCuUrHmvlX$bhujdMLdk0qx7iCK7h6/gXc7AelMNK3gBFGAaSyDThg=','2018-06-26 07:56:26.843105',1,'root','','','',1,1,'2018-04-19 06:26:59.448589'),(2,'pbkdf2_sha256$100000$N0RdJxt3dJ5w$waXLeJMFTSmM2E9A+G9uRvGHc4M1wgfcDTKabejHS3o=','2018-08-29 07:47:31.725155',1,'admin','','','evaseemefly@126.com',1,1,'2018-06-05 02:00:48.853570'),(3,'pbkdf2_sha256$100000$M5eg5w3iptWS$N0FbWSTSEbYm5ZZaL3pFGZna3BEtAM07zWDZ2KEPVCc=','2018-07-24 09:39:31.605574',1,'tongxin','','','123@1.com',1,1,'2018-07-11 08:32:50.939030'),(4,'pbkdf2_sha256$100000$2SAIaftTIPbY$a876EbaxVcJY6sdnSBdB9f20+f0d/EVpr6q+Ucn1R00=',NULL,1,'yujing','','','1@1.com',1,1,'2018-07-12 02:31:57.053368'),(5,'pbkdf2_sha256$100000$s79MHalnRMcM$lJJShjvYE4OKSf/iE+e/T0ANPyikFLWroCDzHtDpbhg=','2018-08-30 07:28:18.488662',1,'nmefc','','','123@123.com',1,1,'2018-08-30 07:25:01.589483'),(6,'pbkdf2_sha256$100000$R1hGGeJMfYK0$11mzvXHGbYSiN3nStlMFGjG5ZYH20QcI1qtmVLS2nfA=',NULL,1,'yewuchu','','','123@123.com',1,1,'2018-08-30 07:25:35.535634');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('1981edece5ce5a487b79ac172d38a564fd4aca98','2018-07-11 08:03:23.881987',2),('573d56994b28022276230b3be45030d81e704521','2018-07-12 02:33:11.906479',4),('87d44bfee2816133c759a6d14a73ca708fe90875','2018-07-11 08:38:43.393016',3);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
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
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(18,'authtoken','token'),(5,'contenttypes','contenttype'),(7,'duty','departmentinfo'),(8,'duty','dutyinfo'),(9,'duty','dutyschedule'),(23,'duty','dutyschedulemidmodel'),(17,'duty','dutyscheduleproxymodel'),(22,'duty','duty_dutydepartment'),(19,'duty','r_authuser_department'),(10,'duty','r_departmentinfo_dutyinfo'),(11,'duty','r_userinfo_departmentinfo'),(12,'duty','userinfo'),(6,'sessions','session'),(21,'users','mytest'),(20,'users','r_author_department'),(13,'xadmin','bookmark'),(16,'xadmin','log'),(14,'xadmin','usersettings'),(15,'xadmin','userwidget');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'duty','0001_initial','2018-04-17 08:46:16.237359'),(2,'contenttypes','0001_initial','2018-04-19 06:20:39.543007'),(3,'auth','0001_initial','2018-04-19 06:20:40.391765'),(4,'admin','0001_initial','2018-04-19 06:20:40.594909'),(5,'admin','0002_logentry_remove_auto_add','2018-04-19 06:20:40.606917'),(6,'contenttypes','0002_remove_content_type_name','2018-04-19 06:20:40.729006'),(7,'auth','0002_alter_permission_name_max_length','2018-04-19 06:20:40.808045'),(8,'auth','0003_alter_user_email_max_length','2018-04-19 06:20:40.873107'),(9,'auth','0004_alter_user_username_opts','2018-04-19 06:20:40.884116'),(10,'auth','0005_alter_user_last_login_null','2018-04-19 06:20:40.942156'),(11,'auth','0006_require_contenttypes_0002','2018-04-19 06:20:40.949162'),(12,'auth','0007_alter_validators_add_error_messages','2018-04-19 06:20:40.962172'),(13,'auth','0008_alter_user_username_max_length','2018-04-19 06:20:41.128272'),(14,'auth','0009_alter_user_last_name_max_length','2018-04-19 06:20:41.190316'),(15,'sessions','0001_initial','2018-04-19 06:20:41.260384'),(16,'xadmin','0001_initial','2018-04-19 06:20:41.752771'),(17,'xadmin','0002_log','2018-04-19 06:20:41.953913'),(18,'xadmin','0003_auto_20160715_0100','2018-04-19 06:20:42.045978'),(19,'duty','0002_auto_20180419_1500','2018-04-19 07:05:00.659038'),(20,'duty','0003_auto_20180419_1510','2018-04-19 07:10:26.297978'),(21,'duty','0004_auto_20180419_1516','2018-04-19 07:17:32.680280'),(22,'duty','0005_auto_20180419_1647','2018-04-19 08:47:21.733374'),(23,'duty','0006_auto_20180419_1647','2018-04-20 01:13:11.496938'),(24,'duty','0007_auto_20180420_0913','2018-04-20 01:14:12.357065'),(25,'duty','0008_auto_20180420_0913','2018-04-20 01:14:12.366072'),(26,'duty','0009_auto_20180420_0914','2018-04-20 02:53:10.396274'),(27,'duty','0010_auto_20180420_1053','2018-04-20 02:53:34.503244'),(28,'duty','0011_auto_20180420_1053','2018-04-20 02:58:41.387003'),(29,'duty','0012_auto_20180420_1059','2018-04-20 03:00:18.615938'),(30,'duty','0013_auto_20180420_1100','2018-04-20 03:00:18.625945'),(31,'duty','0014_auto_20180420_1100','2018-04-20 03:02:52.755527'),(32,'duty','0015_auto_20180420_1103','2018-04-20 03:03:29.480454'),(33,'duty','0016_auto_20180420_1103','2018-04-20 03:19:57.171941'),(34,'duty','0017_auto_20180420_1120','2018-04-20 03:20:38.030271'),(35,'duty','0018_auto_20180420_1120','2018-04-25 06:44:14.733633'),(36,'duty','0019_auto_20180425_1451','2018-04-25 07:05:31.564320'),(37,'duty','0020_auto_20180425_1506','2018-04-25 07:07:24.864714'),(38,'duty','0021_auto_20180612_1621','2018-06-12 08:21:47.153441'),(39,'authtoken','0001_initial','2018-07-11 07:45:18.815196'),(40,'authtoken','0002_auto_20160226_1747','2018-07-11 07:45:18.935281'),(41,'duty','0022_auto_20180711_1543','2018-07-11 07:45:18.945306'),(42,'duty','0023_auto_20180716_1620','2018-07-16 08:20:23.480144'),(43,'duty','0024_auto_20180718_0925','2018-07-18 01:26:11.481573'),(44,'duty','0025_auto_20180718_0929','2018-07-18 01:29:20.182226'),(45,'users','0001_initial','2018-07-18 01:29:20.477436'),(46,'duty','0002_auto_20180828_1154','2018-08-28 03:57:02.400633'),(47,'duty','0003_auto_20180829_1059','2018-08-29 02:59:52.596577');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('021a4wy5ykq4l0daxn810r4timjie2nn','NWY2ZGQ5OTliY2JmZDI1NDI2NDg2ODk3YzZhZmMzMDg2YmExNjY3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsImRlcGFydG1lbnRpbmZvIl0sIiJdfQ==','2018-05-24 01:19:26.052371'),('49ageurirln1hou44p5ombux9bruys7y','ZDEyMjE0YzBlOTQ1YWRlYmM5ZTNjMTM2MzM4ODEwYzEwMTE2YWVjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-05-21 01:37:15.429795'),('5zjard7fg7h9euwhs3x7lpvstkyxrmxx','ZjVjZTFmZmExY2IxZDNjYzVmNmJmOTE1OWFkMWUyYzM3NmNjZDQ3ZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1OTk4YTgwZjg0ODRmYTRmYWY0ZGYxMmI3MTgxNWM3ODczMGM2OTg1IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfdXNlcmluZm9fZGVwYXJ0bWVudGluZm8iXSwiIl19','2018-09-12 07:48:29.274213'),('8ofpl5f22fw77vzuaz7lsvpd4mhieshg','YjI0MjBhNjIxNzllYzA4MjU4ZjA5MmNmZmE3YmU3NTE1NzhmOTQ0YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfdXNlcmluZm9fZGVwYXJ0bWVudGluZm8iXSwiIl19','2018-05-10 02:54:23.806528'),('eb9wg0ic5tf3ioym9c1akkx86w6sxrtr','ZjE2NzBhM2I1NmFmMGIwNmYzNmNjN2YyZmQ3YjE1NTJkYjlhYjQ5Nzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1OTk4YTgwZjg0ODRmYTRmYWY0ZGYxMmI3MTgxNWM3ODczMGM2OTg1IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-06-19 03:04:50.955152'),('ezwhm8yqicy0iksl2nxvgae8ho1pdv4t','ZDEyMjE0YzBlOTQ1YWRlYmM5ZTNjMTM2MzM4ODEwYzEwMTE2YWVjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-05-07 03:19:56.471781'),('hifretea24k699zxpkdhr2590tvqxcc0','NDJiY2QyNmNhN2Q3ZWEwM2ZlOTA4ZGFkOWEyYzQxNjEyYWZjMWFjNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1OTk4YTgwZjg0ODRmYTRmYWY0ZGYxMmI3MTgxNWM3ODczMGM2OTg1IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsImR1dHlpbmZvIl0sIiJdfQ==','2018-09-07 07:04:06.380895'),('ivqt2hruofdx6g7n48fszw3gp5u9fxar','OGIwMWZiNmFmYzdlYTQwMjkwYWQyZmMxMmFlMTFjYTdlMjhjOGUxNjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYzZkZmRiYzc1ZjY5NWEyODRlNTU1OWRhZGY2ZTFlOGRkNzQ3NjkyIiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-09-13 07:37:13.376515'),('m4z40df9xgoxkanp3o7r6g7t8b1jn1jl','ZDEyMjE0YzBlOTQ1YWRlYmM5ZTNjMTM2MzM4ODEwYzEwMTE2YWVjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-06-27 01:35:33.145379'),('nm3nkl7qlkvpb24qpvu8a70o1caj72z8','YmI2MWZiODNmMWFiNTIzOTMzMGQ0OGRiOWEwMjFkMjMxODUzYTc4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1OTk4YTgwZjg0ODRmYTRmYWY0ZGYxMmI3MTgxNWM3ODczMGM2OTg1IiwiTElTVF9RVUVSWSI6W1sieGFkbWluIiwibG9nIl0sIiJdfQ==','2018-08-07 10:14:21.744304'),('o0kbnn3c2i8w56bi9suotp10hcmjy5qx','ZDEyMjE0YzBlOTQ1YWRlYmM5ZTNjMTM2MzM4ODEwYzEwMTE2YWVjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-05-04 03:21:12.940289'),('o8vwg1i90jwkz7sjh1nzw9y0m0s5juyi','ZDEyMjE0YzBlOTQ1YWRlYmM5ZTNjMTM2MzM4ODEwYzEwMTE2YWVjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3Mzk5OTNjY2EyMGExZGRhYmNjY2UwMzc2NDEzNWJmZGI4NDk3M2E2IiwiTElTVF9RVUVSWSI6W1siZHV0eSIsInJfZGVwYXJ0bWVudGluZm9fZHV0eWluZm8iXSwiIl19','2018-07-10 07:56:43.472573');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_departmentinfo`
--

DROP TABLE IF EXISTS `duty_departmentinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_departmentinfo` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `derpartmentname` varchar(20) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_departmentinfo`
--

LOCK TABLES `duty_departmentinfo` WRITE;
/*!40000 ALTER TABLE `duty_departmentinfo` DISABLE KEYS */;
INSERT INTO `duty_departmentinfo` VALUES (-999,0,'默认值'),(1,0,'测试组'),(2,4,'默认部门风暴潮组'),(3,6,'海浪组'),(4,4,'海啸'),(5,6,'海冰组'),(6,0,'预警室'),(7,0,'环境室'),(8,0,'业务处'),(9,0,'中心领导');
/*!40000 ALTER TABLE `duty_departmentinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_duty_dutydepartment`
--

DROP TABLE IF EXISTS `duty_duty_dutydepartment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_duty_dutydepartment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_duty_dutydepartment`
--

LOCK TABLES `duty_duty_dutydepartment` WRITE;
/*!40000 ALTER TABLE `duty_duty_dutydepartment` DISABLE KEYS */;
/*!40000 ALTER TABLE `duty_duty_dutydepartment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_dutyinfo`
--

DROP TABLE IF EXISTS `duty_dutyinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_dutyinfo` (
  `duid` int(11) NOT NULL AUTO_INCREMENT,
  `dutyname` varchar(20) NOT NULL,
  `createdate` date DEFAULT NULL,
  `isdel` tinyint(1) NOT NULL,
  `modeificateddate` date DEFAULT NULL,
  `desc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`duid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_dutyinfo`
--

LOCK TABLES `duty_dutyinfo` WRITE;
/*!40000 ALTER TABLE `duty_dutyinfo` DISABLE KEYS */;
INSERT INTO `duty_dutyinfo` VALUES (-999,'默认值','2018-05-31',0,'2018-05-31',NULL),(1,'主班','2018-04-19',0,'2018-04-19',NULL),(2,'副班','2018-04-19',0,'2018-04-19',NULL),(3,'警报班','2018-04-19',0,'2018-04-19',NULL),(4,'24小时班','2018-04-23',0,'2018-04-23',NULL),(5,'带班领导','2018-08-30',0,'2018-08-30','中心带班领导'),(6,'业务值班岗','2018-08-30',0,'2018-08-30','业务处每日带班人员');
/*!40000 ALTER TABLE `duty_dutyinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_dutyschedule`
--

DROP TABLE IF EXISTS `duty_dutyschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_dutyschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dutydate` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `rDepartmentDuty_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `duty_dutyschedule_user_id_1386a9fb_fk_duty_userinfo_uid` (`user_id`),
  KEY `duty_dutyschedule_rDepartmentDuty_id_1327f391_fk_duty_r_de` (`rDepartmentDuty_id`),
  CONSTRAINT `duty_dutyschedule_rDepartmentDuty_id_1327f391_fk_duty_r_de` FOREIGN KEY (`rDepartmentDuty_id`) REFERENCES `duty_r_departmentinfo_dutyinfo` (`id`),
  CONSTRAINT `duty_dutyschedule_user_id_1386a9fb_fk_duty_userinfo_uid` FOREIGN KEY (`user_id`) REFERENCES `duty_userinfo` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=286 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_dutyschedule`
--

LOCK TABLES `duty_dutyschedule` WRITE;
/*!40000 ALTER TABLE `duty_dutyschedule` DISABLE KEYS */;
INSERT INTO `duty_dutyschedule` VALUES (1,'2018-05-10',5,5),(3,'2018-04-25',3,3),(4,'2018-05-07',1,1),(5,'2018-05-07',2,2),(7,'2018-05-08',1,4),(166,'2018-06-09',1,3),(167,'2018-06-09',1,8),(168,'2018-06-09',1,9),(169,'2018-06-09',1,10),(170,'2018-06-10',3,3),(171,'2018-06-10',3,8),(172,'2018-06-10',3,9),(173,'2018-06-10',3,10),(174,'2018-06-11',1,3),(175,'2018-06-11',1,8),(176,'2018-06-11',1,9),(177,'2018-06-11',3,10),(186,'2018-06-14',1,3),(187,'2018-06-14',1,8),(188,'2018-06-14',-999,9),(189,'2018-06-14',-999,10),(194,'2018-06-15',1,3),(195,'2018-06-15',3,8),(196,'2018-06-15',1,9),(197,'2018-06-15',3,10),(198,'2018-06-16',-999,3),(199,'2018-06-16',-999,8),(200,'2018-06-16',-999,9),(201,'2018-06-16',-999,10),(202,'2018-06-17',-999,3),(203,'2018-06-17',-999,8),(204,'2018-06-17',-999,9),(205,'2018-06-17',-999,10),(206,'2018-06-18',-999,3),(207,'2018-06-18',-999,8),(208,'2018-06-18',-999,9),(209,'2018-06-18',-999,10),(210,'2018-06-19',-999,3),(211,'2018-06-19',-999,8),(212,'2018-06-19',-999,9),(213,'2018-06-19',-999,10),(214,'2018-06-20',1,3),(215,'2018-06-20',1,8),(216,'2018-06-20',1,9),(217,'2018-06-20',1,10),(218,'2018-06-21',-999,3),(219,'2018-06-21',-999,8),(220,'2018-06-21',-999,9),(221,'2018-06-21',-999,10),(222,'2018-08-02',-999,1),(223,'2018-08-02',-999,2),(224,'2018-08-02',-999,4),(225,'2018-08-02',-999,5),(226,'2018-08-02',1,3),(227,'2018-08-02',5,8),(228,'2018-08-02',2,9),(229,'2018-08-02',4,10),(230,'2018-08-03',3,3),(231,'2018-08-03',3,8),(232,'2018-08-03',3,9),(233,'2018-08-03',3,10),(234,'2018-08-04',1,3),(235,'2018-08-04',1,8),(236,'2018-08-04',1,9),(237,'2018-08-04',1,10),(238,'2018-08-05',1,3),(239,'2018-08-05',3,8),(240,'2018-08-05',1,9),(241,'2018-08-05',-999,10),(242,'2018-08-06',-999,3),(243,'2018-08-06',-999,8),(244,'2018-08-06',-999,9),(245,'2018-08-06',-999,10),(246,'2018-08-07',-999,3),(247,'2018-08-07',-999,8),(248,'2018-08-07',-999,9),(249,'2018-08-07',-999,10),(250,'2018-08-08',-999,3),(251,'2018-08-08',-999,8),(252,'2018-08-08',-999,9),(253,'2018-08-08',-999,10),(254,'2018-08-09',-999,3),(255,'2018-08-09',-999,8),(256,'2018-08-09',-999,9),(257,'2018-08-09',-999,10),(258,'2018-08-10',-999,3),(259,'2018-08-10',-999,8),(260,'2018-08-10',-999,9),(261,'2018-08-10',-999,10),(262,'2018-08-11',-999,3),(263,'2018-08-11',-999,8),(264,'2018-08-11',-999,9),(265,'2018-08-11',-999,10),(266,'2018-08-12',-999,3),(267,'2018-08-12',-999,8),(268,'2018-08-12',-999,9),(269,'2018-08-12',-999,10),(270,'2018-08-13',-999,3),(271,'2018-08-13',-999,8),(272,'2018-08-13',-999,9),(273,'2018-08-13',-999,10),(274,'2018-08-14',-999,3),(275,'2018-08-14',-999,8),(276,'2018-08-14',-999,9),(277,'2018-08-14',-999,10),(278,'2018-08-15',-999,3),(279,'2018-08-15',-999,8),(280,'2018-08-15',-999,9),(281,'2018-08-15',-999,10),(282,'2018-08-02',7,13),(283,'2018-08-04',7,13),(284,'2018-08-02',6,12),(285,'2018-08-03',6,12);
/*!40000 ALTER TABLE `duty_dutyschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_dutyschedulemidmodel`
--

DROP TABLE IF EXISTS `duty_dutyschedulemidmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_dutyschedulemidmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dutydate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_dutyschedulemidmodel`
--

LOCK TABLES `duty_dutyschedulemidmodel` WRITE;
/*!40000 ALTER TABLE `duty_dutyschedulemidmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `duty_dutyschedulemidmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_r_departmentinfo_dutyinfo`
--

DROP TABLE IF EXISTS `duty_r_departmentinfo_dutyinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_r_departmentinfo_dutyinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `did_id` int(11) NOT NULL,
  `duid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `duty_r_departmentinf_did_id_a4cb05f0_fk_duty_depa` (`did_id`),
  KEY `duty_r_departmentinf_duid_id_e13552e8_fk_duty_duty` (`duid_id`),
  CONSTRAINT `duty_r_departmentinf_did_id_a4cb05f0_fk_duty_depa` FOREIGN KEY (`did_id`) REFERENCES `duty_departmentinfo` (`did`),
  CONSTRAINT `duty_r_departmentinf_duid_id_e13552e8_fk_duty_duty` FOREIGN KEY (`duid_id`) REFERENCES `duty_dutyinfo` (`duid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_r_departmentinfo_dutyinfo`
--

LOCK TABLES `duty_r_departmentinfo_dutyinfo` WRITE;
/*!40000 ALTER TABLE `duty_r_departmentinfo_dutyinfo` DISABLE KEYS */;
INSERT INTO `duty_r_departmentinfo_dutyinfo` VALUES (-999,-999,-999),(1,1,1),(2,1,2),(3,3,4),(4,1,3),(5,1,4),(8,3,1),(9,3,2),(10,3,3),(11,5,1),(12,9,5),(13,8,6);
/*!40000 ALTER TABLE `duty_r_departmentinfo_dutyinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_r_userinfo_departmentinfo`
--

DROP TABLE IF EXISTS `duty_r_userinfo_departmentinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_r_userinfo_departmentinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `did_id` int(11) NOT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `duty_r_userinfo_depa_did_id_d3acc35f_fk_duty_depa` (`did_id`),
  KEY `duty_r_userinfo_depa_uid_id_4d27970b_fk_duty_user` (`uid_id`),
  CONSTRAINT `duty_r_userinfo_depa_did_id_d3acc35f_fk_duty_depa` FOREIGN KEY (`did_id`) REFERENCES `duty_departmentinfo` (`did`),
  CONSTRAINT `duty_r_userinfo_depa_uid_id_4d27970b_fk_duty_user` FOREIGN KEY (`uid_id`) REFERENCES `duty_userinfo` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_r_userinfo_departmentinfo`
--

LOCK TABLES `duty_r_userinfo_departmentinfo` WRITE;
/*!40000 ALTER TABLE `duty_r_userinfo_departmentinfo` DISABLE KEYS */;
INSERT INTO `duty_r_userinfo_departmentinfo` VALUES (1,3,1),(2,5,2),(3,3,3),(4,1,1),(5,1,2),(6,1,3),(7,1,4),(8,1,5),(9,3,-999),(10,3,2),(11,3,4),(12,3,5),(13,9,6),(14,8,7);
/*!40000 ALTER TABLE `duty_r_userinfo_departmentinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duty_userinfo`
--

DROP TABLE IF EXISTS `duty_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duty_userinfo` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `isdel` tinyint(1) NOT NULL,
  `createdate` date DEFAULT NULL,
  `modeificateddate` date DEFAULT NULL,
  `imgUrl` varchar(200) DEFAULT NULL,
  `level` int(11) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duty_userinfo`
--

LOCK TABLES `duty_userinfo` WRITE;
/*!40000 ALTER TABLE `duty_userinfo` DISABLE KEYS */;
INSERT INTO `duty_userinfo` VALUES (-999,'默认值',0,'2018-05-31','2018-05-31',NULL,4),(1,'李宝辉',0,'2018-04-20','2018-04-20','./src/img/person/预警室/李宝辉.jpg',3),(2,'傅赐福',0,'2018-04-20','2018-04-20','./src/img/person/预警室/傅赐福.jpg',4),(3,'高志一',0,'2018-04-20','2018-04-20','./src/img/person/预警室/高志一.jpg',4),(4,'侯放',0,'2018-05-10','2018-05-10','./src/img/person/预警室/侯放.jpg',4),(5,'王久珂',0,'2018-05-10','2018-05-10','./src/img/person/预警室/王久珂.jpg',4),(6,'易晓蕾',0,'2018-08-30','2018-08-30','./src/img/person/中心领导/易晓蕾.jpg',1),(7,'张志华',0,'2018-08-30','2018-08-30','./src/img/person/业务处/张志华.jpg',2);
/*!40000 ALTER TABLE `duty_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_mytest`
--

DROP TABLE IF EXISTS `users_mytest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_mytest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_mytest`
--

LOCK TABLES `users_mytest` WRITE;
/*!40000 ALTER TABLE `users_mytest` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_mytest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_r_author_department`
--

DROP TABLE IF EXISTS `users_r_author_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_r_author_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid_id` int(11) NOT NULL,
  `did_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_r_author_department_aid_id_05c39f17_fk_auth_user_id` (`aid_id`),
  KEY `users_r_author_depar_did_id_da7e0950_fk_duty_depa` (`did_id`),
  CONSTRAINT `users_r_author_depar_did_id_da7e0950_fk_duty_depa` FOREIGN KEY (`did_id`) REFERENCES `duty_departmentinfo` (`did`),
  CONSTRAINT `users_r_author_department_aid_id_05c39f17_fk_auth_user_id` FOREIGN KEY (`aid_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_r_author_department`
--

LOCK TABLES `users_r_author_department` WRITE;
/*!40000 ALTER TABLE `users_r_author_department` DISABLE KEYS */;
INSERT INTO `users_r_author_department` VALUES (1,3,3),(2,3,5),(3,5,9),(4,6,8);
/*!40000 ALTER TABLE `users_r_author_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_bookmark`
--

DROP TABLE IF EXISTS `xadmin_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_bookmark`
--

LOCK TABLES `xadmin_bookmark` WRITE;
/*!40000 ALTER TABLE `xadmin_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_log`
--

DROP TABLE IF EXISTS `xadmin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_log`
--

LOCK TABLES `xadmin_log` WRITE;
/*!40000 ALTER TABLE `xadmin_log` DISABLE KEYS */;
INSERT INTO `xadmin_log` VALUES (1,'2018-04-19 07:12:07.728313','127.0.0.1','1','DutyInfo object (1)','create','已添加。',8,1),(2,'2018-04-19 07:12:18.579289','127.0.0.1','2','DutyInfo object (2)','create','已添加。',8,1),(3,'2018-04-19 07:12:25.495388','127.0.0.1','3','DutyInfo object (3)','create','已添加。',8,1),(4,'2018-04-19 08:48:14.378600','127.0.0.1','1','DepartmentInfo object (1)','create','已添加。',7,1),(5,'2018-04-19 08:48:27.612197','127.0.0.1','2','DepartmentInfo object (2)','create','已添加。',7,1),(6,'2018-04-19 08:48:37.565861','127.0.0.1','3','DepartmentInfo object (3)','create','已添加。',7,1),(7,'2018-04-19 08:48:47.661197','127.0.0.1','4','DepartmentInfo object (4)','create','已添加。',7,1),(8,'2018-04-19 08:48:56.321998','127.0.0.1','5','DepartmentInfo object (5)','create','已添加。',7,1),(9,'2018-04-20 01:17:18.249412','127.0.0.1','1','UserInfo object (1)','create','已添加。',12,1),(10,'2018-04-20 01:17:21.015424','127.0.0.1','2','UserInfo object (2)','create','已添加。',12,1),(11,'2018-04-20 01:17:23.193612','127.0.0.1','3','UserInfo object (3)','create','已添加。',12,1),(12,'2018-04-20 03:05:16.787529','127.0.0.1','1','R_DepartmentInfo_DutyInfo object (1)','create','已添加。',10,1),(13,'2018-04-20 03:05:27.129612','127.0.0.1','2','R_DepartmentInfo_DutyInfo object (2)','create','已添加。',10,1),(14,'2018-04-23 03:19:23.677333','127.0.0.1','4','24小时班','create','已添加。',8,1),(15,'2018-04-23 03:19:56.166548','127.0.0.1','3','海浪组-24小时班','create','已添加。',10,1),(16,'2018-04-26 02:54:08.399554','127.0.0.1','1','海浪组-值班员A','create','已添加。',11,1),(17,'2018-04-26 02:54:14.401933','127.0.0.1','2','海冰组-值班员B','create','已添加。',11,1),(18,'2018-04-26 02:54:20.235890','127.0.0.1','3','海浪组-值班员C','create','已添加。',11,1),(19,'2018-05-07 01:27:52.008992','127.0.0.1','4','应急组-值班员A','create','已添加。',11,1),(20,'2018-05-07 01:27:54.973558','127.0.0.1','5','应急组-值班员B','create','已添加。',11,1),(21,'2018-05-07 01:27:58.091001','127.0.0.1','6','应急组-值班员C','create','已添加。',11,1),(22,'2018-05-07 01:33:11.383312','127.0.0.1','4','应急组-警报班','create','已添加。',10,1),(23,'2018-05-07 01:33:15.033662','127.0.0.1','5','应急组-24小时班','create','已添加。',10,1),(24,'2018-05-10 00:59:54.320341','127.0.0.1','4','值班员D','create','已添加。',12,1),(25,'2018-05-10 00:59:57.575654','127.0.0.1','5','值班员E','create','已添加。',12,1),(26,'2018-05-10 01:00:34.030337','127.0.0.1','7','应急组-值班员D','create','已添加。',11,1),(27,'2018-05-10 01:00:37.980145','127.0.0.1','8','应急组-值班员E','create','已添加。',11,1),(28,'2018-06-05 02:03:23.249994','127.0.0.1','9','海浪组-默认值','create','已添加。',11,2),(29,'2018-06-05 02:03:54.649510','127.0.0.1','6','海浪组-默认值','create','已添加。',10,2),(30,'2018-06-05 03:04:49.855663','127.0.0.1','7','海冰组-默认值','create','已添加。',10,2),(31,'2018-06-13 01:33:45.457613','127.0.0.1','8','海浪组-主班','create','已添加。',10,1),(32,'2018-06-13 01:33:50.375111','127.0.0.1','9','海浪组-副班','create','已添加。',10,1),(33,'2018-06-13 01:33:54.627137','127.0.0.1','10','海浪组-警报班','create','已添加。',10,1),(34,'2018-06-13 01:35:32.507910','127.0.0.1','11','海冰组-主班','create','已添加。',10,1),(35,'2018-06-26 07:56:37.356386','127.0.0.1','7','海冰组-默认值','delete','',10,1),(36,'2018-06-26 07:56:43.056103','127.0.0.1','6','海浪组-默认值','delete','',10,1),(37,'2018-08-29 07:47:55.193630','127.0.0.1','10','海浪组-傅赐福','create','已添加。',11,2),(38,'2018-08-29 07:48:01.718915','127.0.0.1','11','海浪组-侯放','create','已添加。',11,2),(39,'2018-08-29 07:48:28.777497','127.0.0.1','12','海浪组-王久珂','create','已添加。',11,2),(40,'2018-08-30 07:29:33.990943','127.0.0.1','6','易晓蕾','create','已添加。',12,5),(41,'2018-08-30 07:29:55.046443','127.0.0.1','7','张志华','create','已添加。',12,5),(42,'2018-08-30 07:33:16.929980','127.0.0.1','8','业务处','create','已添加。',7,5),(43,'2018-08-30 07:33:23.254669','127.0.0.1','9','中心领导','create','已添加。',7,5),(44,'2018-08-30 07:33:53.027304','127.0.0.1','5','带班领导','create','已添加。',8,5),(45,'2018-08-30 07:34:14.663208','127.0.0.1','6','业务值班岗','create','已添加。',8,5),(46,'2018-08-30 07:34:24.213064','127.0.0.1','12','中心领导-带班领导','create','已添加。',10,5),(47,'2018-08-30 07:34:32.299773','127.0.0.1','13','业务处-业务值班岗','create','已添加。',10,5),(48,'2018-08-30 07:35:50.930219','127.0.0.1','13','中心领导-易晓蕾','create','已添加。',11,5),(49,'2018-08-30 07:35:58.755434','127.0.0.1','14','业务处-张志华','create','已添加。',11,5);
/*!40000 ALTER TABLE `xadmin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_usersettings`
--

DROP TABLE IF EXISTS `xadmin_usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_usersettings`
--

LOCK TABLES `xadmin_usersettings` WRITE;
/*!40000 ALTER TABLE `xadmin_usersettings` DISABLE KEYS */;
INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',1),(2,'dashboard:home:pos','',2),(3,'dashboard:home:pos','',3),(4,'dashboard:home:pos','',5);
/*!40000 ALTER TABLE `xadmin_usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_userwidget`
--

DROP TABLE IF EXISTS `xadmin_userwidget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_userwidget`
--

LOCK TABLES `xadmin_userwidget` WRITE;
/*!40000 ALTER TABLE `xadmin_userwidget` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_userwidget` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-31 10:00:51
