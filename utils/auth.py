from fastapi import Depends, HTTPException, status, Header
from sqlalchemy.ext.asyncio import AsyncSession
from crud.users import get_user_by_token
from config.db_conf import get_db

async def get_current_user(
        authorization: str = Header(...),  # ✅ 没有 alias
        db: AsyncSession = Depends(get_db)
):
    # ✅ 必须加这个检查！
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的认证格式，请使用 Bearer token"
        )

    # ✅ 安全提取 token
    token = authorization.split(" ")[1]

    user = await get_user_by_token(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的令牌"
        )
    return user