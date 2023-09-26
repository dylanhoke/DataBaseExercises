SELECT_ALL = """
    SELECT character_id,name
    FROM charactercreator_character"""


AVG_ITEM_WEIGHT_PER_CHARACTER = """
    SELECT ccc.name,avg(ai.weight) AS avg_item_weight
    FROM charactercreator_character as ccc
    JOIN charactercreator_character_inventory as ccci
    ON ccc.character_id = ccci.character_id
    JOIN armory_item as ai
    ON ai.item_id = ccci.item_id
    GROUP BY ccc.character_id"""


TOTAL_CHARACTERS = """
    SELECT count(character_id)
    FROM charactercreator_character"""


TOTAL_SUBCLASS = """
    SELECT COUNT(character_id)
    FROM charactercreator_character AS ccc
    JOIN charactercreator_mage AS ccm 
    ON ccc.character_id = ccm.character_ptr_id
    JOIN charactercreator_necromancer AS ccn
    ON ccm.character_ptr_id = ccn.mage_ptr_id"""


TOTAL_ITEMS = """
    SELECT item_id, count(*) as volume
    FROM charactercreator_character_inventory
    GROUP BY item_id"""


WEAPONS = """
    SELECT item_id,count(*)
    FROM armory_item as ai
    JOIN armory_weapon as aw
    ON ai.item_id = aw.item_ptr_id
    GROUP BY item_id"""


NON_WEAPONS = """
    SELECT item_id,count(*)
    FROM armory_item
    WHERE item_id
    NOT IN (SELECT item_ptr_id FROM armory_weapon)"""


CHARACTER_ITEMS = """
    SELECT character_id,count(*)
    FROM charactercreator_character_inventory
    GROUP BY character_id
    LIMIT 20"""


CHARACTER_WEAPONS = """
    SELECT character_id,COUNT(*)
    FROM charactercreator_character_inventory AS ccci
    JOIN armory_weapon AS aw
    ON ccci.item_id = aw.item_ptr_id
    GROUP BY character_id
    LIMIT 20"""


AVG_CHARACTER_ITEMS = """
    SELECT AVG(item_count) as average_item_count
    FROM (
    SELECT character_id, count(*) AS item_count 
    FROM charactercreator_character_inventory
    GROUP BY character_id
    ) AS subquery"""


AVG_CHARACTER_WEAPONS = """
    SELECT AVG(weapon_item_count) as average_item_count
    FROM (
    SELECT character_id,COUNT(*) AS weapon_item_count
    FROM charactercreator_character_inventory AS ccci
    JOIN armory_weapon AS aw
    ON ccci.item_id = aw.item_ptr_id
    GROUP BY character_id
    ) AS subquery"""

ROW_COUNT = """
    SELECT *
    FROM review"""

USER_REVIEWS = """
    SELECT *
    FROM review
    WHERE Nature > 100 AND Shopping > 100"""


AVG_REVIEWS = """
    SELECT AVG(Sports),avg(Religious),avg(Nature),avg(Theatre),
    avg(Shopping),avg(Picnic) 
    FROM review"""


CREATE_TEST_TABLE = """
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
     "name" VARCHAR(200) NOT NULL,
     "age" INT NOT NULL,
     "country_of_origin" VARCHAR(200) NOT NULL);
"""

INSERT_TEST_TABLE = """
    INSERT INTO test_table ("name","age","country_of_origin")
    VALUES ('Dylan Hoke',30,'U.S.A');
"""

DROP_TEST_TABLE = """
    DROP TABLE IF EXISTS test_table
"""

GET_CHARACTERS = """
    SELECT * FROM charactercreator_character;
"""

CREATE_CHARACTER_TABLE = """
    CREATE TABLE IF NOT EXISTS characters
    ("character_id" SERIAL NOT NULL PRIMARY KEY,
     "name" VARCHAR(200) NOT NULL,
     "level" INT NOT NULL,
     "exp" INT NOT NULL,
     "hp" INT NOT NULL,
     "strength" INT NOT NULL,
     "intelligence" INT NOT NULL,
     "dexterity" INT NOT NULL,
     "wisdom" INT NOT NULL
    );
"""

INSERT_DYLAN = """
    INSERT INTO characters ("name","level","exp","hp","strength",
    "intelligence","dexterity","wisdom")
    VALUES ('Dylan Hoke',50,100,1000,9000,4,-5,12)
"""

DROP_CHARACTER_TABLE = """
    DROP TABLE IF EXISTS characters
"""