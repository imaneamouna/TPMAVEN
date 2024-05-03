-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: 14 فبراير 2024 الساعة 20:47
-- إصدار الخادم: 8.3.0
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `php_docker`
--

-- --------------------------------------------------------

--
-- بنية الجدول `php_dacker_table`
--

CREATE TABLE `php_dacker_table` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `date_created` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- إرجاع أو استيراد بيانات الجدول `php_dacker_table`
--

INSERT INTO `php_dacker_table` (`id`, `title`, `description`, `date_created`) VALUES
(1, 'first title', 'first description', '2024-02-01'),
(2, 'second title', '(message)econd description', '2024-02-03');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `php_dacker_table`
--
ALTER TABLE `php_dacker_table`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `php_dacker_table`
--
ALTER TABLE `php_dacker_table`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
