## Cookie parameter example
# from fastapi import FastAPI, Cookie
# from typing import Annotated

# app = FastAPI()

# @app.get("/products/recommendations")
# async def get_recommendations(session_id: Annotated[str | None, Cookie()] = None):
#     if session_id:
#         return {"message": f"Recommendations for session {session_id}",
#                 "session_id": session_id}
#     else:
#         return {"message": "No session ID provided, showing generic recommendations"}













