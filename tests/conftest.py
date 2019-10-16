"""
This module contains shared fixtures.
LambdaTest docs are here:
https://www.lambdatest.com/support/docs/pytest-with-selenium-running-pytest-automation-script-on-lambdatest-selenium-grid/
"""

import json
import pytest
import selenium.webdriver


# ----------------------------------------------------------------------
# Fixture: Read the LambdaTest config file
# ----------------------------------------------------------------------

@pytest.fixture
def lt_config(scope='session'):

  # Read the config file
  with open('lt_config.json') as config_file:
    config = json.load(config_file)
  
  # Verify authentication config
  assert 'authentication' in config
  assert 'username' in config['authentication']
  assert 'key' in config['authentication']

  # Verify webdriver config
  assert 'webdriver' in config
  assert 'browserName' in config['webdriver']
  assert 'platform' in config['webdriver']

  # Return the config data
  return config


# ----------------------------------------------------------------------
# Fixture: Create the WebDriver instance
# ----------------------------------------------------------------------

@pytest.fixture
def browser(lt_config, request):

  # Concatenate the URL
  username = lt_config['authentication']['username'].replace('@', '%40')
  key = lt_config['authentication']['key']
  url = f"http://{username}:{key}@hub.lambdatest.com/wd/hub"

  # Request a remote browser from LambdaTest
  caps = lt_config['webdriver']
  caps['name'] = request.node.name
  driver = selenium.webdriver.Remote(command_executor=url, desired_capabilities=caps)

  # Make its calls wait up to 30 seconds for elements to appear
  driver.implicitly_wait(30)

  # Return the WebDriver instance for the setup
  yield driver
  
  # Create a finalizer for the remote browser
  def finalizer():
      if request.node.rep_call.failed:
          driver.execute_script("lambda-status=failed")
      else:
          driver.execute_script("lambda-status=passed")
          driver.quit()
  
  # Add the finalizer to the test
  request.addfinalizer(finalizer)


# ----------------------------------------------------------------------
# Hook: Set the test result
# ----------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
  # This sets the result as a test attribute for LambdaTest reporting.
  # Execute all other hooks to obtain the report object.
  outcome = yield
  rep = outcome.get_result()

  # Set an report attribute for each phase of a call, which can
  # be "setup", "call", "teardown"
  setattr(item, "rep_" + rep.when, rep)
