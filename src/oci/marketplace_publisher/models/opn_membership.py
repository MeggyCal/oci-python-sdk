# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpnMembership(object):
    """
    OPN membership information
    """

    #: A constant which can be used with the opn_status property of a OpnMembership.
    #: This constant has a value of "ACTIVE"
    OPN_STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the opn_status property of a OpnMembership.
    #: This constant has a value of "INACTIVE"
    OPN_STATUS_INACTIVE = "INACTIVE"

    #: A constant which can be used with the opn_status property of a OpnMembership.
    #: This constant has a value of "RENEWAL_IN_PROGRESS"
    OPN_STATUS_RENEWAL_IN_PROGRESS = "RENEWAL_IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new OpnMembership object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_start:
            The value to assign to the time_start property of this OpnMembership.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this OpnMembership.
        :type time_end: datetime

        :param opn_status:
            The value to assign to the opn_status property of this OpnMembership.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "RENEWAL_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type opn_status: str

        :param opn_number:
            The value to assign to the opn_number property of this OpnMembership.
        :type opn_number: str

        :param opn_membership_type:
            The value to assign to the opn_membership_type property of this OpnMembership.
        :type opn_membership_type: str

        """
        self.swagger_types = {
            'time_start': 'datetime',
            'time_end': 'datetime',
            'opn_status': 'str',
            'opn_number': 'str',
            'opn_membership_type': 'str'
        }

        self.attribute_map = {
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'opn_status': 'opnStatus',
            'opn_number': 'opnNumber',
            'opn_membership_type': 'opnMembershipType'
        }

        self._time_start = None
        self._time_end = None
        self._opn_status = None
        self._opn_number = None
        self._opn_membership_type = None

    @property
    def time_start(self):
        """
        Gets the time_start of this OpnMembership.
        OPN membership start date. An RFC3339 formatted datetime string


        :return: The time_start of this OpnMembership.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this OpnMembership.
        OPN membership start date. An RFC3339 formatted datetime string


        :param time_start: The time_start of this OpnMembership.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this OpnMembership.
        OPN membership end date. An RFC3339 formatted datetime string


        :return: The time_end of this OpnMembership.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this OpnMembership.
        OPN membership end date. An RFC3339 formatted datetime string


        :param time_end: The time_end of this OpnMembership.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def opn_status(self):
        """
        Gets the opn_status of this OpnMembership.
        OPN status

        Allowed values for this property are: "ACTIVE", "INACTIVE", "RENEWAL_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The opn_status of this OpnMembership.
        :rtype: str
        """
        return self._opn_status

    @opn_status.setter
    def opn_status(self, opn_status):
        """
        Sets the opn_status of this OpnMembership.
        OPN status


        :param opn_status: The opn_status of this OpnMembership.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "RENEWAL_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(opn_status, allowed_values):
            opn_status = 'UNKNOWN_ENUM_VALUE'
        self._opn_status = opn_status

    @property
    def opn_number(self):
        """
        Gets the opn_number of this OpnMembership.
        OPN Number number


        :return: The opn_number of this OpnMembership.
        :rtype: str
        """
        return self._opn_number

    @opn_number.setter
    def opn_number(self, opn_number):
        """
        Sets the opn_number of this OpnMembership.
        OPN Number number


        :param opn_number: The opn_number of this OpnMembership.
        :type: str
        """
        self._opn_number = opn_number

    @property
    def opn_membership_type(self):
        """
        Gets the opn_membership_type of this OpnMembership.
        OPN membership type


        :return: The opn_membership_type of this OpnMembership.
        :rtype: str
        """
        return self._opn_membership_type

    @opn_membership_type.setter
    def opn_membership_type(self, opn_membership_type):
        """
        Sets the opn_membership_type of this OpnMembership.
        OPN membership type


        :param opn_membership_type: The opn_membership_type of this OpnMembership.
        :type: str
        """
        self._opn_membership_type = opn_membership_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other