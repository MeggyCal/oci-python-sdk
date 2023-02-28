# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecoveryServiceSubnetDetails(object):
    """
    Details of the Recovery Service Subnet.
    """

    #: A constant which can be used with the lifecycle_state property of a RecoveryServiceSubnetDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RecoveryServiceSubnetDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RecoveryServiceSubnetDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecoveryServiceSubnetDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RecoveryServiceSubnetDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a RecoveryServiceSubnetDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new RecoveryServiceSubnetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recovery_service_subnet_id:
            The value to assign to the recovery_service_subnet_id property of this RecoveryServiceSubnetDetails.
        :type recovery_service_subnet_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RecoveryServiceSubnetDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'recovery_service_subnet_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'recovery_service_subnet_id': 'recoveryServiceSubnetId',
            'lifecycle_state': 'lifecycleState'
        }

        self._recovery_service_subnet_id = None
        self._lifecycle_state = None

    @property
    def recovery_service_subnet_id(self):
        """
        **[Required]** Gets the recovery_service_subnet_id of this RecoveryServiceSubnetDetails.
        Recovery Service Subnet Identifier.


        :return: The recovery_service_subnet_id of this RecoveryServiceSubnetDetails.
        :rtype: str
        """
        return self._recovery_service_subnet_id

    @recovery_service_subnet_id.setter
    def recovery_service_subnet_id(self, recovery_service_subnet_id):
        """
        Sets the recovery_service_subnet_id of this RecoveryServiceSubnetDetails.
        Recovery Service Subnet Identifier.


        :param recovery_service_subnet_id: The recovery_service_subnet_id of this RecoveryServiceSubnetDetails.
        :type: str
        """
        self._recovery_service_subnet_id = recovery_service_subnet_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RecoveryServiceSubnetDetails.
        The current state of the Recovery Service Subnet.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RecoveryServiceSubnetDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RecoveryServiceSubnetDetails.
        The current state of the Recovery Service Subnet.


        :param lifecycle_state: The lifecycle_state of this RecoveryServiceSubnetDetails.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other