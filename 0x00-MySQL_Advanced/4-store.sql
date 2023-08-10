-- SQL script that creates a trigger that decreases 
-- quantity of an item
DELIMITER //
CREATE TRIGGER dq
AFTER INSERT
ON `orders`
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE NEW.item_name = items.name;
END;
//
DELIMITER ;
