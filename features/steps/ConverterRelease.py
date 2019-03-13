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
    name = 'm'
    #raise NotImplementedError(u'STEP: When I have entered name \'m\' as name')


@step("I have empty list Quantities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
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


