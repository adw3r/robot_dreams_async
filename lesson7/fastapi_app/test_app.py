import pytest
import app


@pytest.mark.asyncio
async def test_create_item():
    repo = app.ItemRepo()
    r = await app.create_item(
        item=app.Item(
            id=1, name="item", price=1.0, tax=0.1, description="desc"
        ),
        repo=repo,
    )

    assert r.id is not None

    assert len(repo.list()) == 1
