from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


# Multiple body parameters
class Product(BaseModel):
    name: str
    price: float
    stock: int

class Seller(BaseModel):
    username: str
    full_name: str | None = None

# @app.post("/products/")
# async def create_product(product: Product, seller: Seller):
#     return {"product": product, "seller": seller}

## Make Body optional
# @app.post("/products")
# async def create_product_optional(product: Product, seller: Seller | None = None):
#     return {"product": product, "seller": seller}


## Singular value in the body
# @app.post("/products")
# async def create_product(
#     product: Product,
#     seller:Seller,
#     sec_key: Annotated[str, Body()]
# ):
#     return {"product": product, "seller": seller, "sec_key": sec_key}



## Embed a single body parameter


# without embed
# @app.post("/products")
# async def create_product(product: Product):
#     return product

# the output:->
# {
#   "name": "string",
#   "price": 0,
#   "stock": 0
# }



# with embed
@app.post("/products")
async def create_product(product: Annotated[Product,Body(embed=True)]):
    return product

# the output:->
# {
#   "product": {
#     "name": "string",
#     "price": 0,
#     "stock": 0
#   }
# }