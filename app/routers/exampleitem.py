from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from app.models.exampleitem import ExampleItem
from app.schemas.exampleitem import UpdateExampleItem


router = APIRouter(prefix="/exampleitems", tags=["exampleitems"])


@router.post("/", response_model=ExampleItem, response_model_by_alias=False, status_code=status.HTTP_201_CREATED)
async def create_exampleitem(payload: ExampleItem):
    await payload.insert()
    return payload


@router.get("/", response_model=list[ExampleItem], response_model_by_alias=False)
async def list_exampleitems():
    return await ExampleItem.find_all().to_list()


@router.get("/{id}", response_model=ExampleItem, response_model_by_alias=False)
async def get_exampleitem(id: str):
    item = await ExampleItem.get(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExampleItem {id} not found")
    return item


@router.patch("/{id}", response_model=ExampleItem, response_model_by_alias=False)
async def update_exampleitem(id: str, payload: UpdateExampleItem):
    item = await ExampleItem.get(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExampleItem {id} not found")
    update_data = {k: v for k, v in payload.model_dump().items() if v is not None}
    await item.set(update_data)
    return item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exampleitem(id: str):
    item = await ExampleItem.get(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExampleItem {id} not found")
    await item.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
