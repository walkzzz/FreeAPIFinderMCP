import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import main_router
from app.db.database import engine, Base
from app.crawler.spiders import PublicAPISpider, FreeAPISpider, RapidAPISpider, ProgrammableWebSpider
from app.crawler.scheduler import CrawlScheduler
from app.utils.logger import get_logger
from app.config_simple import API_HOST, API_PORT, CRAWL_INTERVAL

# Initialize logger
logger = get_logger(__name__)

# Create FastAPI application
app = FastAPI(
    title="FreeAPIFinderMCP",
    description="API for discovering free APIs",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(main_router)

# Initialize database
Base.metadata.create_all(bind=engine)

# Initialize crawler scheduler
spiders = [
    PublicAPISpider(),
    FreeAPISpider(),
    RapidAPISpider(),
    ProgrammableWebSpider()
]

scheduler = CrawlScheduler(spiders=spiders, interval=CRAWL_INTERVAL)

@app.on_event("startup")
async def startup_event():
    """Event handler for application startup"""
    logger.info("Starting FreeAPIFinderMCP server")
    # Start crawler scheduler in background
    import asyncio
    asyncio.create_task(scheduler.start())

@app.on_event("shutdown")
async def shutdown_event():
    """Event handler for application shutdown"""
    logger.info("Shutting down FreeAPIFinderMCP server")
    # Stop crawler scheduler
    await scheduler.stop()

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to FreeAPIFinderMCP",
        "version": "1.0.0",
        "documentation": "/docs"
    }

if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "app.main:app",
        host=API_HOST,
        port=API_PORT,
        reload=True
    )