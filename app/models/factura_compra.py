from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, date
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.status_factura_compra import StatusFacturaCompra
    from app.models.proveedor import Proveedor
    from app.models.item_compra import ItemCompra


class FacturaCompra(SQLModel, table=True):
    __tablename__='facturas_compras'

    id: int = Field(default=None, primary_key=True)
    fecha_factura: date
    num_factura = str | None = Field(default=None)
    costo_total: Decimal = Field(max_digits=25,decimal_places=2)


    proveedor_id: int = Field(foreign_key='proveedores.id')
    status_factura_compra_id: int = Field(foreign_key='status_facturas_compras.id')


    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    status_facturas_compras: 'StatusFacturaCompra' = Relationship(back_populates='facturas_compras')
    proveedores: 'Proveedor' = Relationship(back_populates='facturas_compras')
    items_compras: list[ItemCompra] = Relationship(back_populates='facturas_compras')

