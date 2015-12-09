# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from django import forms

log = logging.getLogger(__name__)

class StartMatchForm(forms.Form):
    player1_white = forms.CharField(label='Player 1', max_length=255)
    player2_white = forms.CharField(label='Player 2', max_length=255, required=False)
    player1_black = forms.CharField(label='Player 1', max_length=255)
    player2_black = forms.CharField(label='Player 2', max_length=255, required=False)
