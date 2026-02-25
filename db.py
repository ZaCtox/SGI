from flask_sqlalchemy import SQLAlchemy

# Crear instancia global de la base de datos
db = SQLAlchemy()


def init_db(app):
    """
    Inicializa la base de datos con la app
    """
    db.init_app(app)

    with app.app_context():
        db.create_all()