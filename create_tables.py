from app.database import Base
from app.database import engine

import app.models

Base.metadata.create_all(bind=engine)

print("Tables created")
