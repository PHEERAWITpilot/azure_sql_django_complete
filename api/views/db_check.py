from rest_framework import response
from rest_framework.decorators import api_view
from django.conf import settings
from django.db import connections

@api_view(['GET'])
def check_db_connection(request):
    # Check SQL Database
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
        sql_status = "Connected"
    except Exception as e:
        sql_status = f"Error: {str(e)}"

    sql_info = {
        'engine': settings.DATABASES['default']['ENGINE'],
        'name': settings.DATABASES['default']['NAME'],
        'status': sql_status
    }

    # Check MongoDB
    mongo_uri = getattr(settings, 'MONGO_URI', 'Not Configured')
    # Mask credentials if present
    masked_uri = mongo_uri
    if '@' in mongo_uri:
        try:
            protocol = mongo_uri.split('://')[0]
            host_part = mongo_uri.split('@')[1]
            masked_uri = f"{protocol}://****:****@{host_part}"
        except:
            masked_uri = "Could not parse URI for masking"

    mongo_info = {
        'uri': masked_uri,
        'db_name': getattr(settings, 'MONGO_DB_NAME', 'Not Configured')
    }

    return response.Response({
        'sql_database': sql_info,
        'mongo_database': mongo_info
    })
