import certifi
from pymongo import MongoClient
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
_client = None


class MongoConfigurationError(Exception):
    pass


def _normalize_mongo_uri(uri):
    if uri is None:
        return ''

    cleaned = str(uri).strip().strip('"').strip("'").rstrip(',').strip()
    return cleaned

def get_db_handle():
    global _client
    try:
        mongo_uri = _normalize_mongo_uri(getattr(settings, 'MONGO_URI', ''))
        if not mongo_uri:
            raise MongoConfigurationError(
                'MONGO_URI is not configured. Set it in environment variables or settings.'
            )

        if _client is None:
            _client = MongoClient(mongo_uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)
        
        # Test connection
        _client.admin.command('ping')
        
        db = _client[settings.MONGO_DB_NAME]
        return db
    except MongoConfigurationError:
        raise
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        print(f"Error connecting to MongoDB: {e}")
        raise Exception(f"MongoDB connection failed: {str(e)}")
