from fastapi import FastAPI, Request, HTTPException, Response,status, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from typing import Annotated

from sqlalchemy import select, exists,delete
from sqlalchemy.sql import func

from backend.db import Base, engine, get_db
from backend.model import urlmap
from backend.validation_model import LongUrl, UrlMapResponse, UrlMapStats
from backend.utility import create_short_code

mem = {}
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors()},
    )

db_dependancy = Annotated[Session,Depends(get_db)]

def mapping_exists(shortcode: str, db: Session):
    stmt = select(exists().where(urlmap.shortcode == shortcode))
    return db.execute(stmt).scalar()


@app.post("/shrtn", status_code=status.HTTP_201_CREATED, response_model=UrlMapResponse)
async def create_url(originalurl: LongUrl,db: db_dependancy):
    
    while True:
        short_code = create_short_code()
        print(short_code,mapping_exists(short_code, db))
        if not mapping_exists(short_code, db):
            break

    urlmapping = urlmap(url=originalurl.url, shortcode = short_code)
    db.add(urlmapping)
    db.commit()
    db.refresh(urlmapping)     
    return urlmapping


@app.get('/shrtn/{short_code}',response_model=UrlMapResponse)
async def get_url(short_code: str, db: db_dependancy):
    if not mapping_exists(short_code, db):
        raise HTTPException(404,"No url mapped to this short url")
    stmt = select(urlmap).where(urlmap.shortcode == short_code)
    urlmapping = db.execute(stmt).scalars().first()
    urlmapping.accessCount += 1
    db.commit()
    db.refresh(urlmapping)
    return urlmapping
    

@app.put('/shrtn/{short_code}',response_model=UrlMapResponse)
async def update_original_url(short_code: str, originalurl: LongUrl, db: db_dependancy):
    if not mapping_exists(short_code, db):
        raise HTTPException(404,"No url mapped to this short url")
    stmt = select(urlmap).where(urlmap.shortcode == short_code)
    urlmapping = db.execute(stmt).scalars().first()
    urlmapping.url = originalurl.url
    urlmapping.updatedAt = func.now() 
    db.commit()
    db.refresh(urlmapping)
    return urlmapping



@app.delete('/shrtn/{short_code}')
async def delete_url(short_code: str,db:db_dependancy):
    if not mapping_exists(short_code, db):
        raise HTTPException(404,"No url mapped to this short url")
    stmt = delete(urlmap).where(urlmap.shortcode == short_code)
    db.execute(stmt)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/shrtn/{short_code}/stats',response_model=UrlMapStats)
async def get_url(short_code: str,db:db_dependancy):
    if not mapping_exists(short_code, db):
        raise HTTPException(404,"No url mapped to this short url")
    stmt = select(urlmap).where(urlmap.shortcode == short_code)
    urlmapping = db.execute(stmt).scalar()
    return urlmapping


