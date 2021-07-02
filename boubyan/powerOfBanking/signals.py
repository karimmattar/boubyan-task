# import signals db(trigger)
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# django translation
from django.utils.translation import gettext as _

# import our models
from .models import PowerOfBanking


@receiver(pre_save, sender=PowerOfBanking)
def check_active_instance(sender, instance, *args, **kwargs):
    if instance.is_active:
        try:
            PowerOfBanking.objects.get(is_active=True)
        except ObjectDoesNotExist:
            pass
        raise Exception(_("instance with is active key is exist."))
