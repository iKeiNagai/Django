ALTER TABLE organizers
MODIFY COLUMN specialty VARCHAR(50);

INSERT INTO user(u_name,u_address,entriesNo) VALUES
('Sheila O.', '408 Circle Street Auburn, NY 13021', 2),
('Linda', 'Address: 1234 Drury Lane NC', 2),
('Tracie', 'Address: 896 East St. Orland Park, IL 60462', 3),
('Sheila H.', 'Address: 632 53rd Ave. Kennesaw, GA 30144', 1),
('Mandy', '7964 Arlington Dr.Mentor, OH 44060', 2),
('Lucas', '7666 Indian Spring Ave. Rapid City, SD 57701', 2),
('Phil', 'Cedar Swamp Street Park Ridge, IL 60068', 1),
('Donna', '210 Queen Street North Kingstown, RI 02852', 3),
('Elizabeth', '880 Amherst St. Kernersville, NC 27284', 2),
('Lydia', '683 Blackburn Dr. Benton Harbor, MI 49022', 2),
('Carrie', '2 S. Lawrence Dr. Williamsport, PA 17701', 1);

INSERT INTO flower (u_id,species, size, color, age) VALUES
(1,'Bearded Iris', 26.4, 'Blue', 15 ),
(3,'Bearded Iris', 23.7, 'White', 7),
(8,'Columbine', 25.1, 'Pink',10),
(11,'Blazing Star', 51.0, 'Purple',18),
(9,'Dianthus', 17.3, 'Pink',14),
(9,'Chrysanthemum', 9.5, 'Red',9),
(3,'Hosta', 27.6, 'Purple', 39 ),
(8,'Hosta', 19.3, 'White',24),
(2,'Lenten Rose', 14, 'Pink', 5 ),
(4,'Yarrow', 14.4, 'Red', 22 ),
(2,'Begonia', 23, 'Yellow', 5 ),
(5,'Begonia', 27, 'Orange',8),
(3,'Geranium', 39, 'Pink', 29 ),
(5,'Petunia', 13.1, 'Purple',14 ),
(6,'Portulaca', 6.8, 'Red', 24),
(1,'Streptocarpella', 9.2, 'Purple',14 ),
(10,'Poinsettia', 17.0, 'Red',27),
(10,'Marigold', 19.4, 'Orange',9),
(7,'Snapdragon', 8.9, 'White', 5),
(8,'Fuschia', 23.1, 'White',7),
(6,'Lantana', 4.2, 'Pink', 8);








INSERT INTO organizers(o_name,specialty) VALUES
('Kayla','Flowering Bushes: Azaeleas, Hydrangeas'),
('Garland','Small Flowers: Begonias, Petunias'),
('Brant','Fruit Bearing Trees');


INSERT INTO competition(c_name, c_location,c_date, participantsNo) VALUES
('Atlanta Botanical Gardens','345 Piedmont Ave NE, Atlanta, GA 30309', '2024-02-25 01:00:00', 100),
('North Georgia State Fair','2245 Callaway Rd SW, Marietta, GA 30008, USA', '2024-09-24 10:00:00', 10),
('Macon County Fair', '1436 Georgia Rd, Franklin, NC 28734', '2024-06-09 02:00:00', 20);



INSERT INTO Perennials(comp, perennials) VALUES
(1,'Bearded Iris'),
(1,'Columbine'),
(1,'Blazing Star'),
(1,'Dianthus'),
(1,'Chrysanthemum'),
(1,'Hosta'),
(1,'Yarrow'),
(3,'Bearded Iris'),
(3,'Columbine'),
(3,'Blazing Star'),
(3,'Dianthus'),
(3,'Chrysanthemum'),
(3,'Hosta'),
(3,'Yarrow');



INSERT INTO annuals(comp,cosmos) VALUES 
(2,'Begonia'),
(2,'Geranium'),
(2,'Petunia'),
(2,'Portulaca'),
(2,'Streptocarpella'),
(2,'Poinsettia'),
(2,'Marigolds'),
(2,'Snapdragon'),
(2,'Fuschia'),
(2,'Lantana Camara'),
(3,'Begonia'),
(3,'Geranium'),
(3,'Petunia'),
(3,'Portulaca'),
(3,'Streptocarpella'),
(3,'Poinsettia'),
(3,'Marigolds'),
(3,'Snapdragon'),
(3,'Fuschia'),
(3,'Lantana Camara');

INSERT INTO Creates (o_id, c_id) VALUES 
(1,1),
(2,2),
(3,3);

INSERT INTO Participates (f_id, c_id) VALUES 
(1,1),
(2,1),
(3,1),
(4,1),
(5,1),
(6,1),
(7,1),
(8,1),
(9,1),
(10,1),
(1,3),
(2,3),
(3,3),
(4,3),
(5,3),
(6,3),
(7,3),
(8,3),
(9,3),
(10,3),
(11,2),
(12,2),
(13,2),
(14,2),
(15,2),
(16,2),
(17,2),
(18,2),
(19,2),
(20,2),
(21,2),
(11,3),
(12,3),
(13,3),
(14,3),
(15,3),
(16,3),
(17,3),
(18,3),
(19,3),
(20,3),
(21,3);


INSERT INTO has (u_id, c_id) VALUES 
(1,1),
(1,3),
(1,2),
(2,1),
(2,2),
(2,3),
(3,1),
(3,2),
(3,3),
(4,1),
(4,3),
(5,2),
(5,3),
(6,2),
(6,3),
(7,2),
(7,3),
(8,1),
(8,2),
(8,3),
(9,1),
(9,3),
(10,2),
(10,3),
(11,1),
(11,3)
;
