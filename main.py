from enum import Enum

from fastapi import FastAPI

class Musician(str, Enum):
    trane = 'trane'
    mccoy = 'mccoy'
    elvin = 'elvin'

app = FastAPI()

# messy function to show different parameters etc.
# @app.get('/users/{user_id}/items/{item_id}')
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
#     ):
#     item = {'item_id': item_id, "owner_id": user_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {'description': 'ok whatever'}
#         )
#     return item

@app.get('/items/{item_id}')
async def read_user_utem(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item

@app.get('/musicians/{musician}')
async def get_musician(musician: Musician):
    if musician is Musician.trane:
        return {'musician': musician, 'instrument': 'tenor'}
    
    if musician.value == 'mccoy':
        return {'musician': musician, 'instrument': 'piano'}

    return {'musician': musician, 'instrument': drums}
    

