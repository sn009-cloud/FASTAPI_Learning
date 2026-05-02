from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

## Using Field-level Exaples
# class Product(BaseModel):
#     name: str = Field(example=["Laptop"])
#     price: float = Field(example=[999.99])
#     stock: int | None = Field(default=None, example=[45])


# @app.post("/products")
# async def create_product(product: Product):
#     return product


## Using Pydantic’s json_schema_extra
class Product(BaseModel):
  name: str
  price: float
  stock: int | None = None

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "name": "Laptop",
          "price": 999.99,
          "stock": 45
        }
      ]
    }
  }

@app.post("/products")
async def create_product(product: Product):
    return product