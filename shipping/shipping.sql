# MySQL-Front 5.1  (Build 4.13)

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE */;
/*!40101 SET SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES */;
/*!40103 SET SQL_NOTES='ON' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;


# Host: 127.0.0.1    Database: shipping
# ------------------------------------------------------
# Server version 5.0.45-community-nt

#
# Source for table auth_group
#

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table auth_group
#

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table auth_group_permissions
#

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table auth_group_permissions
#

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table auth_permission
#

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;

#
# Dumping data for table auth_permission
#

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission');
INSERT INTO `auth_permission` VALUES (2,'Can change permission',1,'change_permission');
INSERT INTO `auth_permission` VALUES (3,'Can delete permission',1,'delete_permission');
INSERT INTO `auth_permission` VALUES (4,'Can add group',2,'add_group');
INSERT INTO `auth_permission` VALUES (5,'Can change group',2,'change_group');
INSERT INTO `auth_permission` VALUES (6,'Can delete group',2,'delete_group');
INSERT INTO `auth_permission` VALUES (7,'Can add user',3,'add_user');
INSERT INTO `auth_permission` VALUES (8,'Can change user',3,'change_user');
INSERT INTO `auth_permission` VALUES (9,'Can delete user',3,'delete_user');
INSERT INTO `auth_permission` VALUES (10,'Can add content type',4,'add_contenttype');
INSERT INTO `auth_permission` VALUES (11,'Can change content type',4,'change_contenttype');
INSERT INTO `auth_permission` VALUES (12,'Can delete content type',4,'delete_contenttype');
INSERT INTO `auth_permission` VALUES (13,'Can add session',5,'add_session');
INSERT INTO `auth_permission` VALUES (14,'Can change session',5,'change_session');
INSERT INTO `auth_permission` VALUES (15,'Can delete session',5,'delete_session');
INSERT INTO `auth_permission` VALUES (16,'Can add site',6,'add_site');
INSERT INTO `auth_permission` VALUES (17,'Can change site',6,'change_site');
INSERT INTO `auth_permission` VALUES (18,'Can delete site',6,'delete_site');
INSERT INTO `auth_permission` VALUES (19,'Can add log entry',7,'add_logentry');
INSERT INTO `auth_permission` VALUES (20,'Can change log entry',7,'change_logentry');
INSERT INTO `auth_permission` VALUES (21,'Can delete log entry',7,'delete_logentry');
INSERT INTO `auth_permission` VALUES (22,'Can add 设备',8,'add_device');
INSERT INTO `auth_permission` VALUES (23,'Can change 设备',8,'change_device');
INSERT INTO `auth_permission` VALUES (24,'Can delete 设备',8,'delete_device');
INSERT INTO `auth_permission` VALUES (25,'Can add 特种设备',9,'add_specialdevice');
INSERT INTO `auth_permission` VALUES (26,'Can change 特种设备',9,'change_specialdevice');
INSERT INTO `auth_permission` VALUES (27,'Can delete 特种设备',9,'delete_specialdevice');
INSERT INTO `auth_permission` VALUES (28,'Can add 分包商',10,'add_provider');
INSERT INTO `auth_permission` VALUES (29,'Can change 分包商',10,'change_provider');
INSERT INTO `auth_permission` VALUES (30,'Can delete 分包商',10,'delete_provider');
INSERT INTO `auth_permission` VALUES (31,'Can add 部门',11,'add_department');
INSERT INTO `auth_permission` VALUES (32,'Can change 部门',11,'change_department');
INSERT INTO `auth_permission` VALUES (33,'Can delete 部门',11,'delete_department');
INSERT INTO `auth_permission` VALUES (34,'Can add 能源记录',12,'add_energylog');
INSERT INTO `auth_permission` VALUES (35,'Can change 能源记录',12,'change_energylog');
INSERT INTO `auth_permission` VALUES (36,'Can delete 能源记录',12,'delete_energylog');
INSERT INTO `auth_permission` VALUES (37,'Can add 工作记录',13,'add_worklog');
INSERT INTO `auth_permission` VALUES (38,'Can change 工作记录',13,'change_worklog');
INSERT INTO `auth_permission` VALUES (39,'Can delete 工作记录',13,'delete_worklog');
INSERT INTO `auth_permission` VALUES (40,'Can add 工具记录',14,'add_toollog');
INSERT INTO `auth_permission` VALUES (41,'Can change 工具记录',14,'change_toollog');
INSERT INTO `auth_permission` VALUES (42,'Can delete 工具记录',14,'delete_toollog');
INSERT INTO `auth_permission` VALUES (43,'Can add 派工单',15,'add_assignwork');
INSERT INTO `auth_permission` VALUES (44,'Can change 派工单',15,'change_assignwork');
INSERT INTO `auth_permission` VALUES (45,'Can delete 派工单',15,'delete_assignwork');
INSERT INTO `auth_permission` VALUES (46,'Can add 验收单',16,'add_acceptance');
INSERT INTO `auth_permission` VALUES (47,'Can change 验收单',16,'change_acceptance');
INSERT INTO `auth_permission` VALUES (48,'Can delete 验收单',16,'delete_acceptance');
INSERT INTO `auth_permission` VALUES (49,'Can add 报价单',17,'add_bidding');
INSERT INTO `auth_permission` VALUES (50,'Can change 报价单',17,'change_bidding');
INSERT INTO `auth_permission` VALUES (51,'Can delete 报价单',17,'delete_bidding');
INSERT INTO `auth_permission` VALUES (52,'Can add 估价单',18,'add_estimate');
INSERT INTO `auth_permission` VALUES (53,'Can change 估价单',18,'change_estimate');
INSERT INTO `auth_permission` VALUES (54,'Can delete 估价单',18,'delete_estimate');
INSERT INTO `auth_permission` VALUES (55,'Can add 支付费用',19,'add_payment');
INSERT INTO `auth_permission` VALUES (56,'Can change 支付费用',19,'change_payment');
INSERT INTO `auth_permission` VALUES (57,'Can delete 支付费用',19,'delete_payment');
INSERT INTO `auth_permission` VALUES (58,'Can add 项目',20,'add_project');
INSERT INTO `auth_permission` VALUES (59,'Can change 项目',20,'change_project');
INSERT INTO `auth_permission` VALUES (60,'Can delete 项目',20,'delete_project');
INSERT INTO `auth_permission` VALUES (61,'Can add project item',21,'add_projectitem');
INSERT INTO `auth_permission` VALUES (62,'Can change project item',21,'change_projectitem');
INSERT INTO `auth_permission` VALUES (63,'Can delete project item',21,'delete_projectitem');
INSERT INTO `auth_permission` VALUES (64,'Can add 事件',22,'add_event');
INSERT INTO `auth_permission` VALUES (65,'Can change 事件',22,'change_event');
INSERT INTO `auth_permission` VALUES (66,'Can delete 事件',22,'delete_event');
INSERT INTO `auth_permission` VALUES (67,'Can add 派工',23,'add_assignwork');
INSERT INTO `auth_permission` VALUES (68,'Can change 派工',23,'change_assignwork');
INSERT INTO `auth_permission` VALUES (69,'Can delete 派工',23,'delete_assignwork');
INSERT INTO `auth_permission` VALUES (70,'Can add 领料',24,'add_claimmaterial');
INSERT INTO `auth_permission` VALUES (71,'Can change 领料',24,'change_claimmaterial');
INSERT INTO `auth_permission` VALUES (72,'Can delete 领料',24,'delete_claimmaterial');
INSERT INTO `auth_permission` VALUES (73,'Can add 合同',25,'add_contract');
INSERT INTO `auth_permission` VALUES (74,'Can change 合同',25,'change_contract');
INSERT INTO `auth_permission` VALUES (75,'Can delete 合同',25,'delete_contract');
INSERT INTO `auth_permission` VALUES (76,'Can add project tree',26,'add_projecttree');
INSERT INTO `auth_permission` VALUES (77,'Can change project tree',26,'change_projecttree');
INSERT INTO `auth_permission` VALUES (78,'Can delete project tree',26,'delete_projecttree');
INSERT INTO `auth_permission` VALUES (79,'Can add event node',27,'add_eventnode');
INSERT INTO `auth_permission` VALUES (80,'Can change event node',27,'change_eventnode');
INSERT INTO `auth_permission` VALUES (81,'Can delete event node',27,'delete_eventnode');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table auth_user
#

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table auth_user
#

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'lijie','','','lijiemjx@163.com','pbkdf2_sha256$10000$5Kg9hw5wOsEv$rRGcCZvpBRktlGK0e/Wcm9xEqvddACkwhCWMMdQlUU4=',1,1,1,'2013-03-22 22:41:32','2013-03-22 22:40:25');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table auth_user_groups
#

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table auth_user_groups
#

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table auth_user_user_permissions
#

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table auth_user_user_permissions
#

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table daily_department
#

DROP TABLE IF EXISTS `daily_department`;
CREATE TABLE `daily_department` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table daily_department
#

LOCK TABLES `daily_department` WRITE;
/*!40000 ALTER TABLE `daily_department` DISABLE KEYS */;
INSERT INTO `daily_department` VALUES (1,'部门1');
/*!40000 ALTER TABLE `daily_department` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table daily_energylog
#

DROP TABLE IF EXISTS `daily_energylog`;
CREATE TABLE `daily_energylog` (
  `id` int(11) NOT NULL auto_increment,
  `date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `daily_energylog_403f60f` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table daily_energylog
#

LOCK TABLES `daily_energylog` WRITE;
/*!40000 ALTER TABLE `daily_energylog` DISABLE KEYS */;
/*!40000 ALTER TABLE `daily_energylog` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table daily_provider
#

DROP TABLE IF EXISTS `daily_provider`;
CREATE TABLE `daily_provider` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table daily_provider
#

LOCK TABLES `daily_provider` WRITE;
/*!40000 ALTER TABLE `daily_provider` DISABLE KEYS */;
INSERT INTO `daily_provider` VALUES (1,'分包商1');
/*!40000 ALTER TABLE `daily_provider` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table daily_toollog
#

DROP TABLE IF EXISTS `daily_toollog`;
CREATE TABLE `daily_toollog` (
  `id` int(11) NOT NULL auto_increment,
  `date` date NOT NULL,
  `type` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `daily_toollog_5d52dd10` (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table daily_toollog
#

LOCK TABLES `daily_toollog` WRITE;
/*!40000 ALTER TABLE `daily_toollog` DISABLE KEYS */;
/*!40000 ALTER TABLE `daily_toollog` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table daily_worklog
#

DROP TABLE IF EXISTS `daily_worklog`;
CREATE TABLE `daily_worklog` (
  `id` int(11) NOT NULL auto_increment,
  `date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `log` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `daily_worklog_403f60f` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table daily_worklog
#

LOCK TABLES `daily_worklog` WRITE;
/*!40000 ALTER TABLE `daily_worklog` DISABLE KEYS */;
/*!40000 ALTER TABLE `daily_worklog` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table device_device
#

DROP TABLE IF EXISTS `device_device`;
CREATE TABLE `device_device` (
  `id` int(11) NOT NULL auto_increment,
  `number` varchar(40) NOT NULL,
  `name` varchar(40) NOT NULL,
  `type` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `capital` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

#
# Dumping data for table device_device
#

LOCK TABLES `device_device` WRITE;
/*!40000 ALTER TABLE `device_device` DISABLE KEYS */;
INSERT INTO `device_device` VALUES (1,'资产1','设备','1','1',0,'2013-03-22');
INSERT INTO `device_device` VALUES (2,'21','2','2','2',0,'2013-03-22');
INSERT INTO `device_device` VALUES (3,'4','4','4','4',0,'2013-03-22');
/*!40000 ALTER TABLE `device_device` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table device_specialdevice
#

DROP TABLE IF EXISTS `device_specialdevice`;
CREATE TABLE `device_specialdevice` (
  `device_ptr_id` int(11) NOT NULL,
  `old_number` varchar(40) NOT NULL,
  `safe_start` varchar(40) NOT NULL,
  `production_date` date NOT NULL,
  `manufacturer` varchar(100) NOT NULL,
  `license_unit` varchar(100) NOT NULL,
  `license_period` varchar(50) NOT NULL,
  `license_number` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `memo` longtext NOT NULL,
  `scan_document` varchar(100) NOT NULL,
  PRIMARY KEY  (`device_ptr_id`),
  KEY `device_specialdevice_2ae7390` (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table device_specialdevice
#

LOCK TABLES `device_specialdevice` WRITE;
/*!40000 ALTER TABLE `device_specialdevice` DISABLE KEYS */;
/*!40000 ALTER TABLE `device_specialdevice` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table django_admin_log
#

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) default NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

#
# Dumping data for table django_admin_log
#

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-03-22 22:43:05',1,20,'1','[1] project1',1,'');
INSERT INTO `django_admin_log` VALUES (2,'2013-03-22 22:45:39',1,11,'1','部门1',1,'');
INSERT INTO `django_admin_log` VALUES (3,'2013-03-22 22:45:57',1,10,'1','分包商1',1,'');
INSERT INTO `django_admin_log` VALUES (4,'2013-03-22 22:46:05',1,19,'1','[2013-03-22] 支付费用1',1,'');
INSERT INTO `django_admin_log` VALUES (5,'2013-03-22 22:46:08',1,25,'1','太阳能热水器系统设备订货合同书',1,'');
INSERT INTO `django_admin_log` VALUES (6,'2013-03-22 22:46:34',1,24,'3','2013-03-22',1,'');
INSERT INTO `django_admin_log` VALUES (7,'2013-03-22 22:47:11',1,8,'1','[资产1] 1',1,'');
INSERT INTO `django_admin_log` VALUES (8,'2013-03-22 22:47:21',1,8,'2','[21] 2',1,'');
INSERT INTO `django_admin_log` VALUES (9,'2013-03-22 22:47:32',1,8,'3','[4] 4',1,'');
INSERT INTO `django_admin_log` VALUES (10,'2013-03-22 22:47:52',1,15,'1','维修编号:1, 派工单编号1',1,'');
INSERT INTO `django_admin_log` VALUES (11,'2013-03-22 22:48:03',1,16,'1','[2013-03-22] 32',1,'');
INSERT INTO `django_admin_log` VALUES (12,'2013-03-22 22:48:10',1,17,'1','[2013-03-22] 撒的分撒的分',1,'');
INSERT INTO `django_admin_log` VALUES (13,'2013-03-22 22:48:23',1,18,'1','[2013-03-22] 发撒地方',1,'');
INSERT INTO `django_admin_log` VALUES (14,'2013-03-22 22:48:27',1,23,'5','2013-03-22',1,'');
INSERT INTO `django_admin_log` VALUES (15,'2013-03-22 22:48:44',1,22,'7','2013-03-22',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table django_content_type
#

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

#
# Dumping data for table django_content_type
#

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission');
INSERT INTO `django_content_type` VALUES (2,'group','auth','group');
INSERT INTO `django_content_type` VALUES (3,'user','auth','user');
INSERT INTO `django_content_type` VALUES (4,'content type','contenttypes','contenttype');
INSERT INTO `django_content_type` VALUES (5,'session','sessions','session');
INSERT INTO `django_content_type` VALUES (6,'site','sites','site');
INSERT INTO `django_content_type` VALUES (7,'log entry','admin','logentry');
INSERT INTO `django_content_type` VALUES (8,'设备','device','device');
INSERT INTO `django_content_type` VALUES (9,'特种设备','device','specialdevice');
INSERT INTO `django_content_type` VALUES (10,'分包商','daily','provider');
INSERT INTO `django_content_type` VALUES (11,'部门','daily','department');
INSERT INTO `django_content_type` VALUES (12,'能源记录','daily','energylog');
INSERT INTO `django_content_type` VALUES (13,'工作记录','daily','worklog');
INSERT INTO `django_content_type` VALUES (14,'工具记录','daily','toollog');
INSERT INTO `django_content_type` VALUES (15,'派工单','sheet','assignwork');
INSERT INTO `django_content_type` VALUES (16,'验收单','sheet','acceptance');
INSERT INTO `django_content_type` VALUES (17,'报价单','sheet','bidding');
INSERT INTO `django_content_type` VALUES (18,'估价单','sheet','estimate');
INSERT INTO `django_content_type` VALUES (19,'支付费用','sheet','payment');
INSERT INTO `django_content_type` VALUES (20,'项目','project','project');
INSERT INTO `django_content_type` VALUES (21,'project item','project','projectitem');
INSERT INTO `django_content_type` VALUES (22,'事件','project','event');
INSERT INTO `django_content_type` VALUES (23,'派工','project','assignwork');
INSERT INTO `django_content_type` VALUES (24,'领料','project','claimmaterial');
INSERT INTO `django_content_type` VALUES (25,'合同','project','contract');
INSERT INTO `django_content_type` VALUES (26,'project tree','tree','projecttree');
INSERT INTO `django_content_type` VALUES (27,'event node','tree','eventnode');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table django_session
#

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table django_session
#

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('096a8bb7388bb399539fff3be9e09dfa','NWI4Yzg4ODBiMDEzZTkxMDRmYjBlODgzZGU4MzFhYzZlODY1ZWU0MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-04-05 22:41:32');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table django_site
#

DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table django_site
#

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table project_assignwork
#

DROP TABLE IF EXISTS `project_assignwork`;
CREATE TABLE `project_assignwork` (
  `projectitem_ptr_id` int(11) NOT NULL,
  `assign_work_sheet_id` int(11) default NULL,
  `acceptance_sheet_id` int(11) default NULL,
  `bidding_sheet_id` int(11) default NULL,
  `estimate_sheet_id` int(11) default NULL,
  `payment_id` int(11) default NULL,
  PRIMARY KEY  (`projectitem_ptr_id`),
  KEY `project_assignwork_ff2ac18` (`assign_work_sheet_id`),
  KEY `project_assignwork_7028db5f` (`acceptance_sheet_id`),
  KEY `project_assignwork_4dde87a8` (`bidding_sheet_id`),
  KEY `project_assignwork_182f297c` (`estimate_sheet_id`),
  KEY `project_assignwork_7bd3acc3` (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table project_assignwork
#

LOCK TABLES `project_assignwork` WRITE;
/*!40000 ALTER TABLE `project_assignwork` DISABLE KEYS */;
INSERT INTO `project_assignwork` VALUES (5,1,1,1,1,1);
/*!40000 ALTER TABLE `project_assignwork` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table project_claimmaterial
#

DROP TABLE IF EXISTS `project_claimmaterial`;
CREATE TABLE `project_claimmaterial` (
  `projectitem_ptr_id` int(11) NOT NULL,
  `claimer_id` int(11) NOT NULL,
  `price` double NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY  (`projectitem_ptr_id`),
  KEY `project_claimmaterial_4f995b26` (`claimer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table project_claimmaterial
#

LOCK TABLES `project_claimmaterial` WRITE;
/*!40000 ALTER TABLE `project_claimmaterial` DISABLE KEYS */;
INSERT INTO `project_claimmaterial` VALUES (3,1,23,'领料');
/*!40000 ALTER TABLE `project_claimmaterial` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table project_contract
#

DROP TABLE IF EXISTS `project_contract`;
CREATE TABLE `project_contract` (
  `projectitem_ptr_id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `scan_document` varchar(100) NOT NULL,
  `payment_id` int(11) default NULL,
  PRIMARY KEY  (`projectitem_ptr_id`),
  KEY `project_contract_7bd3acc3` (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table project_contract
#

LOCK TABLES `project_contract` WRITE;
/*!40000 ALTER TABLE `project_contract` DISABLE KEYS */;
INSERT INTO `project_contract` VALUES (1,'太阳能热水器系统设备订货合同书','太阳能热水器系统设备订货合同书','media/contract/hetong.jpg',1);
/*!40000 ALTER TABLE `project_contract` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table project_event
#

DROP TABLE IF EXISTS `project_event`;
CREATE TABLE `project_event` (
  `projectitem_ptr_id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY  (`projectitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table project_event
#

LOCK TABLES `project_event` WRITE;
/*!40000 ALTER TABLE `project_event` DISABLE KEYS */;
INSERT INTO `project_event` VALUES (7,'生发生大幅');
/*!40000 ALTER TABLE `project_event` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table project_project
#

DROP TABLE IF EXISTS `project_project`;
CREATE TABLE `project_project` (
  `id` int(11) NOT NULL auto_increment,
  `type` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `manager_id` int(11) NOT NULL,
  `investment` int(11) NOT NULL,
  `reply` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `project_project_501a2222` (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table project_project
#

LOCK TABLES `project_project` WRITE;
/*!40000 ALTER TABLE `project_project` DISABLE KEYS */;
INSERT INTO `project_project` VALUES (1,0,'太阳能供热系统','基建项目1',1,111,'同意','2013-03-22');
/*!40000 ALTER TABLE `project_project` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table project_projectitem
#

DROP TABLE IF EXISTS `project_projectitem`;
CREATE TABLE `project_projectitem` (
  `id` int(11) NOT NULL auto_increment,
  `project_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `parent_id` int(11) default NULL,
  `rank` int(11) default NULL,
  `index` int(11) default NULL,
  PRIMARY KEY  (`id`),
  KEY `project_projectitem_499df97c` (`project_id`),
  KEY `project_projectitem_63f17a16` (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

#
# Dumping data for table project_projectitem
#

LOCK TABLES `project_projectitem` WRITE;
/*!40000 ALTER TABLE `project_projectitem` DISABLE KEYS */;
INSERT INTO `project_projectitem` VALUES (1,1,'2013-03-22',NULL,-1,-1);
INSERT INTO `project_projectitem` VALUES (2,1,'2013-03-22',NULL,0,1);
INSERT INTO `project_projectitem` VALUES (3,1,'2013-03-22',NULL,-1,-1);
INSERT INTO `project_projectitem` VALUES (4,1,'2013-03-22',NULL,1,3);
INSERT INTO `project_projectitem` VALUES (5,1,'2013-03-22',NULL,-1,-1);
INSERT INTO `project_projectitem` VALUES (6,1,'2013-03-22',NULL,2,5);
INSERT INTO `project_projectitem` VALUES (7,1,'2013-03-22',NULL,-1,-1);
INSERT INTO `project_projectitem` VALUES (8,1,'2013-03-22',10,0,7);
INSERT INTO `project_projectitem` VALUES (9,1,'2013-03-22',2,0,5);
INSERT INTO `project_projectitem` VALUES (10,1,'2013-03-22',4,0,7);
/*!40000 ALTER TABLE `project_projectitem` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table sheet_acceptance
#

DROP TABLE IF EXISTS `sheet_acceptance`;
CREATE TABLE `sheet_acceptance` (
  `id` int(11) NOT NULL auto_increment,
  `requirement` varchar(100) NOT NULL,
  `other_requirement` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `check_date` date NOT NULL,
  `finish_date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table sheet_acceptance
#

LOCK TABLES `sheet_acceptance` WRITE;
/*!40000 ALTER TABLE `sheet_acceptance` DISABLE KEYS */;
INSERT INTO `sheet_acceptance` VALUES (1,'验收要求','23','32','2013-03-22','2013-03-22');
/*!40000 ALTER TABLE `sheet_acceptance` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table sheet_assignwork
#

DROP TABLE IF EXISTS `sheet_assignwork`;
CREATE TABLE `sheet_assignwork` (
  `id` int(11) NOT NULL auto_increment,
  `number` varchar(40) NOT NULL,
  `assign_work_number` varchar(40) NOT NULL,
  `contractor_id` int(11) NOT NULL,
  `assign_work_date` date NOT NULL,
  `require_finish_date` date NOT NULL,
  `description` longtext NOT NULL,
  `capital_id` int(11) default NULL,
  `location_id` int(11) default NULL,
  `device_id` int(11) default NULL,
  `manager_id` int(11) NOT NULL,
  `safety_hint` varchar(40) NOT NULL,
  `acceptance` varchar(40) NOT NULL,
  `scan_document` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `sheet_assignwork_5eeefde9` (`contractor_id`),
  KEY `sheet_assignwork_26302b89` (`capital_id`),
  KEY `sheet_assignwork_319d859` (`location_id`),
  KEY `sheet_assignwork_5b7abc50` (`device_id`),
  KEY `sheet_assignwork_501a2222` (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table sheet_assignwork
#

LOCK TABLES `sheet_assignwork` WRITE;
/*!40000 ALTER TABLE `sheet_assignwork` DISABLE KEYS */;
INSERT INTO `sheet_assignwork` VALUES (1,'1','1',1,'2013-03-22','2013-03-22','维修',1,2,3,1,'注意安全','验收要求','media/assign_work/1_1.jpg','2013-03-22');
/*!40000 ALTER TABLE `sheet_assignwork` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table sheet_bidding
#

DROP TABLE IF EXISTS `sheet_bidding`;
CREATE TABLE `sheet_bidding` (
  `id` int(11) NOT NULL auto_increment,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table sheet_bidding
#

LOCK TABLES `sheet_bidding` WRITE;
/*!40000 ALTER TABLE `sheet_bidding` DISABLE KEYS */;
INSERT INTO `sheet_bidding` VALUES (1,'撒的分撒的分','2013-03-22');
/*!40000 ALTER TABLE `sheet_bidding` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table sheet_estimate
#

DROP TABLE IF EXISTS `sheet_estimate`;
CREATE TABLE `sheet_estimate` (
  `id` int(11) NOT NULL auto_increment,
  `estimator_id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  `scan_document` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `sheet_estimate_660fbc4b` (`estimator_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table sheet_estimate
#

LOCK TABLES `sheet_estimate` WRITE;
/*!40000 ALTER TABLE `sheet_estimate` DISABLE KEYS */;
INSERT INTO `sheet_estimate` VALUES (1,1,'发撒地方','2013-03-22','media/estimation/gujia.jpg');
/*!40000 ALTER TABLE `sheet_estimate` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table sheet_payment
#

DROP TABLE IF EXISTS `sheet_payment`;
CREATE TABLE `sheet_payment` (
  `id` int(11) NOT NULL auto_increment,
  `date` date NOT NULL,
  `department_id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `operator_id` int(11) NOT NULL,
  `account` varchar(20) NOT NULL,
  `provider_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `number` varchar(40) NOT NULL,
  `category` varchar(40) NOT NULL,
  `will_pay` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `sheet_payment_2ae7390` (`department_id`),
  KEY `sheet_payment_4198106c` (`operator_id`),
  KEY `sheet_payment_261a2069` (`provider_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table sheet_payment
#

LOCK TABLES `sheet_payment` WRITE;
/*!40000 ALTER TABLE `sheet_payment` DISABLE KEYS */;
INSERT INTO `sheet_payment` VALUES (1,'2013-03-22',1,'支付费用1',1,'11111111111111',1,111,'1212','1',1);
/*!40000 ALTER TABLE `sheet_payment` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tree_eventnode
#

DROP TABLE IF EXISTS `tree_eventnode`;
CREATE TABLE `tree_eventnode` (
  `id` int(11) NOT NULL auto_increment,
  `first_child` int(11) NOT NULL,
  `next_sibling` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table tree_eventnode
#

LOCK TABLES `tree_eventnode` WRITE;
/*!40000 ALTER TABLE `tree_eventnode` DISABLE KEYS */;
/*!40000 ALTER TABLE `tree_eventnode` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tree_projecttree
#

DROP TABLE IF EXISTS `tree_projecttree`;
CREATE TABLE `tree_projecttree` (
  `id` int(11) NOT NULL auto_increment,
  `project_id` int(11) NOT NULL,
  `root` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `tree_projecttree_499df97c` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table tree_projecttree
#

LOCK TABLES `tree_projecttree` WRITE;
/*!40000 ALTER TABLE `tree_projecttree` DISABLE KEYS */;
/*!40000 ALTER TABLE `tree_projecttree` ENABLE KEYS */;
UNLOCK TABLES;

#
#  Foreign keys for table auth_group_permissions
#

ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

#
#  Foreign keys for table auth_permission
#

ALTER TABLE `auth_permission`
ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

#
#  Foreign keys for table auth_user_groups
#

ALTER TABLE `auth_user_groups`
ADD CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table auth_user_user_permissions
#

ALTER TABLE `auth_user_user_permissions`
ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table daily_energylog
#

ALTER TABLE `daily_energylog`
ADD CONSTRAINT `user_id_refs_id_38f193a1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table daily_toollog
#

ALTER TABLE `daily_toollog`
ADD CONSTRAINT `owner_id_refs_id_4e64b0b9` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table daily_worklog
#

ALTER TABLE `daily_worklog`
ADD CONSTRAINT `user_id_refs_id_74929360` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table device_specialdevice
#

ALTER TABLE `device_specialdevice`
ADD CONSTRAINT `department_id_refs_id_1a87ba41` FOREIGN KEY (`department_id`) REFERENCES `daily_department` (`id`),
ADD CONSTRAINT `device_ptr_id_refs_id_8c50ac1` FOREIGN KEY (`device_ptr_id`) REFERENCES `device_device` (`id`);

#
#  Foreign keys for table django_admin_log
#

ALTER TABLE `django_admin_log`
ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table project_assignwork
#

ALTER TABLE `project_assignwork`
ADD CONSTRAINT `acceptance_sheet_id_refs_id_1ce90ec0` FOREIGN KEY (`acceptance_sheet_id`) REFERENCES `sheet_acceptance` (`id`),
ADD CONSTRAINT `assign_work_sheet_id_refs_id_62b87881` FOREIGN KEY (`assign_work_sheet_id`) REFERENCES `sheet_assignwork` (`id`),
ADD CONSTRAINT `bidding_sheet_id_refs_id_6c792f99` FOREIGN KEY (`bidding_sheet_id`) REFERENCES `sheet_bidding` (`id`),
ADD CONSTRAINT `estimate_sheet_id_refs_id_4b7472e9` FOREIGN KEY (`estimate_sheet_id`) REFERENCES `sheet_estimate` (`id`),
ADD CONSTRAINT `payment_id_refs_id_15236346` FOREIGN KEY (`payment_id`) REFERENCES `sheet_payment` (`id`),
ADD CONSTRAINT `projectitem_ptr_id_refs_id_7221570e` FOREIGN KEY (`projectitem_ptr_id`) REFERENCES `project_projectitem` (`id`);

#
#  Foreign keys for table project_claimmaterial
#

ALTER TABLE `project_claimmaterial`
ADD CONSTRAINT `claimer_id_refs_id_528c2a50` FOREIGN KEY (`claimer_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `projectitem_ptr_id_refs_id_62598116` FOREIGN KEY (`projectitem_ptr_id`) REFERENCES `project_projectitem` (`id`);

#
#  Foreign keys for table project_contract
#

ALTER TABLE `project_contract`
ADD CONSTRAINT `payment_id_refs_id_4e471e8a` FOREIGN KEY (`payment_id`) REFERENCES `sheet_payment` (`id`),
ADD CONSTRAINT `projectitem_ptr_id_refs_id_dd03082` FOREIGN KEY (`projectitem_ptr_id`) REFERENCES `project_projectitem` (`id`);

#
#  Foreign keys for table project_event
#

ALTER TABLE `project_event`
ADD CONSTRAINT `projectitem_ptr_id_refs_id_6a7577b3` FOREIGN KEY (`projectitem_ptr_id`) REFERENCES `project_projectitem` (`id`);

#
#  Foreign keys for table project_project
#

ALTER TABLE `project_project`
ADD CONSTRAINT `manager_id_refs_id_b79dcd2` FOREIGN KEY (`manager_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table project_projectitem
#

ALTER TABLE `project_projectitem`
ADD CONSTRAINT `parent_id_refs_id_b290425` FOREIGN KEY (`parent_id`) REFERENCES `project_projectitem` (`id`),
ADD CONSTRAINT `project_id_refs_id_170d3532` FOREIGN KEY (`project_id`) REFERENCES `project_project` (`id`);

#
#  Foreign keys for table sheet_assignwork
#

ALTER TABLE `sheet_assignwork`
ADD CONSTRAINT `capital_id_refs_id_312de0b5` FOREIGN KEY (`capital_id`) REFERENCES `device_device` (`id`),
ADD CONSTRAINT `contractor_id_refs_id_5480da0a` FOREIGN KEY (`contractor_id`) REFERENCES `daily_provider` (`id`),
ADD CONSTRAINT `device_id_refs_id_312de0b5` FOREIGN KEY (`device_id`) REFERENCES `device_device` (`id`),
ADD CONSTRAINT `location_id_refs_id_312de0b5` FOREIGN KEY (`location_id`) REFERENCES `device_device` (`id`),
ADD CONSTRAINT `manager_id_refs_id_3a0d9a28` FOREIGN KEY (`manager_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table sheet_estimate
#

ALTER TABLE `sheet_estimate`
ADD CONSTRAINT `estimator_id_refs_id_12fe0bd0` FOREIGN KEY (`estimator_id`) REFERENCES `auth_user` (`id`);

#
#  Foreign keys for table sheet_payment
#

ALTER TABLE `sheet_payment`
ADD CONSTRAINT `department_id_refs_id_75aba4d8` FOREIGN KEY (`department_id`) REFERENCES `daily_department` (`id`),
ADD CONSTRAINT `operator_id_refs_id_261b6b93` FOREIGN KEY (`operator_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `provider_id_refs_id_6aab49a5` FOREIGN KEY (`provider_id`) REFERENCES `daily_provider` (`id`);

#
#  Foreign keys for table tree_projecttree
#

ALTER TABLE `tree_projecttree`
ADD CONSTRAINT `project_id_refs_id_132adabb` FOREIGN KEY (`project_id`) REFERENCES `project_project` (`id`);


/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
