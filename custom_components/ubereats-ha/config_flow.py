import json
from homeassistant import config_entries
import pytz

with open('locale_codes.json', 'r') as f:
    LOCALE_CODE_MAPPING = json.load(f)

class UberEatsConfigFlow(config_entries.ConfigFlow, domain="uber_eats"):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            user_input['locale_code'] = LOCALE_CODE_MAPPING.get(user_input['timezone'], 'za')
            return self.async_create_entry(title="Uber Eats", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("cookie"): str,
                    vol.Required("userUuid"): str,
                    vol.Required("timezone", default="Africa/Johannesburg"): vol.In(pytz.all_timezones),
                }
            ),
        )
