# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiskStatistics(object):
    """
    Aggregated data per disk.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiskStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disk_name:
            The value to assign to the disk_name property of this DiskStatistics.
        :type disk_name: str

        :param disk_unallocated_in_gbs:
            The value to assign to the disk_unallocated_in_gbs property of this DiskStatistics.
        :type disk_unallocated_in_gbs: float

        :param disk_usage_in_gbs:
            The value to assign to the disk_usage_in_gbs property of this DiskStatistics.
        :type disk_usage_in_gbs: float

        :param disk_size_in_gbs:
            The value to assign to the disk_size_in_gbs property of this DiskStatistics.
        :type disk_size_in_gbs: float

        """
        self.swagger_types = {
            'disk_name': 'str',
            'disk_unallocated_in_gbs': 'float',
            'disk_usage_in_gbs': 'float',
            'disk_size_in_gbs': 'float'
        }

        self.attribute_map = {
            'disk_name': 'diskName',
            'disk_unallocated_in_gbs': 'diskUnallocatedInGBs',
            'disk_usage_in_gbs': 'diskUsageInGBs',
            'disk_size_in_gbs': 'diskSizeInGBs'
        }

        self._disk_name = None
        self._disk_unallocated_in_gbs = None
        self._disk_usage_in_gbs = None
        self._disk_size_in_gbs = None

    @property
    def disk_name(self):
        """
        **[Required]** Gets the disk_name of this DiskStatistics.
        Name of the disk.


        :return: The disk_name of this DiskStatistics.
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """
        Sets the disk_name of this DiskStatistics.
        Name of the disk.


        :param disk_name: The disk_name of this DiskStatistics.
        :type: str
        """
        self._disk_name = disk_name

    @property
    def disk_unallocated_in_gbs(self):
        """
        **[Required]** Gets the disk_unallocated_in_gbs of this DiskStatistics.
        Value for unallocated space in a disk.


        :return: The disk_unallocated_in_gbs of this DiskStatistics.
        :rtype: float
        """
        return self._disk_unallocated_in_gbs

    @disk_unallocated_in_gbs.setter
    def disk_unallocated_in_gbs(self, disk_unallocated_in_gbs):
        """
        Sets the disk_unallocated_in_gbs of this DiskStatistics.
        Value for unallocated space in a disk.


        :param disk_unallocated_in_gbs: The disk_unallocated_in_gbs of this DiskStatistics.
        :type: float
        """
        self._disk_unallocated_in_gbs = disk_unallocated_in_gbs

    @property
    def disk_usage_in_gbs(self):
        """
        **[Required]** Gets the disk_usage_in_gbs of this DiskStatistics.
        Disk usage.


        :return: The disk_usage_in_gbs of this DiskStatistics.
        :rtype: float
        """
        return self._disk_usage_in_gbs

    @disk_usage_in_gbs.setter
    def disk_usage_in_gbs(self, disk_usage_in_gbs):
        """
        Sets the disk_usage_in_gbs of this DiskStatistics.
        Disk usage.


        :param disk_usage_in_gbs: The disk_usage_in_gbs of this DiskStatistics.
        :type: float
        """
        self._disk_usage_in_gbs = disk_usage_in_gbs

    @property
    def disk_size_in_gbs(self):
        """
        **[Required]** Gets the disk_size_in_gbs of this DiskStatistics.
        Size of the disk.


        :return: The disk_size_in_gbs of this DiskStatistics.
        :rtype: float
        """
        return self._disk_size_in_gbs

    @disk_size_in_gbs.setter
    def disk_size_in_gbs(self, disk_size_in_gbs):
        """
        Sets the disk_size_in_gbs of this DiskStatistics.
        Size of the disk.


        :param disk_size_in_gbs: The disk_size_in_gbs of this DiskStatistics.
        :type: float
        """
        self._disk_size_in_gbs = disk_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other