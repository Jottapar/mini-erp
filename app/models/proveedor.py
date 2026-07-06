from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from pydantic import EmailStr 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.tipo_proveedor import TipoProveedor
    from app.models.factura_compra import FacturaCompra

class Proveedor(SQLModel, table=True):
    __tablename__= 'proveedores'

    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50)
    telefono: str = Field(max_length=10)
    correo: EmailStr
    tipo_proveedor_id: int = Field                  (foreign_key=TipoProveedor.id)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    created_by: int
    updated_by: int | None = Field(default=None)

    tipos_proveedores: 'TipoProveedor' = Relationship(back_populates='proveedores')
    facturas_compras: list[FacturaCompra] = Relationship(back_populates='proveedores')




