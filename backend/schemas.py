from typing import List, Literal

from common import Status

from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    price: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int
    item_id: int
    order_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    status: Status = Status.submitted

class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    date: datetime
    items: List[OrderItem] = []

    class Config:
        orm_mode = True
