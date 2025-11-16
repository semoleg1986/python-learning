from month2.week1.day4_responses_status.application.commands.item.update_item import (
    UpdateItemCommand,
)
from month2.week1.day4_responses_status.domain.entitites.item_model import Item
from month2.week1.day4_responses_status.interface.api.v1.items.request import (
    RequestUpdateItem,
)
from month2.week1.day4_responses_status.interface.api.v1.items.response import (
    ResponseItem,
)


class ItemMapper:
    @staticmethod
    def dto_to_command(dto: RequestUpdateItem) -> UpdateItemCommand:
        return UpdateItemCommand(
            name=dto.name,
            price=dto.price,
        )

    @staticmethod
    def domain_to_dto(item: Item) -> ResponseItem:
        """Превратить доменную сущность → DTO для ответа API."""
        return ResponseItem(
            id=item.id,
            name=item.name,
            price=item.price,
        )
