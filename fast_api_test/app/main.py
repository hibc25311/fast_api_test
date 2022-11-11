from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from . import crud, models
from .schemas import CustomerBase, CustomerSchema, OrderSchema, ProductBase, ProductSchema, OrderBase, OrderItemBase
from .database import SessionLocal, engine

from sqlalchemy.orm.session import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------------
origins = ["http://localhost:8000", "http://localhost:3000"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# -----------------------------------


@app.get("/customers/{customer_id}", response_model=CustomerSchema)
def read_customer_id(customer_id: int, db: Session = Depends(get_db)):
    res = crud.get_customer(db, customer_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res


@app.get("/customers", response_model=List[CustomerBase])
def read_customers(skip: int = 0,
                   limit: int = 100,
                   db: Session = Depends(get_db)):
    res = crud.get_customers(db, skip, limit)
    return res


@app.post("/customers", response_model=CustomerBase)
def create_customer(customer: CustomerBase, db: Session = Depends(get_db)):
    try:
        res = crud.create_customer(db, customer)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)


#------------------------------
@app.get("/orders/{order_id}", response_model=OrderSchema)
def read_order_id(order_id: int, db: Session = Depends(get_db)):
    res = crud.get_order(db, order_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res


@app.get("/orders", response_model=List[OrderBase])
def read_orders(skip: int = 0,
                limit: int = 100,
                db: Session = Depends(get_db)):
    res = crud.get_orders(db, skip, limit)
    return res


@app.post("/orders", response_model=OrderBase)
def create_order(order: OrderBase, db: Session = Depends(get_db)):
    try:
        res = crud.create_order(db, order)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)


#------------------------------
@app.get("/products/{product_id}", response_model=ProductSchema)
def read_product_id(product_id: int, db: Session = Depends(get_db)):
    res = crud.get_product(db, product_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res


@app.get("/products", response_model=List[ProductBase])
def read_products(skip: int = 0,
                  limit: int = 100,
                  db: Session = Depends(get_db)):
    res = crud.get_products(db, skip, limit)
    return res


@app.post("/products", response_model=ProductBase)
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    try:
        res = crud.create_product(db, product)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)


#------------------------------
@app.get("/order_items/{order_id}", response_model=List[OrderItemBase])
def read_order_items_id(order_id: int, db: Session = Depends(get_db)):
    res = crud.get_order_item(db, order_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res


@app.get("/order_items", response_model=List[OrderItemBase])
def read_order_items(skip: int = 0,
                     limit: int = 100,
                     db: Session = Depends(get_db)):
    res = crud.get_order_items(db, skip, limit)
    return res


@app.post("/order_items", response_model=OrderItemBase)
def create_order_items(order_items: OrderItemBase,
                       db: Session = Depends(get_db)):
    try:
        res = crud.create_order_items(db, order_items)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)


@app.put("/order_items/{order_id}", response_model=OrderItemBase)
def update_order_item(update_order_item: OrderItemBase,
                      order_id: int,
                      product_id: int,
                      db: Session = Depends(get_db)):
    try:
        res = crud.update_order_item(db, order_id, product_id,
                                     update_order_item)
        return res
    except Exception as err:
        raise HTTPException(**err.__dict__)
