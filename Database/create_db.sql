-- Create the database
CREATE DATABASE noicee_tshirts;
USE noicee_tshirts;

-- Create the t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for each t-shirt entry',
    brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas') NOT NULL COMMENT 'Brand of the t-shirt',
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL COMMENT 'Color of the t-shirt',
    size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL COMMENT 'Size of the t-shirt',
    price INT CHECK (price BETWEEN 10 AND 50) COMMENT 'Price in arbitrary units, between 10 and 50',
    stock_quantity INT NOT NULL COMMENT 'Number of items available in stock',
    UNIQUE KEY brand_color_size (brand, color, size)
) COMMENT = 'Table storing t-shirt product information';

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for each discount entry',
    t_shirt_id INT NOT NULL COMMENT 'Foreign key referencing the t-shirt being discounted',
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100) COMMENT 'Discount percentage (0-100)',
    FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
) COMMENT = 'Table storing discount information for t-shirts';

-- Create a stored procedure to populate the t_shirts table
DELIMITER $$
CREATE PROCEDURE PopulateTShirts()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 100;
    DECLARE brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas');
    DECLARE color ENUM('Red', 'Blue', 'Black', 'White');
    DECLARE size ENUM('XS', 'S', 'M', 'L', 'XL');
    DECLARE price INT;
    DECLARE stock INT;

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values
        SET brand = ELT(FLOOR(1 + RAND() * 4), 'Van Huesen', 'Levi', 'Nike', 'Adidas');
        SET color = ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White');
        SET size = ELT(FLOOR(1 + RAND() * 5), 'XS', 'S', 'M', 'L', 'XL');
        SET price = FLOOR(10 + RAND() * 41);
        SET stock = FLOOR(10 + RAND() * 91);

        -- Attempt to insert a new record
        -- Duplicate brand, color, size combinations will be ignored due to the unique constraint
        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;  -- Handle duplicate key error
            INSERT INTO t_shirts (brand, color, size, price, stock_quantity)
            VALUES (brand, color, size, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to populate the t_shirts table
CALL PopulateTShirts();

-- Insert at least 10 records into the discounts table
INSERT INTO discounts (t_shirt_id, pct_discount)
VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00);