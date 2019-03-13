Feature: CheckValue

  Scenario: Run test check type value
    Given I have my software Converter
    When I have entered name 'm' as name
    And I have empty list Quantities
    And I press 'Add'
    Then I add a new value named 'm', I have 2 lists, one two-dimensional array, one will have 'm'