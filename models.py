# Externo (não meu)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

db = SQLAlchemy()


class Setor(db.Model):
    __tablename__ = "setor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, nome: str):
        self.nome = nome


class Cargo(db.Model):
    __tablename__ = "cargo"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    setor_id = db.Column(db.Integer, db.ForeignKey("setor.id"), nullable=False)

    # Permite usar qualquer informação (coluna) da tabela (1 linha).: Ex: setor.id, setor.nome
    setor = db.relationship("Setor", backref=db.backref("cargos", lazy=True))

    def init(self, nome: str, setor_id: int) -> None:
        self.nome = nome
        self.setor_id = setor_id


class Funcionario(db.Model):
    __tablename__ = "funcionario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey("cargo.id"), nullable=False)
    setor_id = db.Column(db.Integer, db.ForeignKey("setor.id"), nullable=False)

    cargo = db.relationship("Cargo", backref=db.backref("funcionarios", lazy=True))
    setor = db.relationship("Setor", backref=db.backref("funcionarios", lazy=True))

    def __init__(
        self,
        nome: str,
        sobrenome: str,
        data_admissao: DateTime,
        status: bool,
        cargo_id: int,
        setor_id: int,
    ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_admissao = data_admissao
        self.status = status
        self.cargo_id = cargo_id
        self.setor_id = setor_id