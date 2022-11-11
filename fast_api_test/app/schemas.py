from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    id: int
    customer_name: str
    customer_id: int
    puechase_time: datetime

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):

    order_id: int
    product_name: str
    amount: int
    product_id: int
    price: int

    class Config:
        orm_mode = True


class CustomerSchema(CustomerBase):
    orders: List[OrderBase]


class ProductSchema(ProductBase):
    orders: List[OrderBase]


class OrderSchema(OrderBase):
    products: List[ProductBase]


class OrderItemSchema(OrderItemBase):
    products: List[ProductBase]
    orders: List[OrderBase]
