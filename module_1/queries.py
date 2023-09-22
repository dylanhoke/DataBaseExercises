SELECT_ALL = "SELECT character_id,name FROM charactercreator_character;"

AVG_ITEM_WEIGHT_PER_CHARACTER = """SELECT ccc.name,avg(ai.weight) AS avg_item_weight FROM charactercreator_character as ccc
JOIN charactercreator_character_inventory as ccci 
ON ccc.character_id = ccci.character_id
JOIN armory_item as ai
ON ai.item_id = ccci.item_id
GROUP BY ccc.character_id"""