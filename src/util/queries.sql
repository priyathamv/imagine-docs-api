create table
  public.document (
    id uuid DEFAULT gen_random_uuid(),
    data_source_id uuid not null,
    content text not null,
    token_count integer not null,
    metadata jsonb not null,
    embedding vector(1536) not null,
    constraint document_pkey primary key (id),
    constraint document_data_source_id_fkey foreign key (data_source_id) references data_source (id) on delete cascade
  ) tablespace pg_default;

-- Function to search for documents
CREATE OR REPLACE FUNCTION fetch_similar_documents (
  project_id_input uuid,
  embedding_input VECTOR(1536),
  match_count_input INT DEFAULT NULL,
  match_threshold_input FLOAT
) RETURNS TABLE (
  source_link TEXT,
  content TEXT,
  token_count INT,
  metadata JSONB,
  similarity FLOAT
)
LANGUAGE plpgsql
AS $$
#variable_conflict use_column
BEGIN
  RETURN query
  SELECT
    data_source.source_link,
    document.content,
    document.token_count,
    document.metadata,
    1 - (document.embedding <=> embedding_input) AS similarity
  FROM document
  JOIN data_source ON document.data_source_id = data_source.id
  WHERE (data_source.project_id = project_id_input) AND (1 - (document.embedding <=> embedding_input) > match_threshold_input)
  ORDER BY document.embedding <=> embedding_input
  LIMIT match_count_input;
END;
$$;



