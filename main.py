from enum import Enum

from fastapi import FastAPI

class Musician(str, Enum):
    trane = 'trane'
    mccoy = 'mccoy'
    elvin = 'elvin'

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str | None = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get('/musicians/{musician}')
async def get_musician(musician: Musician):
    if musician is Musician.trane:
        return {'musician': musician, 'instrument': 'tenor'}
    
    if musician.value == 'mccoy':
        return {'musician': musician, 'instrument': 'piano'}

    return {'musician': musician, 'instrument': drums}
    

