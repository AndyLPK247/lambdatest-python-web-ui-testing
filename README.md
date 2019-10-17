# lambdatest-python-web-ui-testing
This repository contains the example test project for the
"Web UI Testing with Python and LambdaTest" webinar delivered by
[LambdaTest](https://www.lambdatest.com/) in collaboration with
[Automation Panda](https://automationpanda.com) on October 29, 2019. 

## Setup
This project requires [Python 3](https://www.python.org/).

To set up the Python environment and install dependencies,
change directory into the example project and run:

    pip install pipenv
    pipenv install

## Running Tests
You will need a LambdaTest license to run the tests in this project.
You can obtain a trial license from https://www.lambdatest.com/.
Add your username and authentication token to lt_config.json.

To run tests, run the following command from the project's root directory:

    pipenv run python -m pytest

To run tests in parallel, add "-n \[num-threads\]":

    pipenv run python -m pytest -n 5

The terminal will print the pytest banner.
Be patient - tests may take a few seconds to complete.
You can also check results on the LambdaTest website.

## Writing New Tests
This project can be the starting point for more testing.
Try writing new tests on your own! Here are some ideas for additional DuckDuckGo tests:

* use different search phrases
* click a search result
* do an image search
* do a video search

You can also try to write tests for other Web apps!

## Additional Resources

* [LambdaTest](https://www.lambdatest.com/) website
* [Automation Panda](https://www.automationpanda.com/) blog
* [Hands-On Web UI Testing](https://github.com/AndyLPK247/djangocon-2019-web-ui-testing) DjangoCon 2019 tutorial
* [Hands-On Web UI Testing](https://github.com/AndyLPK247/pyohio-2019-web-ui-testing) PyOhio 2019 tutorial
* [Test Automation University](https://testautomationu.applitools.com/) courses
  * [Web Element Locator Strategies](https://testautomationu.applitools.com/web-element-locator-strategies/)
  * [Behavior Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
