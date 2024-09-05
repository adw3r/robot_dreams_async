from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from collections.abc import Sequence
from .models import Address, User


def make_user(name: str, age: int) -> User:
    return User(name=name, age=age)


def make_address(user: User, line: str, city: str, country: str):
    return Address(user=user, line=line, city=city, country=country)


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.name)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_all_users_with_addresses(session: AsyncSession) -> Sequence[User]:
    stmt = (
        select(User)
        .options(joinedload(User.addresses, innerjoin=True))
        .order_by(User.name)
    )
    result = await session.scalars(stmt)
    return result.unique().all()
