from fastapi import FastAPI
from prisma import Prisma, register
from api.auth.login import router as login_router
from api.auth.admin_auth import router as admin_auth_router
from fastapi.middleware.cors import CORSMiddleware
from api.blogs.blogs import router as blog_router
from api.search.search import router as search_router
from api.ats.resume_routes import router as ats_router
from api.internships.internships import router as internships_router
app = FastAPI()

from api.auth.register import router as register_router

db = Prisma()
register(db)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(register_router)
app.include_router(login_router)
app.include_router(internships_router)
app.include_router(admin_auth_router)
app.include_router(blog_router)
app.include_router(ats_router)
app.include_router(search_router)
