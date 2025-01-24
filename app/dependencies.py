from typing import Annotated

from fastapi import Depends, Request

from app.ip_tags.repo import IpTagsStateRepo
from app.ip_tags.service import IpTagsService
from app.ip_tags.types import BaseIpTagsRepo, BaseIpTagsService


async def get_ip_tags_state_repo(request: Request) -> BaseIpTagsRepo:
    return IpTagsStateRepo(request)


async def get_ip_tags_service(
    ip_tags_repo: Annotated[BaseIpTagsRepo, Depends(get_ip_tags_state_repo)],
) -> BaseIpTagsService:
    return IpTagsService(ip_tags_repo)
