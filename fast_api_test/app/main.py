from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from . import crud, models
from .schemas import CustomerBase, CustomerSchema, ProductBase, ProductSchema, OrderBase, OrderItemBase
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
@app.get("/orders/{order_id}", response_model=OrderBase)
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
def create_order(customer_id: int,
                 order: OrderBase,
                 db: Session = Depends(get_db)):
    try:
        res = crud.create_order(db, order, customer_id)
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
@app.get("/order_items/{order_id}", response_model=OrderItemBase)
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
def create_order_items(product_id: int,
                       order_id: int,
                       amount: int,
                       order_items: OrderItemBase,
                       db: Session = Depends(get_db)):
    try:
        res = crud.create_order_items(db, order_items, product_id, order_id,
                                      amount)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)


'''

@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int,
                         item: schemas.ItemCreate,
                         db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
'''
'''@app.get("/authors/{author_id}", response_model=AuthorSchema)
def read_author_id(author_id: int, db: Session = Depends(get_db)):
    res = crud.get_author(db, author_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res


@app.get("/authors", response_model=List[AuthorSchema])
def read_authors(skip: int = 0,
                 limit: int = 100,
                 db: Session = Depends(get_db)):
    res = crud.get_authors(db, skip, limit)
    return res


@app.post("/authors", response_model=AuthorSchema)
def create_author(userForm: AuthorSchema, db: Session = Depends(get_db)):
    try:
        res = crud.create_author(db, userForm)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)


#-------
@app.get("/books/{book_id}", response_model=BookSchema)
def read_book_id(book_id: int, db: Session = Depends(get_db)):
    res = crud.get_book(db, book_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res


@app.get("/books", response_model=BookSchema)
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    res = crud.get_books(db, skip, limit)
    response = {"skip": skip, "limit": limit, "data": res}
    return response


@app.post("/books", response_model=BookSchema)
def create_book(userForm: BookSchema, db: Session = Depends(get_db)):
    try:
        res = crud.create_book(db, userForm)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)'''
