Feature: CheckValue

  Scenario: Run test check type value
    Given I have my software Converter
    When I have entered name 'm' as name
    And I have empty list Quantities
    And I press 'Add'
    Then I add a new value named 'm', I have 2 lists, one two-dimensional array, one will have 'm'

  Scenario: Add Two Quantities
    Given I have my software Converter
    When I have entered name 'm' as name
    And I have empty list Quantities
    And I press 'Add'
    And I have entered name 'km' as name
    And I have list Quantities with value 1000
    And I press 'Add'
    Then I add to new value 'm' and 'km' and matrix quantities 2x2 (elem[0][1] == 0.001, elem[1][0] == 1000)