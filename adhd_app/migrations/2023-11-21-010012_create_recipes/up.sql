-- Your SQL goes here
create table users(
    id_user uuid primary key,
    username varchar not null,
    password_hash varchar not null,
    email varchar not null,
    first_name varchar,
    last_name varchar,
    dob timestamp not null
);

create table recipes (
    id_recipe uuid primary key,
    id_user uuid,
    title varchar not null,
    body varchar not null,
    published boolean not null default false,
    foreign key(id_user) references users(id_user)
);