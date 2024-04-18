# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoKeyRotationDetails(object):
    """
    The details of auto rotation schedule for the Key being create updated or imported.
    """

    #: A constant which can be used with the last_rotation_status property of a AutoKeyRotationDetails.
    #: This constant has a value of "SUCCESS"
    LAST_ROTATION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the last_rotation_status property of a AutoKeyRotationDetails.
    #: This constant has a value of "FAILED"
    LAST_ROTATION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the last_rotation_status property of a AutoKeyRotationDetails.
    #: This constant has a value of "IN_PROGRESS"
    LAST_ROTATION_STATUS_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoKeyRotationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rotation_interval_in_days:
            The value to assign to the rotation_interval_in_days property of this AutoKeyRotationDetails.
        :type rotation_interval_in_days: int

        :param time_of_schedule_start:
            The value to assign to the time_of_schedule_start property of this AutoKeyRotationDetails.
        :type time_of_schedule_start: datetime

        :param time_of_next_rotation:
            The value to assign to the time_of_next_rotation property of this AutoKeyRotationDetails.
        :type time_of_next_rotation: datetime

        :param time_of_last_rotation:
            The value to assign to the time_of_last_rotation property of this AutoKeyRotationDetails.
        :type time_of_last_rotation: datetime

        :param last_rotation_status:
            The value to assign to the last_rotation_status property of this AutoKeyRotationDetails.
            Allowed values for this property are: "SUCCESS", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_rotation_status: str

        :param last_rotation_message:
            The value to assign to the last_rotation_message property of this AutoKeyRotationDetails.
        :type last_rotation_message: str

        """
        self.swagger_types = {
            'rotation_interval_in_days': 'int',
            'time_of_schedule_start': 'datetime',
            'time_of_next_rotation': 'datetime',
            'time_of_last_rotation': 'datetime',
            'last_rotation_status': 'str',
            'last_rotation_message': 'str'
        }

        self.attribute_map = {
            'rotation_interval_in_days': 'rotationIntervalInDays',
            'time_of_schedule_start': 'timeOfScheduleStart',
            'time_of_next_rotation': 'timeOfNextRotation',
            'time_of_last_rotation': 'timeOfLastRotation',
            'last_rotation_status': 'lastRotationStatus',
            'last_rotation_message': 'lastRotationMessage'
        }

        self._rotation_interval_in_days = None
        self._time_of_schedule_start = None
        self._time_of_next_rotation = None
        self._time_of_last_rotation = None
        self._last_rotation_status = None
        self._last_rotation_message = None

    @property
    def rotation_interval_in_days(self):
        """
        Gets the rotation_interval_in_days of this AutoKeyRotationDetails.
        The interval of auto key rotation. For auto key rotation the interval should between 30 day and 365 days (1 year)


        :return: The rotation_interval_in_days of this AutoKeyRotationDetails.
        :rtype: int
        """
        return self._rotation_interval_in_days

    @rotation_interval_in_days.setter
    def rotation_interval_in_days(self, rotation_interval_in_days):
        """
        Sets the rotation_interval_in_days of this AutoKeyRotationDetails.
        The interval of auto key rotation. For auto key rotation the interval should between 30 day and 365 days (1 year)


        :param rotation_interval_in_days: The rotation_interval_in_days of this AutoKeyRotationDetails.
        :type: int
        """
        self._rotation_interval_in_days = rotation_interval_in_days

    @property
    def time_of_schedule_start(self):
        """
        Gets the time_of_schedule_start of this AutoKeyRotationDetails.
        A property indicating  scheduled start date expressed as date YYYY-MM-DD String. Example: `2023-04-04T00:00:00Z` .


        :return: The time_of_schedule_start of this AutoKeyRotationDetails.
        :rtype: datetime
        """
        return self._time_of_schedule_start

    @time_of_schedule_start.setter
    def time_of_schedule_start(self, time_of_schedule_start):
        """
        Sets the time_of_schedule_start of this AutoKeyRotationDetails.
        A property indicating  scheduled start date expressed as date YYYY-MM-DD String. Example: `2023-04-04T00:00:00Z` .


        :param time_of_schedule_start: The time_of_schedule_start of this AutoKeyRotationDetails.
        :type: datetime
        """
        self._time_of_schedule_start = time_of_schedule_start

    @property
    def time_of_next_rotation(self):
        """
        Gets the time_of_next_rotation of this AutoKeyRotationDetails.
        A property indicating Next estimated scheduled Time, as per the interval, expressed as date YYYY-MM-DD String. Example: `2023-04-04T00:00:00Z` .


        :return: The time_of_next_rotation of this AutoKeyRotationDetails.
        :rtype: datetime
        """
        return self._time_of_next_rotation

    @time_of_next_rotation.setter
    def time_of_next_rotation(self, time_of_next_rotation):
        """
        Sets the time_of_next_rotation of this AutoKeyRotationDetails.
        A property indicating Next estimated scheduled Time, as per the interval, expressed as date YYYY-MM-DD String. Example: `2023-04-04T00:00:00Z` .


        :param time_of_next_rotation: The time_of_next_rotation of this AutoKeyRotationDetails.
        :type: datetime
        """
        self._time_of_next_rotation = time_of_next_rotation

    @property
    def time_of_last_rotation(self):
        """
        Gets the time_of_last_rotation of this AutoKeyRotationDetails.
        A  property indicating Last rotation Date Example: `2023-04-04T00:00:00Z`.


        :return: The time_of_last_rotation of this AutoKeyRotationDetails.
        :rtype: datetime
        """
        return self._time_of_last_rotation

    @time_of_last_rotation.setter
    def time_of_last_rotation(self, time_of_last_rotation):
        """
        Sets the time_of_last_rotation of this AutoKeyRotationDetails.
        A  property indicating Last rotation Date Example: `2023-04-04T00:00:00Z`.


        :param time_of_last_rotation: The time_of_last_rotation of this AutoKeyRotationDetails.
        :type: datetime
        """
        self._time_of_last_rotation = time_of_last_rotation

    @property
    def last_rotation_status(self):
        """
        Gets the last_rotation_status of this AutoKeyRotationDetails.
        The status of last execution of auto key rotation.

        Allowed values for this property are: "SUCCESS", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_rotation_status of this AutoKeyRotationDetails.
        :rtype: str
        """
        return self._last_rotation_status

    @last_rotation_status.setter
    def last_rotation_status(self, last_rotation_status):
        """
        Sets the last_rotation_status of this AutoKeyRotationDetails.
        The status of last execution of auto key rotation.


        :param last_rotation_status: The last_rotation_status of this AutoKeyRotationDetails.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(last_rotation_status, allowed_values):
            last_rotation_status = 'UNKNOWN_ENUM_VALUE'
        self._last_rotation_status = last_rotation_status

    @property
    def last_rotation_message(self):
        """
        Gets the last_rotation_message of this AutoKeyRotationDetails.
        The last execution status message.


        :return: The last_rotation_message of this AutoKeyRotationDetails.
        :rtype: str
        """
        return self._last_rotation_message

    @last_rotation_message.setter
    def last_rotation_message(self, last_rotation_message):
        """
        Sets the last_rotation_message of this AutoKeyRotationDetails.
        The last execution status message.


        :param last_rotation_message: The last_rotation_message of this AutoKeyRotationDetails.
        :type: str
        """
        self._last_rotation_message = last_rotation_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other