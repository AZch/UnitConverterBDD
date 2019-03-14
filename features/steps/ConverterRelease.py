from Converter import Converter
from behave import *
from hamcrest import assert_that, greater_than

use_step_matcher("re")


converter = None
name = None
quantities = None

@given("I have my software Converter")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global converter
    converter = Converter()
    #raise NotImplementedError(u'STEP: Given I have my software Converter')


@when("I have entered name 'm' as name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global name
    name = 'm'
    #raise NotImplementedError(u'STEP: When I have entered name \'m\' as name')


@step("I have empty list Quantities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global quantities
    quantities = []
    #raise NotImplementedError(u'STEP: And I have empty list Quantities')


@step("I press 'Add'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    converter.addQuantities(name, quantities)
    print(converter.getNames()[0])
    #raise NotImplementedError(u'STEP: And I press \'Add\'')


@then("I add a new value named 'm', I have 2 lists, one two-dimensional array, one will have 'm'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global converter
    if converter.getNames()[0] != "m" \
            or not isinstance(converter.getNames(), list) \
            or not isinstance(converter.getQuantities(), list) \
            or len(converter.getNames()) != 1:
        raise NotImplementedError(
            u'STEP: Then I add a new value named \'m\', I  have 2 lists, one two-dimensional array, one will have \'m\'')


@step("I have entered name 'km' as name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I have entered name \'km\' as name')


@step("I have list Quantities with value 1000")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I have list Quantities with value 1000')


@then("I add to new value 'm' and 'km' and matrix quantities 2x2 \(elem\[0\]\[1\] == 0\.001, elem\[1\]\[0\] == 1000\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I add to new value \'m\' and \'km\' and matrix quantities 2x2 (elem[0][1] == 0.001, elem[1][0] == 1000)')