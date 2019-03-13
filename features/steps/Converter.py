from behave import *

use_step_matcher("re")


@step("I have empty list Quantities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I have empty list Quantities')