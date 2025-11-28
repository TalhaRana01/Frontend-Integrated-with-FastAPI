from sqlmodel import Session, select
from app.products.models import Product, ProductOut


# Create Product
def create_product(session : Session, new_product: Product)-> ProductOut:
  product = Product(title=new_product.title, description=new_product.description)
  session.add(product)
  session.commit()
  session.refresh(product)
  return product

def get_all_products(session:Session):
  statement = select(Product)
  product = session.exec(statement)
  return product.all()


