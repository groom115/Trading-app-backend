from app import create_app
# from app.api import auth, random_number, file_operations, streaming

app = create_app()

# Include routers
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(random_number.router, prefix="/random", tags=["Random Numbers"])
# app.include_router(file_operations.router, prefix="/csv", tags=["CSV Operations"])
# app.include_router(streaming.router, prefix="/stream", tags=["Streaming"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend!"}
