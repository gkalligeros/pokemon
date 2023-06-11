import json
from typing import Optional, Union, List, Any
from zlib import adler32
from abc import ABC, abstractmethod

try:
    from redis import Redis
    from redis.exceptions import RedisError
except ImportError:
    Redis = object
    RedisError = Exception
from config import config


class Cache(ABC):
    @abstractmethod
    def get_json(self, key: str) -> Optional[Union[list, dict]]:
        """Return decoded JSON value from cache if key exists, else None"""

    @abstractmethod
    def store_json(self, key: str, value: Any, expire: Optional[int] = None) -> None:
        """Store value as JSON string in cache under `key`, optionally for `expire` seconds """

    @abstractmethod
    def del_key(self, key: str) -> None:
        """Delete a key from cache"""

    @abstractmethod
    def in_cache(self, key: str) -> bool:
        """Check if key exists in cache"""


class RedisCache(Cache):
    def __init__(self):
        if Redis is object:
            self.client = None
            return
        try:
            self.client = Redis(
                host=config.REDIS_HOST,
                username=config.REDIS_USER,
                password=config.REDIS_PASSWORD,
                db=0,
                socket_timeout=5,
                decode_responses=True,
            )
        except Exception:
            self.client = None

    def get_json(self, key: str) -> Optional[Union[list, dict]]:
        if not self.client:
            return None
        value = self.client.get(key)
        if value:
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError) as e:
                return None
        return None

    def del_key(self, key: str) -> None:
        if not self.client:
            return
        if self.in_cache(key):
            self.client.delete(key)
        return

    def in_cache(self, key: str) -> bool:
        return self.client.exists(key)

    def store_json(
            self, key: str, value: Union[list, dict], expire: int = None
    ) -> None:
        if not self.client:
            return
        self.client.set(key, json.dumps(value), ex=expire)

    def generate_key(self, function_name: str, params: List[Any]):
        params_str = f"{[str(param) for param in params]}"
        return f"{function_name}:{adler32(params_str.encode())}"


class DummyCache(Cache):

    def __init__(self):
        pass

    def get_json(self, key: str) -> Optional[Union[list, dict]]:
        return None

    def del_key(self, key: str) -> None:
        return

    def in_cache(self, key: str) -> bool:
        return False

    def store_json(
            self, key: str, value: Union[list, dict], expire: int = None
    ) -> None:
        pass

    def generate_key(self, function_name: str, params: List[Any]):
        params_str = f"{[str(param) for param in params]}"
        return f"{function_name}:{adler32(params_str.encode())}"


def get_cache() -> Any:
    if config.CACHE_DRIVER == 'redis':
        return RedisCache()
    return DummyCache()
