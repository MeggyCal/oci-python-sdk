# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HydratedVolume(object):
    """
    Description of the hydration server volume.
    """

    #: A constant which can be used with the volume_type property of a HydratedVolume.
    #: This constant has a value of "BOOT"
    VOLUME_TYPE_BOOT = "BOOT"

    #: A constant which can be used with the volume_type property of a HydratedVolume.
    #: This constant has a value of "BLOCK"
    VOLUME_TYPE_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new HydratedVolume object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param uuid:
            The value to assign to the uuid property of this HydratedVolume.
        :type uuid: str

        :param volume_id:
            The value to assign to the volume_id property of this HydratedVolume.
        :type volume_id: str

        :param volume_type:
            The value to assign to the volume_type property of this HydratedVolume.
            Allowed values for this property are: "BOOT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type volume_type: str

        :param unmodified_volume_id:
            The value to assign to the unmodified_volume_id property of this HydratedVolume.
        :type unmodified_volume_id: str

        """
        self.swagger_types = {
            'uuid': 'str',
            'volume_id': 'str',
            'volume_type': 'str',
            'unmodified_volume_id': 'str'
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'volume_id': 'volumeId',
            'volume_type': 'volumeType',
            'unmodified_volume_id': 'unmodifiedVolumeId'
        }

        self._uuid = None
        self._volume_id = None
        self._volume_type = None
        self._unmodified_volume_id = None

    @property
    def uuid(self):
        """
        **[Required]** Gets the uuid of this HydratedVolume.
        ID of the vCenter disk obtained from Inventory.


        :return: The uuid of this HydratedVolume.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this HydratedVolume.
        ID of the vCenter disk obtained from Inventory.


        :param uuid: The uuid of this HydratedVolume.
        :type: str
        """
        self._uuid = uuid

    @property
    def volume_id(self):
        """
        **[Required]** Gets the volume_id of this HydratedVolume.
        ID of the hydration server volume


        :return: The volume_id of this HydratedVolume.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this HydratedVolume.
        ID of the hydration server volume


        :param volume_id: The volume_id of this HydratedVolume.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def volume_type(self):
        """
        **[Required]** Gets the volume_type of this HydratedVolume.
        The hydration server volume type

        Allowed values for this property are: "BOOT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The volume_type of this HydratedVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """
        Sets the volume_type of this HydratedVolume.
        The hydration server volume type


        :param volume_type: The volume_type of this HydratedVolume.
        :type: str
        """
        allowed_values = ["BOOT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(volume_type, allowed_values):
            volume_type = 'UNKNOWN_ENUM_VALUE'
        self._volume_type = volume_type

    @property
    def unmodified_volume_id(self):
        """
        **[Required]** Gets the unmodified_volume_id of this HydratedVolume.
        ID of the unmodified volume


        :return: The unmodified_volume_id of this HydratedVolume.
        :rtype: str
        """
        return self._unmodified_volume_id

    @unmodified_volume_id.setter
    def unmodified_volume_id(self, unmodified_volume_id):
        """
        Sets the unmodified_volume_id of this HydratedVolume.
        ID of the unmodified volume


        :param unmodified_volume_id: The unmodified_volume_id of this HydratedVolume.
        :type: str
        """
        self._unmodified_volume_id = unmodified_volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
