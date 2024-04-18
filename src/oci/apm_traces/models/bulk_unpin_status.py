# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUnpinStatus(object):
    """
    Response of a bulk attribute unpin operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUnpinStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_statuses:
            The value to assign to the attribute_statuses property of this BulkUnpinStatus.
        :type attribute_statuses: list[oci.apm_traces.models.AttributeUnpinResponse]

        :param bulk_unpin_metadata:
            The value to assign to the bulk_unpin_metadata property of this BulkUnpinStatus.
        :type bulk_unpin_metadata: oci.apm_traces.models.BulkUnpinMetadata

        """
        self.swagger_types = {
            'attribute_statuses': 'list[AttributeUnpinResponse]',
            'bulk_unpin_metadata': 'BulkUnpinMetadata'
        }

        self.attribute_map = {
            'attribute_statuses': 'attributeStatuses',
            'bulk_unpin_metadata': 'bulkUnpinMetadata'
        }

        self._attribute_statuses = None
        self._bulk_unpin_metadata = None

    @property
    def attribute_statuses(self):
        """
        **[Required]** Gets the attribute_statuses of this BulkUnpinStatus.
        We preserve the order of the attribute items from the bulk unpin request in this collection.  The ith object in this collection represents the
        bulk unpin operation status of the ith object in the BulkUnpinAttributeDetails object in the Bulk unpin request.  If the
        bulk unpin operation results in a processing error or a validation error, the operationStatus property in the  BulkUnpinMetadata object will
        contain the appropriate bulk error status for the bulk operation.


        :return: The attribute_statuses of this BulkUnpinStatus.
        :rtype: list[oci.apm_traces.models.AttributeUnpinResponse]
        """
        return self._attribute_statuses

    @attribute_statuses.setter
    def attribute_statuses(self, attribute_statuses):
        """
        Sets the attribute_statuses of this BulkUnpinStatus.
        We preserve the order of the attribute items from the bulk unpin request in this collection.  The ith object in this collection represents the
        bulk unpin operation status of the ith object in the BulkUnpinAttributeDetails object in the Bulk unpin request.  If the
        bulk unpin operation results in a processing error or a validation error, the operationStatus property in the  BulkUnpinMetadata object will
        contain the appropriate bulk error status for the bulk operation.


        :param attribute_statuses: The attribute_statuses of this BulkUnpinStatus.
        :type: list[oci.apm_traces.models.AttributeUnpinResponse]
        """
        self._attribute_statuses = attribute_statuses

    @property
    def bulk_unpin_metadata(self):
        """
        **[Required]** Gets the bulk_unpin_metadata of this BulkUnpinStatus.

        :return: The bulk_unpin_metadata of this BulkUnpinStatus.
        :rtype: oci.apm_traces.models.BulkUnpinMetadata
        """
        return self._bulk_unpin_metadata

    @bulk_unpin_metadata.setter
    def bulk_unpin_metadata(self, bulk_unpin_metadata):
        """
        Sets the bulk_unpin_metadata of this BulkUnpinStatus.

        :param bulk_unpin_metadata: The bulk_unpin_metadata of this BulkUnpinStatus.
        :type: oci.apm_traces.models.BulkUnpinMetadata
        """
        self._bulk_unpin_metadata = bulk_unpin_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other