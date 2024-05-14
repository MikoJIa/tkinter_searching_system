from django.urls import path, include
from .models import CategoryResource, CourseResource
from tastypie.api import Api

# Создаём экземпляр класса Api
api = Api(api_name='v1')

# Необходимо создать экземпляры классов: CategoryResource, CourseResource
api.register(CourseResource())
api.register(CategoryResource())

# пути к ресурсам будут вот такие:
# api/v1/courses
# api/v1/categories

# for POST, DELETE we have to add header
# Key: Authorozation
# Value: ApiKey Mikola:mikolamikolau1234567

urlpatterns = [
    path('', include(api.urls), name='index')
]