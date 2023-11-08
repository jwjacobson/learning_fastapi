from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title='Description of the item', max_length=200
    )
    price: float = Field(gt=0, description='price must be greater than zero')
    tax: float | None = None

app = FastAPI()

# @app.post('/items/')
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({'price with tax': price_with_tax})
#     return item_dict

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item=Body(embed=True)):
    result = {'item_id': item_id, 'item': item}
    return result