# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkBondingModeDetails(object):
    """
    Details of bonding mode for Client and Backup networks of an Exadata infrastructure.
    """

    #: A constant which can be used with the client_network_bonding_mode property of a NetworkBondingModeDetails.
    #: This constant has a value of "ACTIVE_BACKUP"
    CLIENT_NETWORK_BONDING_MODE_ACTIVE_BACKUP = "ACTIVE_BACKUP"

    #: A constant which can be used with the client_network_bonding_mode property of a NetworkBondingModeDetails.
    #: This constant has a value of "LACP"
    CLIENT_NETWORK_BONDING_MODE_LACP = "LACP"

    #: A constant which can be used with the backup_network_bonding_mode property of a NetworkBondingModeDetails.
    #: This constant has a value of "ACTIVE_BACKUP"
    BACKUP_NETWORK_BONDING_MODE_ACTIVE_BACKUP = "ACTIVE_BACKUP"

    #: A constant which can be used with the backup_network_bonding_mode property of a NetworkBondingModeDetails.
    #: This constant has a value of "LACP"
    BACKUP_NETWORK_BONDING_MODE_LACP = "LACP"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkBondingModeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param client_network_bonding_mode:
            The value to assign to the client_network_bonding_mode property of this NetworkBondingModeDetails.
            Allowed values for this property are: "ACTIVE_BACKUP", "LACP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type client_network_bonding_mode: str

        :param backup_network_bonding_mode:
            The value to assign to the backup_network_bonding_mode property of this NetworkBondingModeDetails.
            Allowed values for this property are: "ACTIVE_BACKUP", "LACP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_network_bonding_mode: str

        """
        self.swagger_types = {
            'client_network_bonding_mode': 'str',
            'backup_network_bonding_mode': 'str'
        }

        self.attribute_map = {
            'client_network_bonding_mode': 'clientNetworkBondingMode',
            'backup_network_bonding_mode': 'backupNetworkBondingMode'
        }

        self._client_network_bonding_mode = None
        self._backup_network_bonding_mode = None

    @property
    def client_network_bonding_mode(self):
        """
        Gets the client_network_bonding_mode of this NetworkBondingModeDetails.
        The network bonding mode for the Exadata infrastructure.

        Allowed values for this property are: "ACTIVE_BACKUP", "LACP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The client_network_bonding_mode of this NetworkBondingModeDetails.
        :rtype: str
        """
        return self._client_network_bonding_mode

    @client_network_bonding_mode.setter
    def client_network_bonding_mode(self, client_network_bonding_mode):
        """
        Sets the client_network_bonding_mode of this NetworkBondingModeDetails.
        The network bonding mode for the Exadata infrastructure.


        :param client_network_bonding_mode: The client_network_bonding_mode of this NetworkBondingModeDetails.
        :type: str
        """
        allowed_values = ["ACTIVE_BACKUP", "LACP"]
        if not value_allowed_none_or_none_sentinel(client_network_bonding_mode, allowed_values):
            client_network_bonding_mode = 'UNKNOWN_ENUM_VALUE'
        self._client_network_bonding_mode = client_network_bonding_mode

    @property
    def backup_network_bonding_mode(self):
        """
        Gets the backup_network_bonding_mode of this NetworkBondingModeDetails.
        The network bonding mode for the Exadata infrastructure.

        Allowed values for this property are: "ACTIVE_BACKUP", "LACP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_network_bonding_mode of this NetworkBondingModeDetails.
        :rtype: str
        """
        return self._backup_network_bonding_mode

    @backup_network_bonding_mode.setter
    def backup_network_bonding_mode(self, backup_network_bonding_mode):
        """
        Sets the backup_network_bonding_mode of this NetworkBondingModeDetails.
        The network bonding mode for the Exadata infrastructure.


        :param backup_network_bonding_mode: The backup_network_bonding_mode of this NetworkBondingModeDetails.
        :type: str
        """
        allowed_values = ["ACTIVE_BACKUP", "LACP"]
        if not value_allowed_none_or_none_sentinel(backup_network_bonding_mode, allowed_values):
            backup_network_bonding_mode = 'UNKNOWN_ENUM_VALUE'
        self._backup_network_bonding_mode = backup_network_bonding_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
