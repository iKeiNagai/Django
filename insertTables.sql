ALTER TABLE organizers
MODIFY COLUMN specialty VARCHAR(50);


INSERT INTO organizers(o_name,specialty) VALUES
('name_','specialty_'),
('name_1','specialty_1'),
('name_2','specialty_2'),
('name_3','specialty_3'),
('name_4','specialty_4'),
('name_5','specialty_5'),
('name_6','specialty_6'),
('name_7','specialty_7'),
('name_8','specialty_8'),
('name_9','specialty_9');

INSERT INTO competition(c_name,c_location,c_date, participantsNo) VALUES
('name','c_location_', '2024-03-25 01:00:00', 100),
('name','c_location_1', '2024-03-25 10:00:00', 10),
('name','c_location_2', '2024-03-25 02:00:00', 20),
('name','c_location_3', '2024-03-25 03:00:00', 30),
('name','c_location_4', '2024-03-25 04:00:00', 40),
('name','c_location_5', '2024-03-25 05:00:00', 50),
('name','c_location_6', '2024-03-25 06:00:00', 60),
('name','c_location_7', '2024-03-25 07:00:00', 70),
('name','c_location_8', '2024-03-25 08:00:00', 80),
('name','c_location_9', '2024-03-25 09:00:00', 90);

INSERT INTO user(u_name,u_address,entriesNo) VALUES
('u_name_', '1 Main St', 100),
('u_name_1', '2 Main St', 10),
('u_name_2', '3 Main St', 20),
('u_name_3', '4 Main St', 30),
('u_name_4', '5 Main St', 40),
('u_name_5', '6 Main St', 50),
('u_name_6', '7 Main St', 60),
('u_name_7', '8 Main St', 70),
('u_name_8', '9 Main St', 80),
('u_name_9', '0 Main St', 90);

INSERT INTO flower (u_id, species, size, color, age) VALUES
(1,'species_', 12., 'color_',0 ),
(1,'species_1', 12.1, 'color_1',1 ),
(1,'species_2', 12.2, 'color_2',2 ),
(3,'species_3', 12.3, 'color_3',3 ),
(5,'species_4', 12.4, 'color_4',4 ),
(6,'species_5', 12.5, 'color_5',5 ),
(7,'species_6', 12.6, 'color_6',6 ),
(8,'species_7', 12.7, 'color_7',7 ),
(9,'species_8', 12.8, 'color_8',8 ),
(10,'species_9', 12.9, 'color_9',9 );

INSERT INTO Perennials(perennial_id, perennials) VALUES
(1,'perennial_'),
(2,'perennial_1'),
(3,'perennial_2'),
(4,'perennial_3'),
(5,'perennial_4'),
(6,'perennial_5'),
(7,'perennial_6'),
(8,'perennial_7'),
(9,'perennial_8'),
(10,'perennial_9');


INSERT INTO annuals(annual_id,cosmos) VALUES 
(1,'annual_'),
(2,'annual_1'),
(3,'annual_2'),
(4,'annual_3'),
(5,'annual_4'),
(6,'annual_5'),
(7,'annual_6'),
(8,'annual_7'),
(9,'annual_8'),
(10,'annual_9');

INSERT INTO Participates (f_id, c_id) VALUES 
(1, 1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10)
;

INSERT INTO has (u_id, c_id) VALUES 
(1, 1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10)
;