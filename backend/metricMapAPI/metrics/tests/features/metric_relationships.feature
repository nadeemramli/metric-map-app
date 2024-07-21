Feature: Metric Relationships
  @historical_data
  Scenario: User analyzes relationships between metrics
    Given a logged-in user in the "Growth Initiative" project with historical data
    When the user views the metric relationship visualization
    Then the system should display a network graph of all metrics
    And show correlation coefficients between connected metrics
    When the user clicks on the connection between "CAC" and "Conversion Rate"
    Then the system should provide detailed insights on their relationship
    And suggest potential actions to optimize both metrics