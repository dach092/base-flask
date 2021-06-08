
create table if not exists tasks(
    id integer primary key,
    title text not null,
    created_date text not null,
    completed integer not null default 0
)