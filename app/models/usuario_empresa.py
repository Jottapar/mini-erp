from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.empresa import Empresa
    from app.models.usuario import Usuario


class UsuarioEmpresa(SQLModel, table=True):
    __tablename__= 'usuarios_empresas'

    id: int = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key=Usuario.id)
    empresa_id: int = Field(foreign_key=Empresa.id)

    usuarios: Usuario = Relationship(back_populates='usuarios_empresas')
    empresas: Empresa = Relationship(back_populates='usuarios_empresas')