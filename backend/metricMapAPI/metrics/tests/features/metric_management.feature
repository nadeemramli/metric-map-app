Feature: Metric Management
  Scenario: User manages metrics and their properties
    Given a logged-in user in the "Growth Initiative" project
    When the user creates a new metric "CAC" of type "KPI" with value type "currency"
    Then the metric "CAC" should be saved successfully
    When the user creates a category "Financial" and assigns "CAC" to it
    Then the category assignment should be saved successfully
    When the user adds a tag "Q3 Focus" to the "CAC" metric
    Then the tag should be saved and associated with "CAC"
    When the user sets a target of 50 for "CAC" to be achieved by "2023-12-31"
    Then the target should be saved successfully for "CAC"
    When the user inputs historical data for "CAC" from "2023-01-01" to "2023-06-30"
    Then the historical data should be saved successfully for "CAC"
    When the user defines a connection between "CAC" and "Conversion Rate" with correlation -0.8
    Then the connection should be saved successfully

  Scenario: User manages multiple metrics
    Given a logged-in user in the "Growth Initiative" project
    When the user creates the following metrics:
      | name              | type         | value_type |
      | Conversion Rate   | KPI          | percentage |
      | Lead Registration | Input Metric | number     |
      | Sales             | Output Metric| currency   |
      | Customer LTV      | North Star   | currency   |
    Then all metrics should be saved successfully