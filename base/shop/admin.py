from django.contrib import admin
from .models import Category, Course


admin.site.site_header = 'Courses Admin'  # Поменяли название navbar - на админ панели
admin.site.site_title = 'My Curses'
admin.site.index_title = 'Welcome to the Courses admin area'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'students_qty')


admin.site.register(Course, CourseAdmin)


class CoursesInLine(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        }),
    ]
    inlines = [CoursesInLine]


admin.site.register(Category, CategoryAdmin)
