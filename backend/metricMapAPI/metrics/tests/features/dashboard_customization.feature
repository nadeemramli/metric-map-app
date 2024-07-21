Feature: Dashboard Customization
  Scenario: User customizes and generates reports
    Given a logged-in user in the "Growth Initiative" project
    When the user creates a new dashboard "Executive Summary"
    And adds "CAC", "Conversion Rate", and "Sales" metrics to the dashboard
    And arranges the metrics in a custom layout
    Then the dashboard "Executive Summary" should be saved successfully
    When the user generates a report from the "Executive Summary" dashboard
    Then the report should be generated successfully with all included metrics