-- SQL script that creates a trigger that decreases quantity of an item
DELIMITER //
CREATE TRIGGER after_insert_order
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    -- Decrease the quantity of the corresponding item in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE id = NEW.item_id;
END;
//
DELIMITER ;
