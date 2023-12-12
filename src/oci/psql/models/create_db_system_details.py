# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbSystemDetails(object):
    """
    The information about new database system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbSystemDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDbSystemDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDbSystemDetails.
        :type compartment_id: str

        :param system_type:
            The value to assign to the system_type property of this CreateDbSystemDetails.
        :type system_type: str

        :param db_version:
            The value to assign to the db_version property of this CreateDbSystemDetails.
        :type db_version: str

        :param config_id:
            The value to assign to the config_id property of this CreateDbSystemDetails.
        :type config_id: str

        :param storage_details:
            The value to assign to the storage_details property of this CreateDbSystemDetails.
        :type storage_details: oci.psql.models.StorageDetails

        :param shape:
            The value to assign to the shape property of this CreateDbSystemDetails.
        :type shape: str

        :param instance_ocpu_count:
            The value to assign to the instance_ocpu_count property of this CreateDbSystemDetails.
        :type instance_ocpu_count: int

        :param instance_memory_size_in_gbs:
            The value to assign to the instance_memory_size_in_gbs property of this CreateDbSystemDetails.
        :type instance_memory_size_in_gbs: int

        :param instance_count:
            The value to assign to the instance_count property of this CreateDbSystemDetails.
        :type instance_count: int

        :param instances_details:
            The value to assign to the instances_details property of this CreateDbSystemDetails.
        :type instances_details: list[oci.psql.models.CreateDbInstanceDetails]

        :param credentials:
            The value to assign to the credentials property of this CreateDbSystemDetails.
        :type credentials: oci.psql.models.Credentials

        :param network_details:
            The value to assign to the network_details property of this CreateDbSystemDetails.
        :type network_details: oci.psql.models.NetworkDetails

        :param management_policy:
            The value to assign to the management_policy property of this CreateDbSystemDetails.
        :type management_policy: oci.psql.models.ManagementPolicyDetails

        :param source:
            The value to assign to the source property of this CreateDbSystemDetails.
        :type source: oci.psql.models.SourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'system_type': 'str',
            'db_version': 'str',
            'config_id': 'str',
            'storage_details': 'StorageDetails',
            'shape': 'str',
            'instance_ocpu_count': 'int',
            'instance_memory_size_in_gbs': 'int',
            'instance_count': 'int',
            'instances_details': 'list[CreateDbInstanceDetails]',
            'credentials': 'Credentials',
            'network_details': 'NetworkDetails',
            'management_policy': 'ManagementPolicyDetails',
            'source': 'SourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'system_type': 'systemType',
            'db_version': 'dbVersion',
            'config_id': 'configId',
            'storage_details': 'storageDetails',
            'shape': 'shape',
            'instance_ocpu_count': 'instanceOcpuCount',
            'instance_memory_size_in_gbs': 'instanceMemorySizeInGBs',
            'instance_count': 'instanceCount',
            'instances_details': 'instancesDetails',
            'credentials': 'credentials',
            'network_details': 'networkDetails',
            'management_policy': 'managementPolicy',
            'source': 'source',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._system_type = None
        self._db_version = None
        self._config_id = None
        self._storage_details = None
        self._shape = None
        self._instance_ocpu_count = None
        self._instance_memory_size_in_gbs = None
        self._instance_count = None
        self._instances_details = None
        self._credentials = None
        self._network_details = None
        self._management_policy = None
        self._source = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDbSystemDetails.
        A user-friendly display name for the database system. Avoid entering confidential information.


        :return: The display_name of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbSystemDetails.
        A user-friendly display name for the database system. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDbSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDbSystemDetails.
        A user-provided description of a database system.


        :return: The description of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDbSystemDetails.
        A user-provided description of a database system.


        :param description: The description of this CreateDbSystemDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDbSystemDetails.
        The `OCID`__ of the compartment that contains the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDbSystemDetails.
        The `OCID`__ of the compartment that contains the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDbSystemDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def system_type(self):
        """
        Gets the system_type of this CreateDbSystemDetails.
        Type of the database system.


        :return: The system_type of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """
        Sets the system_type of this CreateDbSystemDetails.
        Type of the database system.


        :param system_type: The system_type of this CreateDbSystemDetails.
        :type: str
        """
        self._system_type = system_type

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this CreateDbSystemDetails.
        Version of database system software.


        :return: The db_version of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateDbSystemDetails.
        Version of database system software.


        :param db_version: The db_version of this CreateDbSystemDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def config_id(self):
        """
        Gets the config_id of this CreateDbSystemDetails.
        The `OCID`__ of the configuration associated with the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The config_id of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """
        Sets the config_id of this CreateDbSystemDetails.
        The `OCID`__ of the configuration associated with the database system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param config_id: The config_id of this CreateDbSystemDetails.
        :type: str
        """
        self._config_id = config_id

    @property
    def storage_details(self):
        """
        **[Required]** Gets the storage_details of this CreateDbSystemDetails.

        :return: The storage_details of this CreateDbSystemDetails.
        :rtype: oci.psql.models.StorageDetails
        """
        return self._storage_details

    @storage_details.setter
    def storage_details(self, storage_details):
        """
        Sets the storage_details of this CreateDbSystemDetails.

        :param storage_details: The storage_details of this CreateDbSystemDetails.
        :type: oci.psql.models.StorageDetails
        """
        self._storage_details = storage_details

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CreateDbSystemDetails.
        The name of the shape for the database instance node. Use the /shapes API for accepted shapes.
        Example: `VM.Standard.E4.Flex`


        :return: The shape of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateDbSystemDetails.
        The name of the shape for the database instance node. Use the /shapes API for accepted shapes.
        Example: `VM.Standard.E4.Flex`


        :param shape: The shape of this CreateDbSystemDetails.
        :type: str
        """
        self._shape = shape

    @property
    def instance_ocpu_count(self):
        """
        Gets the instance_ocpu_count of this CreateDbSystemDetails.
        The total number of OCPUs available to each database instance node.


        :return: The instance_ocpu_count of this CreateDbSystemDetails.
        :rtype: int
        """
        return self._instance_ocpu_count

    @instance_ocpu_count.setter
    def instance_ocpu_count(self, instance_ocpu_count):
        """
        Sets the instance_ocpu_count of this CreateDbSystemDetails.
        The total number of OCPUs available to each database instance node.


        :param instance_ocpu_count: The instance_ocpu_count of this CreateDbSystemDetails.
        :type: int
        """
        self._instance_ocpu_count = instance_ocpu_count

    @property
    def instance_memory_size_in_gbs(self):
        """
        Gets the instance_memory_size_in_gbs of this CreateDbSystemDetails.
        The total amount of memory available to each database instance node, in gigabytes.


        :return: The instance_memory_size_in_gbs of this CreateDbSystemDetails.
        :rtype: int
        """
        return self._instance_memory_size_in_gbs

    @instance_memory_size_in_gbs.setter
    def instance_memory_size_in_gbs(self, instance_memory_size_in_gbs):
        """
        Sets the instance_memory_size_in_gbs of this CreateDbSystemDetails.
        The total amount of memory available to each database instance node, in gigabytes.


        :param instance_memory_size_in_gbs: The instance_memory_size_in_gbs of this CreateDbSystemDetails.
        :type: int
        """
        self._instance_memory_size_in_gbs = instance_memory_size_in_gbs

    @property
    def instance_count(self):
        """
        Gets the instance_count of this CreateDbSystemDetails.
        Count of database instances nodes to be created in the database system.


        :return: The instance_count of this CreateDbSystemDetails.
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """
        Sets the instance_count of this CreateDbSystemDetails.
        Count of database instances nodes to be created in the database system.


        :param instance_count: The instance_count of this CreateDbSystemDetails.
        :type: int
        """
        self._instance_count = instance_count

    @property
    def instances_details(self):
        """
        Gets the instances_details of this CreateDbSystemDetails.
        Details of database instances nodes to be created. This parameter is optional.
        If specified, its size must match `instanceCount`.


        :return: The instances_details of this CreateDbSystemDetails.
        :rtype: list[oci.psql.models.CreateDbInstanceDetails]
        """
        return self._instances_details

    @instances_details.setter
    def instances_details(self, instances_details):
        """
        Sets the instances_details of this CreateDbSystemDetails.
        Details of database instances nodes to be created. This parameter is optional.
        If specified, its size must match `instanceCount`.


        :param instances_details: The instances_details of this CreateDbSystemDetails.
        :type: list[oci.psql.models.CreateDbInstanceDetails]
        """
        self._instances_details = instances_details

    @property
    def credentials(self):
        """
        Gets the credentials of this CreateDbSystemDetails.

        :return: The credentials of this CreateDbSystemDetails.
        :rtype: oci.psql.models.Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this CreateDbSystemDetails.

        :param credentials: The credentials of this CreateDbSystemDetails.
        :type: oci.psql.models.Credentials
        """
        self._credentials = credentials

    @property
    def network_details(self):
        """
        **[Required]** Gets the network_details of this CreateDbSystemDetails.

        :return: The network_details of this CreateDbSystemDetails.
        :rtype: oci.psql.models.NetworkDetails
        """
        return self._network_details

    @network_details.setter
    def network_details(self, network_details):
        """
        Sets the network_details of this CreateDbSystemDetails.

        :param network_details: The network_details of this CreateDbSystemDetails.
        :type: oci.psql.models.NetworkDetails
        """
        self._network_details = network_details

    @property
    def management_policy(self):
        """
        Gets the management_policy of this CreateDbSystemDetails.

        :return: The management_policy of this CreateDbSystemDetails.
        :rtype: oci.psql.models.ManagementPolicyDetails
        """
        return self._management_policy

    @management_policy.setter
    def management_policy(self, management_policy):
        """
        Sets the management_policy of this CreateDbSystemDetails.

        :param management_policy: The management_policy of this CreateDbSystemDetails.
        :type: oci.psql.models.ManagementPolicyDetails
        """
        self._management_policy = management_policy

    @property
    def source(self):
        """
        Gets the source of this CreateDbSystemDetails.

        :return: The source of this CreateDbSystemDetails.
        :rtype: oci.psql.models.SourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateDbSystemDetails.

        :param source: The source of this CreateDbSystemDetails.
        :type: oci.psql.models.SourceDetails
        """
        self._source = source

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDbSystemDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDbSystemDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDbSystemDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
