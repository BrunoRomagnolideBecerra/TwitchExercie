Feature: Twitch test using Chrome's mobile emulator

  Scenario: Twitch Scenario
    Given Access to a browser.
    When The user navigates to "Twitch".
    And The user searches "StarCraft II"
    And The user click the tab "Channels"
    And The user scrolls "down".
    And The user scrolls "down".
    And The user selects any streamer.
    Then A screenshot is taken and saved.
