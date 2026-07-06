from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.factura_compra import FacturaCompra


class StatusFacturaCompra(SQLModel, table=True):
    __tablename__='status_facturas_compras'

    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=25)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    facturas_compras: list[FacturaCompra] = Relationship(back_populates='status_facturas_compras')