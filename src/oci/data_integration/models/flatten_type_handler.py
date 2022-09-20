# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dynamic_type_handler import DynamicTypeHandler
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FlattenTypeHandler(DynamicTypeHandler):
    """
    The flatten type handler.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FlattenTypeHandler object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.FlattenTypeHandler.model_type` attribute
        of this class is ``FLATTEN_TYPE_HANDLER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this FlattenTypeHandler.
            Allowed values for this property are: "RULE_TYPE_CONFIGS", "FLATTEN_TYPE_HANDLER"
        :type model_type: str

        :param key:
            The value to assign to the key property of this FlattenTypeHandler.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this FlattenTypeHandler.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this FlattenTypeHandler.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param scope:
            The value to assign to the scope property of this FlattenTypeHandler.
        :type scope: str

        :param flatten_details:
            The value to assign to the flatten_details property of this FlattenTypeHandler.
        :type flatten_details: str

        :param config_values:
            The value to assign to the config_values property of this FlattenTypeHandler.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this FlattenTypeHandler.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'scope': 'str',
            'flatten_details': 'str',
            'config_values': 'ConfigValues',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'scope': 'scope',
            'flatten_details': 'flattenDetails',
            'config_values': 'configValues',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._scope = None
        self._flatten_details = None
        self._config_values = None
        self._object_status = None
        self._model_type = 'FLATTEN_TYPE_HANDLER'

    @property
    def key(self):
        """
        Gets the key of this FlattenTypeHandler.
        The key of the object.


        :return: The key of this FlattenTypeHandler.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FlattenTypeHandler.
        The key of the object.


        :param key: The key of this FlattenTypeHandler.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this FlattenTypeHandler.
        The model version of an object.


        :return: The model_version of this FlattenTypeHandler.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this FlattenTypeHandler.
        The model version of an object.


        :param model_version: The model_version of this FlattenTypeHandler.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this FlattenTypeHandler.

        :return: The parent_ref of this FlattenTypeHandler.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this FlattenTypeHandler.

        :param parent_ref: The parent_ref of this FlattenTypeHandler.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def scope(self):
        """
        Gets the scope of this FlattenTypeHandler.
        Reference key for the typed object.


        :return: The scope of this FlattenTypeHandler.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this FlattenTypeHandler.
        Reference key for the typed object.


        :param scope: The scope of this FlattenTypeHandler.
        :type: str
        """
        self._scope = scope

    @property
    def flatten_details(self):
        """
        Gets the flatten_details of this FlattenTypeHandler.
        Contains a key for referencing the flattenDetails information.


        :return: The flatten_details of this FlattenTypeHandler.
        :rtype: str
        """
        return self._flatten_details

    @flatten_details.setter
    def flatten_details(self, flatten_details):
        """
        Sets the flatten_details of this FlattenTypeHandler.
        Contains a key for referencing the flattenDetails information.


        :param flatten_details: The flatten_details of this FlattenTypeHandler.
        :type: str
        """
        self._flatten_details = flatten_details

    @property
    def config_values(self):
        """
        Gets the config_values of this FlattenTypeHandler.

        :return: The config_values of this FlattenTypeHandler.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this FlattenTypeHandler.

        :param config_values: The config_values of this FlattenTypeHandler.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this FlattenTypeHandler.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this FlattenTypeHandler.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this FlattenTypeHandler.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this FlattenTypeHandler.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
