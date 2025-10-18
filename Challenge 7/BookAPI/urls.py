from django.urls import path, include
from rest_framework.routers import DefaultRouter

from BookAPI import views

router = DefaultRouter()
router.register(r"book", views.BookViewSet, basename="book")
router.register(r"book1", views.BooksWithRatingOver7, basename="book1")
router.register(r"book2", views.BooksWithRatingLessThan3, basename="book2")
router.register(r"book3", views.BookWithNameContainingTHE, basename="book3")
router.register(r"book4", views.BookWithCategoryIsFiction, basename="book4")
router.register(r"book5", views.BookWithCategoryIsFantasy, basename="book5")
router.register(r"book6", views.BookWithPastInDescription, basename="book6")
router.register(r"book7", views.BookWithWizardInDescription, basename="book7")
router.register(r"book8", views.BookWithPersonInDescription, basename="book8")
router.register(r"book9", views.BookWithBelieveInDescription, basename="book9")
router.register(r"book10", views.BookWithTaleInDescription, basename="book10")


urlpatterns = [
    path('', include(router.urls))
]