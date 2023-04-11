# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbRecommendationAggregation(object):
    """
    Summarizes a specific ADDM recommendation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbRecommendationAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AddmDbRecommendationAggregation.
        :type id: str

        :param type:
            The value to assign to the type property of this AddmDbRecommendationAggregation.
        :type type: str

        :param message:
            The value to assign to the message property of this AddmDbRecommendationAggregation.
        :type message: str

        :param requires_db_restart:
            The value to assign to the requires_db_restart property of this AddmDbRecommendationAggregation.
        :type requires_db_restart: str

        :param implement_actions:
            The value to assign to the implement_actions property of this AddmDbRecommendationAggregation.
        :type implement_actions: list[str]

        :param rationale:
            The value to assign to the rationale property of this AddmDbRecommendationAggregation.
        :type rationale: str

        :param max_benefit_percent:
            The value to assign to the max_benefit_percent property of this AddmDbRecommendationAggregation.
        :type max_benefit_percent: float

        :param overall_benefit_percent:
            The value to assign to the overall_benefit_percent property of this AddmDbRecommendationAggregation.
        :type overall_benefit_percent: float

        :param max_benefit_avg_active_sessions:
            The value to assign to the max_benefit_avg_active_sessions property of this AddmDbRecommendationAggregation.
        :type max_benefit_avg_active_sessions: float

        :param frequency_count:
            The value to assign to the frequency_count property of this AddmDbRecommendationAggregation.
        :type frequency_count: int

        :param related_object:
            The value to assign to the related_object property of this AddmDbRecommendationAggregation.
        :type related_object: oci.opsi.models.RelatedObjectTypeDetails

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'message': 'str',
            'requires_db_restart': 'str',
            'implement_actions': 'list[str]',
            'rationale': 'str',
            'max_benefit_percent': 'float',
            'overall_benefit_percent': 'float',
            'max_benefit_avg_active_sessions': 'float',
            'frequency_count': 'int',
            'related_object': 'RelatedObjectTypeDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'message': 'message',
            'requires_db_restart': 'requiresDbRestart',
            'implement_actions': 'implementActions',
            'rationale': 'rationale',
            'max_benefit_percent': 'maxBenefitPercent',
            'overall_benefit_percent': 'overallBenefitPercent',
            'max_benefit_avg_active_sessions': 'maxBenefitAvgActiveSessions',
            'frequency_count': 'frequencyCount',
            'related_object': 'relatedObject'
        }

        self._id = None
        self._type = None
        self._message = None
        self._requires_db_restart = None
        self._implement_actions = None
        self._rationale = None
        self._max_benefit_percent = None
        self._overall_benefit_percent = None
        self._max_benefit_avg_active_sessions = None
        self._frequency_count = None
        self._related_object = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AddmDbRecommendationAggregation.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AddmDbRecommendationAggregation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddmDbRecommendationAggregation.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AddmDbRecommendationAggregation.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this AddmDbRecommendationAggregation.
        Type of recommendation


        :return: The type of this AddmDbRecommendationAggregation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AddmDbRecommendationAggregation.
        Type of recommendation


        :param type: The type of this AddmDbRecommendationAggregation.
        :type: str
        """
        self._type = type

    @property
    def message(self):
        """
        **[Required]** Gets the message of this AddmDbRecommendationAggregation.
        Recommendation message


        :return: The message of this AddmDbRecommendationAggregation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AddmDbRecommendationAggregation.
        Recommendation message


        :param message: The message of this AddmDbRecommendationAggregation.
        :type: str
        """
        self._message = message

    @property
    def requires_db_restart(self):
        """
        Gets the requires_db_restart of this AddmDbRecommendationAggregation.
        Indicates implementation of the recommended action requires a database restart in order for it
        to take effect. Possible values \"Y\", \"N\" and null.


        :return: The requires_db_restart of this AddmDbRecommendationAggregation.
        :rtype: str
        """
        return self._requires_db_restart

    @requires_db_restart.setter
    def requires_db_restart(self, requires_db_restart):
        """
        Sets the requires_db_restart of this AddmDbRecommendationAggregation.
        Indicates implementation of the recommended action requires a database restart in order for it
        to take effect. Possible values \"Y\", \"N\" and null.


        :param requires_db_restart: The requires_db_restart of this AddmDbRecommendationAggregation.
        :type: str
        """
        self._requires_db_restart = requires_db_restart

    @property
    def implement_actions(self):
        """
        Gets the implement_actions of this AddmDbRecommendationAggregation.
        Actions that can be performed to implement the recommendation (such as 'ALTER PARAMETER',
        'RUN SQL TUNING ADVISOR')


        :return: The implement_actions of this AddmDbRecommendationAggregation.
        :rtype: list[str]
        """
        return self._implement_actions

    @implement_actions.setter
    def implement_actions(self, implement_actions):
        """
        Sets the implement_actions of this AddmDbRecommendationAggregation.
        Actions that can be performed to implement the recommendation (such as 'ALTER PARAMETER',
        'RUN SQL TUNING ADVISOR')


        :param implement_actions: The implement_actions of this AddmDbRecommendationAggregation.
        :type: list[str]
        """
        self._implement_actions = implement_actions

    @property
    def rationale(self):
        """
        Gets the rationale of this AddmDbRecommendationAggregation.
        Recommendation message


        :return: The rationale of this AddmDbRecommendationAggregation.
        :rtype: str
        """
        return self._rationale

    @rationale.setter
    def rationale(self, rationale):
        """
        Sets the rationale of this AddmDbRecommendationAggregation.
        Recommendation message


        :param rationale: The rationale of this AddmDbRecommendationAggregation.
        :type: str
        """
        self._rationale = rationale

    @property
    def max_benefit_percent(self):
        """
        Gets the max_benefit_percent of this AddmDbRecommendationAggregation.
        Maximum estimated benefit in terms of percentage of total activity


        :return: The max_benefit_percent of this AddmDbRecommendationAggregation.
        :rtype: float
        """
        return self._max_benefit_percent

    @max_benefit_percent.setter
    def max_benefit_percent(self, max_benefit_percent):
        """
        Sets the max_benefit_percent of this AddmDbRecommendationAggregation.
        Maximum estimated benefit in terms of percentage of total activity


        :param max_benefit_percent: The max_benefit_percent of this AddmDbRecommendationAggregation.
        :type: float
        """
        self._max_benefit_percent = max_benefit_percent

    @property
    def overall_benefit_percent(self):
        """
        Gets the overall_benefit_percent of this AddmDbRecommendationAggregation.
        Overall estimated benefit in terms of percentage of total activity


        :return: The overall_benefit_percent of this AddmDbRecommendationAggregation.
        :rtype: float
        """
        return self._overall_benefit_percent

    @overall_benefit_percent.setter
    def overall_benefit_percent(self, overall_benefit_percent):
        """
        Sets the overall_benefit_percent of this AddmDbRecommendationAggregation.
        Overall estimated benefit in terms of percentage of total activity


        :param overall_benefit_percent: The overall_benefit_percent of this AddmDbRecommendationAggregation.
        :type: float
        """
        self._overall_benefit_percent = overall_benefit_percent

    @property
    def max_benefit_avg_active_sessions(self):
        """
        Gets the max_benefit_avg_active_sessions of this AddmDbRecommendationAggregation.
        Maximum estimated benefit in terms of average active sessions


        :return: The max_benefit_avg_active_sessions of this AddmDbRecommendationAggregation.
        :rtype: float
        """
        return self._max_benefit_avg_active_sessions

    @max_benefit_avg_active_sessions.setter
    def max_benefit_avg_active_sessions(self, max_benefit_avg_active_sessions):
        """
        Sets the max_benefit_avg_active_sessions of this AddmDbRecommendationAggregation.
        Maximum estimated benefit in terms of average active sessions


        :param max_benefit_avg_active_sessions: The max_benefit_avg_active_sessions of this AddmDbRecommendationAggregation.
        :type: float
        """
        self._max_benefit_avg_active_sessions = max_benefit_avg_active_sessions

    @property
    def frequency_count(self):
        """
        Gets the frequency_count of this AddmDbRecommendationAggregation.
        Number of occurrences for this recommendation


        :return: The frequency_count of this AddmDbRecommendationAggregation.
        :rtype: int
        """
        return self._frequency_count

    @frequency_count.setter
    def frequency_count(self, frequency_count):
        """
        Sets the frequency_count of this AddmDbRecommendationAggregation.
        Number of occurrences for this recommendation


        :param frequency_count: The frequency_count of this AddmDbRecommendationAggregation.
        :type: int
        """
        self._frequency_count = frequency_count

    @property
    def related_object(self):
        """
        Gets the related_object of this AddmDbRecommendationAggregation.

        :return: The related_object of this AddmDbRecommendationAggregation.
        :rtype: oci.opsi.models.RelatedObjectTypeDetails
        """
        return self._related_object

    @related_object.setter
    def related_object(self, related_object):
        """
        Sets the related_object of this AddmDbRecommendationAggregation.

        :param related_object: The related_object of this AddmDbRecommendationAggregation.
        :type: oci.opsi.models.RelatedObjectTypeDetails
        """
        self._related_object = related_object

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other