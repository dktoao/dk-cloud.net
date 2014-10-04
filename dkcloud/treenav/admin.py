from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import TreeNav

# Register your models here.
class TreeNavAdmin(TreeAdmin):
    form = movenodeform_factory(TreeNav)
    
admin.site.register(TreeNav, TreeNavAdmin)