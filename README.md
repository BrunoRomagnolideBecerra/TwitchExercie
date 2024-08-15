
# Twitch exercise

This exercise uses Behave (cucumber for python), selenium and python.

Additional to this, the library "expects" is used to evaluate results (https://pypi.org/project/expects/)

The framework follows page-object-model pattern in order to represent each web page as a class, and a page factory class is implemented in order to instantiate each class dinamicaly and assign it to the context, which is empty when a test starts.

There is a BasePage class with commonly used functions that is inherited by other classes.

Each page is its own class (in this case only the page Twitch exists).

In the environment file, the driver is initiated in a fixture that is called by a before_scenario block to have a clean singleton context for each test.

When each "Scenario" runs, the before_scenario initiates a browse in mobile mode, then the engine runs each step in the scenario, creating an instance of the corresponding class and assigning it to "context.page" to be used in all the steps.

This allows the steps to call functions as context.page.function_name() regardless of the actual class name, allowing for steps to be reused endlessly in any tests, as many times needed; and for classes/pages to have functions tailored for tis web page (if needed).

A yaml config file is used to allocate URL, user/pass.

Execute "behave" at root to run the test.
