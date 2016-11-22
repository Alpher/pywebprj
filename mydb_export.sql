-- MySQL dump 10.13  Distrib 5.7.12, for Win32 (AMD64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.16-log

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
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
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
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 账号状态',7,'add_acctstatus'),(20,'Can change 账号状态',7,'change_acctstatus'),(21,'Can delete 账号状态',7,'delete_acctstatus'),(22,'Can add 地区',8,'add_region'),(23,'Can change 地区',8,'change_region'),(24,'Can delete 地区',8,'delete_region'),(25,'Can add 账号类型',9,'add_accttype'),(26,'Can change 账号类型',9,'change_accttype'),(27,'Can delete 账号类型',9,'delete_accttype'),(28,'Can add 头衔',10,'add_usertitle'),(29,'Can change 头衔',10,'change_usertitle'),(30,'Can delete 头衔',10,'delete_usertitle'),(31,'Can add 中奖纪录',11,'add_myrewards'),(32,'Can change 中奖纪录',11,'change_myrewards'),(33,'Can delete 中奖纪录',11,'delete_myrewards'),(34,'Can add 奖品',12,'add_rewards'),(35,'Can change 奖品',12,'change_rewards'),(36,'Can delete 奖品',12,'delete_rewards'),(37,'Can add 活动类型',13,'add_actiontype'),(38,'Can change 活动类型',13,'change_actiontype'),(39,'Can delete 活动类型',13,'delete_actiontype'),(40,'Can add 奖品类型',14,'add_rewardstype'),(41,'Can change 奖品类型',14,'change_rewardstype'),(42,'Can delete 奖品类型',14,'delete_rewardstype'),(43,'Can add 卡品类型',15,'add_ecardtype'),(44,'Can change 卡品类型',15,'change_ecardtype'),(45,'Can delete 卡品类型',15,'delete_ecardtype'),(46,'Can add 运营商手机号段',16,'add_phonenumtype'),(47,'Can change 运营商手机号段',16,'change_phonenumtype'),(48,'Can delete 运营商手机号段',16,'delete_phonenumtype'),(49,'Can add 卡品清单',17,'add_ecards'),(50,'Can change 卡品清单',17,'change_ecards'),(51,'Can delete 卡品清单',17,'delete_ecards'),(52,'Can add avatar',18,'add_avatar'),(53,'Can change avatar',18,'change_avatar'),(54,'Can delete avatar',18,'delete_avatar'),(55,'Can add 用户积分操作类型',19,'add_uscoreoptype'),(56,'Can change 用户积分操作类型',19,'change_uscoreoptype'),(57,'Can delete 用户积分操作类型',19,'delete_uscoreoptype'),(58,'Can add 用户积分操作历史',20,'add_uscorelog'),(59,'Can change 用户积分操作历史',20,'change_uscorelog'),(60,'Can delete 用户积分操作历史',20,'delete_uscorelog'),(61,'Can add 用户积分统计预览',21,'add_uscoreov'),(62,'Can change 用户积分统计预览',21,'change_uscoreov'),(63,'Can delete 用户积分统计预览',21,'delete_uscoreov');
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
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `acct_type_id` int(11) NOT NULL,
  `birth` date,
  `nickname` varchar(50),
  `phone` varchar(20) DEFAULT NULL,
  `region_id` int(11) NOT NULL,
  `scores` int(11),
  `sex` varchar(10),
  `status_id` int(11) NOT NULL,
  `title_id` int(11) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `auth_user_9366919b` (`acct_type_id`),
  KEY `auth_user_0f442f96` (`region_id`),
  KEY `auth_user_dc91ed4b` (`status_id`),
  KEY `auth_user_1f38f0e7` (`title_id`),
  CONSTRAINT `auth_user_acct_type_id_f23b0d53_fk_profiles_accttype_id` FOREIGN KEY (`acct_type_id`) REFERENCES `profiles_accttype` (`id`),
  CONSTRAINT `auth_user_region_id_b34a28e4_fk_profiles_region_id` FOREIGN KEY (`region_id`) REFERENCES `profiles_region` (`id`),
  CONSTRAINT `auth_user_status_id_7620a729_fk_profiles_acctstatus_id` FOREIGN KEY (`status_id`) REFERENCES `profiles_acctstatus` (`id`),
  CONSTRAINT `auth_user_title_id_1d3a746d_fk_profiles_usertitle_id` FOREIGN KEY (`title_id`) REFERENCES `profiles_usertitle` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$30000$buDivvYl4tOb$PrXEDA9sxdskuHD1uLkrKgXV+oGGZyo3sB+3cl9Xq40=','2016-11-22 21:31:20',1,'admin','','','01050@163.com',1,1,'2016-11-15 12:35:48',1,NULL,'','',1,0,'',1,1,'static/images/useravatars/admin_avatar.jpg'),(3,'pbkdf2_sha256$30000$H1DTd2kBWr0L$u8otrP9moOIpHUpYMLooG4rMRml/TQQVcyOsKw8gDZw=','2016-11-22 21:33:16',0,'user1','','','',0,1,'2016-11-15 12:48:34',1,'1988-02-02','alpher','',1,120,'男',1,1,'static/images/useravatars/user1_avatar.jpg');
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
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
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
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
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
-- Table structure for table `checkin_uscorelog`
--

DROP TABLE IF EXISTS `checkin_uscorelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkin_uscorelog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `score` int(11) NOT NULL,
  `opby` varchar(50) NOT NULL,
  `remark` varchar(1000) DEFAULT NULL,
  `update_ts` datetime NOT NULL,
  `usot_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `checkin_uscorelog_31372fe5` (`usot_id`),
  CONSTRAINT `checkin_uscorelog_usot_id_3acd1b6c_fk_checkin_uscoreoptype_id` FOREIGN KEY (`usot_id`) REFERENCES `checkin_uscoreoptype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkin_uscorelog`
--

LOCK TABLES `checkin_uscorelog` WRITE;
/*!40000 ALTER TABLE `checkin_uscorelog` DISABLE KEYS */;
INSERT INTO `checkin_uscorelog` VALUES (1,'user1',10,'admin','','2016-11-21 21:32:47',1),(9,'user2',15,'system',NULL,'2016-11-22 21:54:43',1),(10,'user3',15,'system',NULL,'2016-11-22 21:55:54',1),(11,'user1',15,'system',NULL,'2016-11-22 22:00:04',1);
/*!40000 ALTER TABLE `checkin_uscorelog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checkin_uscoreoptype`
--

DROP TABLE IF EXISTS `checkin_uscoreoptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkin_uscoreoptype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_code` varchar(50) NOT NULL,
  `type_desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkin_uscoreoptype`
--

LOCK TABLES `checkin_uscoreoptype` WRITE;
/*!40000 ALTER TABLE `checkin_uscoreoptype` DISABLE KEYS */;
INSERT INTO `checkin_uscoreoptype` VALUES (1,'1','签到积分'),(2,'2','兑换抵扣'),(3,'3','违规罚扣');
/*!40000 ALTER TABLE `checkin_uscoreoptype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checkin_uscoreov`
--

DROP TABLE IF EXISTS `checkin_uscoreov`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkin_uscoreov` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `days_in_a_row` int(11) NOT NULL,
  `days_in_month` int(11) NOT NULL,
  `days_in_year` int(11) NOT NULL,
  `accum_score` int(11) NOT NULL,
  `last_chkin_dt` date NOT NULL,
  `last_chkin_score` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkin_uscoreov`
--

LOCK TABLES `checkin_uscoreov` WRITE;
/*!40000 ALTER TABLE `checkin_uscoreov` DISABLE KEYS */;
INSERT INTO `checkin_uscoreov` VALUES (1,'user1',12,15,15,120,'2016-11-22',15);
/*!40000 ALTER TABLE `checkin_uscoreov` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_actiontype`
--

DROP TABLE IF EXISTS `credit_actiontype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_actiontype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actiontype_code` varchar(50) NOT NULL,
  `actiontype_desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_actiontype`
--

LOCK TABLES `credit_actiontype` WRITE;
/*!40000 ALTER TABLE `credit_actiontype` DISABLE KEYS */;
INSERT INTO `credit_actiontype` VALUES (1,'1','积分兑换'),(2,'2','抽奖活动');
/*!40000 ALTER TABLE `credit_actiontype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_ecards`
--

DROP TABLE IF EXISTS `credit_ecards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_ecards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ecardnum` varchar(200) NOT NULL,
  `ecardpsw` varchar(200) NOT NULL,
  `isValid` tinyint(1) NOT NULL,
  `ecardtype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `credit_ecards_1081321d` (`ecardtype_id`),
  CONSTRAINT `credit_ecards_ecardtype_id_d103dc63_fk_credit_ecardtype_id` FOREIGN KEY (`ecardtype_id`) REFERENCES `credit_ecardtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_ecards`
--

LOCK TABLES `credit_ecards` WRITE;
/*!40000 ALTER TABLE `credit_ecards` DISABLE KEYS */;
INSERT INTO `credit_ecards` VALUES (1,'10001','lt001',0,3),(2,'10002','lt002',0,3),(3,'10003','lt003',0,3);
/*!40000 ALTER TABLE `credit_ecards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_ecardtype`
--

DROP TABLE IF EXISTS `credit_ecardtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_ecardtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ecardtype_code` varchar(50) NOT NULL,
  `ecardtype_desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_ecardtype`
--

LOCK TABLES `credit_ecardtype` WRITE;
/*!40000 ALTER TABLE `credit_ecardtype` DISABLE KEYS */;
INSERT INTO `credit_ecardtype` VALUES (1,'EC001','移动'),(2,'EC002','电信'),(3,'EC003','联通');
/*!40000 ALTER TABLE `credit_ecardtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_myrewards`
--

DROP TABLE IF EXISTS `credit_myrewards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_myrewards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `reward_dt` date DEFAULT NULL,
  `isExchg` tinyint(1) NOT NULL,
  `exchg_dt` date DEFAULT NULL,
  `exchg_name` varchar(50) DEFAULT NULL,
  `exchg_phone` varchar(11) DEFAULT NULL,
  `exchg_addr` varchar(1000) DEFAULT NULL,
  `addr_code` varchar(10) DEFAULT NULL,
  `express_id` varchar(100) DEFAULT NULL,
  `express_name` varchar(200) DEFAULT NULL,
  `ecardnum` varchar(200) DEFAULT NULL,
  `update_ts` datetime NOT NULL,
  `reward_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `credit_myrewards_c6279609` (`reward_id`),
  CONSTRAINT `credit_myrewards_reward_id_dd2b6c99_fk_credit_rewards_id` FOREIGN KEY (`reward_id`) REFERENCES `credit_rewards` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_myrewards`
--

LOCK TABLES `credit_myrewards` WRITE;
/*!40000 ALTER TABLE `credit_myrewards` DISABLE KEYS */;
INSERT INTO `credit_myrewards` VALUES (1,'user1','2016-11-15',0,NULL,'','','','','','','','2016-11-15 12:48:19',1),(2,'user1','2016-11-15',1,'2016-11-15','user1','18680221111','addddddr','111111','','','','2016-11-15 13:06:11',2),(3,'user1','2016-11-15',0,'2016-11-15','--','18680222222','--','--','','','10001','2016-11-15 13:44:17',3),(4,'user1','2016-11-15',1,'2016-11-15','','18680222225','','','','','10002','2016-11-15 12:49:19',4);
/*!40000 ALTER TABLE `credit_myrewards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_phonenumtype`
--

DROP TABLE IF EXISTS `credit_phonenumtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_phonenumtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prefixnum` varchar(11) NOT NULL,
  `prefixnumtype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `credit_phonenum_prefixnumtype_id_e6bf9d87_fk_credit_ecardtype_id` (`prefixnumtype_id`),
  CONSTRAINT `credit_phonenum_prefixnumtype_id_e6bf9d87_fk_credit_ecardtype_id` FOREIGN KEY (`prefixnumtype_id`) REFERENCES `credit_ecardtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_phonenumtype`
--

LOCK TABLES `credit_phonenumtype` WRITE;
/*!40000 ALTER TABLE `credit_phonenumtype` DISABLE KEYS */;
INSERT INTO `credit_phonenumtype` VALUES (1,'186',3);
/*!40000 ALTER TABLE `credit_phonenumtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_rewards`
--

DROP TABLE IF EXISTS `credit_rewards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_rewards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reward_code` varchar(50) NOT NULL,
  `reward_desc` varchar(200) NOT NULL,
  `reward_cost` int(11) DEFAULT NULL,
  `reward_effdt` date NOT NULL,
  `reward_enddt` date NOT NULL,
  `reward_nums` int(11) NOT NULL,
  `reward_left` int(11) NOT NULL,
  `reward_rmk` varchar(1000) DEFAULT NULL,
  `action_type_id` int(11) NOT NULL,
  `reward_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `credit_rewards_action_type_id_7b713b7e_fk_credit_actiontype_id` (`action_type_id`),
  KEY `credit_rewards_425d3d13` (`reward_type_id`),
  CONSTRAINT `credit_rewards_action_type_id_7b713b7e_fk_credit_actiontype_id` FOREIGN KEY (`action_type_id`) REFERENCES `credit_actiontype` (`id`),
  CONSTRAINT `credit_rewards_reward_type_id_c44cea67_fk_credit_rewardstype_id` FOREIGN KEY (`reward_type_id`) REFERENCES `credit_rewardstype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_rewards`
--

LOCK TABLES `credit_rewards` WRITE;
/*!40000 ALTER TABLE `credit_rewards` DISABLE KEYS */;
INSERT INTO `credit_rewards` VALUES (1,'R001','保温杯',0,'2016-11-01','2016-11-05',1,1,'',2,1),(2,'R002','加热棒',0,'2016-11-15','2016-11-30',1,1,'',2,1),(3,'R003','50话费-抽奖活动',0,'2016-11-01','2016-11-30',1,1,'',2,2),(4,'R005','50话费-积分兑换',-10,'2016-11-01','2016-11-30',1,1,'',1,2);
/*!40000 ALTER TABLE `credit_rewards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_rewardstype`
--

DROP TABLE IF EXISTS `credit_rewardstype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_rewardstype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rewardstype_code` varchar(50) NOT NULL,
  `rewardstype_desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_rewardstype`
--

LOCK TABLES `credit_rewardstype` WRITE;
/*!40000 ALTER TABLE `credit_rewardstype` DISABLE KEYS */;
INSERT INTO `credit_rewardstype` VALUES (1,'A001','实物'),(2,'V001','虚拟物品');
/*!40000 ALTER TABLE `credit_rewardstype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-11-15 12:38:02','1','移动',1,'[{\"added\": {}}]',15,2),(2,'2016-11-15 12:38:21','2','电信',1,'[{\"added\": {}}]',15,2),(3,'2016-11-15 12:38:38','3','联通',1,'[{\"added\": {}}]',15,2),(4,'2016-11-15 12:38:55','1','186',1,'[{\"added\": {}}]',16,2),(5,'2016-11-15 12:39:40','1','抽奖活动',1,'[{\"added\": {}}]',13,2),(6,'2016-11-15 12:39:54','2','积分兑换',1,'[{\"added\": {}}]',13,2),(7,'2016-11-15 12:40:49','1','实物',1,'[{\"added\": {}}]',14,2),(8,'2016-11-15 12:41:06','2','虚拟物品',1,'[{\"added\": {}}]',14,2),(9,'2016-11-15 12:42:12','2','抽奖活动',2,'[{\"changed\": {\"fields\": [\"actiontype_desc\"]}}]',13,2),(10,'2016-11-15 12:42:27','1','积分兑换',2,'[{\"changed\": {\"fields\": [\"actiontype_desc\"]}}]',13,2),(11,'2016-11-15 12:43:29','1','10001',1,'[{\"added\": {}}]',17,2),(12,'2016-11-15 12:43:42','2','10002',1,'[{\"added\": {}}]',17,2),(13,'2016-11-15 12:43:59','3','10003',1,'[{\"added\": {}}]',17,2),(14,'2016-11-15 12:44:59','1','保温杯',1,'[{\"added\": {}}]',12,2),(15,'2016-11-15 12:45:37','2','加热棒',1,'[{\"added\": {}}]',12,2),(16,'2016-11-15 12:46:18','3','50话费-抽奖活动',1,'[{\"added\": {}}]',12,2),(17,'2016-11-15 12:47:26','4','50话费-积分兑换',1,'[{\"added\": {}}]',12,2),(18,'2016-11-15 12:47:38','2','加热棒',2,'[{\"changed\": {\"fields\": [\"reward_cost\"]}}]',12,2),(19,'2016-11-15 12:48:19','1','中奖序号:1--账号:user1',1,'[{\"added\": {}}]',11,2),(20,'2016-11-15 12:48:34','3','user1',1,'[{\"added\": {}}]',3,2),(21,'2016-11-15 12:48:57','2','中奖序号:2--账号:user1',1,'[{\"added\": {}}]',11,2),(22,'2016-11-15 12:49:11','3','中奖序号:3--账号:user1',1,'[{\"added\": {}}]',11,2),(23,'2016-11-15 12:49:19','4','中奖序号:4--账号:user1',1,'[{\"added\": {}}]',11,2),(24,'2016-11-20 05:02:15','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(25,'2016-11-20 12:34:05','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(26,'2016-11-20 12:37:27','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(27,'2016-11-20 12:48:00','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(28,'2016-11-20 12:49:28','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(29,'2016-11-20 12:51:05','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(30,'2016-11-20 13:02:44','2','admin',2,'[{\"changed\": {\"fields\": [\"avatar\"]}}]',3,2),(31,'2016-11-22 21:32:00','1','签到积分',1,'[{\"added\": {}}]',19,2),(32,'2016-11-22 21:32:10','2','兑换抵扣',1,'[{\"added\": {}}]',19,2),(33,'2016-11-22 21:32:19','3','违规罚扣',1,'[{\"added\": {}}]',19,2),(34,'2016-11-22 21:32:47','1','用户:user1,日志ID:1',1,'[{\"added\": {}}]',20,2),(35,'2016-11-22 21:33:02','1','user1',1,'[{\"added\": {}}]',21,2);
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
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(18,'avatar','avatar'),(20,'checkin','uscorelog'),(19,'checkin','uscoreoptype'),(21,'checkin','uscoreov'),(5,'contenttypes','contenttype'),(13,'credit','actiontype'),(17,'credit','ecards'),(15,'credit','ecardtype'),(11,'credit','myrewards'),(16,'credit','phonenumtype'),(12,'credit','rewards'),(14,'credit','rewardstype'),(7,'profiles','acctstatus'),(9,'profiles','accttype'),(8,'profiles','region'),(10,'profiles','usertitle'),(6,'sessions','session');
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
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-11-15 12:30:39'),(2,'auth','0001_initial','2016-11-15 12:30:44'),(3,'admin','0001_initial','2016-11-15 12:30:44'),(4,'admin','0002_logentry_remove_auto_add','2016-11-15 12:30:44'),(5,'profiles','0001_initial','2016-11-15 12:30:44'),(6,'contenttypes','0002_remove_content_type_name','2016-11-15 12:30:45'),(7,'auth','0002_alter_permission_name_max_length','2016-11-15 12:30:45'),(8,'auth','0003_alter_user_email_max_length','2016-11-15 12:30:46'),(9,'auth','0004_alter_user_username_opts','2016-11-15 12:30:46'),(10,'auth','0005_alter_user_last_login_null','2016-11-15 12:30:47'),(11,'auth','0006_require_contenttypes_0002','2016-11-15 12:30:47'),(12,'auth','0007_alter_validators_add_error_messages','2016-11-15 12:30:47'),(13,'auth','0008_alter_user_username_max_length','2016-11-15 12:30:47'),(14,'auth','0009_auto_20161103_2236','2016-11-15 12:30:51'),(15,'auth','0010_auto_20161106_0918','2016-11-15 12:30:55'),(16,'auth','0011_auto_20161106_1155','2016-11-15 12:30:55'),(17,'credit','0001_initial','2016-11-15 12:30:58'),(18,'profiles','0002_auto_20161115_2030','2016-11-15 12:30:58'),(19,'sessions','0001_initial','2016-11-15 12:30:59'),(20,'avatar','0001_initial','2016-11-19 12:34:34'),(21,'auth','0012_user_avatar','2016-11-20 05:00:55'),(22,'auth','0013_auto_20161120_1553','2016-11-20 07:53:09'),(23,'auth','0014_auto_20161120_1708','2016-11-20 09:08:21'),(24,'auth','0015_auto_20161120_1714','2016-11-20 09:14:51'),(25,'auth','0016_auto_20161120_2042','2016-11-20 12:42:31'),(26,'auth','0017_auto_20161122_2128','2016-11-22 21:28:17'),(27,'checkin','0001_initial','2016-11-22 21:28:19'),(28,'checkin','0002_uscoreov_last_chkin_score','2016-11-22 21:28:19');
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
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('96n1kmfnzdgl7uh3bfj594lf433h9k39','ZWJhNzE4NThjYTI4ODhmMjNkZTc1MTQ3Njc0ZmVlZGM3NWQ3ZGE0Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjNhYzk2ZmQxNjBkMzk3MzdiMWMzMWVlMWMyNWFjMGNlNTBlZTUwYzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2016-12-04 12:58:41'),('gqnkvoirlfdv9g7l3l2re5kyrjuayjav','MzIwODFiZTE4NmI4MmE2MzIwNDZhMGRmMDhmN2RkZWQ4NGNkMDgwMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImY4MzU4ZTgyNmEyN2JiNDliMjA0NmQ5OWNkM2FjNmRiYTQ3NThjN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-12-06 21:33:16'),('uwamjtjwp5gj00741h1emgmfsxz7tpbb','MzIwODFiZTE4NmI4MmE2MzIwNDZhMGRmMDhmN2RkZWQ4NGNkMDgwMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImY4MzU4ZTgyNmEyN2JiNDliMjA0NmQ5OWNkM2FjNmRiYTQ3NThjN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-12-03 12:37:01');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles_acctstatus`
--

DROP TABLE IF EXISTS `profiles_acctstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles_acctstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `acctst_lev` int(11) NOT NULL,
  `acctst_dec` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles_acctstatus`
--

LOCK TABLES `profiles_acctstatus` WRITE;
/*!40000 ALTER TABLE `profiles_acctstatus` DISABLE KEYS */;
INSERT INTO `profiles_acctstatus` VALUES (1,1,'正常');
/*!40000 ALTER TABLE `profiles_acctstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles_accttype`
--

DROP TABLE IF EXISTS `profiles_accttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles_accttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `acct_type_lev` int(11) NOT NULL,
  `acct_type_dec` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles_accttype`
--

LOCK TABLES `profiles_accttype` WRITE;
/*!40000 ALTER TABLE `profiles_accttype` DISABLE KEYS */;
INSERT INTO `profiles_accttype` VALUES (1,1,'普通账号');
/*!40000 ALTER TABLE `profiles_accttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles_region`
--

DROP TABLE IF EXISTS `profiles_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `region_id` int(11) DEFAULT NULL,
  `region_dec` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles_region`
--

LOCK TABLES `profiles_region` WRITE;
/*!40000 ALTER TABLE `profiles_region` DISABLE KEYS */;
INSERT INTO `profiles_region` VALUES (1,1,'广东');
/*!40000 ALTER TABLE `profiles_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles_usertitle`
--

DROP TABLE IF EXISTS `profiles_usertitle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles_usertitle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title_id` int(11) NOT NULL,
  `title_dec` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles_usertitle`
--

LOCK TABLES `profiles_usertitle` WRITE;
/*!40000 ALTER TABLE `profiles_usertitle` DISABLE KEYS */;
INSERT INTO `profiles_usertitle` VALUES (1,1,'新手');
/*!40000 ALTER TABLE `profiles_usertitle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-22 23:20:34
