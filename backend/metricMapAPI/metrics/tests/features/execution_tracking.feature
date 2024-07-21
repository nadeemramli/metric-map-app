Feature: Execution Tracking
  Scenario: User tracks execution and inputs insights
    Given a logged-in user in the "Growth Initiative" project
    When the user adds an "Action Remark" for launching a new product on "2023-07-01"
    Then the "Action Remark" should be saved and visible on the timeline
    When the user inputs an "Insight" about increased social media engagement on "2023-07-15"
    Then the "Insight" should be saved and associated with relevant metrics
    When the user creates an "Experiment" to test a new marketing channel
    And sets the hypothesis, desired impact on "CAC", and timeline for the "Experiment"
    Then the "Experiment" should be saved successfully
    When the user views the "Execution" dashboard
    Then all "Action Remarks", "Insights", and "Experiments" should be visible on the timeline