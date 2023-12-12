# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbInstanceDetails(object):
    """
    Information about the new database instance node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbInstanceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDbInstanceDetails.
        :type description: str

        :param private_ip:
            The value to assign to the private_ip property of this CreateDbInstanceDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'private_ip': 'privateIp'
        }

        self._display_name = None
        self._description = None
        self._private_ip = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbInstanceDetails.
        Display name of the database instance node. Avoid entering confidential information.


        :return: The display_name of this CreateDbInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbInstanceDetails.
        Display name of the database instance node. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDbInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDbInstanceDetails.
        A user-provided description of the database instance node.


        :return: The description of this CreateDbInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDbInstanceDetails.
        A user-provided description of the database instance node.


        :param description: The description of this CreateDbInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def private_ip(self):
        """
        Gets the private_ip of this CreateDbInstanceDetails.
        Private IP in customer subnet that will be assigned to the database instance node. This value is optional.
        If the IP is not provided, the IP will be chosen from the available IP addresses in the specified subnet.


        :return: The private_ip of this CreateDbInstanceDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this CreateDbInstanceDetails.
        Private IP in customer subnet that will be assigned to the database instance node. This value is optional.
        If the IP is not provided, the IP will be chosen from the available IP addresses in the specified subnet.


        :param private_ip: The private_ip of this CreateDbInstanceDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
