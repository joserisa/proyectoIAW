from django.apps import AppConfig


class BlogPyexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_Pyex'
    def ready(self):
        import blog_Pyex.signals
