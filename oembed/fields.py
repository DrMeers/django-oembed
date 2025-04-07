import re
from urllib2 import HTTPError

from django.core import exceptions
from django.db import models

from .core import build_url, fetch, MAX_WIDTH, MAX_HEIGHT
from .models import ProviderRule

class OEmbedField(models.URLField):
    """
    A URL pointing to an oEmbed provider.
    
    See http://www.oembed.com/ for information on providers
    """
    
    description = "A URL pointing to an oEmbed provider"
    
    def validate(self, value, model_instance):
        for pattern in ProviderRule.objects.values_list('regex', flat=True):
            if re.match(pattern, value):
                rule = ProviderRule.objects.filter(regex=pattern).first()
                url = build_url(rule.endpoint, value, MAX_WIDTH, MAX_HEIGHT)
                try:
                    fetch(url)
                except HTTPError as e:
                    if e.code == 401:
                        raise exceptions.ValidationError(
                            'Please ensure the settings for this video allow '
                            'embedding in external sites ({})'.format(
                                e
                            )
                        )
                    raise exceptions.ValidationError(
                        'Cannot embed video: {}'.format(e)
                    )
                except Exception as e:
                    raise exceptions.ValidationError(
                        'Cannot embed video: {}'.format(e)
                    )
                return
        raise exceptions.ValidationError('Not a valid oEmbed link')
