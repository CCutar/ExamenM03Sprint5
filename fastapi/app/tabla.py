from sqlalchemy import Column, ForeignKey, Integer, MetaData, Table, String
from sqlalchemy.orm import relationship
from .database import metadata, engine

metadata = MetaData()

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('password', String(50)),
    Column('email', String(50)),
    Column('created_at', String(50)),
)

usersProducts_table = Table(
    'usersProducts', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('user_id', Integer, ForeignKey('users.id')),  # Define la relación con la tabla de usuarios
    Column('created_at', String(50)),
)

# Define la relación uno a muchos en el modelo de usuario
class User:
    def __init__(self, id, name, password, email, created_at):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.created_at = created_at

    products = relationship("UserProduct", back_populates="user")

# Define la relación inversa en el modelo de productos de usuario
class UserProduct:
    def __init__(self, id, name, user_id, created_at):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.created_at = created_at

    user = relationship("User", back_populates="products")

metadata.create_all(engine)
