from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarConfig


class SimpleCommerceConfig(OscarConfig):
    label = 'simplecommerce'
    name = 'oscar.apps.simplecommerce'
    verbose_name = _('Simple-commerce')
