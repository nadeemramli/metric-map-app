Feature: Stakeholder Views
  @historical_data
  Scenario: Different stakeholders view relevant information
    Given a logged-in user with roles "CEO" and "Marketing Manager"
    And a "Growth Initiative" project with historical data
    When the user views the dashboard as "CEO"
    Then the dashboard should show high-level KPIs across all projects
    And highlight underperforming metrics
    When the user switches to "Marketing Manager" role
    Then the dashboard should focus on marketing-related metrics
    And show detailed trends for "CAC" and "Conversion Rate"
    When the user drills down into the underperforming "CAC" metric
    Then the system should provide a detailed analysis of "CAC"
    And suggest potential actions to improve "CAC"