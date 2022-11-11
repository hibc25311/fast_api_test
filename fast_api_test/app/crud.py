from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session
from .models import Customer, Order, Product, OrderItem
from .schemas import CustomerBase, OrderBase, ProductBase, OrderItemBase


def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: CustomerBase):
    db_customer = Customer(name=customer.name)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


#--------------------------------------
def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: OrderBase):
    customer = db.query(Customer).filter(
        Customer.id == order.customer_id).first()
    db_order = Order(customer_id=customer.id, customer_name=customer.name)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


#-----------------------------------------
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductBase):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


#--------------------------------------
def get_order_item(db: Session, order_id: int):
    return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()


def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OrderItem).offset(skip).limit(limit).all()


def create_order_items(db: Session, order_item: OrderItemBase):
    order = db.query(Order).filter(Order.id == order_item.order_id).first()
    product = db.query(Product).filter(
        Product.id == order_item.product_id).first()
    db_order_item = OrderItem(product_id=product.id,
                              order_id=order.id,
                              product_name=product.name,
                              amount=order_item.amount,
                              price=order_item.amount * product.price)
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


def update_order_item(db: Session, order_id: int, product_id,
                      update_order_item: OrderItemBase):
    orignal_order_item = db.query(OrderItem).filter(
        OrderItem.order_id == order_id).filter(
            OrderItem.product_id == product_id).first()

    if orignal_order_item is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")

    orignal_order_item.product_id = update_order_item.product_id
    orignal_order_item.amount = update_order_item.amount

    db.commit()
    db.refresh(orignal_order_item)

    return orignal_order_item