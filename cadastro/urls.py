"""
Arquivos do rotas/urls da API
"""

from rest_framework.routers import DefaultRouter
import cadastro.views

app_name = 'cadastro'

router = DefaultRouter(trailing_slash=False)
router.register(r'usuarios', cadastro.views.UsuarioViewSet)

urlpatterns = router.urls
