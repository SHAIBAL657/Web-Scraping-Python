# Web-Scraping-Python

### Prerequisites

    Install Python
    Install MySQL and Cofigure

        sudo apt update
        sudo apt install mysql-server
        sudo mysql_secure_installation
        mysql -u root -p

### Create Databse

    CREATE TABLE Condo_House(
        Name varchar(250) NOT NULL,
        Sleeps varchar(30),
        Bedroom varchar(30),
        Bathroom varchar(30),
        Image1 varchar(500),
        Image2 varchar(500),
        Image3 varchar(500),
        Price varchar(10),
        PRIMARY KEY (Name,Sleeps,Bedroom,Bathroom))

##### Run web-scrap-db.py
