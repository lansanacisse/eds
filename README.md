# EDS — Entrepôt de Données de Santé

Projet personnel de Data Engineering consacré à la construction d'une
plateforme locale de données de santé à partir de sources publiques.

L'objectif est de mettre en œuvre une architecture complète de Data
Engineering : ingestion, stockage objet, pseudo-anonymisation,
entrepôt analytique, transformation, orchestration et restitution BI.

---

## 1. Architecture

```text
Sources publiques de santé
          │
          ▼
      Ingestion
          │
          ▼
        MinIO
   données sources
          │
          ▼
Pseudo-anonymisation
          │
          ▼
      ClickHouse
 données analytiques
          │
          ▼
         dbt
          │
     ┌────┴────┐
     │         │
 staging   intermediate
     │         │
     └────┬────┘
          ▼
        marts
          │
          ▼
   Power BI / Grafana


Dagster
   │
   └── orchestration de l'ensemble du pipeline
````

---

## 2. Stack technique

| Composant           | Technologie              |
| ------------------- | ------------------------ |
| OS                  | Ubuntu 26.04 LTS / WSL 2 |
| Langage             | Python 3.13              |
| Gestion Python      | uv                       |
| Versionnement       | Git / GitHub             |
| Conteneurisation    | Docker / Docker Compose  |
| Stockage objet      | MinIO                    |
| Entrepôt analytique | ClickHouse               |
| Transformation      | dbt                      |
| Adaptateur dbt      | dbt-clickhouse           |
| Orchestration       | Dagster                  |
| BI                  | Power BI / Grafana       |

---

## 3. Versions de l'environnement

```text
Python              3.13.15
uv                  0.12.6
Git                 2.53.0
Docker              29.7.2
Docker Compose      5.4.0
dbt-core            1.11.14
dbt-clickhouse      1.10.2
Dagster             1.13.19
Dagster Webserver   1.13.19
```

> Ces versions correspondent à l'environnement initial de développement.
> dbt-core signale actuellement qu'une version plus récente existe, mais
> aucune mise à jour n'est effectuée tant que l'environnement fonctionnel
> n'en a pas besoin.

---

## 4. Structure du projet

```text
eds/
├── README.md
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
│
├── docker-compose.yml
├── docker/
│
├── ingestion/
├── data/
├── scripts/
│
├── src/
│   └── eds/
│       └── __init__.py
│
├── dagster/
│   ├── pyproject.toml
│   └── src/
│       └── eds_dagster/
│           ├── __init__.py
│           └── definitions.py
│
└── dbt/
    ├── dbt_project.yml
    ├── profiles.yml
    ├── models/
    │   ├── staging/
    │   ├── intermediate/
    │   └── marts/
    ├── macros/
    └── tests/
```

---

## 5. Environnement Python

Activation de l'environnement :

```bash
cd ~/projets/eds
source .venv/bin/activate
```

Vérification :

```bash
python --version
uv --version
```

---

## 6. Git

Initialisation :

```bash
git init
git branch -M main
```

Vérification :

```bash
git status
```

Le dépôt est connecté à GitHub via SSH.

Vérification :

```bash
git remote -v
```

Test SSH :

```bash
ssh -T git@github.com
```

Push :

```bash
git push -u origin main
```

---

## 7. Docker

Vérification :

```bash
docker --version
docker compose version
```

Démarrage des services :

```bash
docker compose up -d
```

État des services :

```bash
docker compose ps
```

Arrêt :

```bash
docker compose down
```

---

## 8. MinIO

MinIO est utilisé comme stockage objet.

Console :

```text
http://localhost:9001
```

API :

```text
http://localhost:9000
```

Les identifiants sont stockés dans `.env`.

Ne jamais versionner `.env`.

---

## 9. ClickHouse

ClickHouse constitue l'entrepôt analytique du projet.

Port HTTP :

```text
8123
```

Port natif :

```text
9002
```

Vérification :

```bash
docker exec eds-clickhouse clickhouse-client \
  --query "SHOW DATABASES"
```

La base du projet est :

```text
eds
```

---

## 10. dbt

dbt est utilisé pour transformer et modéliser les données présentes
dans ClickHouse.

Vérification :

```bash
dbt --version
```

Diagnostic :

```bash
dbt debug --project-dir dbt
```

Projet :

```text
dbt/
├── dbt_project.yml
├── profiles.yml
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
├── macros/
└── tests/
```

dbt se connecte directement à ClickHouse.

---

## 11. Dagster

Dagster est utilisé pour orchestrer les différents traitements.

Vérification :

```bash
dagster --version
dagster-webserver --version
```

Lancer l'environnement de développement :

```bash
dg dev
```

Interface :

```text
http://localhost:3000
```

Le code Dagster se trouve dans :

```text
dagster/src/eds_dagster/
```

---

## 12. Variables d'environnement

Les secrets et paramètres locaux sont définis dans :

```text
.env
```

Exemples de variables :

```text
MINIO_ROOT_USER
MINIO_ROOT_PASSWORD

CLICKHOUSE_DB
CLICKHOUSE_USER
CLICKHOUSE_PASSWORD
```

Le fichier `.env` ne doit jamais être envoyé sur GitHub.

---

## 13. Ports

| Service           | Port | Utilisation        |
| ----------------- | ---: | ------------------ |
| MinIO API         | 9000 | API S3             |
| MinIO Console     | 9001 | Interface Web      |
| ClickHouse HTTP   | 8123 | Connexions HTTP    |
| ClickHouse Native | 9002 | Connexions natives |
| Dagster           | 3000 | Interface Web      |

---

## 14. Vérification globale

```bash
python --version
uv --version
git --version
docker --version
docker compose version
dbt --version
dagster --version
dagster-webserver --version
docker compose ps
```

---

## 15. État de l'environnement

L'environnement de développement est fonctionnel.

```text
WSL 2                  ✓
Ubuntu                 ✓
Python                 ✓
uv                     ✓
Git                    ✓
GitHub SSH             ✓
Docker                 ✓
Docker Compose         ✓
MinIO                  ✓
ClickHouse             ✓
dbt                    ✓
dbt-clickhouse         ✓
Dagster                ✓
Dagster Webserver      ✓
```

---

## 16. Prochaine phase

La prochaine phase du projet sera consacrée au pipeline de données.

Elle sera conçue séparément de la phase d'installation.

Le pipeline prévu est :

```text
Sources publiques
        ↓
Ingestion
        ↓
MinIO
        ↓
Pseudo-anonymisation
        ↓
ClickHouse
        ↓
dbt
        ↓
Staging
        ↓
Intermediate
        ↓
Marts
        ↓
BI
```

Dagster aura pour rôle d'orchestrer ces différentes étapes.