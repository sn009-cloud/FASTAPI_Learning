from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

## without pydantic
## create or Insert Data
@app.post("/items/")
async def create_product(new_product: dict):
    return new_product  

## with pydantic
## Define the product model
class Product(BaseModel):
    id : int
    name: str
    price: float
    description: str = None
    stock: int

# @app.post("/products/")
# async def create_product(new_product: Product):
#     return new_product


## Access Attribute inside Function
# @app.post("/products/")
# async def create_product(new_product: Product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product

## Add new calculated attribute
@app.post("/products/")
async def create_product(new_product: Product):
    product_dict = new_product.model_dump()
    product_with_tax = new_product.price + (new_product.price * 18 / 100)
    product_dict.update({"price_with_tax": product_with_tax})
    return product_dict


## Adding Query Parameters
@app.put("/products/{product_id}")
async def update_product(product_id: int, new_updated_product: Product, discount: float | None = None):
    return {"product_id": product_id, "updated_product": new_updated_product, "discount": discount}
























