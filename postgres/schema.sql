-- Crear tabla si no existe
CREATE TABLE IF NOT EXISTS product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

-- Insertar datos iniciales (seed)
INSERT INTO product (name, price) VALUES
('Producto 1', 100.00),
('Producto 2', 150.50),
('Producto 3', 200.99);
