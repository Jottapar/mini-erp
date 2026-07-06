from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.proveedor import Proveedor


class TipoProveedor(SQLModel, table=True):
    __tablename__='tipos_proveedores'

    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=25)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    created_by: int
    updated_by: int | None = Field(default=None)

    proveedores: list[Proveedor] = Relationship(back_populates='tipos_proveedores')