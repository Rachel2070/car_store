-- Step 1: Drop the unique constraint on user_address
-- If the constraint was named explicitly when created:
ALTER TABLE users DROP CONSTRAINT UQ__users__18CD904A699CAAD1;

-- If the constraint name is unknown, you can query the database metadata to find it, or drop the column and recreate it without the unique constraint.
-- Assuming no explicit name, you would need to find and use the actual constraint name.

-- Step 2: Add a unique constraint to user_email
ALTER TABLE users ADD CONSTRAINT UQ_users_user_email UNIQUE (user_email);

-- Step 3: Alter user_name to be not null
ALTER TABLE users ALTER COLUMN user_name varchar(20) NOT NULL;

SELECT CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
WHERE TABLE_NAME = 'users' AND COLUMN_NAME = 'user_address';


alter table users
add password varchar(10)

ALTER TABLE users
ALTER COLUMN password VARCHAR(10) NOT NULL;

CREATE UNIQUE INDEX uq_password ON users(password);

CREATE UNIQUE INDEX uq_user_name ON users(user_name);
