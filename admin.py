from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/vinicius/Desktop/projeto sp pinturas/proj_sp_pinturas/database/SpPintura.db'
app.config['SECRET_KEY'] = 'senha123'

db = SQLAlchemy(app)
admin = Admin(app)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column('Nome',db.String(30),nullable=False)
    sobrenome = db.Column('Sobrenome',db.String(60),nullable=False)
    dataNascimento = db.Column('Data de Nascimento',db.Date,nullable=False)
    CPF = db.Column('CPF',db.Integer,nullable=False)
    telefone = db.Column('Telefone',db.Integer, nullable=False)
    email = db.Column('E-Mail',db.String(70),nullable=False)
    endeCep = db.Column('CEP',db.Integer,nullable=False)
    endeRua = db.Column('Rua',db.String(90),nullable=False)
    endeNum = db.Column('Número',db.Integer,nullable=False)
    endeComplemento = db.Column('Complemento', db.String(50))
    endeBairro = db.Column('Bairro',db.String(50),nullable=False)
    endeCidade = db.Column('Cidade', db.String(80),nullable=False)
    obs = db.Column('Observações', db.String(500))
    orcamentos = db.relationship('Orcamentos', backref='cliente', lazy=True)
    
    def __repr__(self):
        return self.nome

class Orcamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column('Status',db.String(20),nullable=False)
    dataPedido = db.Column('Data do Pedido', db.Date)
    dataFeito = db.Column('Data que foi feito', db.Date)
    dataCancelado = db.Column('Data que foi cancelado', db.Date)
    motivoCancelado = db.Column('Motivo cancelamento',db.Date)
    pdfOrcamento = db.Column('PDF link e/ou nome',db.String(200))
    clienteId = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)

class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column('Nome',db.String(50),nullable=False)
    tipo = db.Column('Tipo',db.String(30),nullable=False)
    qtd = db.Column('Quantidade', db.Integer,nullable=False)
    descricao = db.Column('Descrição', db.String(500))
    codigo = db.Column('Código', db.Integer)

admin.add_view(ModelView(Cliente,db.session))
admin.add_view(ModelView(Orcamentos,db.session))
admin.add_view(ModelView(Estoque,db.session))


if __name__ == '__main__':   
    app.run()