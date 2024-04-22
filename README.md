# catalog

DADA-Forest Application

## Alembic Notes
alembic init alembic
alembic revision --autogenerate -m "migration name/note"

# head refers to the latest migration, 
# but we can provide a different "target" migration here
alembic upgrade head


## Resources
https://medium.com/enterprise-rag/a-first-intro-to-complex-rag-retrieval-augmented-generation-a8624d70090f
https://blog.gopenai.com/rag-with-pg-vector-with-sql-alchemy-d08d96bfa293
