'''
Created on Oct 6, 2013

@author: ezulkosk
'''
from common import Common
from test import i188sumquantifier, multiple_joins, bracketedconstraint_this, \
    this_dot_parent, arithmetic, relations, boolean_connectives, union, \
    simple_abstract, some, simple_set, integer_refs, higher_inheritance, \
    this_integer_relation, equal_references, all_alls, all_threes, zoo, \
    books_tutorial, check_unique_ref_names_with_inheritance, constraints, \
    enforcingInverseReferences, i101, i10, i121comments, i122CVL, i126empty, \
    i131incorrectscope, i137_parsing, i147refdisambiguation, i14, i17, i18, i19, \
    i205refdisambiguationII, i23, i40_integers_strings_assignment, i40textequality, \
    i49_parentReduce, i49_resolve_ancestor, i50_stop_following_references, i55, \
    i57navParent, i61cardinalities, i70, i71, i72sharedreference, \
    i78_transitiveclosure, i83individualscope, i98_toplevelreferences, layout, \
    negative, paths, personRelatives, person_tutorial, resolution, simp, \
    subtypingprimitivetypes, telematics, test_neg_typesystem, simple_books, \
    one_plus_one_equals_one, scope_test


'''
========
| TODO |
========
* Scopes
* Fix any ops left in Operations
* Int refs.
* Real Numbers
* Change my_type to exptype
* Traversal of quantified formulas is exponential...
* Improve support for debugging constraints
* Fix quantifier symmetry breaker, if two locals FROM THE SAME QUANTIFIER are on the left and right of a func, not symmetric
* Documentation
* Change DoubleLiteral to RealLiteral, since that is most likely the Z3 construct that will be used.
'''


GLOBAL_SCOPE = 4#this obviously has to change

MODE = Common.ALL # Common.[EXPERIMENT | MODELSTATS | NORMAL | DEBUG | TEST | ONE | ALL], where ONE outputs one model from each test
PRINT_CONSTRAINTS = False
NUM_INSTANCES = 10 # -1 to produce all instances
INFINITE = -1 #best variable name.
PROFILING = True # True to output the translation time, and time to get first model
CPROFILING = False #invokes the standard python profiling method (see Z3Run.py)
GET_ISOMORPHISM_CONSTRAINT = False #efficiency bugs in quantified formulas is preventing this from working
BREAK_QUANTIFIER_SYMMETRY = False
EXTEND_ABSTRACT_SCOPES = True

MY_TESTS = 1 # my tests from debugging
POSITIVE_TESTS = 2 # tests from test/positive in the Clafer repository
TEST_SET = MY_TESTS 

#MODULE = bracketedconstraint_this.getModule()
#MODULE = multiple_joins.getModule()
#MODULE = this_dot_parent.getModule()
#MODULE = arithmetic.getModule()
#MODULE = relations.getModule()
#MODULE = boolean_connectives.getModule()
#MODULE = union.getModule()
#MODULE = simple_abstract.getModule()
#MODULE = some.getModule()
#MODULE = simple_set.getModule()
#MODULE = zoo.getModule()
#MODULE = simple_zoo.getModule()
#MODULE = integer_refs.getModule()
#MODULE = minimal_integer_refs.getModule()
#MODULE = phone_feature_model.getModule()
#MODULE = higher_inheritance.getModule()
#MODULE = this_integer_relation.getModule()
MODULE = equal_references.getModule()
#MODULE = dag_test.getModule()
#MODULE = books_tutorial.getModule()
#MODULE = simple_books.getModule()
#MODULE = subbooks.getModule()
#MODULE = int_ref_set.getModule()
#MODULE = one_plus_one_equals_one.getModule()
#MODULE = iso.getModule()
#MODULE = isowithcons.getModule()
#MODULE = all_alls.getModule()
#MODULE = some_somes.getModule()
#MODULE = constraints.getModule()
#MODULE = constraintswithbounds.getModule()
#MODULE = AADL_simplified_with_lists.getModule()
#MODULE = all_threes.getModule()
#MODULE = i101.getModule()
#MODULE = top_level_constraints_with_relational_joins.getModule()
#MODULE = telematics.getModule()
#MODULE = i17.getModule()
#MODULE = i188sumquantifier.getModule()
#MODULE = i78_transitiveclosure.getModule()
#MODULE = scope_test.getModule()
#MODULE = i131incorrectscope.getModule()

my_tests = [ 
          (multiple_joins, 1),
          (bracketedconstraint_this, 6),
          (this_dot_parent, 2),
          (arithmetic, 2),
          (relations, 1),
          (boolean_connectives, 1),
          (union, 6),
          (simple_abstract, 0),
          (some, 1),
          (simple_set, 6),
          (integer_refs, 1),
          (higher_inheritance, 1),
          (this_integer_relation, 2),
          (equal_references, 2),
          (all_alls, 1),
          (all_threes, 1),
          (zoo, INFINITE)
         ]

positive_tests = [
        (books_tutorial, 1),
        (check_unique_ref_names_with_inheritance, 1),
        (constraints, 1),
        (enforcingInverseReferences, 1),
        (i101, 1),
        (i10, 1),
        (i121comments, 1),
        (i122CVL, 1),
        (i126empty, 1),
        (i131incorrectscope, 1),
        (i137_parsing, 1),
        (i147refdisambiguation, 1),
        (i14, 1),
        (i17, 1),
        (i188sumquantifier, 1),
        (i18, 1),
        (i19, 1),
        (i205refdisambiguationII, 1),
        (i23, 1),
        (i40_integers_strings_assignment, 1),
        (i40textequality, 1),
        (i49_parentReduce, 1),
        (i49_resolve_ancestor, 1),
        (i50_stop_following_references, 1),
        (i55, 1),
        (i57navParent, 1),
        (i61cardinalities, 1),
        (i70, 1),
        (i71, 1),
        (i72sharedreference, 1),
        (i78_transitiveclosure, 1),
        (i83individualscope, 1),
        (i98_toplevelreferences, 1),
        (layout, 1),
        (negative, 1),
        (paths, 1),
        (personRelatives, 1),
        (person_tutorial, 1),
        (resolution, 1),
        (simp, 1),
        (subtypingprimitivetypes, 1),
        (telematics, 1),
        (test_neg_typesystem, 1)
                  ]



