Feature: Project Management
  Scenario: User creates and switches projects
    Given a logged-in user
    When the user creates a new project called "Growth Initiative"
    Then the project "Growth Initiative" should be saved successfully
    When the user switches to the "Growth Initiative" project
    Then the active project should be updated to "Growth Initiative"