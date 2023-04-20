-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2022 at 06:51 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kakashi_chatbot`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(9) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'All-rounder'),
(2, 'Cruiser'),
(3, 'Sport'),
(4, 'Off-road');

-- --------------------------------------------------------

--
-- Table structure for table `motorcycles`
--

CREATE TABLE `motorcycles` (
  `id_number` int(9) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` varchar(9) NOT NULL,
  `power` varchar(9) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `fuel_capacity` varchar(9) NOT NULL,
  `year` varchar(10) NOT NULL,
  `category_id` int(100) NOT NULL,
  `description` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `motorcycles`
--

INSERT INTO `motorcycles` (`id_number`, `name`, `price`, `power`, `brand`, `fuel_capacity`, `year`, `category_id`, `description`) VALUES
(1, 'S 1000 R', '11000', '120', 'BMW', '32', '2009', 3, 'This bike has a wet weight of 204 kg (450 lb), and produces 148.4 kW (199.0 hp; 201.8 PS) at 13,500 rpm. With 133.6 kW (179.2 hp; 181.6 PS) to the rear wheel, it was the most powerful motorcycle in the class on the dyno.'),
(2, 'Lac Rose', '12000', '110', 'BMW', '34', '2005', 4, 'This bike is BMW\'s individual interpretation of the bike that won the Paris-Dakar Rallye in 1985. It puts the BMW R nineT into an exciting new context and shows what passion for our brand heritage, imagination and a few modifications can achieve.'),
(3, 'F 650 cs scarver', '5000', '55', 'BMW', '25', '1989', 1, 'CS stood for city/street, as it was aimed at urban commuters and it was also known as the Scarver, a portmanteau of street and carver.'),
(4, 'R 100', '6500', '72', 'BMW', '45', '2001', 2, 'The R100 was the mainstay of BMW\'s range between 1976 and 1996, giving it an incredible 20-year production run. It\'s now hugely popular with custom builders, who have transformed R100s into cafe racers, bobbers, scramblers and street trackers.'),
(5, 'Ninja rr', '8000', '60', 'Kawasaki', '30', '2005', 3, 'Kawasaki Ninja RR Mono is one of the most powerful quarter liter motorcycle on sale internationally. It is powered by a 249cc, single cylinder, 4-stroke engine producing 27.62 BHP and 22.6 Nm of torque. Kawasaki mated the engine to a 6-speed gearbox, claiming a top speed of 153 kmph.'),
(6, '350 S 2 mach II', '10000', '100', 'Kawasaki', '26', '1983', 1, 'This bike is a 350 cc Kawasaki motorcycle introduced for the 1972 model year and discontinued at the end of the 1974 model year. It has a 3-cylinder two-stroke engine with a displacement of 346 cc (21.1 cu in), and superseded the rotary disc valve twin-cylinder Kawasaki A7 Avenger.'),
(7, '900 Z 1 super 4', '13000', '120', 'Kawasaki', '33', '1995', 2, 'The 900 z 1 super 4 has an air-cooled, 4-stroke (transversely mounted) DOHC engine. Bore-stroke ratio is a perfect-square 66 x 66 mm (2.6 x 2.6 inches), while compression ratio is set to 8.5:1. Piston displacement is 903 cm³ (55.1 in³). Four Mikuni VM28 carburetors handle air-fuel mixture across all production models.'),
(8, '100 g5', '4500', '77', 'Kawasaki', '41', '2004', 4, 'The dry weight is 86.6 kg (191.0 pounds) and it is equipped with a Single cylinder, two-stroke motor. The engine produces a maximum peak output power of and a maximum torque of . With this drive-train, the Kawasaki 100 G5 is capable of reaching a maximum top speed of 106.2 km/h.'),
(9, 'Mt-01', '20500', '150', 'Yamaha', '28', '2020', 3, 'This bike remains highly-regarded among a sub-set of collectors. Want another? The MT-01, a fusion of cruiser engine in a street chassis. The whole premise behind the MT-01 was very attractive.'),
(10, 'Mt-07 tr', '9000', '125', 'Yamaha', '39', '2007', 2, 'This bike has a Diamond frame with front suspension being 41mm telescopic fork and at the rear, it is equipped with Single shock, adjustable preload and rebound damping '),
(11, 'Pw80', '3500', '110', 'Yamaha', '25', '1986', 4, 'This bike is considered the ideal learner\'s bike. It features an aggressive, two-tone styling, a robust chassis, and a monocross rear swingarm. This two-wheeler perfectly caters to beginners and more experienced young riders.'),
(12, 'Road star', '11000', '130', 'Yamaha', '37', '2014', 1, 'It was produced from 1999 through model year 2014 when the Roadstar model line was discontinued. The 1999-2003 models were the same 1602 cc naturally aspirated engines. In 2004 they changed the displacement to 1,670 cc. There were also a few design changes in 2004, including new tubeless aluminum wheels, a skinnier drive belt, and different engine casing color.'),
(13, 'Monster 1200 S', '19000', '250', 'Kakashi Motors', '40', '2022', 3, 'This bike has a top speed of Top speed 439kph and is our fastest bike for sale. It also features a rapid 0-100 speed of 2.6 seconds');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `motorcycles`
--
ALTER TABLE `motorcycles`
  ADD PRIMARY KEY (`id_number`),
  ADD KEY `category` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `motorcycles`
--
ALTER TABLE `motorcycles`
  MODIFY `id_number` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `motorcycles`
--
ALTER TABLE `motorcycles`
  ADD CONSTRAINT `category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
