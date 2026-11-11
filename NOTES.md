
# FastAPI Learning Notes

## Installed Packages

- FastAPI (Build APIs)
- Uvicorn (Runs the API server)
- SQLAlchemy (Handles database operations)
- psycopg2-binary (Connects Python to PostgreSQL)
- python-dotenv 
- pydantic (Data Validation)

## Database Configuration

- create_engine: Creates database connection.
- sessionmaker: Creates database sessions.
- declarative_base: Creates base class for models.
- load_dotenv: Loads environment variables.

## Pydantic – Data Validation.

In FastAPI, Pydantic is used to:
- Validate incoming data.
- Define data structures (schemas).
- Check data types.
- Serialize data into JSON.