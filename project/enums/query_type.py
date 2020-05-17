from enum import Enum


class QueryType(Enum):
    select = 0,
    insert = 1,
    update = 2,
    delete = 3
