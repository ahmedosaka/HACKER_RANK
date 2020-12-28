--/*Task 0: Drop the table INSTRUCTOR from the database in case it already exists, so that we start from a clean state.
--
--(Hint: Ignore the undefined error if this table does not already exist in your database)*/

DROP TABLE IF EXISTS INSTRUCTOR;
--Task 1: Create the INSTRUCTOR table as defined above. Have the ins_id be the primary key, and ensure the lastname and firstname are not null.
--
--(Hint: ins_id is of type INTEGER, country of type CHAR(2), and rest of the fields VARCHAR)
create table INSTRUCTOR (
id INTEGER PRIMARY KEY ,
firstname VARCHAR(50) NOT NULL,
lastname VARCHAR(50) NOT NULL,
city VARCHAR(20),
country char(2));

--Task 2A: Insert one row into the INSTRUCTOR table for the the instructor Rav Ahuja.
insert into INSTRUCTOR (id, firstname, lastname, city, country) values (1,'Rav' , 'Ahuja', 'Toronto', CA);

--Task 2B: Insert two rows at once in the INSTRUCTOR table for instructors Raul Chong and Hima Vasudevan.
--(Hint: list the values for the second row after the first row)
insert into INSTRUCTOR(id, firstname, lastname, city, country) values (2,'Raul','Chong','Toronto', CA ),(3,'Hima','Vasudevan', 'Chicago', 'US');

--Task 3: Select all rows from the INSTRUCTOR table.
select * from INSTRUCTOR;

--Task 3B: Select the firstname, lastname and country where the city is Toronto
select firstname, lastname from INSTRUCTOR where city ='Toronto';

--Task 4: Update the row for Rav Ahuja and change his city to Markham.
update INSTRUCTOR set city = 'Markham' where firstname = 'Rav'  and lastname = 'Ahuja';

--Task 5: Delete the row for Raul Chong from the table.
delete from INSTRUCTOR where firstname = 'Raul' and lastname = 'Raul Chong';

--Task 5B: Retrieve all rows in the INSTRUCTOR table
select * from INSTRUCTOR;
