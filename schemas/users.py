from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic import Field


class UserRequest(BaseModel):
    username:str
    password:str

class UserInfoBase(BaseModel):
    nickname:Optional[str] = Field(None,max_length=50,description="昵称")
    avatar: Optional[str] = Field(None, max_length=255, description="头像")
    gender: Optional[str] = Field(None, max_length=10,description="性别")
    bio: Optional[str] = Field(None, max_length=500, description="个人简介")

class UserInfoResponse(UserInfoBase):
    id:int
    username:str
    model_config = ConfigDict(
        from_attributes=True
    )

class UserAuthResponse(BaseModel):
    token:str
    user_info:UserInfoResponse = Field(...,alias="userInfo")
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )

class UserUpdateRequest(BaseModel):
    nickname:str=None
    avatar:str=None
    gender:str=None
    bio:str=None
    phone:str=None


class UserChangePasswordRequest(BaseModel):
    old_password:str = Field(...,description="旧密码",alias="oldPassword")
    new_password: str = Field(...,min_length=6,max_length=50, description="新密码", alias="newPassword")

