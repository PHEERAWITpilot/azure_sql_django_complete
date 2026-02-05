# Teaching Guide: Django Store & Product API

This guide is designed to help you explain and demonstrate the Django Store and Product API project.

## 1. Project Overview
This project is a RESTful API built with **Django** and **Django REST Framework (DRF)**.
It manages two main resources:
*   **Stores**: Physical locations.
*   **Products**: Items for sale (independent of stores).

## 2. Key Concepts to Explain

### A. Models (`api/models.py`)
- **What they are**: The blueprint for your database tables.
- **Code Highlights**:
    - `Store`: Has `store_id` and `store_location`.
    - `Product`: Has `name`, `description`, `price`.
    - `__str__`: Explain how this method makes object representation readable (e.g., in Admin).

### B. Serializers (`api/serializers.py`)
- **What they are**: Translators that convert complex data (Model instances) into native Python datatypes (and then JSON) and vice-versa.
- **Code Highlights**:
    - `StoreSerializer`, `ProductSerializer`.
    - `ModelSerializer`: Reduces boilerplate code by automatically creating fields from the Model.

### C. Views (`api/views.py`)
- **What they are**: The logic that handles HTTP requests and returns responses.
- **Code Highlights**:
    - `generics.ListCreateAPIView`: Handles `GET` (list) and `POST` (create).
    - `generics.RetrieveUpdateDestroyAPIView`: Handles `GET` (single), `PUT/PATCH`, and `DELETE`.
    - `api_root`: A custom functional view to show the API entry points at `/`.

### D. URLs (`azure_project/urls.py` & `api/urls.py`)
- **What they are**: The router. It matches the incoming URL path to a specific View.
- **Code Highlights**:
    - `api/urls.py`: Defines endpoints like `stores/`, `products/`.
    - `azure_project/urls.py`: The main entry point, including `api.urls` and the Admin site.

## 3. Lesson Plan & Demo Script

### Phase 1: Exploring the Existing Store API
*Goal: Understand how Django REST Framework works using the pre-built Store API.*

1.  **Start the Server**: `python manage.py runserver 8000`
2.  **Explore URL**: Go to `http://127.0.0.1:8000/api/stores/`.
    *   Explain the **List** view: Data comes from the database.
    *   Explain the **JSON** format.
3.  **Code Walkthrough**:
    *   **Model** (`api/models.py`): Show `Store` class.
    *   **Serializer** (`api/serializers.py`): Show `StoreSerializer`.
    *   **View** (`api/views.py`): Show `StoreList`.
    *   **URL** (`api/urls.py`): Show the path mapping.
    *   **Admin**: Show `Store` in Django Admin.

### Phase 2: Live Coding - Building the Product API
*Goal: Students follow along to build the Product API from scratch.*

#### Step 1: Create the Model
*   Open `api/models.py`.
*   **Task**: Create `Product` model with `name`, `description`, `price`.
*   **Action**: Add `Product` class.
*   **Migration**: Run `makemigrations` and `migrate`.

#### Step 2: Create the Serializer
*   Open `api/serializers.py`.
*   **Task**: Create `ProductSerializer`.
*   **Explain**: Inheriting from `ModelSerializer`.

#### Step 3: Create the Views
*   Open `api/views.py`.
*   **Task**: Create `ProductList` (for users to see products).
*   **Task**: Create `ProductDetail` (for updating/deleting).

#### Step 4: Wire up the URLs
*   Open `api/urls.py`.
*   **Task**: Add paths for `products/` and `products/<int:id>/`.

#### Step 5: Verification
*   Go to `http://127.0.0.1:8000/api/products/`.
*   Test creating a new Product (e.g., "Latte").

## 4. Common Questions
*   **Q: Why separate `api/urls.py`?**
    *   A: For modularity. If we had multiple apps, we'd want each to manage its own URLs.
*   **Q: What is `venv`?**
    *   A: It isolates this project's Python libraries from the rest of your system.

## 5. MongoDB Integration

This project is set up to use MongoDB for storing certain data (like product reviews or logs), demonstrating a hybrid SQL/NoSQL architecture.

### A. Local Setup (Development)

1.  **Install MongoDB**: Download and install MongoDB Community Server for your OS.
2.  **Start MongoDB**: Run the MongoDB server (usually `mongod` or via a service).
3.  **Configure `settings.py`**:
    *   In `azure_project/settings.py`, ensure the local `MONGO_URI` is active and the Azure one is commented out for local development.
    *   ```python
        # Local Development
        MONGO_URI = 'mongodb://localhost:27017/'
        MONGO_DB_NAME = 'django_store_reviews'
        ```
4.  **Verify**: You can use tools like **MongoDB Compass** to connect to `mongodb://localhost:27017/` and view your data.

### B. Azure Cosmos DB for MongoDB (Production)

To run this in the cloud, we use Azure Cosmos DB (API for MongoDB).

1.  **Create Resource**: Create a "Azure Cosmos DB for MongoDB" resource in the Azure Portal (vCore or Request Unit based).
2.  **Get Connection String**:
    *   Go to **Settings** > **Connection strings**.
    *   Copy the Primary Connection String.
3.  **Update `settings.py`** (or use Environment Variables):
    *   In a real production environment, **NEVER** commit secrets to code.
    *   For this teaching demo, we show where it goes:
        ```python
        # Production (Azure Cosmos DB)
        mongo_username = urllib.parse.quote_plus('your_username')
        mongo_password = urllib.parse.quote_plus('your_password')
        MONGO_URI = f'mongodb+srv://{mongo_username}:{mongo_password}@your-cluster.mongocluster.cosmos.azure.com/...'
        ```

### C. The Connection Code (`api/mongo_utils.py`)
Show students the helper function `get_db_handle()` in `api/mongo_utils.py`. It uses the `pymongo` library to create a client based on the settings.

## 6. Azure Deployment via GitHub Actions

We use **GitHub Actions** for Continuous Deployment (CD). Every time you push to the `main` branch, the code is automatically deployed to Azure App Service.

### A. The Workflow File
Show `.github/workflows/main_bearlab-backend.yml`.

*   **Trigger**: `on: push: branches: [ main ]` - Runs when code is pushed to main.
*   **Build Job**: Sets up Python, installs dependencies (optional step for verification).
*   **Deploy Job**:
    *   `azure/login`: Authenticates with Azure using a Service Principal (stored in GitHub Secrets).
    *   `azure/webapps-deploy`: Copies the code to your Azure App Service.

### B. Setting Up Secrets
For the action to assume identity and deploy, we need secrets in the GitHub Repository (**Settings > Secrets and variables > Actions**):
*   `AZUREAPPSERVICE_CLIENTID_...`
*   `AZUREAPPSERVICE_TENANTID_...`
*   `AZUREAPPSERVICE_SUBSCRIPTIONID_...`

*Note: These are usually automatically created if you set up deployment via the Azure Portal "Deployment Center".*

### C. Connecting App Service to Databases
The deployed code needs to know how to connect to Azure SQL and Cosmos DB. We **do not** hardcode these in `settings.py` for production safety.

1.  Go to your **App Service** in Azure Portal.
2.  Select **Settings** > **Environment variables**.
3.  Add the new settings:
    *   `MONGO_URI`: Your Cosmos DB connection string.
    *   `MONGO_DB_NAME`: `django_store_reviews`
    *   *(And any SQL settings if you converted them to env vars)*
4.  **Save** and **Restart** the app.

## 7. Full Stack Deployment Overview

Explain to students how the pieces fit together in the cloud:

1.  **Backend (Azure App Service)**: Runs the Django API. Connects to Azure SQL and Cosmos DB via environment variables.
2.  **Frontend (Azure App Service)**: Runs the React/Vite app (Node.js).
    *   It is a separate resource from the backend.
    *   It needs to know the **Backend URL** (via `VITE_API_URL`) to send API requests.
3.  **Database Layer**:
    *   **Azure SQL**: Relational data (Products, Stores).
    *   **Cosmos DB**: NoSQL data (Reviews).

*Tip: Emphasize that in production, the frontend browser makes requests directly to the backend API, so CORS must be enabled on the backend.*
