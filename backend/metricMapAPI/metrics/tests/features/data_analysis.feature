Feature: Data Analysis
  @historical_data
  Scenario: User analyzes metric performance
    Given a logged-in user in the "Growth Initiative" project with historical data
    When the user views the "CAC" metric
    Then the system should display the "CAC" trend over time
    And the system should highlight any anomalies in "CAC"
    When the user compares "CAC" with "Conversion Rate"
    Then the system should show the correlation between "CAC" and "Conversion Rate"
    And provide insights on how changes in "Conversion Rate" affect "CAC"
    When the user runs a what-if scenario decreasing "CAC" by 10%
    Then the system should simulate the impact on "Conversion Rate" and "Sales"