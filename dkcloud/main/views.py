from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import login, password_change, password_change_done

from treenav.views import TreeNavAccessMixin, TreeNavMenuMixin


class MainPageView(TreeNavMenuMixin, TemplateView):

    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['forward_nav_items'] = self.get_forward_nav_items(**kwargs)
        context['backward_nav_items'] = None
        context['username'] = get_username_or_none(self.request)

        return context


class NodeView(TreeNavAccessMixin, TreeNavMenuMixin, TemplateView):

    template_name = 'main/info.html'

    def get_context_data(self, **kwargs):
        context = super(NodeView, self).get_context_data(**kwargs)
        context['node'] = kwargs.get('node')
        context['forward_nav_items'] = self.get_forward_nav_items(**kwargs)
        context['backward_nav_items'] = self.get_backward_nav_items(**kwargs)
        context['username'] = get_username_or_none(self.request)

        return context

 
def user_message_view(request, message):
    """
    Displays a message to the user
    """
    return render(request, 'main/user_message.html', {
        'message': message,
        'username': request.user.username,
    })


def password_change_main(request):
    """
    View to update the user password
    """
    extra_context = {
        'form_title': 'Change Password',
        'username': request.user.username,
    }
    return password_change(request, template_name='main/user_form.html',
                           extra_context=extra_context)


def password_change_done_main(request):
    """
    View to confirm user password is updated
    """
    extra_context = {
        'message': 'Your password has been changed',
        'username': request.user.username,
    }
    return password_change_done(request, template_name='main/user_message.html',
                                extra_context=extra_context)


def login_main(request):
    """
    View to log user in.
    """

    if request.user.is_authenticated():
        return user_message_view(request, "You are already logged in.")

    extra_context = {
        'form_title': 'User Login',
        'button_caption': 'Login',
        'username': request.user.username,
    }

    return login(request, template_name='main/user_form.html', extra_context=extra_context)


## Helper functions ##
def get_username_or_none(request):
    """
    Gets the username of the logged in user or none if they are not logged in
    """
    if request.user.is_authenticated():
        return request.user.username
    else:
        return None