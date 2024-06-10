CREATE TABLE manufacturers(
	manufacturer_id int identity(2,2) primary key,
	manufacturer_name varchar(15) not null,
	business_num varchar(30) UNIQUE not null,
	manufacturer_country varchar(30) 
)


CREATE TABLE cars (
	car_id int identity(1,2) primary key,
	model varchar(15) not null,
	color varchar(15) DEFAULT 'balck',
	manufacturer int FOREIGN KEY REFERENCES manufacturers(manufacturer_id) not null,
	manufacturer_date DATE DEFAULT getdate(),
	license_num varchar(11) UNIQUE not null,
	price int not null,
	num_seats int
)


CREATE TABLE users(
	user_id int identity(100,100) primary key,
	user_name varchar(20),
	user_address varchar(50) UNIQUE not null,
	user_email varchar(30) not null,
	credit_card varchar(16),
	user_age int
)

