# GROUP NUMBER: 36, NAME: DOMAINEXPANSION
# GROUP MEMBERS,
# MASROOR POSH
# ANGELO JEROME REYNANTE
# ABRAR REHAN
# ARPON CHOWDHURY 


DROP DATABASE IF EXISTS MUSEUM;
CREATE DATABASE MUSEUM; 
USE MUSEUM;


CREATE TABLE ARTIST
(Name_		varchar(25), 
DateBorn 	varchar(25), 
Date_died	varchar(25),
Country_of_origin	varchar(15) not null, 
Epoch		varchar(25)  not null, 
Main_style	varchar(25)  not null, 
Description_	varchar(25)  not null,
primary key(Name_)
);



CREATE TABLE ART_OBJECTS
(Id_no		integer  not null ,
artist_name	varchar(25),
year_created varchar(15),
Title	varchar(25) not null,
description_ varchar(5000),
Exhibition_Name	varchar(50),
primary key(Id_no),
foreign key(artist_name) references ARTIST (Name_)
);






CREATE TABLE PAINTING 
(Id_no	integer,
Paint_Type	varchar(25),
Drawn_on	varchar(25),
Style		varchar(10),
foreign KEY(Id_no) references ART_OBJECTS(Id_no)
);



CREATE TABLE SCULPTURE
(Id_no	integer not null,
Material varchar(25),
Height   varchar(25),
Weight	 VARCHAR(25),
Style	 varchar(10),
foreign KEY(Id_no) references ART_OBJECTS(Id_no)
);



CREATE TABLE OTHER
(Id_no	integer not null,
Type_	varchar(25),
Style	varchar(25),
foreign KEY(Id_no) references ART_OBJECTS(Id_no)
);


CREATE TABLE PERMANENT_COLLECTION
(Id_no	integer not null,
Date_acquired varchar(25),
Status_		varchar(25),
Cost		varchar(50),
foreign KEY(Id_no) references ART_OBJECTS(Id_no)
);



CREATE TABLE BORROWED_COLLECTION
(Id_no	integer not null,
Collection_Name varchar(25),
Date_Borrowed	date,
Date_Returned	date,
foreign KEY(Id_no) references ART_OBJECTS(Id_no)
);



CREATE TABLE OTHER_COLLECTION
(Name_ varchar(25),
Type_	varchar(25),
Address	varchar(25),
Description_ varchar(25),
Contact_phone	integer,
Contact_name	varchar(25),
primary key(Name_)

);

ALTER TABLE ART_OBJECTS ADD Epoch VARCHAR(25);
ALTER TABLE ART_OBJECTS ADD country_of_origin VARCHAR(50);

CREATE TABLE EXHIBITIONS
(Name_  varchar(500),
Start_Date	date,
End_Date date
);


INSERT INTO ARTIST
VALUES('Benedetto da Rovezzano','1474','ca. 1554','Italy','','',''),
	  ('','','','Netherlands','','',''),
      ('R W','','','','','',''),
      ('Juan Gris','1887','1927','Spain','','','')
      ;


INSERT INTO ART_OBJECTS
VALUES('1','Benedetto da Rovezzano','ca. 1500','Candelabrum','','The Tudors: Art and Majesty in Renaissance England','Renaissance','Belgium'),
	('2','','1505','Henry VII','','The Tudors: Art and Majesty in Renaissance England','Renaissance','London'),
    ('3','R W','1590–91','Cup with Cover','Principally sourced from the interiors of exotic shells, Indian mother-of-pearl was admired and sought after by Europeans, and imports sold at astronomical prices. Though some vessels worked by Gujarati craftsmen (from Western India) were kept in their original forms, others—such as this one—were carefully dismantled and their mother-of-pearl inlays set in new precious-metal mounts. The extremely delicate gilded silver foot and cover decorated with miniature heraldic roses locate this piece to Elizabethan London.','','Renaissance','london'),
    ('4','','ca. 1505','Unidentified Saint','','The Tudors: Art and Majesty in Renaissance England','','London'),
    ('5','Juan Gris','1914','Guitar and Glasses','Gris seamlessly combined cuttings from a tobacco package and his favorite faux wood-grain wallpapers with his handmade imitations of printed materials: the checked tablecloth that doubles as floor tiles, sheet of music, and label for “BOR[DEAUX] V[IN].” The tabletop tips up vertically, all but negating spatial recession, and the glinting bottle and wineglasses seem to push through the picture plane in classic trompe l’oeil style. The haunting fusion of guitar and table in a shadowy room and the remnants of a past gathering with music recall the theme of Baschenis’s rediscovered masterpiece (shown nearby), which Gris may have known in reproduction.','','','New York')
    ;
    
INSERT INTO PAINTING
VALUES('2','Oil','Panel','Portrait');

INSERT INTO SCULPTURE
VALUES('4','Terracotta','13','','');

INSERT INTO OTHER
VALUES('1','Metalwork','Renaissance'),
	  ('3','Metalwork','Silver In Combination'),
      ('5','Collages','')
      ;

INSERT INTO PERMANENT_COLLECTION
VALUES('1','','Loan',''),
	  ('2','','Loan',''),
      ('3','1968','On View','£6,500'),
      ('4','','Loan','')
      ;
      

INSERT INTO EXHIBITIONS
VALUES('The Tudors: Art and Majesty in Renaissance England','2022-10-10','2023-08-01'),
      ('Highlights of the Untermyer Collection of English and Continental Decorative Arts','1977-09-29','1978-04-21')
      ;

DROP ROLE IF EXISTS db_admin@localhost, read_access@localhost;
CREATE ROLE db_admin@localhost, read_access@localhost;
GRANT ALL PRIVILEGES ON MUSEUM.* TO db_admin@localhost;
GRANT Select ON MUSEUM.* TO read_access@localhost;

DROP USER IF EXISTS mp@localhost;
DROP USER IF EXISTS guest@localhost;
CREATE USER mp@localhost IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER guest@localhost;
GRANT db_admin@localhost TO mp@localhost;
GRANT read_access@localhost TO guest@localhost;
SET DEFAULT ROLE ALL TO mk@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;