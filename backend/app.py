from fastapi import FastAPI, Request, HTTPException, Response,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import random
import string

from backend.models import LongUrl


mem = {}
app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors()},
    )


def create_short_code(length=7):
    """Generate a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.post("/shrtn", status_code=status.HTTP_201_CREATED)
async def create_url(originalurl: LongUrl):
    short_code = create_short_code()
    mem[short_code] = {
        'id': str(len(mem)),
        'url': originalurl.url,
        "shortCode": short_code,
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z",
        'accessCount':0
    }
    return {k:v for k,v in mem[short_code].items() if k != "accessCount"}


@app.get('/shrtn/{short_code}')
async def get_url(short_code: str):
    if short_code not in mem:
        raise HTTPException(404,"No url mapped to this short url")
    mem[short_code]['accessCount'] += 1    
    return {k:v for k,v in mem[short_code].items() if k != "accessCount"}
    

@app.put('/shrtn/{short_code}')
async def update_original_url(short_code: str, originalurl: LongUrl):
    if short_code not in mem:
        raise HTTPException(404,"No url mapped to this short url")
    mem[short_code]['url'] = originalurl.url    
    return {k:v for k,v in mem[short_code].items() if k != "accessCount"}



@app.delete('/shrtn/{short_code}')
async def delete_url(short_code: str):
    if short_code not in mem:
        raise HTTPException(404,"No url mapped to this short url")
    mem.pop(short_code)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/shrtn/{short_code}/stats')
async def get_url(short_code: str):
    if short_code not in mem:
        raise HTTPException(404,"No url mapped to this short url") 
    return mem[short_code]
    



