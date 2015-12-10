# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

log = logging.getLogger(__name__)

from django import template

register = template.Library()

MOMENT = 0  # duration in seconds within which the time difference
# will be rendered as 'a moment ago'

@register.filter
def naturalTimeDifference(delta):
    """
    Finds the difference between the datetime value given and now()
    and returns appropriate humanize form
    """

    from datetime import timedelta

    if isinstance(delta, timedelta):
        s = delta.total_seconds()
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '%sh %sm %ss' % (int(hours), int(minutes), int(seconds))
    else:
        return str(delta)