from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    orders = relationship("Order", back_populates="customers")
    # User to order 1 to many


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(ForeignKey("products.id"))
    order_id = Column(ForeignKey("orders.id"))

    product_name = Column(String, index=True)
    amount = Column(Integer)
    price = Column(Integer)

    orders = relationship("Order", back_populates="products")
    products = relationship("Product", back_populates="orders")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(ForeignKey("customers.id"))
    customer_name = Column(String, index=True)
    puechase_time = Column(DateTime, default=func.now())

    customers = relationship("Customer", back_populates="orders")
    ##
    products = relationship("OrderItem", back_populates="orders")


'''
    __table_args__ = (ForeignKeyConstraint(
        ['customer_id', 'customer_name'],
        ['customers.id', 'customers.name']), )
'''


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

    orders = relationship("OrderItem", back_populates="products")


'''
    __table_args__ = (ForeignKeyConstraint(['product_id', 'product_name'],
                                           ['products.id', 'products.name']), )'''
