Feature: User Authentication
  Scenario: User logs in to the application
    Given a user with valid credentials
    When the user attempts to log in
    Then the user should be successfully logged in