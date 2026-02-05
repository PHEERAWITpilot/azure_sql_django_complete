# Setup Guide

## Prerequisites

- **[Python 3.10+](https://www.python.org/downloads/)**
- **ODBC Driver 18 for SQL Server** (Required for `mssql-django`)
  - [Download for Windows](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
  - [Install on Linux](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server)
  - [Install on macOS](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos)

### CLI Installation

**Windows** (via `winget`)
```powershell
winget install Python.Python.3.12
winget install Microsoft.SQLServer.ODBCDriver
```

**macOS** (via `homebrew`)
```bash
brew install python@3.12
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install msodbcsql18
```

**Linux (Ubuntu)**
```bash
# Python 3
sudo apt-get update && sudo apt-get install python3 python3-pip

# ODBC Driver 18 (Ubuntu 22.04 example)
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/raksit/azure_sql_django
   cd azure_sql_django
   ```

2. **Create and activate a virtual environment**
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Database Configuration

### Option A: SQLite (Default)
The project is configured to use SQLite by default for local development.

### Option B: Azure SQL
1. **Prepare Azure SQL Resource**:
   - Create a SQL Database in the Azure Portal.
   - **Important**: Allow your client IP address in the **server-level firewall rules**.

2. **Configure Settings**:
   - Open `azure_project/settings.py`.
   - Comment out the `sqlite3` `DATABASES` setting.
   - Uncomment the `mssql` `DATABASES` setting.
   - Update the keys with your credentials:
     ```python
     'NAME': 'your-database-name',
     'USER': 'your-admin-username',
     'PASSWORD': 'your-password',
     'HOST': 'your-server.database.windows.net',
     ```

## Running the Application

1. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Start the server**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.
