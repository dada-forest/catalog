# catalog

## Alembic Notes
alembic init alembic
alembic revision --autogenerate -m "migration name/note"

# head refers to the latest migration, 
# but we can provide a different "target" migration here
alembic upgrade head