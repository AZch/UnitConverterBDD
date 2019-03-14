import random
import string

from Converter import Converter
from behave import *
from hamcrest import assert_that, greater_than

use_step_matcher("re")


converter = None
name = None
quantities = None
names = None
quantitiesMult = None
countElem = 100

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
    if converter.getNames()[0] != "m" or len(converter.getNames()) != 1:
        raise NotImplementedError(
            u'STEP: Then I add a new value named \'m\'')
    if not isinstance(converter.getNames(), list) \
            or not isinstance(converter.getQuantities(), list):
        raise NotImplementedError(
            u'STEP: I  have 2 lists, one two-dimensional array')



@step("I have entered name 'km' as name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global name
    name = "km"
    #raise NotImplementedError(u'STEP: And I have entered name \'km\' as name')


@step("I have list Quantities with value 1000")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global quantities
    quantities = 1000
    #raise NotImplementedError(u'STEP: And I have list Quantities with value 1000')

@then(
    "I add to new value 'm' and 'km' and matrix quantities 2x2 \(elem\[0\]\[1\] == 0\.001, elem\[1\]\[0\] == 1000 and other one\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global converter
    if len(converter.getNames()) != 2 \
            or converter.getNames()[0] != 'm' \
            or converter.getNames()[1] != 'km':
        raise NotImplementedError(
            u'STEP: Then I add to new value \'m\' and \'km\'')

    if len(converter.getQuantities()) != 2 \
            or len(converter.getQuantities()[0]) != 2 \
            or len(converter.getQuantities()[1]) != 2:
        raise NotImplementedError(
            u'STEP: matrix quantities 2x2')

    if converter.getQuantities()[0][0] != 1 \
            or converter.getQuantities()[1][1] != 1 \
            or (converter.getQuantities()[0][1] <= 0.00099999 or converter.getQuantities()[0][1] >= 0.001111111111) \
            or (converter.getQuantities()[1][0] <= 999.99999999 or converter.getQuantities()[0][1] >= 1000.000001):
        raise NotImplementedError(
            u'STEP: elem[0][1] == 0.001, elem[1][0] == 1000 and other one')

def nameGenerator(sizeName=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(sizeName))

@step("I have list of names 'names'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global names
    global countElem
    names = []
    for i in range(countElem):
        names.append(nameGenerator())
    #raise NotImplementedError(u'STEP: And I have list of names \'names\'')


@step("I have two-demensional list of quateres 'quantitiesMult'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global countElem
    global quantitiesMult
    quantitiesMult = []
    #raise NotImplementedError(u'STEP: And I have two-demensional list of quateres \'quantitiesMult\'')


@when("I add in cycle 100 random names")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global countElem
    countElem = 100
    #raise NotImplementedError(u'STEP: When I add in cycle 100 random names')


@step(
    "add them in converter with generate list quantities for them \(size list for i not more current size quantities\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global countElem
    for i in range(countElem):
        converter.addQuantities(names[i], [random.randint(0, 100)] * (i + 1))
    #raise NotImplementedError(
    #    u'STEP: And add them in converter with generate list quantities for them (size list for i not more current size quantities)')


@then("have matrix with size 100x100")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global converter
    global countElem
    if len(converter.getQuantities()) != countElem:
        raise NotImplementedError(u'STEP: Then have matrix with size 100')
    for i in range(countElem):
        if len(converter.getQuantities()[i]) != countElem:
            raise NotImplementedError(u'STEP: Then have matrix with size 100x100')


@step("have matrix with subDiag have all 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    global countElem
    global converter
    for i in range(countElem):
        if converter.getQuantities()[i][i] != 1:
            raise NotImplementedError(u'STEP: And have matrix with subDiag have all 1')



@step("have matrix with elem under subDiag have i\(row\) \+ 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global countElem
    global converter
    for i in range(countElem):
        for j in range(countElem):
            if (i > j):
                if converter.getQuantities()[i][j] != i + 1:
                    raise NotImplementedError(u'STEP: And have matrix with elem under subDiag have i(row) + 1')


@step("have matrix with elem upper subDiag have 1 / \(i\(row\) \+ 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global countElem
    global converter
    for i in range(countElem):
        for j in range(countElem):
            if (i < j):
                if converter.getQuantities()[i][j] != i + 1:
                    raise NotImplementedError(u'STEP: And have matrix with elem upper subDiag have 1 / (i(row) + 1)')
