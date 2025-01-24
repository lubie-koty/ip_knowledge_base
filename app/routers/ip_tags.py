from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from app.dependencies import get_ip_tags_service
from app.ip_tags.types import BaseIpTagsService

router = APIRouter(
    tags=["ip-tags"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="templates")


@router.get("/ip-tags/{ip_address}")
async def get_ip_tags_list(
    ip_tags_service: Annotated[BaseIpTagsService, Depends(get_ip_tags_service)],
    ip_address: str,
):
    return JSONResponse(await ip_tags_service.get_tags_list(ip_address))


@router.get("/ip-tags-report/{ip_address}")
async def get_ip_tags_report(
    ip_tags_service: Annotated[BaseIpTagsService, Depends(get_ip_tags_service)],
    request: Request,
    ip_address: str,
):
    tags_list = await ip_tags_service.get_tags_list(ip_address)
    return templates.TemplateResponse(
        request=request,
        name="ip_tags_report.html",
        context={"ip_address": ip_address, "tags": tags_list},
    )
