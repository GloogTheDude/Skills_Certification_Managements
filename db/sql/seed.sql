-- seed.sql
-- Jeu de données de test pour module_certificator
-- Compatible avec le schéma où training_request utilise id_validator.

BEGIN;

-- Nettoyage optionnel.
-- À utiliser uniquement en développement.
TRUNCATE TABLE
    certificationxskill,
    diplomaxskill,
    employeexcertification,
    employeexdiploma,
    participation,
    provide,
    skill_validation,
    training_request,
    trainingxcertification,
    trainingxdiploma,
    trainingxskill,
    certification,
    diploma,
    employee,
    role,
    skill,
    validation_type,
    domaine,
    training,
    training_source
RESTART IDENTITY CASCADE;

-- =========================
-- ROLE
-- =========================

INSERT INTO role(denomination_role)
VALUES
('Employee'),
('Team Lead'),
('Manager'),
('HR');

-- =========================
-- DOMAINE
-- =========================

INSERT INTO domaine(nom_domaine)
VALUES
('Software Development'),
('Cloud'),
('Project Management');

-- =========================
-- SKILL
-- =========================

INSERT INTO skill(name_skill)
VALUES
('Python'),
('PostgreSQL'),
('Docker'),
('Azure'),
('Scrum');

-- =========================
-- VALIDATION TYPE
-- =========================

INSERT INTO validation_type(source, denomination_validation)
VALUES
('Manager', 'Manager Validation'),
('Training', 'Training Completion'),
('Certification', 'Certification Validation');

-- =========================
-- TRAINING SOURCE
-- =========================

INSERT INTO training_source(name_source)
VALUES
('Technifutur'),
('Microsoft Learn'),
('Udemy');

-- =========================
-- EMPLOYEE
-- Insertion en plusieurs étapes pour respecter la FK self-reference id_manager.
-- =========================

INSERT INTO employee(
    first_name,
    last_name,
    hash_password,
    mail,
    id_role,
    id_manager
)
VALUES (
    'John',
    'Boss',
    'hash',
    'john@company.be',
    (SELECT id_role FROM role WHERE denomination_role = 'Manager'),
    NULL
);

INSERT INTO employee(
    first_name,
    last_name,
    hash_password,
    mail,
    id_role,
    id_manager
)
VALUES (
    'Alice',
    'Lead',
    'hash',
    'alice@company.be',
    (SELECT id_role FROM role WHERE denomination_role = 'Team Lead'),
    (SELECT id_employee FROM employee WHERE mail = 'john@company.be')
);

INSERT INTO employee(
    first_name,
    last_name,
    hash_password,
    mail,
    id_role,
    id_manager
)
VALUES (
    'David',
    'Henrichmann',
    'hash',
    'david@company.be',
    (SELECT id_role FROM role WHERE denomination_role = 'Employee'),
    (SELECT id_employee FROM employee WHERE mail = 'alice@company.be')
);

INSERT INTO employee(
    first_name,
    last_name,
    hash_password,
    mail,
    id_role,
    id_manager
)
VALUES (
    'Pierre',
    'Martin',
    'hash',
    'pierre@company.be',
    (SELECT id_role FROM role WHERE denomination_role = 'Employee'),
    (SELECT id_employee FROM employee WHERE mail = 'alice@company.be')
);

-- =========================
-- DIPLOMA
-- =========================

INSERT INTO diploma(
    subject_diploma,
    level_diploma,
    id_domaine
)
VALUES (
    'Bachelor Informatique',
    'Bachelor',
    (SELECT id_domaine FROM domaine WHERE nom_domaine = 'Software Development')
);

-- =========================
-- CERTIFICATION
-- =========================

INSERT INTO certification(
    subject_certification,
    id_domaine
)
VALUES
(
    'Azure Fundamentals',
    (SELECT id_domaine FROM domaine WHERE nom_domaine = 'Cloud')
),
(
    'Professional Scrum Master',
    (SELECT id_domaine FROM domaine WHERE nom_domaine = 'Project Management')
);

-- =========================
-- TRAINING
-- =========================

INSERT INTO training(
    title,
    id_domaine,
    start_,
    end_
)
VALUES
(
    'Python Advanced',
    (SELECT id_domaine FROM domaine WHERE nom_domaine = 'Software Development'),
    '2026-09-01',
    '2026-09-05'
),
(
    'Azure Introduction',
    (SELECT id_domaine FROM domaine WHERE nom_domaine = 'Cloud'),
    '2026-10-01',
    '2026-10-03'
);

-- =========================
-- DIPLOMA X SKILL
-- =========================

INSERT INTO diplomaxskill(
    id_diploma,
    id_skill,
    min_level
)
VALUES
(
    (SELECT id_diploma FROM diploma WHERE subject_diploma = 'Bachelor Informatique'),
    (SELECT id_skill FROM skill WHERE name_skill = 'Python'),
    2
),
(
    (SELECT id_diploma FROM diploma WHERE subject_diploma = 'Bachelor Informatique'),
    (SELECT id_skill FROM skill WHERE name_skill = 'PostgreSQL'),
    2
);

-- =========================
-- CERTIFICATION X SKILL
-- =========================

INSERT INTO certificationxskill(
    id_certification,
    id_skill,
    granted_level
)
VALUES
(
    (SELECT id_certification FROM certification WHERE subject_certification = 'Azure Fundamentals'),
    (SELECT id_skill FROM skill WHERE name_skill = 'Azure'),
    3
),
(
    (SELECT id_certification FROM certification WHERE subject_certification = 'Professional Scrum Master'),
    (SELECT id_skill FROM skill WHERE name_skill = 'Scrum'),
    3
);

-- =========================
-- TRAINING X SKILL
-- =========================

INSERT INTO trainingxskill(
    id_skill,
    id_training,
    granted_level
)
VALUES
(
    (SELECT id_skill FROM skill WHERE name_skill = 'Python'),
    (SELECT id_training FROM training WHERE title = 'Python Advanced'),
    3
),
(
    (SELECT id_skill FROM skill WHERE name_skill = 'Docker'),
    (SELECT id_training FROM training WHERE title = 'Python Advanced'),
    2
),
(
    (SELECT id_skill FROM skill WHERE name_skill = 'Azure'),
    (SELECT id_training FROM training WHERE title = 'Azure Introduction'),
    2
);

-- =========================
-- TRAINING X CERTIFICATION
-- =========================

INSERT INTO trainingxcertification(
    id_certification,
    id_training
)
VALUES (
    (SELECT id_certification FROM certification WHERE subject_certification = 'Azure Fundamentals'),
    (SELECT id_training FROM training WHERE title = 'Azure Introduction')
);

-- =========================
-- EMPLOYEE X DIPLOMA
-- =========================

INSERT INTO employeexdiploma(
    id_employee,
    id_diploma,
    start_,
    end_,
    school,
    distinction,
    doc
)
VALUES (
    (SELECT id_employee FROM employee WHERE mail = 'david@company.be'),
    (SELECT id_diploma FROM diploma WHERE subject_diploma = 'Bachelor Informatique'),
    '2021-09-01',
    '2025-06-30',
    'ECI Liege',
    'Grande distinction',
    'diploma_david.pdf'
);

-- =========================
-- EMPLOYEE X CERTIFICATION
-- =========================

INSERT INTO employeexcertification(
    id_employee,
    id_certification,
    start_,
    end_,
    expiration,
    organism,
    evaluation,
    doc
)
VALUES (
    (SELECT id_employee FROM employee WHERE mail = 'david@company.be'),
    (SELECT id_certification FROM certification WHERE subject_certification = 'Azure Fundamentals'),
    '2026-01-01',
    '2026-01-15',
    '2029-01-15',
    'Microsoft',
    'Passed',
    'azure_david.pdf'
);

-- =========================
-- PARTICIPATION
-- =========================

INSERT INTO participation(
    id_employee,
    id_training,
    status
)
VALUES
(
    (SELECT id_employee FROM employee WHERE mail = 'david@company.be'),
    (SELECT id_training FROM training WHERE title = 'Python Advanced'),
    'COMPLETED'
),
(
    (SELECT id_employee FROM employee WHERE mail = 'pierre@company.be'),
    (SELECT id_training FROM training WHERE title = 'Azure Introduction'),
    'REGISTERED'
);

-- =========================
-- TRAINING REQUEST
-- =========================

INSERT INTO training_request(
    status,
    reason,
    requested_at,
    id_employee,
    id_training,
    id_validator
)
VALUES
(
    'PENDING',
    'Need Azure skills',
    '2026-06-10',
    (SELECT id_employee FROM employee WHERE mail = 'pierre@company.be'),
    (SELECT id_training FROM training WHERE title = 'Azure Introduction'),
    (SELECT id_employee FROM employee WHERE mail = 'alice@company.be')
),
(
    'APPROVED',
    'Improve Python skills',
    '2026-06-09',
    (SELECT id_employee FROM employee WHERE mail = 'david@company.be'),
    (SELECT id_training FROM training WHERE title = 'Python Advanced'),
    (SELECT id_employee FROM employee WHERE mail = 'alice@company.be')
);

-- =========================
-- SKILL VALIDATION
-- =========================

INSERT INTO skill_validation(
    date_,
    level_skill,
    id_validation,
    id_employee,
    id_validator,
    id_skill
)
VALUES
(
    '2026-06-01',
    3,
    (SELECT id_validation FROM validation_type WHERE denomination_validation = 'Manager Validation'),
    (SELECT id_employee FROM employee WHERE mail = 'david@company.be'),
    (SELECT id_employee FROM employee WHERE mail = 'alice@company.be'),
    (SELECT id_skill FROM skill WHERE name_skill = 'Python')
),
(
    '2026-06-01',
    2,
    (SELECT id_validation FROM validation_type WHERE denomination_validation = 'Manager Validation'),
    (SELECT id_employee FROM employee WHERE mail = 'david@company.be'),
    (SELECT id_employee FROM employee WHERE mail = 'alice@company.be'),
    (SELECT id_skill FROM skill WHERE name_skill = 'PostgreSQL')
);

-- =========================
-- PROVIDE
-- =========================

INSERT INTO provide(
    id_training,
    id_source,
    cost_hour,
    duration_hours
)
VALUES
(
    (SELECT id_training FROM training WHERE title = 'Python Advanced'),
    (SELECT id_source FROM training_source WHERE name_source = 'Technifutur'),
    120.00,
    35.00
),
(
    (SELECT id_training FROM training WHERE title = 'Azure Introduction'),
    (SELECT id_source FROM training_source WHERE name_source = 'Microsoft Learn'),
    80.00,
    14.00
);

COMMIT;
