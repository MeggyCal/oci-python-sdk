# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMonitoredResourceTypeDetails(object):
    """
    The information to be updated for the monitored resource type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMonitoredResourceTypeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMonitoredResourceTypeDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateMonitoredResourceTypeDetails.
        :type description: str

        :param metric_namespace:
            The value to assign to the metric_namespace property of this UpdateMonitoredResourceTypeDetails.
        :type metric_namespace: str

        :param metadata:
            The value to assign to the metadata property of this UpdateMonitoredResourceTypeDetails.
        :type metadata: oci.stack_monitoring.models.ResourceTypeMetadataDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMonitoredResourceTypeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMonitoredResourceTypeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'metric_namespace': 'str',
            'metadata': 'ResourceTypeMetadataDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'metric_namespace': 'metricNamespace',
            'metadata': 'metadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._metric_namespace = None
        self._metadata = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMonitoredResourceTypeDetails.
        Monitored resource type display name.


        :return: The display_name of this UpdateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMonitoredResourceTypeDetails.
        Monitored resource type display name.


        :param display_name: The display_name of this UpdateMonitoredResourceTypeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateMonitoredResourceTypeDetails.
        A friendly description.


        :return: The description of this UpdateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateMonitoredResourceTypeDetails.
        A friendly description.


        :param description: The description of this UpdateMonitoredResourceTypeDetails.
        :type: str
        """
        self._description = description

    @property
    def metric_namespace(self):
        """
        Gets the metric_namespace of this UpdateMonitoredResourceTypeDetails.
        Metric namespace for resource type.


        :return: The metric_namespace of this UpdateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._metric_namespace

    @metric_namespace.setter
    def metric_namespace(self, metric_namespace):
        """
        Sets the metric_namespace of this UpdateMonitoredResourceTypeDetails.
        Metric namespace for resource type.


        :param metric_namespace: The metric_namespace of this UpdateMonitoredResourceTypeDetails.
        :type: str
        """
        self._metric_namespace = metric_namespace

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateMonitoredResourceTypeDetails.

        :return: The metadata of this UpdateMonitoredResourceTypeDetails.
        :rtype: oci.stack_monitoring.models.ResourceTypeMetadataDetails
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateMonitoredResourceTypeDetails.

        :param metadata: The metadata of this UpdateMonitoredResourceTypeDetails.
        :type: oci.stack_monitoring.models.ResourceTypeMetadataDetails
        """
        self._metadata = metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMonitoredResourceTypeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateMonitoredResourceTypeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMonitoredResourceTypeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateMonitoredResourceTypeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMonitoredResourceTypeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMonitoredResourceTypeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMonitoredResourceTypeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMonitoredResourceTypeDetails.
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