from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from collections.abc import Sequence
from .models import User


def make_user(name: str, age: int) -> User:
    return User(name=name, age=age)


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.name)
    result = await session.execute(stmt)
    return result.scalars().all()
