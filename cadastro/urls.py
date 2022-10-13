from rest_framework.routers import DefaultRouter
from cadastro.views import CadastroViewSet

app_name = 'cadastro'

router = DefaultRouter(trailing_slash=False)
router.register(r'cadastros', CadastroViewSet)

urlpatterns = router.urls