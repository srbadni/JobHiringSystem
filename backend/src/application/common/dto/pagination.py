from dataclasses import dataclass


@dataclass
class Pagination:
    total: int
    page_index: int
    page_size: int