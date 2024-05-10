from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.item_model import ItemModel
from models.user_model import UserModel

from schemas.item_schema import ItemSchema
from core.deps import get_session, get_current_user