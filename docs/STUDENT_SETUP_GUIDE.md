# Student Setup Guide (Week 2)

This guide covers the necessary steps to prepare your development environment for the Django & Azure project.

## 1. MongoDB Setup (Local)

We will use MongoDB to store unstructured data (reviews).

### A. Install MongoDB Community Server

**For Windows:**
1.  Download the MSI installer from the [MongoDB Download Center](https://www.mongodb.com/try/download/community).
2.  Run the installer. **Important**: Select "Install MongoDB as a Service".
3.  Complete the installation.

**For macOS:**
1.  Open your terminal.
2.  Tap the MongoDB Homebrew Tap:
    ```bash
    brew tap mongodb/brew
    ```
3.  Install MongoDB:
    ```bash
    brew install mongodb-community
    ```

### B. Start MongoDB Service

**For Windows:**
*   Open **Task Manager** > **Services**.
*   Look for `MongoDB` and ensure the status is "Running".

**For macOS:**
*   Start the service using Homebrew:
    ```bash
    brew services start mongodb-community
    ```

### C. Install MongoDB Compass (GUI)

1.  Download **MongoDB Compass** from the [official site](https://www.mongodb.com/try/download/compass).
2.  Install and open the application.
3.  Connect to your local database using the connection string: `mongodb://localhost:27017`.

---

## 2. Project Setup

### A. Clone the Repository

Open your terminal or VS Code and run:

```bash
git clone https://github.com/raksit/azure_sql_django_complete.git
cd azure_sql_django_complete
```

### B. GitHub Setup for Deployment

To deploy this project to Azure later, you need your own copy of the repository on GitHub.

1.  **Create a GitHub Account**: If you don't have one, sign up at [github.com](https://github.com/).
2.  **Fork the Repository**:
    *   Go to the page of the repository you just cloned (or the one provided by your instructor).
    *   Click the **Fork** button in the top-right corner.
    *   This creates a copy under *your* account (e.g., `your-username/azure_sql_django_complete`).
3.  **Update Remote (Optional but Recommended)**:
    *   If you want to push changes to *your* fork:
        ```bash
        git remote set-url origin https://github.com/YOUR_USERNAME/azure_sql_django_complete.git
        ```

### C. Create Virtual Environment

Isolate your project dependencies:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### D. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### E. Run the Application

Start the local development server:

```bash
python manage.py runserver
```

Open your browser to `http://127.0.0.1:8000/`. You should see the API root or a 404 page (depending on configuration), but the server should be running without errors.

---

## 3. Frontend Setup

To run the full application, you will also need the frontend.

### A. Clone the Frontend Repository

Open a **new** terminal window (keep the backend running) and run:

```bash
git clone https://github.com/raksit/azure_sql_django_frontend.git
cd azure_sql_django_frontend
```
