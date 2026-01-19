# Dataverse SDK Learning Journey

This repository documents my progression from Data Analyst to Platform Architect using the PowerPlatform-Dataverse-Client Python SDK.

It follows a structured learning roadmap consisting of isolated Labs and integration Capstones.

## 📂 Project Structure

- `common/`: Shared utilities, loggers, and retry wrappers used across gates.
- `gate1_analyst/`: Labs focused on reading data (SQL/OData) and authentication.
- `gate2_migration/`: Labs focused on writing data (CRUD), batching, and error handling.
- `gate3_content/`: Handling file uploads/downloads and binary data.
- `gate4_architect/`: Infrastructure as Code (IaC) and schema management.

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Azure AD app registration with Dataverse API permissions
- Azure CLI (`az login` required for local dev)

### Setup Environment

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configuration

1. Copy `.env.example` to `.env`
2. Ensure `DATAVERSE_URL` is set in `.env`
3. Run `az login` to authenticate locally

## 📜 Development Protocol

Code in this repository adheres to the following standards:

- **Authentication:** No hardcoded secrets. Use `AzureCliCredential` locally, `ClientSecretCredential` in CI/CD.
- **Error Handling:** No silent failures. Specific `try/except` blocks with logging.
- **Code Quality:** Mandatory type hints and standard `logging` (no `print`).
- **SDK Constraints:** Awareness of v0.1.0 limitations (no upsert, limited SQL).

## 🗺️ Progress Tracker

### 🟢 Gate 1: Data Analyst

*Focus: Authentication, SQL, OData*

- [x] Lab 1.1: Credential Validator
- [x] Lab 1.2: SQL Query Basics
- [ ] Lab 1.3: OData Query Explorer
- [ ] Capstone: The Analyst's View (Region Export)

### 🟡 Gate 2: Migration Engineer

*Focus: CRUD, Batch Operations, Resilience*

- [ ] Lab 2.1: Contact Lifecycle Manager
- [ ] Lab 2.2: Mass Field Update
- [ ] Lab 2.3: Historical Data Loader
- [ ] Lab 2.4: Retry-Aware Wrapper
- [ ] Capstone: The Bulk Lead Migrator

### 🔵 Gate 3: Content Manager

*Focus: File/Image Columns, Binary Data*

- [ ] Lab 3.1: Document Uploader
- [ ] Lab 3.2: Batch Document Ingestion
- [ ] Lab 3.3: File Download Workaround
- [ ] Capstone: The Claims Adjuster

### 🔴 Gate 4: Platform Architect

*Focus: Schema Management, IaC*

- [ ] Lab 4.1: Table Inspector
- [ ] Lab 4.2: Schema Provisioner
- [ ] Lab 4.3: Operations Monitor
- [ ] Capstone: The Schema Bot

---

*Roadmap based on Dataverse SDK Learning Protocol v1.0*
