create extension if not exists vector with schema public

create table "public"."document" (
    id bigserial primary key,
    source_link text not null unique,
    source_type text not null
)

create table "public"."section" (
    id bigserial primary key,
    document_id bigint not null references public.document on delete cascade,
    content text,
    token_count int,
    embedding vector(1536)
)
