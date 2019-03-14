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
    Then I add to new value 'm' and 'km' and matrix quantities 2x2 (elem[0][1] == 0.001, elem[1][0] == 1000 and other one)

  Scenario: Add 100 Quantities
    Given I have my software Converter
    And I have list of names 'names'
    And I have two-demensional list of quateres 'quantitiesMult'
    When I add in cycle 100 random names
    And add them in converter with generate list quantities for them (size list for i not more current size quantities)
    Then have matrix with size 100x100
    And have matrix with elem under subDiag have i(row) + 1
    And have matrix with subDiag have all 1
    And have matrix with elem upper subDiag have 1 / (i(row) + 1)