
# Twitch exercise

This exercise uses Behave (cucumber for python), selenium and python.

Additional to this, the library "expects" is used to evaluate results (https://pypi.org/project/expects/)

The framework follows page-object-model pattern in order to represent each web page as a "page" (class), and a pageFactory class is implemented in order to instantiate classes dinamicaly and assign it to the context, which is empty when a test starts.

There is a BasePage class with commonly used functions that is inherited by other classes.

In the environment file the driver is initiated in a fixture that is called by a before_scenario block to have a clean singleton context for each test.

A yaml config file is used to allocate URL, user/pass.

Test are orgnized in .feature files.
Steps are organized by pageName_steps.py for the sake of organization.
Pages are single class files named as the web page they represent, and the class is also named as the web page it represents.

MyWebPage.feature > myWebPage_steps.py > myWebPage.py (class MyWebPage)

/config
  config_file.yaml
/features
    /steps
      common_steps.py
      MyWebPage_steps.py
      pageName2_steps.py
      pageName3_steps.py
  environment.py
  MyWebPage.feature
  pageName2.feature
  pageName3.feature
/pages
  base_page.py
  MyWebPage.py
  pageName2.py
  pageName3.py

Execute "behave" at root to run tests.
