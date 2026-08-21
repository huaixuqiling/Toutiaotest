import redis.asyncio as redis

REDIS_HOST="localhost"
REDIS_PORT=6379
REDIS_DB=0

#创建Redis链接对象
redis_client=redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True
)

async def get_cache(key:str):
    await redis_client.get(key)
