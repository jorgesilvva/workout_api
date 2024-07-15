from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

from workout_api.contrib.schemas import BaseSchema, OutMixin

from datetime import datetime
from typing import Annotated
from pydantic import UUID4, Field
from workout_api.categorias.schemas import CategoriaOut
from workout_api.centro_treinamento.schemas import CentroTreinamentoOut
from workout_api.contrib.schemas import BaseSchema

class AtletaIn(BaseSchema):
    nome: str = Field(..., description='Nome do atleta', max_length=50)
    cpf: str = Field(..., description='CPF do atleta', max_length=14)
    categoria: CategoriaOut
    centro_treinamento: CentroTreinamentoOut

class AtletaOut(AtletaIn):
    id: UUID4 = Field(..., description='Identificador do atleta')
    created_at: datetime = Field(..., description='Data e hora de criação')

    @classmethod
    def model_validate(cls, atleta: AtletaOut) -> AtletaOut:
        return atleta

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(description='Nome do atleta', max_length=50)] = None
    cpf: Annotated[Optional[str], Field(description='CPF do atleta', max_length=14)] = None
    categoria: Annotated[Optional[CategoriaOut], Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[Optional[CentroTreinamentoOut], Field(description='Centro de treinamento do atleta')]
