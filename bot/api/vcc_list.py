from fastapi import APIRouter

router = APIRouter(tags=["list"])


@router.get("/vcc/list/")
async def vcc_list():
    return {"message": "Hello World"}
