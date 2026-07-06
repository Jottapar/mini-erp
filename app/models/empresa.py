from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.usuario_empresa import UsuarioEmpresa

class Empresa(SQLModel, table=True):
    __tablesname__='empresas'

    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50)
    status: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.now)
    created_by: str | None = Field(default=None)

    updated_at: datetime = Field(default_factory=datetime.now)
    updated_by: str | None = Field(default=None)

    usuarios_empresas: list[UsuarioEmpresa] = Relationship(back_populates='empresas')