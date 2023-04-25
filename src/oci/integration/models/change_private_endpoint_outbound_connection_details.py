# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangePrivateEndpointOutboundConnectionDetails(object):
    """
    Input payload to ADD/REMOVE Private Endpoint Outbound Connection for given IntegrationInstance.

    Some actions may not be applicable to specific integration types,
    see `Differences in Instance Management`__
    for details.

    __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/application-integration&id=INTOO-GUID-931B5E33-4FE6-4997-93E5-8748516F46AA__GUID-176E43D5-4116-4828-8120-B929DF2A6B5E
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangePrivateEndpointOutboundConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param private_endpoint_outbound_connection:
            The value to assign to the private_endpoint_outbound_connection property of this ChangePrivateEndpointOutboundConnectionDetails.
        :type private_endpoint_outbound_connection: oci.integration.models.OutboundConnection

        """
        self.swagger_types = {
            'private_endpoint_outbound_connection': 'OutboundConnection'
        }

        self.attribute_map = {
            'private_endpoint_outbound_connection': 'privateEndpointOutboundConnection'
        }

        self._private_endpoint_outbound_connection = None

    @property
    def private_endpoint_outbound_connection(self):
        """
        Gets the private_endpoint_outbound_connection of this ChangePrivateEndpointOutboundConnectionDetails.

        :return: The private_endpoint_outbound_connection of this ChangePrivateEndpointOutboundConnectionDetails.
        :rtype: oci.integration.models.OutboundConnection
        """
        return self._private_endpoint_outbound_connection

    @private_endpoint_outbound_connection.setter
    def private_endpoint_outbound_connection(self, private_endpoint_outbound_connection):
        """
        Sets the private_endpoint_outbound_connection of this ChangePrivateEndpointOutboundConnectionDetails.

        :param private_endpoint_outbound_connection: The private_endpoint_outbound_connection of this ChangePrivateEndpointOutboundConnectionDetails.
        :type: oci.integration.models.OutboundConnection
        """
        self._private_endpoint_outbound_connection = private_endpoint_outbound_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
