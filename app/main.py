from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.api.routes import router as api_router


# Create all database tables on startup (based on SQLAlchemy models)
Base.metadata.create_all(bind=engine)


# Initialize FastAPI application with custom metadata
app = FastAPI(
    title="Progresso API",
    version="1.0.0"
)


# can communicate with the API without being blocked by the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],        
)


# Load all API routes from the central router
app.include_router(api_router)


# Root endpoint to verify that the API is running
@app.get("/")
def root():
    return {"message": "Progresso API running"}
