from homeassistant import config_entries
import pytz

class UberEatsConfigFlow(config_entries.ConfigFlow, domain="uber_eats"):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        if user_input is not None:
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
