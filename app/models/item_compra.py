from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.factura_compra import FacturaCompra
    


class ItemCompra(SQLModel, table=True):
    __tablename__='items_compras'

    id: int = Field(default=None, primary_key=True)
    cantidad: int
    detalle: str
    costo_unitario: Decimal = Field(max_digits=25, decimal_places=2)
    subtotal: Decimal = Field(max_digits=25, decimal_places=2)


    facturas_compras_id: int = Field(foreign_key='facturas_compras.id')


    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    facturas_compras: 'FacturaCompra' = Relationship(back_populates='items_compras')