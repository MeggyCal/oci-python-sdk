# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVbInstanceDetails(object):
    """
    The information about new VbInstance.
    """

    #: A constant which can be used with the consumption_model property of a CreateVbInstanceDetails.
    #: This constant has a value of "UCM"
    CONSUMPTION_MODEL_UCM = "UCM"

    #: A constant which can be used with the consumption_model property of a CreateVbInstanceDetails.
    #: This constant has a value of "GOV"
    CONSUMPTION_MODEL_GOV = "GOV"

    #: A constant which can be used with the consumption_model property of a CreateVbInstanceDetails.
    #: This constant has a value of "VB4SAAS"
    CONSUMPTION_MODEL_VB4_SAAS = "VB4SAAS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVbInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateVbInstanceDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVbInstanceDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVbInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVbInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param idcs_open_id:
            The value to assign to the idcs_open_id property of this CreateVbInstanceDetails.
        :type idcs_open_id: str

        :param node_count:
            The value to assign to the node_count property of this CreateVbInstanceDetails.
        :type node_count: int

        :param is_visual_builder_enabled:
            The value to assign to the is_visual_builder_enabled property of this CreateVbInstanceDetails.
        :type is_visual_builder_enabled: bool

        :param custom_endpoint:
            The value to assign to the custom_endpoint property of this CreateVbInstanceDetails.
        :type custom_endpoint: oci.visual_builder.models.CreateCustomEndpointDetails

        :param alternate_custom_endpoints:
            The value to assign to the alternate_custom_endpoints property of this CreateVbInstanceDetails.
        :type alternate_custom_endpoints: list[oci.visual_builder.models.CreateCustomEndpointDetails]

        :param consumption_model:
            The value to assign to the consumption_model property of this CreateVbInstanceDetails.
            Allowed values for this property are: "UCM", "GOV", "VB4SAAS"
        :type consumption_model: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'idcs_open_id': 'str',
            'node_count': 'int',
            'is_visual_builder_enabled': 'bool',
            'custom_endpoint': 'CreateCustomEndpointDetails',
            'alternate_custom_endpoints': 'list[CreateCustomEndpointDetails]',
            'consumption_model': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'idcs_open_id': 'idcsOpenId',
            'node_count': 'nodeCount',
            'is_visual_builder_enabled': 'isVisualBuilderEnabled',
            'custom_endpoint': 'customEndpoint',
            'alternate_custom_endpoints': 'alternateCustomEndpoints',
            'consumption_model': 'consumptionModel'
        }

        self._display_name = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._idcs_open_id = None
        self._node_count = None
        self._is_visual_builder_enabled = None
        self._custom_endpoint = None
        self._alternate_custom_endpoints = None
        self._consumption_model = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateVbInstanceDetails.
        Vb Instance Identifier.


        :return: The display_name of this CreateVbInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVbInstanceDetails.
        Vb Instance Identifier.


        :param display_name: The display_name of this CreateVbInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVbInstanceDetails.
        Compartment Identifier.


        :return: The compartment_id of this CreateVbInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVbInstanceDetails.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CreateVbInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVbInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateVbInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVbInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateVbInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVbInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateVbInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVbInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateVbInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def idcs_open_id(self):
        """
        Gets the idcs_open_id of this CreateVbInstanceDetails.
        Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter


        :return: The idcs_open_id of this CreateVbInstanceDetails.
        :rtype: str
        """
        return self._idcs_open_id

    @idcs_open_id.setter
    def idcs_open_id(self, idcs_open_id):
        """
        Sets the idcs_open_id of this CreateVbInstanceDetails.
        Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter


        :param idcs_open_id: The idcs_open_id of this CreateVbInstanceDetails.
        :type: str
        """
        self._idcs_open_id = idcs_open_id

    @property
    def node_count(self):
        """
        **[Required]** Gets the node_count of this CreateVbInstanceDetails.
        The number of Nodes


        :return: The node_count of this CreateVbInstanceDetails.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this CreateVbInstanceDetails.
        The number of Nodes


        :param node_count: The node_count of this CreateVbInstanceDetails.
        :type: int
        """
        self._node_count = node_count

    @property
    def is_visual_builder_enabled(self):
        """
        Gets the is_visual_builder_enabled of this CreateVbInstanceDetails.
        Visual Builder is enabled or not.


        :return: The is_visual_builder_enabled of this CreateVbInstanceDetails.
        :rtype: bool
        """
        return self._is_visual_builder_enabled

    @is_visual_builder_enabled.setter
    def is_visual_builder_enabled(self, is_visual_builder_enabled):
        """
        Sets the is_visual_builder_enabled of this CreateVbInstanceDetails.
        Visual Builder is enabled or not.


        :param is_visual_builder_enabled: The is_visual_builder_enabled of this CreateVbInstanceDetails.
        :type: bool
        """
        self._is_visual_builder_enabled = is_visual_builder_enabled

    @property
    def custom_endpoint(self):
        """
        Gets the custom_endpoint of this CreateVbInstanceDetails.

        :return: The custom_endpoint of this CreateVbInstanceDetails.
        :rtype: oci.visual_builder.models.CreateCustomEndpointDetails
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """
        Sets the custom_endpoint of this CreateVbInstanceDetails.

        :param custom_endpoint: The custom_endpoint of this CreateVbInstanceDetails.
        :type: oci.visual_builder.models.CreateCustomEndpointDetails
        """
        self._custom_endpoint = custom_endpoint

    @property
    def alternate_custom_endpoints(self):
        """
        Gets the alternate_custom_endpoints of this CreateVbInstanceDetails.
        A list of alternate custom endpoints to be used for the vb instance URL
        (contact Oracle for alternateCustomEndpoints availability for a specific instance).


        :return: The alternate_custom_endpoints of this CreateVbInstanceDetails.
        :rtype: list[oci.visual_builder.models.CreateCustomEndpointDetails]
        """
        return self._alternate_custom_endpoints

    @alternate_custom_endpoints.setter
    def alternate_custom_endpoints(self, alternate_custom_endpoints):
        """
        Sets the alternate_custom_endpoints of this CreateVbInstanceDetails.
        A list of alternate custom endpoints to be used for the vb instance URL
        (contact Oracle for alternateCustomEndpoints availability for a specific instance).


        :param alternate_custom_endpoints: The alternate_custom_endpoints of this CreateVbInstanceDetails.
        :type: list[oci.visual_builder.models.CreateCustomEndpointDetails]
        """
        self._alternate_custom_endpoints = alternate_custom_endpoints

    @property
    def consumption_model(self):
        """
        Gets the consumption_model of this CreateVbInstanceDetails.
        Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.

        Allowed values for this property are: "UCM", "GOV", "VB4SAAS"


        :return: The consumption_model of this CreateVbInstanceDetails.
        :rtype: str
        """
        return self._consumption_model

    @consumption_model.setter
    def consumption_model(self, consumption_model):
        """
        Sets the consumption_model of this CreateVbInstanceDetails.
        Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.


        :param consumption_model: The consumption_model of this CreateVbInstanceDetails.
        :type: str
        """
        allowed_values = ["UCM", "GOV", "VB4SAAS"]
        if not value_allowed_none_or_none_sentinel(consumption_model, allowed_values):
            raise ValueError(
                "Invalid value for `consumption_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._consumption_model = consumption_model

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
