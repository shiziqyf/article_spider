/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80015 (8.0.15)
 Source Host           : localhost:3306
 Source Schema         : freedom_project

 Target Server Type    : MySQL
 Target Server Version : 80015 (8.0.15)
 File Encoding         : 65001

 Date: 02/03/2023 17:44:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for spider_task
-- ----------------------------
DROP TABLE IF EXISTS `spider_task`;
CREATE TABLE `spider_task` (
  `id` bigint(20) NOT NULL,
  `identifies` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `status` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `module_name` varchar(255) NOT NULL,
  `execute_func_name` varchar(255) NOT NULL,
  `params` text,
  `task_type` varchar(255) DEFAULT NULL,
  `serial_id` varchar(255) NOT NULL,
  `repeat_expire_time` bigint(20) NOT NULL,
  `priority` int(11) NOT NULL,
  `created_time` bigint(20) DEFAULT NULL,
  `gmt_created_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  `gmt_updated_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_identifies` (`identifies`) USING BTREE,
  KEY `idx_status` (`status`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
