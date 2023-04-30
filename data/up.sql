create table faqs
(
    id           serial
        constraint faqs_pk
            primary key,
    question_str varchar(4000),
    answer_str   varchar(4000),
    team_id      varchar(12)
);