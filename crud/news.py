from unittest import result

from sqlalchemy import select,func,update
from sqlalchemy.ext.asyncio import AsyncSession
from models.news import News
from models.news import Category

async def get_categories(db:AsyncSession,skip:int=0,limit:int=10):
    stmt = select(Category).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_news_list(db:AsyncSession,category_id:int,skip:int = 0,limit:int =10):
    #查询指定分类下所有新闻
    stmt = select(News).where(News.category_id == category_id).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_news_count(db:AsyncSession,category_id:int):
    #查询指定分类下新闻数量
    stmt = select(func.count(News.id)).where(News.category_id == category_id)
    result = await db.execute(stmt)
    return result.scalar_one() #只能有一个结果

async def get_new_detail(db:AsyncSession,news_id:int):
    #查询指定分类下新闻数量
    stmt = select(News).where(News.id == news_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def increase_news_views(db:AsyncSession,news_id:int):
    #增加新闻浏览量
    stmt = update(News).where(News.id == news_id).values(views=News.views+1)
    result = await db.execute(stmt)
    await db.flush()
    #更新————检查数据库是否真正命中
    return result.rowcount > 0

async def get_related_news(db:AsyncSession,news_id:int,category_id:int,limit:int =5):
    stmt = select(News).where(News.category_id == category_id,News.id != news_id).order_by(News.views.desc(),News.publish_time.desc()).limit(limit)
    result = await db.execute(stmt)
    # return result.scalars().all()
    related_news=result.scalars().all()
    return [{"id": news.id,
            "title": news.title,
            "content": news.content,
            "image": news.image,
            "author": news.author,
            "publishTime": news.publish_time,
            "categoryId": news.category_id,
            "views": news.views,
             } for news in related_news]
