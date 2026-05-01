from fastapi import FastAPI

app = FastAPI()

# single query parameter
# @app.get("/products")
# async def products(category: str):
#     return {"status": "ok", "category": category}


# multiple query parameter
# @app.get("/products")
# async def products(category: str, limit: int):
#     return {"status": "ok", "category": category, "limit": limit}


# Default query parameter
# @app.get("/products")
# async def products(category: str = "all", limit: int = 10):
#     return {"status": "ok", "category": category, "limit": limit}


# Optional query parameter
# @app.get("/products")
# async def products(category: str = None, limit: int = 10):
#     return {"status": "ok", "category": category, "limit": limit}


# path and query parameter
@app.get("/products/{year}")
async def products(year: str, category: str ):
    return {"status": "ok", "year": year, "category": category}







































