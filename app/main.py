import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 5678))
ptvsd.wait_for_attach()


from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel

from .routers import auth

app = FastAPI()

app.include_router(auth.router)

@app.get("/users/me/", response_model=auth.User)
async def read_users_me(current_user: auth.User = Depends(auth.get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: auth.User = Depends(auth.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]