# Externo (não meu)
from flask import Flask, flash, redirect, render_template, request, url_for

# Externo (meu)
from models import Cargo, Funcionario, Setor, db

app = Flask(__name__)
app.secret_key = "I MUST SAY SOMETHING HERE"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@localhost/empresa"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    setor = Setor.query.order_by(Setor.id).all()
    cargo = Cargo.query.order_by(Cargo.id).all()
    funcionario = Funcionario.query.order_by(Funcionario.id).all()

    return render_template(
        "index.html", setor=setor, cargo=cargo, funcionario=funcionario
    )


# Setor
@app.route("/inserir_setor", methods=["POST"])
def inserir_setor():
    if request.method == "POST":
        setor_nome = request.form["setor_nome"]

        # Verifica se o nome já existe na tabela
        if Setor.query.filter_by(nome=setor_nome).first() is None:
            db.session.add(Setor(nome=setor_nome))
            db.session.commit()
        else:
            flash("Já existe um setor com esse nome!")
        return redirect(url_for("index"))


@app.route("/deletar_setor/<int:id>", methods=["GET", "POST"])
def deletar_setor(id):
    setor = Setor.query.get(id)

    db.session.delete(setor)
    db.session.commit()
    return redirect(url_for("index"))


# Cargo
@app.route("/inserir_cargo", methods=["POST"])
def inserir_cargo():
    setor_nome = request.form["setor_nome"]

    cargo_nome = request.form["cargo_nome"]
    setor_id = Setor.query.filter_by(nome=setor_nome).first().id

    # verificando se o nome do cargo é único para cada setor
    if Cargo.query.filter_by(nome=cargo_nome, setor_id=setor_id).first() is None:
        db.session.add(Cargo(nome=cargo_nome, setor_id=setor_id))
        db.session.commit()
    else:
        flash("Já existe um cargo com esse nome neste setor!")
    return redirect(url_for("index"))


@app.route("/deletar_cargo/<int:id>", methods=["GET", "POST"])
def deletar_cargo(id):
    cargo = Cargo.query.get(id)

    db.session.delete(cargo)
    db.session.commit()
    return redirect(url_for("index"))


# Funcionário
@app.route("/inserir_funcionario", methods=["POST"])
def inserir_funcionario():
    funcionario_nome = request.form["funcionario_nome"]
    funcionario_sobrenome = request.form["funcionario_sobrenome"]
    funcionario_data_admissao = request.form["funcionario_data_admissao"]
    funcionario_status = request.form["funcionario_status"]

    funcionario_cargo_nome = request.form["funcionario_cargo_nome"]
    funcionario_setor_nome = request.form["funcionario_setor_nome"]

    cargo = Cargo.query.filter_by(nome=funcionario_cargo_nome).first()
    setor = Setor.query.filter_by(nome=funcionario_setor_nome).first()

    db.session.add(
        Funcionario(
            nome=funcionario_nome,
            sobrenome=funcionario_sobrenome,
            data_admissao=funcionario_data_admissao,
            status=bool(funcionario_status),
            cargo_id=cargo.id,
            setor_id=setor.id,
        )
    )
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/deletar_funcionario/<int:id>", methods=["GET", "POST"])
def deletar_funcionario(id):
    funcionario = Funcionario.query.get(id)

    db.session.delete(funcionario)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
