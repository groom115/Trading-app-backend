from app import create_app
from app.routes import auth_routes
from app.core.db import engine
from app.models.user_model import Base 

app = create_app()
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
# app.include_router(random_number.router, prefix="/random", tags=["Random Numbers"])
# app.include_router(file_operations.router, prefix="/csv", tags=["CSV Operations"])
# app.include_router(streaming.router, prefix="/stream", tags=["Streaming"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend!"}
