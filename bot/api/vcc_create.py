from fastapi import APIRouter

router = APIRouter(tags=["create"])


@router.post("/vcc/create/")
async def vcc_create():
    return {"message": "Hello World"}
