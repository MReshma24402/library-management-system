-- ===== BOOKS TABLE =====
CREATE TABLE books (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR2(255) NOT NULL,
    author VARCHAR2(255) NOT NULL,
    quantity NUMBER NOT NULL,
    CONSTRAINT chk_quantity CHECK (quantity >= 0)
);

-- ===== ISSUED BOOKS TABLE =====
CREATE TABLE issued_books (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    book_id NUMBER NOT NULL,
    user_name VARCHAR2(255) NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    fine NUMBER(10,2) DEFAULT 0,
    
    CONSTRAINT fk_book
    FOREIGN KEY (book_id) REFERENCES books(id)
    ON DELETE CASCADE
);

