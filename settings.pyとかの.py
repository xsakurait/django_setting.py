css使うには
settings.py
STATIC_URL='/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)
html 
{% load static %}
<link href="{% static 'test.css' %}"