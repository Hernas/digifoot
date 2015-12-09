# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import requests
import logging
from twilio.rest import TwilioRestClient
from django.conf import settings
import sendgrid

log = logging.getLogger(__name__)
ACCESS_TOKEN = "5541eaa7540d5ea319e9906093f06cbc7f04f6df"

class SparkIO(object):
    def __init__(self, device_id):
        self.account_token = ACCESS_TOKEN
        self.device_id = device_id

    def ping(self):
        return self._send_request('play', "5000")

    def engage_alarm(self):
        self._send_alarm_engage('on')

    def disengage_alarm(self):
        self._send_alarm_engage('off')

    def _send_alarm_engage(self, state):
        return self._send_request('alarmEngaged', state)

    def _send_request(self, function, args):
        response = requests.post(
            'https://api.particle.io/v1/devices/{device_id}/{function}'.format(device_id=self.device_id,
                                                                               function=function),
            data={'args': args},
            headers={'Authorization': 'Bearer {0}'.format(self.account_token)})
        print('Request: %s' % response.request.url)
        print('Response: %s' % response.text)
        return response


class Twillo:
    @classmethod
    def send_sms(cls):
        print ("Sending sms using Twillo")
        try:
            client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            sms = client.sms.messages.create(body="Someone is stealing your bike!",
                to="+491724694679",
                from_="+4915735984369")

            print ("Sms sent")
        except Exception:
            print ("Error occurred while sending sms")


class SendGrid:
    @classmethod
    def send_email(cls):
        print ("Sending email using SendGrid")

        try:
            client = sendgrid.SendGridClient(settings.SENDGRID_API_USER, settings.SENDGRID_API_KEY)
            message = sendgrid.Mail()

            message.add_to("michal@hernas.pl")
            message.set_from("alarm@whispering-island-7058.herokuapp.com")
            message.set_subject("Someone is stealing your bike!")
            message.set_html("Your bike lock had been <b>broken</b> - go and check it!")

            client.send(message)

            print ("Email sent")

        except Exception:
            print ("Error occurred while sending mail")



# curl https://api.particle.io/v1/devices/0123456789abcdef/brew \
#      -d access_token=123412341234 \
#      -d "args=on"