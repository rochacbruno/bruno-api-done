"""
bruno_api base module.
"""
from fastapi import FastAPI
from .routes import main_router
from .db import init_db
from .security import router as security_router


app = FastAPI(  
    title="project_name",
    description="**API** 123 ![](http://place.dog/50/50/)",
    version="0.1.0",
    terms_of_service="http://project_name.com/terms/",
    contact={
        "name": "author_name",
        "url": "http://project_name.com/contact/",
        "email": "authorname@projectname.com",
    },
    license_info={
        "name": "The Unlicense",
        "url": "https://unlicense.org",
    },
    on_startup=[init_db]
)

app.include_router(main_router)
app.include_router(security_router)