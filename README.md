
# Twitch exercise

This exercise uses Behave (cucumber for python), selenium and python.

Additional to this, the library "expects" is used to evaluate results (https://pypi.org/project/expects/)

The framework follows page-object-model pattern in order to represent each web page as a "page" (class), and a pageFactory class is implemented in order to instantiate classes dinamicaly and assign it to the context, which is empty when a test starts.

There is a BasePage class with commonly used functions that is inherited by other classes.

In the environment file the driver is initiated in a fixture that is called by a before_scenario block to have a clean singleton context for each test.

A yaml file is used to allocate environment credentials.

- Test are organized in .feature files.
- Steps are organized by pageName_steps.py to have small manageable files instead of a single monolithic file.
- Pages are single class files named as the web page they represent, and the class is also named as the web page it represents.

#### MyWebPage.feature > myWebPage_steps.py > myWebPage.py (class MyWebPage)

- /config 
  - env_credentials.yaml 
- /features 
  - /steps  
    - twitch_steps.py
  - environment.py 
  - twitch_test.feature
- /pages 
  - base_page.py 
  - twitch.py
- /tools
  - credentials.py
  - helpers.py
  - page_factory.py
  - 
Execute "behave" at root to run tests.