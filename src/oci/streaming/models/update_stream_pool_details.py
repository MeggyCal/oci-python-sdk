# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStreamPoolDetails(object):
    """
    Object used to update the stream pool's details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStreamPoolDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateStreamPoolDetails.
        :type name: str

        :param kafka_settings:
            The value to assign to the kafka_settings property of this UpdateStreamPoolDetails.
        :type kafka_settings: KafkaSettings

        :param custom_encryption_key_details:
            The value to assign to the custom_encryption_key_details property of this UpdateStreamPoolDetails.
        :type custom_encryption_key_details: CustomEncryptionKeyDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateStreamPoolDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateStreamPoolDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'kafka_settings': 'KafkaSettings',
            'custom_encryption_key_details': 'CustomEncryptionKeyDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'kafka_settings': 'kafkaSettings',
            'custom_encryption_key_details': 'customEncryptionKeyDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._kafka_settings = None
        self._custom_encryption_key_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        Gets the name of this UpdateStreamPoolDetails.

        :return: The name of this UpdateStreamPoolDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateStreamPoolDetails.

        :param name: The name of this UpdateStreamPoolDetails.
        :type: str
        """
        self._name = name

    @property
    def kafka_settings(self):
        """
        Gets the kafka_settings of this UpdateStreamPoolDetails.

        :return: The kafka_settings of this UpdateStreamPoolDetails.
        :rtype: KafkaSettings
        """
        return self._kafka_settings

    @kafka_settings.setter
    def kafka_settings(self, kafka_settings):
        """
        Sets the kafka_settings of this UpdateStreamPoolDetails.

        :param kafka_settings: The kafka_settings of this UpdateStreamPoolDetails.
        :type: KafkaSettings
        """
        self._kafka_settings = kafka_settings

    @property
    def custom_encryption_key_details(self):
        """
        Gets the custom_encryption_key_details of this UpdateStreamPoolDetails.

        :return: The custom_encryption_key_details of this UpdateStreamPoolDetails.
        :rtype: CustomEncryptionKeyDetails
        """
        return self._custom_encryption_key_details

    @custom_encryption_key_details.setter
    def custom_encryption_key_details(self, custom_encryption_key_details):
        """
        Sets the custom_encryption_key_details of this UpdateStreamPoolDetails.

        :param custom_encryption_key_details: The custom_encryption_key_details of this UpdateStreamPoolDetails.
        :type: CustomEncryptionKeyDetails
        """
        self._custom_encryption_key_details = custom_encryption_key_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateStreamPoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateStreamPoolDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateStreamPoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateStreamPoolDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateStreamPoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateStreamPoolDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateStreamPoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateStreamPoolDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
