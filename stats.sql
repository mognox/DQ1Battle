BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "DQ1NFEQ" (
	"Id"	INTEGER,
	"Name"	TEXT UNIQUE,
	"Type"	TEXT,
	"Modifier"	INTEGER,
	"Special"	TEXT,
	"ModifierType"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "DQ1NFEI" (
	"Id"	INTEGER,
	"Name"	TEXT UNIQUE,
	"Effect"	TEXT,
	"Modifier"	INTEGER,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "DQ1NFS" (
	"Id"	INTEGER,
	"Name"	TEXT UNIQUE,
	"Mp"	INTEGER,
	"Effect"	TEXT,
	"Lvl"	INTEGER,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "DQ1NFE" (
	"Id"	INTEGER,
	"Name"	TEXT UNIQUE,
	"Hp"	INTEGER,
	"Xp"	INTEGER,
	"Locations"	TEXT,
	"Family"	TEXT,
	"Strength"	INTEGER,
	"Agility"	INTEGER,
	"SleepResist"	REAL,
	"StopSpellResist"	REAL,
	"HurtResist"	REAL,
	"Dodge"	REAL,
	"Gold"	INTEGER,
	"Pattern"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (1,'Clothes','Armor',2,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (2,'Leather Armor','Armor',4,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (3,'Chain Mail','Armor',10,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (4,'Half Plate','Armor',16,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (5,'Full Plate','Armor',24,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (6,'Magic Armor','Armor',24,'Restores one HP for every four steps','Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (7,'Erdrick''s Armor','Armor',28,'Restores HP every step

Prevents damage from walking on damaging tiles

Reduces damage from HURT and HURTMORE by 1/3

Reduces damage from flame breath attacks by 1/3

Prevents Stopstell','Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (8,'Leather Shield','Shield',4,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (9,'Iron Shield','Shield',10,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (10,'Silver Shield','Shield',20,NULL,'Defense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (11,'Bamboo Pole','Weapon',2,NULL,'Offense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (12,'Club','Weapon',4,NULL,'Offense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (13,'Copper Sword','Weapon',10,NULL,'Offense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (14,'Hand Axe','Weapon',15,NULL,'Offense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (15,'Broad Sword','Weapon',20,NULL,'Offense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (16,'Flame Sword','Weapon',28,NULL,'Offense');
INSERT INTO "DQ1NFEQ" ("Id","Name","Type","Modifier","Special","ModifierType") VALUES (17,'Erdrick''s Sword','Weapon',40,NULL,'Offense');
INSERT INTO "DQ1NFEI" ("Id","Name","Effect","Modifier") VALUES (1,'Herb','Restores 20-35 HP',NULL);
INSERT INTO "DQ1NFEI" ("Id","Name","Effect","Modifier") VALUES (2,'Dragon''s Scale','+2 Defense',2);
INSERT INTO "DQ1NFEI" ("Id","Name","Effect","Modifier") VALUES (3,'Fairie''s Flute','Puts certain enemies to sleep',NULL);
INSERT INTO "DQ1NFS" ("Id","Name","Mp","Effect","Lvl") VALUES (1,'Heal',4,'Heals 10-17 HP',3);
INSERT INTO "DQ1NFS" ("Id","Name","Mp","Effect","Lvl") VALUES (2,'Hurt',2,'Deals 5-12 damage to an enemy',4);
INSERT INTO "DQ1NFS" ("Id","Name","Mp","Effect","Lvl") VALUES (3,'Sleep',2,'Sometimes puts enemy to sleep',7);
INSERT INTO "DQ1NFS" ("Id","Name","Mp","Effect","Lvl") VALUES (4,'StopSpell',2,'Prevents enemy from casting spells',10);
INSERT INTO "DQ1NFS" ("Id","Name","Mp","Effect","Lvl") VALUES (5,'HealMore',10,'Heals 85-100 HP',17);
INSERT INTO "DQ1NFS" ("Id","Name","Mp","Effect","Lvl") VALUES (6,'HurtMore',5,'Deals 58-65 damage',19);
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (1,'Slime',3,1,'A B ','Slime',5,3,NULL,0.9375,NULL,0.015625,1,'Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (2,'She-slime',4,1,'A B ','Slime',7,3,NULL,0.9375,NULL,0.015625,2,'Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (3,'Dracky','5 6',2,'A','Bird',9,6,NULL,0.9375,NULL,0.015625,2,'Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (4,'Ghost','6 7',3,'B C D E ','Undead',11,8,NULL,0.9375,NULL,0.0625,'3 4','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (5,'Prestidigitator','10 13',4,'B D F C E ','Humanoid',11,12,NULL,NULL,NULL,0.015625,'9 11','1/2 cast Hurt
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (6,'Drackolyte','12 15',5,'C ','Bird',14,14,NULL,NULL,NULL,0.015625,'9 11','1/2 cast Hurt
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (7,'Scorpion','16 20',6,'C F G E ','Bug',18,16,NULL,0.9375,NULL,0.015625,'12 15','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (8,'Skeleton','23 30',11,'H D I ','Undead',28,22,NULL,0.9375,NULL,0.0625,'22 29','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (9,'Lunatick','17 22',7,'D ','Bug',20,18,NULL,0.9375,NULL,0.03125,'12 15','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (10,'Gold golem','38 50',6,'M L ','Material',48,40,0.8125,0.9375,NULL,0.015625,'150 199','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (11,'Drohl drone','19 25',10,'D J ','Bug',24,24,NULL,0.875,NULL,0.03125,'18 24','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (12,'Drackyma','16 20',11,'D ','Bird',22,26,NULL,NULL,NULL,0.09375,'15 19','1/4 cast Heal if under 1/4 of max HP
Else 1/2 cast Hurt else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (13,'Legerdeman','23 30',13,'D J K ','Undead',28,22,0.1875,0.0625,NULL,0.03125,'26 34','1/4 cast sleep if player not asleep
Else 1/2 cast hurt else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (14,'Bewarewolf','26 34',16,'K J ','Beast',40,30,0.0625,0.9375,NULL,0.03125,'30 39','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (15,'Iron scorpion','17 22',14,'K L J ','Bug',36,42,NULL,0.9375,NULL,0.03125,'30 39','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (16,'Skeleton scrapper','28 36',17,'K ','Undead',44,34,0.4375,NULL,NULL,0.0625,'45 59','1/4 cast Heal if HP less than 1/4 of max
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (17,'Scarewolf','29 38',20,'M O J ','Beast',50,36,0.25,0.4375,NULL,0.03125,'60 79','1/2 cast StopSpell if spell is not blocked
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (18,'Fightgeist','18 23',8,'D J ','Undead',18,20,NULL,NULL,NULL,0.09375,'13 17','3/4 cast Hurt
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (19,'Chimaera','32 42',24,'M L ','Bird',56,48,0.25,0.9375,NULL,0.03125,'75 99','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (20,'Spitegeist','28 36',18,'J ','Undead',40,38,0.1875,0.0625,NULL,0.0625,'52 69','1/4 cast Sleep if player not asleep
Else 3/4 cast Hurt else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (21,'Raving lunatick','27 35',20,'J ','Bug',47,40,0.9375,NULL,NULL,0.0625,'63 84','3/4 cast Heal if HP less than 1/4 of max
Else 1/4 cast Hurt else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (22,'Drohl diabolist','29 38',22,'J ','Bug',52,50,0.125,0.125,NULL,0.015625,'67 89','1/2 cast StopSpell if spell is not blocked
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (23,'Skeleton soldier','35 46',28,'J L ','Undead',68,56,0.3125,NULL,0.1875,0.0625,'90 119','3/4 cast Heal if HP 1/4 of max
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (24,'Death scorpion','27 35',26,'L ','Bug',60,90,0.4375,NULL,NULL,0.03125,'82 109','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (25,'Knight errant','42 55',33,'L N P ','Demon',76,78,0.375,0.4375,NULL,0.015625,'97 129','1/2 cast StopSpell if spell is not blocked
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (26,'Dark skeleton','38 50',37,'L ','Undead',79,64,0.9375,0.9375,0.9375,0.234375,'112 149','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (27,'Hocus chimaera','44 58',34,'Q N ','Bird',78,68,0.125,NULL,NULL,0.03125,'105 139','1/2 cast Sleep if player not asleep
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (28,'Metal slime',4,115,'Q ','Slime',10,255,0.9375,0.9375,0.9375,0.015625,'4 5','3/4 cast Hurt
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (29,'Tearwolf','46 60',40,'O N P S ','Beast',86,70,0.4375,0.9375,NULL,0.109375,'116 154','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (30,'Cosmic chimaera','49 65',43,'O N R S ','Bird',86,80,0.5,NULL,0.0625,0.03125,'120 159','3/4 cast HealMore if HP less than 1/4 max
Else 1/4 breathe fire else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (31,'Green dragon','49 65',45,'E N O S ','Dragon',88,74,0.4375,0.9375,0.125,0.125,'120 159','3/4 cast HealMore if HP less than 1/4 max
Else 1/4 breathe fire else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (32,'Vis mager','49 65',50,'N O S ','Humanoid',80,70,0.9375,0.4375,0.9375,0.03125,'123 164','1/2 cast HurtMore
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (33,'Golem','53 70',5,'T ','Material',120,60,0.9375,0.9375,0.9375,NULL,'7 9','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (34,'Knight aberrant','53 70',54,'O S ','Demon',94,82,0.9375,0.1875,0.0625,0.015625,'123 164','1/4 cast Sleep if player not asleep
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (35,'Blue dragon','53 70',60,'S ','Dragon',98,84,0.9375,0.9375,0.4375,0.03125,'112 149','1/4 breathe fire
Else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (36,'Stone golem','121 160',65,'S ','Material',100,40,0.125,0.9375,0.4375,0.015625,'105 139','Attack only');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (37,'Knight abhorrent','68 90',70,'S ','Demon',105,86,0.9375,0.4375,0.0625,0.03125,'105 139','3/4 cast HealMore if HP less than 1/4 max
Else 1/4 cast HurtMore else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (38,'Red dragon','76 100',100,'S ','Dragon',120,90,0.9375,0.4375,0.9375,0.03125,'105 139','1/4 cast Sleep if player not asleep
Else 1/4 breathe fire else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (39,'Dragonlord','76 100',0,'S ','???',90,75,0.9375,0.9375,0.9375,NULL,NULL,'1/4 cast StopSpell if spell is not blocked
Else 3/4 cast HurtMore else attack');
INSERT INTO "DQ1NFE" ("Id","Name","Hp","Xp","Locations","Family","Strength","Agility","SleepResist","StopSpellResist","HurtResist","Dodge","Gold","Pattern") VALUES (40,'Dragonlord (Dragon form)',130,0,'S ','???',140,200,0.9375,0.9375,0.9375,NULL,NULL,'1/2 breathe strong fire
Else attack');
COMMIT;