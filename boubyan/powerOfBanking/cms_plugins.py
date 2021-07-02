# django imports
from cms.models import CMSPlugin
from django.core.exceptions import ObjectDoesNotExist

# cms imports
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

# our models imports
from .models import PowerOfBanking, CardIcon, Title, CardBox, CardBoxWithImage

# django translation
from django.utils.translation import gettext as _


class PowerOfBankingPlugin(CMSPluginBase):
    name = _("Power Banking Plugin")
    model = PowerOfBanking
    render_template = "powerOfBanking/_base.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


class CardIconPlugin(CMSPluginBase):
    name = _("Card with Icon")
    model = CardIcon
    render_template = "powerOfBanking/_card_icon.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


class TitlePlugin(CMSPluginBase):
    name = _("Title")
    model = Title
    render_template = "powerOfBanking/_title.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


class CardBoxPlugin(CMSPluginBase):
    name = _("Card Box")
    model = CardBox
    render_template = "powerOfBanking/_card_box.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


class CardBoxWithImagePlugin(CMSPluginBase):
    name = _("Card Box Image")
    model = CardBoxWithImage
    render_template = "powerOfBanking/_card_box_image.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


class LoveUsCarousel(CMSPluginBase):
    name = _("Love Us Carousel")
    model = CMSPlugin
    render_template = "powerOfBanking/_love_us_carousel.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


plugin_pool.register_plugin(PowerOfBankingPlugin)
plugin_pool.register_plugin(CardIconPlugin)
plugin_pool.register_plugin(TitlePlugin)
plugin_pool.register_plugin(CardBoxPlugin)
plugin_pool.register_plugin(CardBoxWithImagePlugin)
plugin_pool.register_plugin(LoveUsCarousel)
