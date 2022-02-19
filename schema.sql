-- Initialize the database.
-- Drop any existing data and create empty tables.
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
CREATE TABLE IF NOT EXISTS `SYUSER` (
  `UID` varchar(36) NOT NULL,
  `UPDATEDATETIME` datetime DEFAULT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `USERNAME` varchar(100) DEFAULT NULL,
  `AVATER` varchar(200) DEFAULT NULL,
  `PASSWORD` varchar(100) DEFAULT NULL,
  -- `AGE` int(11) DEFAULT NULL,
  -- `LOGINNAME` varchar(100) NOT NULL,
  -- `SEX` varchar(1) DEFAULT NULL,
  -- `EMPLOYDATE` datetime DEFAULT NULL,
  UNIQUE KEY `UK_eiov1gsncrds3rean3dmu822p` (`USERNAME`),
  PRIMARY KEY (`UID`)
) ENGINE = InnoDB DEFAULT CHARSET = gbk;