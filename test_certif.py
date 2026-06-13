from core.database import SessionLocal
from db.repositories.certification_repository import CertificationRepository

session = SessionLocal()
repo = CertificationRepository(session)
result = repo.get_certification_skill_by_id_employee(4)
i=0
if not result:
    print("Hmmmmm")
for row in result:
    print(f'*****{i}*****')
    print(type(row))
    print(row)
    i+=1