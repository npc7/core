"""The test for the Random binary sensor platform."""
from homeassistant.setup import async_setup_component

from tests.async_mock import patch


async def test_random_binary_sensor_on(hass):
    """Test the Random binary sensor."""
    config = {"binary_sensor": {"platform": "random", "name": "test"}}

    with patch(
        "homeassistant.components.random.binary_sensor.getrandbits",
        return_value=1,
    ):
        assert await async_setup_component(
            hass,
            "binary_sensor",
            config,
        )
        await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.test")

    assert state.state == "on"


async def test_random_binary_sensor_off(hass):
    """Test the Random binary sensor."""
    config = {"binary_sensor": {"platform": "random", "name": "test"}}

    with patch(
        "homeassistant.components.random.binary_sensor.getrandbits",
        return_value=False,
    ):
        assert await async_setup_component(
            hass,
            "binary_sensor",
            config,
        )
        await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.test")

    assert state.state == "off"
