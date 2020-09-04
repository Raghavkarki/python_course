-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 07:00 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `libbooks`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `IDnumber` int(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Contact` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `BOOKID` varchar(100) NOT NULL,
  `BOOKtit` varchar(100) NOT NULL,
  `Author` varchar(100) NOT NULL,
  `DateB` varchar(100) NOT NULL,
  `DateD` varchar(100) NOT NULL,
  `lrf` varchar(100) NOT NULL,
  `Dod` varchar(100) NOT NULL,
  `SL` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`IDnumber`, `Name`, `Contact`, `Address`, `BOOKID`, `BOOKtit`, `Author`, `DateB`, `DateD`, `lrf`, `Dod`, `SL`) VALUES
(12, 'rangesh', '98234484', 'india', '15', 'ramayan', 'buktha', '12-15-2020', '19-15-2020', '0$', '9 days', '55$\n'),
(15, 'raghav', '9823470164', 'balaju', '17', 'comic', 'dwayan', '19-7-2020', '21-7-2020', '4$', '9 days', '98$\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`IDnumber`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
