from core.database import engine

with engine.connect() as connection:
    print("Connexion OK")