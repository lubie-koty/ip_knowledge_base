from fastapi import status
from fastapi.exceptions import HTTPException

from app.ip_tags.types import BaseIpTagsRepo, BaseIpTagsService


class IpTagsService(BaseIpTagsService):
    def __init__(self, tags_repo: BaseIpTagsRepo) -> None:
        self.tags_repo = tags_repo

    async def get_tags_list(self, ip_address: str) -> list[str]:
        try:
            all_tags = await self.tags_repo.get_tags_for_ip_address(ip_address)
        except Exception:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Incorrect IP address")
        result = set()
        for tags in all_tags:
            result |= tags
        return sorted(result)
