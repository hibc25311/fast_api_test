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
    id: Optional[int]
    customer_name: Optional[str]
    customer_id: int
    puechase_time: Optional[datetime]

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):

    order_id: int
    product_name: Optional[str]
    amount: int
    product_id: int
    price: Optional[int]

    class Config:
        orm_mode = True


class CustomerSchema(CustomerBase):
    orders: List[OrderBase]


class ProductSchema(ProductBase):
    orders: List[OrderItemBase]


class OrderSchema(OrderBase):
    products: List[OrderItemBase]
