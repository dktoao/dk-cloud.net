from django.shortcuts import Http404
from django.core.exceptions import PermissionDenied

from .models import TreeNav


class TreeNavAccessMixin(object):
    """
    Allows access to nodes via database authentication system defined by the
    TreeNav model
    """
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is allowed to access the navigation node that is 
        # requested and then dispatch normally
        node_id = kwargs.get('node_id', None)
        if request.method == 'GET':
            if node_id is not None:
                try:
                    node = TreeNav.objects.get(pk=node_id)
                    kwargs['node'] = node
                except TreeNav.DoesNotExist:
                    raise Http404

                if node.requires_auth:
                    if not request.user.is_authenticated():
                        raise PermissionDenied

                    if not (len(request.user.groups.all() & node.auth_groups.all()) > 0
                            or request.user.is_superuser):
                        #TODO: Delete this if it doesn't start raising issues
                        #print("Group Test: {}".format(len(request.user.groups.all() & node.auth_groups.all()) < 1))
                        #print("Superuser Test: {}".format(not request.user.is_superuser))
                        #print("Should have access?: {}".format(
                        #    len(request.user.groups.all() & node.auth_groups.all()) < 1 or \
                        #    not request.user.is_superuser
                        #))
                        raise PermissionDenied
            else:
                kwargs['node'] = None

        return super(TreeNavAccessMixin, self).dispatch(
            request, *args, **kwargs)


class TreeNavMenuMixin(object):
    """
    Adds functions to the class based view to render the ancestor and children
    of the current node.
    """

    @staticmethod
    def get_forward_nav_items(**kwargs):

        node = kwargs.get('node')
        if node is None:
            forward_nav_items = TreeNav.get_root_nodes()
        else:
            forward_nav_items = node.get_children()
        return forward_nav_items

    @staticmethod
    def get_backward_nav_items(**kwargs):
        node = kwargs.get('node')
        if node is None:
            backward_nav_items = None
        elif node.is_root():
            backward_nav_items = None
        else:
            backward_nav_items = node.get_ancestors()
        return backward_nav_items