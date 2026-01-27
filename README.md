# Azure SQL Django Template

A starter template for building a REST API with **Django 5.2** connected to **Azure SQL Database**.

## Quick Start

For detailed installation, prerequisites, and database configuration, please refer to the [Setup Guide](docs/SETUP.md).

## API Endpoints

The project implements a simple "Store" resource.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/stores/` | List all stores |
| `POST` | `/api/stores/` | Create a new store |
| `GET` | `/api/stores/<id>/` | Get details of a specific store |
| `PUT` | `/api/stores/<id>/` | Update a store |
| `DELETE` | `/api/stores/<id>/` | Delete a store |
| `DELETE` | `/api/stores/deleteAll/` | Delete ALL stores |

## Project Structure

- `api/`: Django app containing Models, Views, and Serializers.
- `azure_project/`: Project settings and URL configuration.
