CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	birthdate DATE,
	street TEXT,
	city TEXT,
	phone TEXT UNIQUE,
	created_at TIMESTAMP
);
