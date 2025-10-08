from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from app.core.config import settings

# Create SQLAlchemy engine using SQLite database
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create a scoped session factory
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# Base class for all ORM models
Base = declarative_base()

def init_db():
    """
    Initialize the database by creating all tables defined in the models.
    """
    import app.models.user  # noqa
    import app.models.recipe  # noqa
    import app.models.rating  # noqa
    Base.metadata.create_all(bind=engine)
