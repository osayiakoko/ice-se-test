from .development import *

# Database URL
DATABASES['default']['HOST'] = 'postgresql://postgres@localhost/icetest?sslmode=disable'
