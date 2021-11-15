-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: localhost
-- Üretim Zamanı: 14 Kas 2021, 23:59:41
-- Sunucu sürümü: 10.4.21-MariaDB
-- PHP Sürümü: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `hastane`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `basvurular`
--

CREATE TABLE `basvurular` (
  `name` text NOT NULL,
  `hastalik` text NOT NULL,
  `basvurulacak_pol` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `basvurular`
--

INSERT INTO `basvurular` (`name`, `hastalik`, `basvurulacak_pol`) VALUES
('ucuncuKullanici', 'Kemik Ağrısı', 'Ortopedi'),
('ikinciKullanici', 'Kemik Ağrısı', 'Ortopedi'),
('birinciKullanici', 'Kemik Ağrısı', 'Ortopedi'),
('ikinciKullanici', 'Uyku Sorunu', 'Psikiyatri'),
('Melek Kurt', 'Mide Ağrısı', 'Dahiliye'),
('Melek Kurt', 'Göğüs Ağrısı', 'Kardiyoloji'),
('ucuncuKullanici', 'Göğüs Ağrısı', 'Kardiyoloji');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doctors`
--

CREATE TABLE `doctors` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `doctortitle` text NOT NULL,
  `doctorbranch` text NOT NULL,
  `recordno` text NOT NULL,
  `identitynumber` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `doctors`
--

INSERT INTO `doctors` (`id`, `name`, `doctortitle`, `doctorbranch`, `recordno`, `identitynumber`, `password`) VALUES
(1, 'birinciDoktor', 'Pratisyen Doktor', 'Psikiyatri', '21321654080', '21321654080', '$5$rounds=535000$irZ/6kVDfRTqh0zX$timWi.f0AJZ0CiUTWhAFmElhh7QE.bGs8W8YHktzBe1'),
(2, 'ikinciKullanici', 'Doçent', 'Ortopedi', '22222230808', '22222230808', '$5$rounds=535000$i04LNOvLD9j9dzmo$F5kslkNKiDapCDRO6VBWANZ09DFXVjl/Nk6JSSSLV48'),
(3, 'ucuncuDoktor', 'Profesör', 'Nöroloji', '21321566408', '21321566408', '$5$rounds=535000$T4rP2otzn/Jjt2EY$UlDjt4m6bkLC5Z/zSKjto3GSheqPNhqzS3wMm1HRj88'),
(4, 'Ali Veli', 'Operatör Doktor', 'Dahiliye', '45288102768', '45288102768', '$5$rounds=535000$6j9eBfY2IzhNDpVC$hvKPkArikX78yN5/aMoft5MOTSqQUf3m9pCbpkOR0d.'),
(5, 'Alican Atahan', 'Profesör', 'Kardiyoloji', '11468799882', '11468799882', '$5$rounds=535000$AbMUr1aeZTZT3uXF$iMrjv.nh9LqsZmdSRx6WMe0HT20/pN6c0RAL4rrQVM8');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hastalar`
--

CREATE TABLE `hastalar` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phonenumber` text NOT NULL,
  `identitynumber` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `hastalar`
--

INSERT INTO `hastalar` (`id`, `name`, `email`, `phonenumber`, `identitynumber`, `password`) VALUES
(1, 'birinciKullanici', 'birinciKullanici@gmail.com', '', '12345678088', '$5$rounds=535000$nYnZKoMtSWNcXiv4$RmyGI1.oJCjMauVu/uvzNao41IDdmIRDgD19mZUdZ50'),
(2, 'ikinciKullanici', 'asdasd@gmail.comm', '05365645858', '12345678088', '$5$rounds=535000$aUAmv6dUsDXlyaig$ry7Nd9aq62UzfgIdhe5HOkdbRMNEJSJmxw97744dhL8'),
(3, 'ucuncuKullanici', 'asdasdasd@gmail.com', '05366645858', '12345658088', '$5$rounds=535000$cZZKFdN0YuTYRVXb$yETVggC80OcUa3sllrPN154iK06oCVXCAiZMK8WD.y7'),
(4, 'Melek Kurt', 'melek_kurt@yahoo.com', '05353261215', '45286102768', '$5$rounds=535000$du8JnhKvYWq0WO31$lwB8YE5/RT.f1PeXngSyZIgWhfbg/XE3HCWs94PNGID');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `hastalar`
--
ALTER TABLE `hastalar`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `doctors`
--
ALTER TABLE `doctors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Tablo için AUTO_INCREMENT değeri `hastalar`
--
ALTER TABLE `hastalar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
