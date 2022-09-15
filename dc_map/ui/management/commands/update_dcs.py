import requests
from django.core.management.base import BaseCommand, CommandError
from ui import models

API_URL = 'https://graphql.cloud-mercato.com/graphql'
DC_REQUEST = """
query {
  zones (region: eu)  {
    name
    country
    lat
    lng
    provider {
      name
    }
  }
}
"""


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        response = requests.get(API_URL, params={'query': DC_REQUEST})
        json_reponse = response.json()
        dcs = json_reponse['data']['zones']

        for dc in dcs:
            provider, _ = models.Provider.objects.get_or_create(name=dc['provider']['name'])
            if not dc['lat'] or not dc['lng']:
                continue
            datacenter, _ = models.Datacenter.objects.get_or_create(
                name=dc['name'],
                country=dc['country'],
                lat=dc['lat'],
                lng=dc['lng'],
                provider=provider,
            )
