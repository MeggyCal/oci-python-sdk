# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .task_summary import TaskSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskSummaryFromIntegrationTask(TaskSummary):
    """
    The information about the integration task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaskSummaryFromIntegrationTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.TaskSummaryFromIntegrationTask.model_type` attribute
        of this class is ``INTEGRATION_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TaskSummaryFromIntegrationTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this TaskSummaryFromIntegrationTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TaskSummaryFromIntegrationTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskSummaryFromIntegrationTask.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskSummaryFromIntegrationTask.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskSummaryFromIntegrationTask.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskSummaryFromIntegrationTask.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this TaskSummaryFromIntegrationTask.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TaskSummaryFromIntegrationTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this TaskSummaryFromIntegrationTask.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this TaskSummaryFromIntegrationTask.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this TaskSummaryFromIntegrationTask.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this TaskSummaryFromIntegrationTask.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this TaskSummaryFromIntegrationTask.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param is_concurrent_allowed:
            The value to assign to the is_concurrent_allowed property of this TaskSummaryFromIntegrationTask.
        :type is_concurrent_allowed: bool

        :param metadata:
            The value to assign to the metadata property of this TaskSummaryFromIntegrationTask.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this TaskSummaryFromIntegrationTask.
        :type key_map: dict(str, str)

        :param data_flow:
            The value to assign to the data_flow property of this TaskSummaryFromIntegrationTask.
        :type data_flow: oci.data_integration.models.DataFlow

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'ConfigProvider',
            'is_concurrent_allowed': 'bool',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)',
            'data_flow': 'DataFlow'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'is_concurrent_allowed': 'isConcurrentAllowed',
            'metadata': 'metadata',
            'key_map': 'keyMap',
            'data_flow': 'dataFlow'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._is_concurrent_allowed = None
        self._metadata = None
        self._key_map = None
        self._data_flow = None
        self._model_type = 'INTEGRATION_TASK'

    @property
    def data_flow(self):
        """
        Gets the data_flow of this TaskSummaryFromIntegrationTask.

        :return: The data_flow of this TaskSummaryFromIntegrationTask.
        :rtype: oci.data_integration.models.DataFlow
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """
        Sets the data_flow of this TaskSummaryFromIntegrationTask.

        :param data_flow: The data_flow of this TaskSummaryFromIntegrationTask.
        :type: oci.data_integration.models.DataFlow
        """
        self._data_flow = data_flow

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
