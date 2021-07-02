# basic django model
from django.db import models
# django translation
from django.utils.translation import gettext as _

# abstracted cms plugin model
from cms.models import CMSPlugin


# first page component as model
class PowerOfBanking(CMSPlugin):
    poster = models.ImageField(upload_to='power_of_banking/posters', null=False, blank=False,
                               help_text=_("plugin poster, it's required"))
    title = models.CharField(max_length=120, null=False, blank=False, help_text=_("plugin title, it's required"))
    subtitle = models.CharField(max_length=120, null=False, blank=False, help_text=_("plugin subtitle, it's required"))
    google_play_link = models.URLField(max_length=160, null=True, blank=True, help_text=_(
        "google play application link, it's not required but we prefer to to include it"))
    app_store_link = models.URLField(max_length=160, null=True, blank=True, help_text=_(
        "app store application link, it's not required but we prefer to to include it"))
    logo = models.ImageField(upload_to='power_of_banking/logos', null=True, blank=True,
                             help_text=_("plugin logo, it's not required"))
    logo_subtitle = models.CharField(max_length=120, null=True, blank=True,
                                     help_text=_("logo subtitle, under logo subtitle it's not required"))
    is_active = models.BooleanField(default=False,
                                    help_text=_("if is active is true the component will appear else will disappear"))


class CardIcon(CMSPlugin):
    icon = models.ImageField(upload_to='power_of_banking/icons', null=False, blank=False)
    title = models.CharField(max_length=120, null=False, blank=False)
    subtitle = models.TextField(null=False, blank=False)


class Title(CMSPlugin):
    title = models.CharField(max_length=180, null=False, blank=False)


class CardBox(CMSPlugin):
    icon = models.ImageField(upload_to='power_of_banking/icons', null=False, blank=False)
    title = models.CharField(max_length=120, null=False, blank=False)
    subtitle = models.TextField(null=False, blank=False)


class CardBoxWithImage(CMSPlugin):
    image = models.ImageField(upload_to='power_of_banking/images', null=False, blank=False)
    title = models.CharField(max_length=120, null=False, blank=False)
    subtitle = models.TextField(null=False, blank=False)
