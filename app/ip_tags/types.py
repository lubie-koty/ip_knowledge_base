from abc import ABC, abstractmethod
from typing import Iterable


class BaseIpTagsRepo(ABC):
    @abstractmethod
    async def get_tags_for_ip_address(self, ip_address: str) -> Iterable[set[str]]:
        pass


class BaseIpTagsService(ABC):
    @abstractmethod
    async def get_tags_list(self, ip_address: str) -> list[str]:
        pass
