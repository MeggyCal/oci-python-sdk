# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VbInstanceSummary(object):
    """
    Summary of the Vb Instance.
    """

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a VbInstanceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the consumption_model property of a VbInstanceSummary.
    #: This constant has a value of "UCM"
    CONSUMPTION_MODEL_UCM = "UCM"

    #: A constant which can be used with the consumption_model property of a VbInstanceSummary.
    #: This constant has a value of "GOV"
    CONSUMPTION_MODEL_GOV = "GOV"

    #: A constant which can be used with the consumption_model property of a VbInstanceSummary.
    #: This constant has a value of "VB4SAAS"
    CONSUMPTION_MODEL_VB4_SAAS = "VB4SAAS"

    def __init__(self, **kwargs):
        """
        Initializes a new VbInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VbInstanceSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this VbInstanceSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VbInstanceSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this VbInstanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VbInstanceSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VbInstanceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this VbInstanceSummary.
        :type state_message: str

        :param instance_url:
            The value to assign to the instance_url property of this VbInstanceSummary.
        :type instance_url: str

        :param node_count:
            The value to assign to the node_count property of this VbInstanceSummary.
        :type node_count: int

        :param is_visual_builder_enabled:
            The value to assign to the is_visual_builder_enabled property of this VbInstanceSummary.
        :type is_visual_builder_enabled: bool

        :param custom_endpoint:
            The value to assign to the custom_endpoint property of this VbInstanceSummary.
        :type custom_endpoint: oci.visual_builder.models.CustomEndpointDetails

        :param alternate_custom_endpoints:
            The value to assign to the alternate_custom_endpoints property of this VbInstanceSummary.
        :type alternate_custom_endpoints: list[oci.visual_builder.models.CustomEndpointDetails]

        :param consumption_model:
            The value to assign to the consumption_model property of this VbInstanceSummary.
            Allowed values for this property are: "UCM", "GOV", "VB4SAAS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type consumption_model: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VbInstanceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VbInstanceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VbInstanceSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'state_message': 'str',
            'instance_url': 'str',
            'node_count': 'int',
            'is_visual_builder_enabled': 'bool',
            'custom_endpoint': 'CustomEndpointDetails',
            'alternate_custom_endpoints': 'list[CustomEndpointDetails]',
            'consumption_model': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage',
            'instance_url': 'instanceUrl',
            'node_count': 'nodeCount',
            'is_visual_builder_enabled': 'isVisualBuilderEnabled',
            'custom_endpoint': 'customEndpoint',
            'alternate_custom_endpoints': 'alternateCustomEndpoints',
            'consumption_model': 'consumptionModel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._state_message = None
        self._instance_url = None
        self._node_count = None
        self._is_visual_builder_enabled = None
        self._custom_endpoint = None
        self._alternate_custom_endpoints = None
        self._consumption_model = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VbInstanceSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this VbInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VbInstanceSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this VbInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VbInstanceSummary.
        Vb Instance Identifier, can be renamed.


        :return: The display_name of this VbInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VbInstanceSummary.
        Vb Instance Identifier, can be renamed.


        :param display_name: The display_name of this VbInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VbInstanceSummary.
        Compartment Identifier.


        :return: The compartment_id of this VbInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VbInstanceSummary.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this VbInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this VbInstanceSummary.
        The time the the Vb Instance was created. An RFC3339 formatted datetime string.


        :return: The time_created of this VbInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VbInstanceSummary.
        The time the the Vb Instance was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this VbInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this VbInstanceSummary.
        The time the VbInstance was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this VbInstanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this VbInstanceSummary.
        The time the VbInstance was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this VbInstanceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VbInstanceSummary.
        The current state of the Vb Instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VbInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VbInstanceSummary.
        The current state of the Vb Instance.


        :param lifecycle_state: The lifecycle_state of this VbInstanceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this VbInstanceSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this VbInstanceSummary.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this VbInstanceSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this VbInstanceSummary.
        :type: str
        """
        self._state_message = state_message

    @property
    def instance_url(self):
        """
        **[Required]** Gets the instance_url of this VbInstanceSummary.
        The Vb Instance URL.


        :return: The instance_url of this VbInstanceSummary.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """
        Sets the instance_url of this VbInstanceSummary.
        The Vb Instance URL.


        :param instance_url: The instance_url of this VbInstanceSummary.
        :type: str
        """
        self._instance_url = instance_url

    @property
    def node_count(self):
        """
        **[Required]** Gets the node_count of this VbInstanceSummary.
        The number of Nodes


        :return: The node_count of this VbInstanceSummary.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this VbInstanceSummary.
        The number of Nodes


        :param node_count: The node_count of this VbInstanceSummary.
        :type: int
        """
        self._node_count = node_count

    @property
    def is_visual_builder_enabled(self):
        """
        Gets the is_visual_builder_enabled of this VbInstanceSummary.
        Visual Builder is enabled or not.


        :return: The is_visual_builder_enabled of this VbInstanceSummary.
        :rtype: bool
        """
        return self._is_visual_builder_enabled

    @is_visual_builder_enabled.setter
    def is_visual_builder_enabled(self, is_visual_builder_enabled):
        """
        Sets the is_visual_builder_enabled of this VbInstanceSummary.
        Visual Builder is enabled or not.


        :param is_visual_builder_enabled: The is_visual_builder_enabled of this VbInstanceSummary.
        :type: bool
        """
        self._is_visual_builder_enabled = is_visual_builder_enabled

    @property
    def custom_endpoint(self):
        """
        Gets the custom_endpoint of this VbInstanceSummary.

        :return: The custom_endpoint of this VbInstanceSummary.
        :rtype: oci.visual_builder.models.CustomEndpointDetails
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """
        Sets the custom_endpoint of this VbInstanceSummary.

        :param custom_endpoint: The custom_endpoint of this VbInstanceSummary.
        :type: oci.visual_builder.models.CustomEndpointDetails
        """
        self._custom_endpoint = custom_endpoint

    @property
    def alternate_custom_endpoints(self):
        """
        Gets the alternate_custom_endpoints of this VbInstanceSummary.
        A list of alternate custom endpoints used for the vb instance URL.


        :return: The alternate_custom_endpoints of this VbInstanceSummary.
        :rtype: list[oci.visual_builder.models.CustomEndpointDetails]
        """
        return self._alternate_custom_endpoints

    @alternate_custom_endpoints.setter
    def alternate_custom_endpoints(self, alternate_custom_endpoints):
        """
        Sets the alternate_custom_endpoints of this VbInstanceSummary.
        A list of alternate custom endpoints used for the vb instance URL.


        :param alternate_custom_endpoints: The alternate_custom_endpoints of this VbInstanceSummary.
        :type: list[oci.visual_builder.models.CustomEndpointDetails]
        """
        self._alternate_custom_endpoints = alternate_custom_endpoints

    @property
    def consumption_model(self):
        """
        Gets the consumption_model of this VbInstanceSummary.
        The entitlement used for billing purposes.

        Allowed values for this property are: "UCM", "GOV", "VB4SAAS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The consumption_model of this VbInstanceSummary.
        :rtype: str
        """
        return self._consumption_model

    @consumption_model.setter
    def consumption_model(self, consumption_model):
        """
        Sets the consumption_model of this VbInstanceSummary.
        The entitlement used for billing purposes.


        :param consumption_model: The consumption_model of this VbInstanceSummary.
        :type: str
        """
        allowed_values = ["UCM", "GOV", "VB4SAAS"]
        if not value_allowed_none_or_none_sentinel(consumption_model, allowed_values):
            consumption_model = 'UNKNOWN_ENUM_VALUE'
        self._consumption_model = consumption_model

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VbInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this VbInstanceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VbInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this VbInstanceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VbInstanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this VbInstanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VbInstanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this VbInstanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this VbInstanceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this VbInstanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this VbInstanceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this VbInstanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
