import ipaddress
import logging
from typing import Iterable

from fastapi import Request
from intervaltree import IntervalTree

from app.ip_tags.types import BaseIpTagsRepo

logger = logging.getLogger("uvicorn")


class IpTagsStateRepo(BaseIpTagsRepo):
    """
    Implementation of `BaseIpTagsRepo` using FastAPI Request's `state` to
    store the knowledge base containing ip networks and their tags.
    """

    def __init__(self, request: Request):
        self.knowledge_base: IntervalTree = request.app.state.knowledge_base

    async def get_tags_for_ip_address(self, ip_address: str) -> Iterable[set[str]]:
        try:
            converted_ip_address = ipaddress.ip_address(ip_address)
        except ValueError:
            logger.error("Invalid IP Address passed to the function")
            raise
        return (
            interval.data
            for interval in self.knowledge_base.at(int(converted_ip_address))
        )
