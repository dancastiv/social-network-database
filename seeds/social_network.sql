-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS accounts cascade;
DROP SEQUENCE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    account_id int,
    constraint fk_account foreign key(account_id)
        references accounts(id)
        on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO accounts (email_address, username) VALUES ('diana_cavendish@lunanova.com', 'dcavendish');
INSERT INTO accounts (email_address, username) VALUES ('kagari.akko@lunanova.com', 'ShinyChariotFan1');
INSERT INTO accounts (email_address, username) VALUES ('manbavaran@lunanova.com', 'kinoko');

INSERT INTO posts (title, content, views, account_id) VALUES ('Samhain Festival', 'This is a reminder to the student body to carry their weight during the festival.', 2552, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Shiny Chariot at Luna Nova', 'I have been following in the footsteps of Chariot while at Luna Nova and I have discovered many things!', 4, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Importance of Schoolwork', 'Please remember that we are at school to learn, not follow terrible role models.', 3452, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Looking for mushrooms', 'I am looking for mushrooms. Will pay for information.', 632, 3);
INSERT INTO posts (title, content, views, account_id) VALUES ('How to unstransform oneself', 'Please help.', 5, 2);


