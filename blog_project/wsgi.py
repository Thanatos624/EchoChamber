import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

# Import WhiteNoise
from whitenoise import WhiteNoise

application = get_wsgi_application()
# Wrap the application with WhiteNoise
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'media'))