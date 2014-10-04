from django.db import models
from treebeard.mp_tree import MP_Node
from django.contrib.auth.models import Group
# Create your models here.

class TreeNav(MP_Node):
    '''
    Main navigation data model, holds a hierarchial structure with nodes for 
    website navigation.
    '''
    node_order_by = ['short_name']
    short_name = models.CharField(unique=True, max_length=20)
    long_name = models.CharField(max_length=100)
    content = models.TextField()
    link = models.URLField(max_length=1000, blank=True)
    direct_link = models.BooleanField(default=False)
    requires_auth = models.BooleanField()
    auth_groups = models.ManyToManyField(Group, blank=True)
    
    def has_node_access(node, user):
        pass
    
    def __str__(self):
        return self.short_name