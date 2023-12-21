# Uber Eats Integration for Home Assistant

This is a custom integration for Home Assistant that fetches data from the Uber Eats API.

## Installation

1. Copy the `uber_eats` directory into your `custom_components` directory.
2. Restart Home Assistant to load the new custom component.

## Configuration

To add the Uber Eats integration to your Home Assistant instance, go to **Configuration** -> **Integrations** and click on the **ADD INTEGRATION** button. Search for "Uber Eats" and fill in the form with your Uber Eats session ID (cookie), user UUID, and timezone.

## How to Get Your Session ID (Cookie) and User UUID

When you sign into Uber Eats and place an order, open the Chrome debug tools & inspector window, and jump over to the network tab. You'll see all of the 'queries' the web application is posting to the back API endpoint. Pay attention to queries sent to "https://www.ubereats.com/api/getActiveOrdersV1?localeCode=[Your_Locale_Code]".

You can replicate these POST calls to the Uber Eats API endpoint periodically (every 120 seconds even) until the cookie expires, and can then just replace the cookie once it expires. If you're hitting the endpoint every couple of minutes, the cookie won't expire for months.

This integration will supply most of the information needed like 'Content-Type:"application/json", ' '"X-CSRF-Token": "x",' however, you need to supply the 'cookie:"sid=[Your_Cookie_SID_Here];_userUuid=[Your_User_UUID_Here]"' <---these can be lifted directly out of the inspector window in chrome. Cookie SID starts with "QA." Place an order on uber eats and jump to the network tab in the Inspector window to get what these are for you.

Lastly, replicate the POST request payload as-is, supplying null for the orderUuid, and, your timezone in "timezone" - just replicate what you see in the Chrome inspector.

## Sensor

This integration provides a sensor named `sensor.uber_eats` that shows the status of your active Uber Eats orders. The sensor fetches data from the Uber Eats API every couple of minutes.

## Note

This is a very basic example and doesn't include error handling or other best practices for creating a custom component. Also, you need to replace `'YOUR_COOKIE'` and `'YOUR_USER_UUID'` with your actual Uber Eats session ID and user UUID.
