# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SortKeyRule(object):
    """
    A rule to define the set of fields to sort by, and whether to sort by ascending or descending values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SortKeyRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wrapped_rule:
            The value to assign to the wrapped_rule property of this SortKeyRule.
        :type wrapped_rule: ProjectionRule

        :param is_ascending:
            The value to assign to the is_ascending property of this SortKeyRule.
        :type is_ascending: bool

        """
        self.swagger_types = {
            'wrapped_rule': 'ProjectionRule',
            'is_ascending': 'bool'
        }

        self.attribute_map = {
            'wrapped_rule': 'wrappedRule',
            'is_ascending': 'isAscending'
        }

        self._wrapped_rule = None
        self._is_ascending = None

    @property
    def wrapped_rule(self):
        """
        Gets the wrapped_rule of this SortKeyRule.

        :return: The wrapped_rule of this SortKeyRule.
        :rtype: ProjectionRule
        """
        return self._wrapped_rule

    @wrapped_rule.setter
    def wrapped_rule(self, wrapped_rule):
        """
        Sets the wrapped_rule of this SortKeyRule.

        :param wrapped_rule: The wrapped_rule of this SortKeyRule.
        :type: ProjectionRule
        """
        self._wrapped_rule = wrapped_rule

    @property
    def is_ascending(self):
        """
        Gets the is_ascending of this SortKeyRule.
        Specifies if the sort key has ascending order.


        :return: The is_ascending of this SortKeyRule.
        :rtype: bool
        """
        return self._is_ascending

    @is_ascending.setter
    def is_ascending(self, is_ascending):
        """
        Sets the is_ascending of this SortKeyRule.
        Specifies if the sort key has ascending order.


        :param is_ascending: The is_ascending of this SortKeyRule.
        :type: bool
        """
        self._is_ascending = is_ascending

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other