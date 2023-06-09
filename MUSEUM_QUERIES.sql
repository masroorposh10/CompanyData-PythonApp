# GROUP NUMBER: 36, NAME: DOMAINEXPANSION
# GROUP MEMBERS,
# MASROOR POSH
# ANGELO JEROME REYNANTE
# ABRAR REHAN
# ARPON CHOWDHURY 



USE MUSEUM;
select * from ART_OBJECTS;
select * from PAINTING;
select * from SCULPTURE;
select * from OTHER;
select * from PERMANENT_COLLECTION;
select * from ARTIST;
select * from EXHIBITIONS;

select Title, year_created from ART_OBJECTS;
#select Name_,year_created from
select distinct Id_no 
from ART_OBJECTS
where (year_created,Title) in (select year_created, Title
								from ART_OBJECTS
                                WHERE Id_no = '5');
                                
select DateBorn, Date_died
from (ART_OBJECTS JOIN ARTIST on name_ = artist_name)
Where Name_ = 'R W';

select * from ART_OBJECTS ORDER BY Id_no;
SET SQL_SAFE_UPDATES = 0;
UPDATE ART_OBJECTS SET description_ = 'EXHIBITIONS IN THE TUDORS'
WHERE Exhibition_Name LIKE '%The Tudors%';

DELETE FROM EXHIBITIONS 
WHERE Start_Date = '1977-09-29';
SET SQL_SAFE_UPDATES = 1;

