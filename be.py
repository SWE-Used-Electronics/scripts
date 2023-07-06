from fastapi import APIRouter, FastAPI

description = """
# SE Project Sugondese
"""

app = FastAPI(
    title="Sugondese API",
    description=description,
    version="0.0.1",
)



router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={401: {"User": "Not authorized"}}
)

_name_ = None

@router.post("")
async def upload_name(name: str):
    global _name_
    _name_ = name


@router.get("")
async def get_name():
    global _name_
    return f"your name: {_name_}"


app.include_router(router)