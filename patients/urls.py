from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    VitalsViewSet,
    VisitFormAViewSet,
    VisitFormBViewSet,
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'vitals', VitalsViewSet)
router.register(r'visit_form_a', VisitFormAViewSet)
router.register(r'visit_form_b', VisitFormBViewSet)

urlpatterns = router.urls
