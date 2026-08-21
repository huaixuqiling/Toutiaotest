from fastapi import FastAPI
from routers import news, users,favorite
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

#挂载路由/注册路由
app.include_router(news.router)
app.include_router(users.router)
app.include_router(favorite.router)





