from .views import TodoViewSet, TodoListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'todos-lists', TodoListViewSet)
urlpatterns = router.urls
