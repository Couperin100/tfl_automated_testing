from functools import partial
from pytest_bdd import given, then, scenario, when
from pytest import fixture

from selenium.webdriver.remote.webdriver import WebDriver

from pages.plan_a_journey import PlanJourneySection

scenario = partial(scenario, '../feature/plan_a_journey_alerts.feature')


@fixture(scope='module')
def suite_setup(driver: WebDriver, env: dict):
    """Setup fixture to open the page and finally close the browser."""
    driver.get(env['site'])


@scenario('I do not enter a station into the From field')
def test_i_do_not_enter_a_station_into_from_field(suite_setup):
    """I do not enter a station into the 'From' field."""
    pass


@scenario('I do not enter a station into the To field')
def test_i_do_not_enter_a_station_into_to_field(suite_setup):
    """I do not enter a station into the 'To' field."""
    pass


@scenario('I do not enter a station into the To or From field')
def test_i_do_not_enter_a_station_into_to_or_from_field(suite_setup):
    """I do not enter a station into the 'From' or 'To' field."""
    pass


@given('I am on the TFL website')
def i_am_on_the_tfl_website(driver: WebDriver, env: dict):
    """Verify I am on the correct page."""
    if driver.current_url != PlanJourneySection(driver, env).url:
        driver.switch_to.window(env['site'])


@given("I leave the 'From' field empty")
def i_leave_the_from_field_empty(driver: WebDriver, env: dict):
    """Clear the 'From' field text."""
    PlanJourneySection(driver, env).clear_from_field_text()


@given("I leave the 'To' field empty")
def i_leave_the_to_field_empty(driver: WebDriver, env: dict):
    """Clear the 'To' field text."""
    PlanJourneySection(driver, env).clear_to_field_text()


@when("I click on the plan my journey button")
def i_click_on_the_plan_my_journey_button(driver: WebDriver, env: dict):
    """Click on the 'plan_my_journey' button."""
    PlanJourneySection(driver, env).click_plan_my_journey_button()


@then("I should see the alert 'The From field is required'")
def i_should_see_alert_from_field_required(driver: WebDriver, env: dict):
    """Assert that the 'From' alert has the expected text."""
    page = PlanJourneySection(driver, env)
    assert (page.get_from_field_alert() == page.get_expected_from_alert_text())


@then("I should see the alert 'The To field is required'")
def i_should_see_alert_to_field_required(driver: WebDriver, env: dict):
    """Assert that the 'To' alert has the expected text."""
    page = PlanJourneySection(driver, env)
    assert (page.get_to_field_alert() == page.get_expected_to_alert_text())
