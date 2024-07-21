Feature: Strategic Insights
  @historical_data
  Scenario: User gains strategic insights from data
    Given a logged-in user in the "Growth Initiative" project with historical data
    When the user views the "Strategy" dashboard
    Then the system should display predictive analysis for all KPI metrics
    And show forecast vs. actual data for each KPI
    When the user sets a target to increase "Sales" by 20% in 6 months
    Then the system should display the target on the "Sales" chart
    And provide a timeline to achieve the "Sales" target
    And show the likelihood of achieving the "Sales" target based on predictive analysis
    When the user changes the "Sales" chart from line to bar type
    Then the chart type should update successfully