from month2.week1.day3_validation.application.services.item_service import ItemService
from month2.week1.day3_validation.application.services.user_service import UserService
from month2.week1.day3_validation.infrastructure.repositories.item_memory import (
    ItemRepositoryMemory,
)
from month2.week1.day3_validation.infrastructure.repositories.user_memory import (
    UserRepositoryMemory,
)

repo_users = UserRepositoryMemory()
user_service = UserService(repo_users)

repo_items = ItemRepositoryMemory()
items_service = ItemService(repo_items)
