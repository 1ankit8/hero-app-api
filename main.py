from fastapi import FastAPI

from app.api import app_router as appRouter

app = FastAPI()

app.include_router(appRouter.router)


@app.get("/health", tags=["App"])
async def health_check():
    return {"status": "healthy again"}