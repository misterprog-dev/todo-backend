import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Todo, TodoList


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0
    

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin, ExportCsvMixin):    
    list_display = ('title', 'due_date', 'completed', 'favorite')
    list_filter = ('due_date', 'completed', 'favorite')
    actions = ['export_as_csv']
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('title',)
    # date_hierarchy = ''
    ordering = ('title', 'due_date', 'completed', 'favorite')   

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):    
    list_display = ('name',)
    list_filter = ('name',)
    inlines = [
        TodoInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    ordering = ('name',)
