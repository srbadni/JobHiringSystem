from dataclasses import dataclass


@dataclass
class PaginatedResult[T]:
    items: list[T]
    total: int
    page_index: int
    page_size: int