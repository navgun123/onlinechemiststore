-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 10, 2020 at 06:11 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthfit`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminregistration`
--

CREATE TABLE `adminregistration` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `mobile` bigint(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminregistration`
--

INSERT INTO `adminregistration` (`email`, `password`, `fullname`, `mobile`) VALUES
('admin@gmail.com', '123', 'Cairo Alston', 18616999663),
('qamimubyqu@wyg.com', 'Pa$$w0rd!', 'Melissa Faulkner', 16346759007),
('sexigiwux@mytymagibo.com', 'Pa$$w0rd!', 'Georgia Knight', 19461362591);

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `billID` int(11) NOT NULL,
  `datatime` datetime NOT NULL,
  `grandtotal` float(10,2) NOT NULL,
  `payment_method` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `zipcode` int(7) NOT NULL,
  `address` text NOT NULL,
  `remarks` text NOT NULL,
  `trackid` int(15) DEFAULT NULL,
  `companyname` varchar(100) DEFAULT NULL,
  `trackurl` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `personrecieved` varchar(100) DEFAULT NULL,
  `cancelledremarks` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`billID`, `datatime`, `grandtotal`, `payment_method`, `city`, `zipcode`, `address`, `remarks`, `trackid`, `companyname`, `trackurl`, `email`, `status`, `personrecieved`, `cancelledremarks`) VALUES
(1, '2020-02-03 14:14:25', 1018.00, 'cash', 'Jalandhar', 70166, 'Architecto delectus.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', 'Mollit seq'),
(2, '2020-02-03 14:16:48', 1018.00, 'cash', 'Jalandhar', 66390, 'Iure quasi ullam min.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', 'Libero ut'),
(3, '2020-02-03 14:19:43', 1018.00, 'cash', 'Pathankot', 76394, 'Culpa, aliqua. Ea vo.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', 'Pariatur'),
(4, '2020-02-03 14:25:25', 510.00, 'cash', 'Bathinda', 66390, 'Molestiae culpa, aut.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', NULL),
(5, '2020-02-03 14:40:45', 2159.00, 'online', 'Malerkotla', 20591, 'Irure itaque odit iu.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', NULL),
(6, '2020-02-03 15:19:01', 2159.00, 'online', 'Abohar', 62691, 'Sunt iure ut proiden.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', NULL),
(7, '2020-02-03 15:22:01', 2159.00, 'online', 'Abohar', 62691, 'Sunt iure ut proiden.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', NULL),
(8, '2020-02-03 15:22:46', 1034.00, 'online', 'Mohali', 75384, 'Deserunt.', 'Laboriosam', 926789, 'Greene and Gilliam Inc', 'https://www.futivepuqukajel.mobi', 'client@gmail.com', 'Dispatched', '', NULL),
(9, '2020-02-03 17:17:06', 187.00, 'cash', 'Jalandhar', 30970, 'Totam elit, laudanti.', 'Ab incidid', 815678, 'Bennett and Lynn Co', 'https://www.xyciqabago.info', 'pekacepy@rarexijowi.com', 'Dispatched', 'Kapil Ke Dada ji', NULL),
(10, '2020-02-03 17:18:45', 27.00, 'cash', 'Mohali', 48628, 'Distinctio. Voluptat.', 'Ab incidid', 815678, 'Bennett and Lynn Co', 'https://www.xyciqabago.info', 'pekacepy@rarexijowi.com', 'Dispatched', 'Kapil Ke Dada ji', 'Fugit con'),
(11, '2020-02-03 17:22:16', 510.00, 'cash', 'Hoshiarpur', 71016, 'Qui mollit voluptate.', 'Ab incidid', 815678, 'Bennett and Lynn Co', 'https://www.xyciqabago.info', 'pekacepy@rarexijowi.com', 'Dispatched', 'Kapil Ke Dada ji', NULL),
(12, '2020-02-03 17:22:45', 381.00, 'cash', 'Mohali', 78060, 'Quas quod dolores et.', 'Est conse', NULL, NULL, NULL, 'pekacepy@rarexijowi.com', 'cancelled', NULL, 'Animi id');

-- --------------------------------------------------------

--
-- Table structure for table `billdetail`
--

CREATE TABLE `billdetail` (
  `billdetailid` int(11) NOT NULL,
  `price` float(10,2) NOT NULL,
  `quantity` int(10) NOT NULL,
  `productid` int(10) NOT NULL,
  `billid` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billdetail`
--

INSERT INTO `billdetail` (`billdetailid`, `price`, `quantity`, `productid`, `billid`) VALUES
(1, 636.79, 1, 13, 2),
(2, 381.92, 1, 14, 2),
(3, 636.79, 1, 13, 3),
(4, 381.92, 1, 14, 3),
(5, 440.51, 1, 5, 4),
(6, 69.90, 1, 6, 4),
(7, 69.90, 1, 6, 5),
(8, 2089.62, 3, 4, 5),
(9, 69.90, 1, 6, 6),
(10, 2089.62, 3, 4, 6),
(11, 69.90, 1, 6, 7),
(12, 2089.62, 3, 4, 7),
(13, 149.05, 1, 9, 8),
(14, 340.20, 4, 7, 8),
(15, 544.89, 3, 8, 8),
(16, 71.34, 2, 2, 9),
(17, 46.05, 1, 1, 9),
(18, 69.90, 4, 6, 9),
(19, 27.27, 1, 10, 10),
(20, 440.51, 1, 5, 11),
(21, 69.90, 1, 6, 11),
(22, 381.92, 1, 14, 12);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `catid` int(11) NOT NULL,
  `catName` varchar(50) NOT NULL,
  `catDescp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`catid`, `catName`, `catDescp`) VALUES
(17, 'Antipyretics', 'reducing fever (pyrexia/pyresis)'),
(18, 'Analgesics', 'reducing pain (painkillers)'),
(19, 'Antimalarial drugs', 'treating malaria'),
(20, 'Antibiotics', 'inhibiting germ growth'),
(21, 'Antiseptics', 'prevention of germ growth near burns, cuts and wounds'),
(22, 'Mood stabilizers', 'lithium and valpromide'),
(23, 'Hormone replacements', 'Premarin'),
(24, 'Stimulants', 'methylphenidate, amphetamine'),
(25, 'Tranquilizers', 'meprobamate, chlorpromazine, reserpine, chlordiazepoxide, diazepam, and alprazolam'),
(26, 'Statins', 'lovastatin, pravastatin, and simvastatin');

-- --------------------------------------------------------

--
-- Table structure for table `clientregistration`
--

CREATE TABLE `clientregistration` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `mobile` bigint(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clientregistration`
--

INSERT INTO `clientregistration` (`email`, `password`, `fullname`, `mobile`) VALUES
('client@gmail.com', 'Pa$$w0rd!', 'client', 765432145),
('pekacepy@rarexijowi.com', 'Pa$$w0rd!', 'Ciaran Delaney', 13527553099);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pid` int(11) NOT NULL,
  `productname` varchar(100) NOT NULL,
  `productprice` int(10) NOT NULL,
  `productstock` int(10) NOT NULL,
  `productdiscount` int(11) NOT NULL,
  `productdesc` text NOT NULL,
  `productimage` varchar(100) NOT NULL,
  `subid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `productname`, `productprice`, `productstock`, `productdiscount`, `productdesc`, `productimage`, `subid`) VALUES
(1, 'Acetaminophen', 307, 419, 85, 'Voluptate ', '2147product_01.png', 6),
(2, 'Adderall', 41, 497, 13, 'Voluptate ', '9413product_02.png', 6),
(3, 'Alprazolam', 905, 427, 13, 'Rerum ipsa', '9359product_03.png', 7),
(4, 'Amitriptyline', 893, 181, 22, 'Voluptas d', '1016product_04.png', 7),
(5, 'Amlodipine', 899, 188, 51, 'Velit tem', '2558product_04.png', 9),
(6, 'Amoxicillin', 699, 831, 90, 'Impedit a', '2057product_05.png', 9),
(7, 'Ativan', 315, 92, 73, 'Incididunt', '9850product_06.png', 9),
(8, 'Atorvastatin', 443, 555, 59, 'Ipsa in s', '2335product_02.png', 11),
(9, 'Azithromycin', 271, 328, 45, 'Quis ad in', '6453product_07_large.png', 11),
(10, 'Ciprofloxacin', 101, 166, 73, 'Nam cupidi', '2860Paracetamol_Tablets_500mg_-_32_Tablets_(Brand_May_Vary)_31.jpg', 12),
(11, 'Citalopram', 660, 875, 68, 'Occaecat e', '4003product_07_large.png', 16),
(12, 'Clindamycin', 881, 202, 84, 'Dignissimo', '8436products_1.png', 17),
(13, 'Clonazepam', 827, 342, 23, 'Beatae ali', '6880products_1.png', 18),
(14, 'Codeine', 616, 424, 38, 'Nemo accus', '8868hero_1.jpg', 18),
(15, 'Cyclobenzaprine', 717, 840, 89, 'Veniam re', '8716product_01.png', 19),
(16, 'Cymbalta', 994, 656, 97, 'Dolorem qu', '6149DABURAJ01A-1.jpg', 20),
(17, 'Doxycycline', 340, 324, 33, 'Neque qui ', '6763product_06.png', 21),
(18, 'Gabapentin', 301, 257, 21, 'Voluptas e', '97hero_1.jpg', 22),
(19, 'Hydrochlorothiazide', 365, 975, 29, 'Recusandae', '2018product_01.png', 23),
(20, 'Ibuprofen', 777, 759, 71, 'Exercitati', '8069product_02.png', 24),
(21, 'Lexapro', 213, 913, 97, 'Rerum vero', '7723product_03.png', 25),
(22, 'Lisinopril', 178, 982, 81, 'Occaecat a', '2066product_04.png', 26),
(23, 'Loratadine', 951, 143, 95, 'Labore iru', '5736product_05.png', 27),
(24, 'Lorazepam', 774, 861, 40, 'Corrupti ', '3249product_06.png', 28),
(25, 'Losartan', 269, 670, 20, 'Incididunt', '3041product_04.png', 29),
(26, 'Lyrica', 736, 703, 71, 'Aspernatur', '9014product_05.png', 30),
(27, 'Meloxicam', 562, 530, 66, 'Suscipit s', '4009product_02.png', 31),
(28, 'Metformin', 33, 42, 46, 'Dolorem al', '5249product_04.png', 32),
(29, 'Metoprolol', 445, 913, 37, 'Possimus ', '549product_06.png', 32),
(30, 'Naproxen', 720, 142, 12, 'Est nihil', '8936hero_1.jpg', 33),
(31, 'Omeprazole', 890, 760, 60, 'Consequatu', '9024product_07_large.png', 34),
(32, 'Oxycodone', 677, 876, 43, 'Error est', '2296product_03.png', 35),
(33, 'Pantoprazole', 988, 200, 96, 'Non non mo', '8969products_1.png', 36),
(34, 'Lyrica', 692, 814, 91, 'Sint nulla', '204hero_1.jpg', 30),
(35, 'Lyrica', 327, 85, 95, 'Ut molesti', '8125product_05.png', 32),
(36, 'Prednisone', 597, 879, 30, 'Eveniet e', '4244product_01.png', 37),
(37, 'Tramadol', 136, 646, 30, 'Veniam fu', '1617product_07_large.png', 38),
(38, 'Trazodone', 885, 456, 24, 'Fugiat cup', '3369product_03.png', 39),
(39, 'Viagra', 731, 60, 95, 'Et duis un', '2670product_06.png', 40),
(40, 'Wellbutrin', 414, 772, 54, 'Soluta ab ', '6909product_07_large.png', 41),
(41, 'Xanax', 97, 292, 45, 'Doloribus ', '8315product_05.png', 41),
(42, 'Zoloft', 739, 350, 73, 'Unde cum d', '8941Paracetamol_Tablets_500mg_-_32_Tablets_(Brand_May_Vary)_31.jpg', 42),
(43, 'Atenolol', 291, 316, 81, 'Consequunt', '4125products_1.png', 43),
(44, 'Atropine', 740, 930, 77, 'Ad cupidat', '1740hero_1.jpg', 44),
(45, 'Aleve', 715, 594, 30, 'Veniam te', '2139product_01.png', 45),
(46, 'Azelastine', 555, 918, 32, 'Adipisci c', '1259product_05.png', 46),
(47, 'Azithromycin ophthalmic', 767, 691, 87, 'Eos conse', '2754product_06.png', 47),
(48, 'Aztreonam', 146, 563, 6, 'Voluptates', '6534product_02.png', 48),
(49, 'Azuphen MB', 556, 885, 76, 'Illo labor', '7879product_06.png', 49),
(50, 'Azilsartan Kamedoxomil', 708, 831, 67, 'Rerum eaqu', '4522hero_1.jpg', 50);

-- --------------------------------------------------------

--
-- Table structure for table `subcategory`
--

CREATE TABLE `subcategory` (
  `subid` int(11) NOT NULL,
  `subname` varchar(50) NOT NULL,
  `subDescription` text NOT NULL,
  `catid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subcategory`
--

INSERT INTO `subcategory` (`subid`, `subname`, `subDescription`, `catid`) VALUES
(6, 'ibuprofen', 'Ibuprofen is a medication in the nonsteroidal anti-inflammatory drug (NSAID) class that is used for treating pain, fever, and inflammation. This includes painful menstrual periods, migraines, and rheumatoid arthritis. It may also be used to close a patent ductus arteriosus in a premature baby. It can be used by mouth or intravenously. It typically begins working within an hour.', 17),
(7, 'Naproxen', 'Naproxen, sold under the brand name Aleve among others, is a nonsteroidal anti-inflammatory drug (NSAID) used to treat pain, menstrual cramps, inflammatory diseases such as rheumatoid arthritis, and fever. It is taken by mouth. It is available in immediate and delayed release formulations. Onset of effects is within an hour and last for up to twelve hours.', 17),
(9, 'Nimesulide', 'Nimesulide is a nonsteroidal anti-inflammatory drug (NSAID) with pain medication and fever reducing properties. ', 17),
(11, 'Aspirin', 'Aspirin, also known as acetylsalicylic acid (ASA), is a medication used to reduce pain, fever, or inflammation. Specific inflammatory conditions which aspirin is used to treat include Kawasaki disease, pericarditis, and rheumatic fever. ', 17),
(12, 'Paracetamol', 'Paracetamol, also known as acetaminophen and APAP, is a medication used to treat pain and fever.', 17),
(16, 'Phenazone', 'Phenazone is an analgesic, a nonsteroidal anti-inflammatory drug (NSAID) and an antipyretic.', 17),
(17, 'Aceclofenac', 'Comes in betadex salt and free acid forms; practically insoluble in water, soluble in many organic solvents; degrades on contact with light; phenylacetic acid derivative.', 18),
(18, 'Acemetacin', 'Comes in free form; practically insoluble in water, soluble in certain organic solvents; degrades upon contact with light.', 18),
(19, 'Aminophenazone', 'Related to phenylbutazone.', 18),
(20, 'Benorilate', 'Aspirin-paracetamol ester. Practically insoluble in water, sparingly soluble in ethanol and methanol, soluble in acetone and chloroform.', 18),
(21, 'Clonixin', 'Comes in free acid and lysine salt forms.', 18),
(22, 'Quinine', 'Quinine has a long history stretching from Peru, and the discovery of the cinchona tree, and the potential uses of its bark, to the current day[when?] and a collection of derivatives that are still frequently used in the prevention and treatment of malaria. Quinine is an alkaloid that acts as a blood schizonticidal and weak gametocide against Plasmodium vivax and Plasmodium malariae. ', 19),
(23, 'Chloroquine', 'Chloroquine was, until recently, the most widely used anti-malarial. It was the original prototype from which most methods of treatment are derived. It is also the least expensive, best tested and safest of all available drugs. The emergence of drug-resistant parasitic strains is rapidly decreasing its effectiveness; however, it is still the first-line drug of choice in most sub-Saharan African countries. ', 19),
(24, 'Amodiaquine', 'Amodiaquine is a 4-aminoquinolone anti-malarial drug similar in structure and mechanism of action to chloroquine. Amodiaquine has tended to be administered in areas of chloroquine resistance while some patients prefer its tendency to cause less itching than chloroquine. ', 19),
(25, 'Pyrimethamine', 'Pyrimethamine is used in the treatment of uncomplicated malaria. It is particularly useful in cases of chloroquine-resistant P. falciparum strains when combined with sulfadoxine. It acts by inhibiting dihydrofolate reductase in the parasite thus preventing the biosynthesis of purines and pyrimidines, thereby halting the processes of DNA replication, cell division and reproduction. ', 19),
(26, 'Proguanil (chloroguanide)', 'Proguanil (chloroguanide) is a biguanide; a synthetic derivative of pyrimidine. It was developed in 1945 by a British Antimalarial research group. It has many mechanisms of action but primarily is mediated through conversion to the active metabolite cycloguanil. This inhibits the malarial dihydrofolate reductase enzyme. Its most prominent effect is on the primary tissue stages of P. falciparum, P. vivax and P. ovale. ', 19),
(27, 'Clindamycin', 'Clindamycin is a derivative of lincomycin, with a slow action against blood schizonticides. It is only used in combination with quinine in the treatment of acute cases of resistant P. falciparum infections and not as a prophylactic. Being more toxic than the other antibiotic alternatives, it is used only in cases where the Tetracyclines are contraindicated (for example in children).', 19),
(28, 'Metronidazole', 'Metronidazole, marketed under the brand name Flagyl among others, is an antibiotic and antiprotozoal medication. It is used either alone or with other antibiotics to treat pelvic inflammatory disease, endocarditis, and bacterial vaginosis. ', 20),
(29, 'Tinidazole', 'Tinidazole is a drug used against protozoan infections. It is widely known throughout Europe and the developing world as a treatment for a variety of amoebic and parasitic infections.', 20),
(30, 'Cefamandole', 'Cefamandole is a second-generation broad-spectrum cephalosporin antibiotic. The clinically used form of cefamandole is the formate ester cefamandole nafate, a prodrug which is administered parenterally.', 20),
(31, 'Latamoxef', 'Latamoxef is an oxacephem antibiotic usually grouped with the cephalosporins. In oxacephems such as latamoxef, the sulfur atom of the cephalosporin core is replaced with an oxygen atom.', 20),
(32, 'Furazolidone', 'Furazolidone is a nitrofuran antibacterial agent and monoamine oxidase inhibitor (MAOI). ', 20),
(33, 'Octenidine dihydrochloride', 'Octenidine dihydrochloride is a cationic surfactant, with a gemini-surfactant structure, derived from pyridine. It is active against Gram-positive and Gram-negative bacteria. Since 1987, it has been used primarily in Europe as an antiseptic prior to medical procedures, including on neonates.', 21),
(34, 'Polyhexanide (polyhexamethylene biguanide, PHMB) ', 'Polyhexanide (polyhexamethylene biguanide, PHMB) is an antimicrobial compound suitable for clinical use in critically colonized or infected acute and chronic wounds.', 21),
(35, 'Chloroxylenol', 'Chloroxylenol is an antiseptic and disinfectant which is used for skin disinfection and cleaning surgical instruments. It is also used within a number of household disinfectants and wound cleaners.', 21),
(36, 'Chlorhexidine gluconate', 'Chlorhexidine gluconate is used as a skin antiseptic and to treat inflammation of the gums (gingivitis).', 21),
(37, 'Aripiprazole', 'Aripiprazole, sold under the brand name Abilify among others, is an atypical antipsychotic. It is primarily used in the treatment of schizophrenia and bipolar disorder. ', 22),
(38, 'Carbamazepine', 'Carbamazepine (CBZ), sold under the trade name Tegretol among others, is an anticonvulsant medication used primarily in the treatment of epilepsy and neuropathic pain.', 22),
(39, 'Ketamine', 'Ketamine is a medication mainly used for starting and maintaining anesthesia. It induces a trance-like state while providing pain relief, sedation, and memory loss. Other uses include sedation in intensive care and treatment of chronic pain and depression.', 22),
(40, 'Paliperidone', 'Paliperidone, sold under the brand name Invega among others, is an atypical antipsychotic. It is marketed by Janssen Pharmaceutica.', 22),
(41, 'Lurasidone', 'Lurasidone, sold under the trade name Latuda among others, is an antipsychotic medication used to treat schizophrenia and bipolar disorder. In bipolar it may be used together with a mood stabilizer such as lithium or valproate. It is taken by mouth.', 22),
(42, 'Tamoxifen', 'Tamoxifen, sold under the brand name Nolvadex among others, is a medication that is used to prevent breast cancer in women and treat breast cancer in women and men. It is also being studied for other types of cancer.', 22),
(43, 'Heart disease', 'The effect of HRT in menopause appears to be divergent, with lower risk when started within five years, but no impact after ten.[21][22][23] There may be an increase in heart disease if HRT is given twenty years post-menopause.[24] There is, however, no actual difference in long-term mortality from HRT, regardless of age.[6]', 23),
(44, 'Blood clots', 'Effects of hormone replacement therapy on venous blood clot formation and potential for pulmonary embolism may vary with different estrogen and progestogen therapies, and with different doses or method of use.[16] Comparisons between routes of administration suggest that when estrogens are applied to the skin or vagina, there is a lower risk of blood clots,[16][26] whereas when used orally, the risk of blood clots and pulmonary embolism is increased.', 23),
(45, 'Stroke', 'Multiple studies suggest that the possibility of HRT related stroke is absent if therapy is started within five years of menopause,[28] and that the association is absent or even preventive when given by non-oral routes.[7] Ischemic stroke risk was increased during the time of intervention in the WHI, with no significant effect after the cessation of therapy[24] and no difference in mortality at long term follow up.', 23),
(46, 'Colorectal cancer', 'In the WHI, women who took combined estrogen-progesterone therapy had a lower risk of getting colorectal cancer. However, the cancers they did have were more likely to have spread to lymph nodes or distant sites than colorectal cancer in women not taking hormones.', 23),
(47, 'Amphetamine', 'Amphetamine is a potent central nervous system (CNS) stimulant of the phenethylamine class that is approved for the treatment of attention deficit hyperactivity disorder (ADHD) and narcolepsy.[45] Amphetamine was discovered in 1887 and exists as two enantiomers: levoamphetamine and dextroamphetamine.', 24),
(48, 'Ephedrine', 'Ephedrine is a sympathomimetic amine similar in molecular structure to the well-known drugs phenylpropanolamine and methamphetamine, as well as to the important neurotransmitter epinephrine (adrenaline). Ephedrine is commonly used as a stimulant, appetite suppressant, concentration aid, and decongestant, and to treat hypotension associated with anaesthesia.', 24),
(49, 'Mephedrone', 'Mephedrone is a synthetic stimulant drug of the amphetamine and cathinone classes. Slang names include drone[93] and MCAT.[94] It is reported to be manufactured in China and is chemically similar to the cathinone compounds found in the khat plant of eastern Africa.', 24),
(50, 'Phenylpropanolamine', 'Phenylpropanolamine (PPA; Accutrim; β-hydroxyamphetamine), also known as the stereoisomers norephedrine and norpseudoephedrine, is a psychoactive drug of the phenethylamine and amphetamine chemical classes that is used as a stimulant, decongestant, and anorectic agent.', 24),
(51, 'Minor Tranquilizer', 'An anxiolytic is a medication, or other intervention, that inhibits anxiety. This effect is in contrast to anxiogenic agents, which increase anxiety. ', 25),
(52, 'Major Tranquilizer', 'Antipsychotics, also known as neuroleptics or major tranquilizers, are a class of medication primarily used to manage psychosis, principally in schizophrenia and bipolar disorder. Antipsychotics are usually effective in relieving symptoms of psychosis in the short term.', 25),
(53, 'Atorvastatin', 'Atorvastatin, sold under the trade name Lipitor among others, is a statin medication used to prevent cardiovascular disease in those at high risk and treat abnormal lipid levels. ', 26),
(54, 'Fluvastatin', 'Fluvastatin is a member of the statin drug class, used to treat hypercholesterolemia and to prevent cardiovascular disease.', 26),
(55, 'Pravastatin', 'Pravastatin, sold under the brand name Pravachol among others, is a statin medication, used preventing cardiovascular disease in those at high risk and treating abnormal lipids.', 26),
(56, 'Simvastatin', 'Simvastatin, marketed under the trade name Zocor among others, is a lipid-lowering medication. It is used along with exercise, diet, and weight loss to decrease elevated lipid levels. It is also used to decrease the risk of heart problems in those at high risk. It is taken by mouth.', 26);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminregistration`
--
ALTER TABLE `adminregistration`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`billID`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `billdetail`
--
ALTER TABLE `billdetail`
  ADD PRIMARY KEY (`billdetailid`),
  ADD KEY `productid` (`productid`),
  ADD KEY `billid` (`billid`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`catid`);

--
-- Indexes for table `clientregistration`
--
ALTER TABLE `clientregistration`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `subid` (`subid`);

--
-- Indexes for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`subid`),
  ADD KEY `catid` (`catid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `billID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `billdetail`
--
ALTER TABLE `billdetail`
  MODIFY `billdetailid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `catid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `subid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`email`) REFERENCES `clientregistration` (`email`);

--
-- Constraints for table `billdetail`
--
ALTER TABLE `billdetail`
  ADD CONSTRAINT `billdetail_ibfk_2` FOREIGN KEY (`productid`) REFERENCES `product` (`pid`),
  ADD CONSTRAINT `billdetail_ibfk_3` FOREIGN KEY (`billid`) REFERENCES `bill` (`billID`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`subid`) REFERENCES `subcategory` (`subid`);

--
-- Constraints for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD CONSTRAINT `subcategory_ibfk_1` FOREIGN KEY (`catid`) REFERENCES `category` (`catid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
