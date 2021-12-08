-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: vrbo
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Condo_House`
--

DROP TABLE IF EXISTS `Condo_House`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Condo_House` (
  `Name` varchar(250) NOT NULL,
  `Sleeps` varchar(30) NOT NULL,
  `Bedroom` varchar(30) NOT NULL,
  `Bathroom` varchar(30) NOT NULL,
  `Image1` varchar(500) DEFAULT NULL,
  `Image2` varchar(500) DEFAULT NULL,
  `Image3` varchar(500) DEFAULT NULL,
  `Price` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Name`,`Sleeps`,`Bedroom`,`Bathroom`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Condo_House`
--

LOCK TABLES `Condo_House` WRITE;
/*!40000 ALTER TABLE `Condo_House` DISABLE KEYS */;
INSERT INTO `Condo_House` VALUES ('3 BDRM / 2 BATH EXTRA LARGE BALCONY ','Sleeps 8','3 Bedrooms','None','\"https://media.vrbo.com/lodging/34000000/33500000/33497600/33497553/4ebe2eca.c6.jpg\"','\"https://media.vrbo.com/lodging/34000000/33500000/33497600/33497553/abfea7e7.c6.jpg\"','\"https://media.vrbo.com/lodging/34000000/33500000/33497600/33497553/594870b9.c6.jpg\"','$155'),('Amazing Beach Front Condo, Low Rates, Great Views','Sleeps 8','2 Bedrooms','2 Bathrooms','\"https://media.vrbo.com/lodging/35000000/34330000/34323500/34323440/cc05393f.c6.jpg\"','\"https://media.vrbo.com/lodging/35000000/34330000/34323500/34323440/9911954e.c6.jpg\"','\"https://media.vrbo.com/lodging/35000000/34330000/34323500/34323440/90-46c0a549.c6.jpg\"','$155'),('Beach Bliss !  Comfortable and Affordable Only Steps From Sugar White Sand Beach','Sleeps 6','2 Bedrooms','2 Bathrooms','\"https://media.vrbo.com/lodging/28000000/27140000/27130500/27130476/34fbbaa4.c6.jpg\"','\"https://media.vrbo.com/lodging/28000000/27140000/27130500/27130476/4ca320ec.c6.jpg\"','\"https://media.vrbo.com/lodging/28000000/27140000/27130500/27130476/f7f0e50a.c6.jpg\"','$110'),('Beachfront One Bedroom Sleeps Six','Sleeps 6','1 Bedroom','1 Bathroom','\"https://media.vrbo.com/lodging/39000000/38730000/38722100/38722092/741f9577.c6.jpg\"','\"https://media.vrbo.com/lodging/39000000/38730000/38722100/38722092/90-6ae8c3f8.c6.jpg\"','\"https://media.vrbo.com/lodging/39000000/38730000/38722100/38722092/54ace978.c6.jpg\"','$113'),('Emerald Skye #56 - Million Dollar View Fifth Floor Corner Unit- Orange Beach AL','Sleeps 4','1 Bedroom','1 Bathroom','\"https://media.vrbo.com/lodging/55000000/54420000/54412300/54412225/84c0ec60.c6.jpg\"','\"https://media.vrbo.com/lodging/55000000/54420000/54412300/54412225/57ff6bbd.c6.jpg\"','\"https://media.vrbo.com/lodging/55000000/54420000/54412300/54412225/d488fc47.c6.jpg\"','$138'),('Gorgeous Beachfront Condo! 3BR/3.5BA in Phoenix 9','Sleeps 10','3 Bedrooms','3 Bathrooms','\"https://media.vrbo.com/lodging/34000000/33940000/33935800/33935759/90c351b8.c6.jpg\"','\"https://media.vrbo.com/lodging/34000000/33940000/33935800/33935759/537bbc55.c6.jpg\"','\"https://media.vrbo.com/lodging/34000000/33940000/33935800/33935759/1b70240f.c6.jpg\"','$145');
/*!40000 ALTER TABLE `Condo_House` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-08 13:45:01
