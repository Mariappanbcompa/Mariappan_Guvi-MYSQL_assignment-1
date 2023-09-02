CREATE TABLE Boxes (Code CHAR(4) NOT NULL,
                    Contents VARCHAR(255) NOT NULL ,
                    Value REAL NOT NULL ,
                    Warehouse INTEGER NOT NULL,
                    PRIMARY KEY (Code),
                    FOREIGN KEY (Warehouse) REFERENCES Warehouses(Code)) ENGINE=INNODB;