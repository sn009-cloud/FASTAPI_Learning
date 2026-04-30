from fastapi import FastAPI

app = FastAPI()

# GET Request
## Read or Fetch All Data
@app.get("/product")
async def all_products():
    return {"response": "All Products"}

## Read or Fetch Single Data
@app.get("/product/{product_id}")
async def all_products(product_id:int):
    return {"response": "Single Data Fetched", "Product_id": product_id}

# POST Request
## Read or Fetch Single Data
@app.post("/product")
async def create_products(new_product:dict):
    return {"response": "product created", "new_Product": new_product}




































