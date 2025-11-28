from sqlmodel import create_engine, Session
import os
from fastapi import Depends
from typing import Annotated

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


db_path = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite:///{db_path}"