from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

## Pydantic's field
class Product(BaseModel):
    name: str = Field(
        title = "Product Name", 
        description="The name of the product",
        max_length=100,
        min_length=3,
        pattern="^[a-zA-Z0-9]+$"
        )
    price: float = Field(
        gt=0,
        title = "Product Price",
        description="The price must be greater than zero"
        )
    stock: int = Field(
        ge=0,
        default=None,
        title = "Stock quantity",
        description="The quantity of the product in stock,must be in non-negative"
        )

@app.post("/products/")
async def create_product(product: Product):
    return product







