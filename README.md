# Uber Eats Integration for Home Assistant

This is a custom integration for Home Assistant that fetches data from the Uber Eats API.

## Installation

1. Copy the `uber_eats` directory into your `custom_components` directory.
2. Restart Home Assistant to load the new custom component.

## Configuration

To add the Uber Eats integration to your Home Assistant instance, go to **Configuration** -> **Integrations** and click on the **ADD INTEGRATION** button. Search for "Uber Eats" and fill in the form with your Uber Eats session ID (cookie) and timezone.

## Sensor

This integration provides a sensor named `sensor.uber_eats` that shows the status of your active Uber Eats orders.

## Note

This is a very basic example and doesn't include error handling or other best practices for creating a custom component. Also, you need to replace `'YOUR_COOKIE'` with your actual Uber Eats session ID. 
