# Azure SQL Django Template

A starter template for building a REST API with **Django 5.2** connected to **Azure SQL Database**.

## Quick Start

For detailed installation, prerequisites, and database configuration, please refer to:
- [General Setup Guide](docs/SETUP.md)
- [Student Preparation Guide (Week 2)](docs/STUDENT_SETUP_GUIDE.md)
- [Azure Database Setup (SQL & Cosmos DB)](docs/DB_SETUP_AZURE.md)
- [Deployment Guide (App Service & Containers)](docs/DEPLOYMENT.md)

## API Endpoints

### Stores
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/stores/` | List all stores |
| `POST` | `/api/stores/` | Create a new store |
| `GET` | `/api/stores/<id>/` | Get details of a specific store |
| `PUT` | `/api/stores/<id>/` | Update a store |
| `DELETE` | `/api/stores/<id>/` | Delete a store |
| `DELETE` | `/api/stores/deleteAll/` | Delete ALL stores |

### Products
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/products/` | List all products |
| `POST` | `/api/products/` | Create a new product |
| `GET` | `/api/products/<id>/` | Get details of a specific product |
| `PUT` | `/api/products/<id>/` | Update a product |
| `DELETE` | `/api/products/<id>/` | Delete a product |
| `DELETE` | `/api/products/deleteAll/` | Delete ALL products |

### Users
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/users/` | List all users |
| `POST` | `/api/users/` | Create a new user |
| `GET` | `/api/users/<id>/` | Get details of a specific user |
| `PUT` | `/api/users/<id>/` | Update a user |
| `DELETE` | `/api/users/<id>/` | Delete a user |

### Orders
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/orders/` | List all orders |
| `POST` | `/api/orders/` | Create a new order |
| `GET` | `/api/orders/<id>/` | Get details of a specific order |
| `DELETE` | `/api/orders/<id>/` | Delete an order |

### Reviews (MongoDB)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/reviews/` | List all reviews (supports `?product_id=` filter) |
| `POST` | `/api/reviews/` | Create a new review |
| `GET` | `/api/reviews/<id>/` | Get details of a review |
| `PUT` | `/api/reviews/<id>/` | Update a review |
| `DELETE` | `/api/reviews/<id>/` | Delete a review |

## Project Structure

- `api/`: Django app containing Models, Views, and Serializers.
- `azure_project/`: Project settings and URL configuration.
