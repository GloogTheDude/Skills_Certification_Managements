# Models SQLAlchemy - module_certificator

Ces fichiers représentent les tables SQL fournies sous forme de classes SQLAlchemy ORM 2.x.

## Installation

```bash
pip install sqlalchemy psycopg[binary]
```

## Exemple d'utilisation

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Role

engine = create_engine("postgresql+psycopg://user:password@localhost:5432/dbname")

# Crée les tables si elles n'existent pas.
Base.metadata.create_all(engine)

with Session(engine) as session:
    role = Role(denomination_role="Admin")
    session.add(role)
    session.commit()
```

## Remarque

Certaines colonnes sont probablement à renommer dans ton SQL :
- `id_employee_1` représente probablement un manager / validateur.
- `date_`, `start_`, `end_` devraient plutôt être des types DATE.
- `statuts` dans `participation` semble être une faute pour `status`.
- Les tables `employeeXdiploma`, etc. fonctionnent, mais en PostgreSQL les noms non quotés sont convertis en minuscules.
