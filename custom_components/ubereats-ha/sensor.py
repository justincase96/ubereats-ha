import requests
from homeassistant.helpers.entity import Entity

def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([UberEatsSensor(entry.data)])

class UberEatsSensor(Entity):
    def __init__(self, config):
        self._state = None
        self._config = config

    @property
    def name(self):
        return 'Uber Eats'

    @property
    def state(self):
        return self._state

    async def async_update(self):
        response = await hass.async_add_executor_job(
            requests.post,
            'https://www.ubereats.com/api/getActiveOrdersV1?localeCode=za',
            headers={
                'accept': 'application/json',
                'cookie': f"sid={self._config['cookie']}; _userUuid={self._config['userUuid']}",
                'x-csrf-token': 'x'
            },
            json={
                'orderUuid': 'null',
                'timezone': self._config['timezone']
            }
        )
        self._state = response.json()['status']
