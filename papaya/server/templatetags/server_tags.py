from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import Library

register = Library()


# FIXME : get rid of hard-coded url
def openid_url(user):
    return settings.SITE_URL + reverse('papaya.server.views.idPage', args=[user.username])


register.simple_tag(openid_url)
