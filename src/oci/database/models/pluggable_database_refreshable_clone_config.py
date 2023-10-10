# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PluggableDatabaseRefreshableCloneConfig(object):
    """
    Pluggable Database Refreshable Clone Configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PluggableDatabaseRefreshableCloneConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_refreshable_clone:
            The value to assign to the is_refreshable_clone property of this PluggableDatabaseRefreshableCloneConfig.
        :type is_refreshable_clone: bool

        """
        self.swagger_types = {
            'is_refreshable_clone': 'bool'
        }

        self.attribute_map = {
            'is_refreshable_clone': 'isRefreshableClone'
        }

        self._is_refreshable_clone = None

    @property
    def is_refreshable_clone(self):
        """
        Gets the is_refreshable_clone of this PluggableDatabaseRefreshableCloneConfig.
        Indicates whether the Pluggable Database is a refreshable clone.


        :return: The is_refreshable_clone of this PluggableDatabaseRefreshableCloneConfig.
        :rtype: bool
        """
        return self._is_refreshable_clone

    @is_refreshable_clone.setter
    def is_refreshable_clone(self, is_refreshable_clone):
        """
        Sets the is_refreshable_clone of this PluggableDatabaseRefreshableCloneConfig.
        Indicates whether the Pluggable Database is a refreshable clone.


        :param is_refreshable_clone: The is_refreshable_clone of this PluggableDatabaseRefreshableCloneConfig.
        :type: bool
        """
        self._is_refreshable_clone = is_refreshable_clone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other