# Build-EDS — Entrepôt de Données de Santé

Build-EDS est un projet personnel de Data Engineering visant à construire une plateforme locale de données de santé à partir de sources publiques.

## Objectif

Le projet met en œuvre une chaîne complète de traitement des données :

1. ingestion des données publiques ;
2. stockage des données sources avec MinIO ;
3. pseudo-anonymisation ;
4. stockage analytique dans ClickHouse ;
5. transformation et modélisation avec dbt ;
6. orchestration des traitements avec Dagster ;
7. restitution via Power BI ou Grafana.

## Architecture

```text
Sources publiques
       │
       ▼
   Ingestion
       │
       ▼
     MinIO
       │
       ▼
Pseudo-anonymisation
       │
       ▼
   ClickHouse
       │
       ▼
      dbt
       │
       ▼
 staging → intermediate → marts
       │
       ▼
Power BI / Grafana

Dagster orchestre l'ensemble du pipeline.
```

## Stack technique

- **Langage :** Python 3.13
- **Gestion Python :** uv
- **Conteneurisation :** Docker et Docker Compose
- **Stockage objet :** MinIO
- **Entrepôt analytique :** ClickHouse
- **Transformation :** dbt avec `dbt-clickhouse`
- **Orchestration :** Dagster
- **BI :** Power BI / Grafana
- **Versionnement :** Git / GitHub
- **Environnement :** Ubuntu 26.04 LTS / WSL 2

## Structure du projet

```text
build-eds/
├── ingestion/              # Ingestion des données
├── data/                   # Données locales
├── scripts/                # Scripts utilitaires
├── src/eds/                # Code source Python
├── dagster/                # Code d'orchestration Dagster
├── dbt/                    # Modèles, macros et tests dbt
├── docker-compose.yml      # Services Docker
├── pyproject.toml          # Configuration Python
└── README.md
```

## Démarrage rapide

### Environnement Python

```bash
cd ~/projets/build-eds
source .venv/bin/activate
python --version
uv --version
```

### Services Docker

```bash
docker compose up -d
docker compose ps
```

Pour arrêter les services :

```bash
docker compose down
```

### dbt

```bash
dbt --version
dbt debug --project-dir dbt
```

### Dagster

```bash
dagster --version
dagster-webserver --version
dg dev
```

L'interface Dagster est accessible à l'adresse suivante :

```text
http://localhost:3000
```

## Services et ports

| Service | Port | Utilisation |
| --- | ---: | --- |
| MinIO API | 9000 | API S3 |
| MinIO Console | 9001 | Interface Web |
| ClickHouse HTTP | 8123 | Connexions HTTP |
| ClickHouse Native | 9002 | Connexions natives |
| Dagster | 3000 | Interface Web |

MinIO est accessible depuis `http://localhost:9001` et ClickHouse utilise la base de données `eds`.

## Variables d'environnement

Les secrets et paramètres locaux sont définis dans le fichier `.env`, notamment :

```text
MINIO_ROOT_USER
MINIO_ROOT_PASSWORD
CLICKHOUSE_DB
CLICKHOUSE_USER
CLICKHOUSE_PASSWORD
```

Le fichier `.env` contient des informations sensibles et ne doit jamais être versionné sur GitHub.
