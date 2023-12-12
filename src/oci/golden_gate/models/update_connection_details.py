# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionDetails(object):
    """
    The information to update a Connection.
    """

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "GOLDENGATE"
    CONNECTION_TYPE_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "KAFKA"
    CONNECTION_TYPE_KAFKA = "KAFKA"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "KAFKA_SCHEMA_REGISTRY"
    CONNECTION_TYPE_KAFKA_SCHEMA_REGISTRY = "KAFKA_SCHEMA_REGISTRY"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "MYSQL"
    CONNECTION_TYPE_MYSQL = "MYSQL"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "JAVA_MESSAGE_SERVICE"
    CONNECTION_TYPE_JAVA_MESSAGE_SERVICE = "JAVA_MESSAGE_SERVICE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "MICROSOFT_SQLSERVER"
    CONNECTION_TYPE_MICROSOFT_SQLSERVER = "MICROSOFT_SQLSERVER"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    CONNECTION_TYPE_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLE"
    CONNECTION_TYPE_ORACLE = "ORACLE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "AZURE_DATA_LAKE_STORAGE"
    CONNECTION_TYPE_AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "POSTGRESQL"
    CONNECTION_TYPE_POSTGRESQL = "POSTGRESQL"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "AZURE_SYNAPSE_ANALYTICS"
    CONNECTION_TYPE_AZURE_SYNAPSE_ANALYTICS = "AZURE_SYNAPSE_ANALYTICS"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "SNOWFLAKE"
    CONNECTION_TYPE_SNOWFLAKE = "SNOWFLAKE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "AMAZON_S3"
    CONNECTION_TYPE_AMAZON_S3 = "AMAZON_S3"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "HDFS"
    CONNECTION_TYPE_HDFS = "HDFS"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLE_NOSQL"
    CONNECTION_TYPE_ORACLE_NOSQL = "ORACLE_NOSQL"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "MONGODB"
    CONNECTION_TYPE_MONGODB = "MONGODB"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "AMAZON_KINESIS"
    CONNECTION_TYPE_AMAZON_KINESIS = "AMAZON_KINESIS"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "AMAZON_REDSHIFT"
    CONNECTION_TYPE_AMAZON_REDSHIFT = "AMAZON_REDSHIFT"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "REDIS"
    CONNECTION_TYPE_REDIS = "REDIS"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ELASTICSEARCH"
    CONNECTION_TYPE_ELASTICSEARCH = "ELASTICSEARCH"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "GENERIC"
    CONNECTION_TYPE_GENERIC = "GENERIC"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "GOOGLE_CLOUD_STORAGE"
    CONNECTION_TYPE_GOOGLE_CLOUD_STORAGE = "GOOGLE_CLOUD_STORAGE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "GOOGLE_BIGQUERY"
    CONNECTION_TYPE_GOOGLE_BIGQUERY = "GOOGLE_BIGQUERY"

    #: A constant which can be used with the routing_method property of a UpdateConnectionDetails.
    #: This constant has a value of "SHARED_SERVICE_ENDPOINT"
    ROUTING_METHOD_SHARED_SERVICE_ENDPOINT = "SHARED_SERVICE_ENDPOINT"

    #: A constant which can be used with the routing_method property of a UpdateConnectionDetails.
    #: This constant has a value of "SHARED_DEPLOYMENT_ENDPOINT"
    ROUTING_METHOD_SHARED_DEPLOYMENT_ENDPOINT = "SHARED_DEPLOYMENT_ENDPOINT"

    #: A constant which can be used with the routing_method property of a UpdateConnectionDetails.
    #: This constant has a value of "DEDICATED_ENDPOINT"
    ROUTING_METHOD_DEDICATED_ENDPOINT = "DEDICATED_ENDPOINT"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.golden_gate.models.UpdateElasticsearchConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateGoogleBigQueryConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateOracleConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateAmazonRedshiftConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateOciObjectStorageConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateRedisConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateMongoDbConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateGoogleCloudStorageConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateAzureDataLakeStorageConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateAmazonKinesisConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateJavaMessageServiceConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateGoldenGateConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdatePostgresqlConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateMicrosoftSqlserverConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateOracleNosqlConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateKafkaSchemaRegistryConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateAmazonS3ConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateSnowflakeConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateHdfsConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateMysqlConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateKafkaConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateGenericConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateAzureSynapseConnectionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'ELASTICSEARCH':
            return 'UpdateElasticsearchConnectionDetails'

        if type == 'GOOGLE_BIGQUERY':
            return 'UpdateGoogleBigQueryConnectionDetails'

        if type == 'ORACLE':
            return 'UpdateOracleConnectionDetails'

        if type == 'AMAZON_REDSHIFT':
            return 'UpdateAmazonRedshiftConnectionDetails'

        if type == 'OCI_OBJECT_STORAGE':
            return 'UpdateOciObjectStorageConnectionDetails'

        if type == 'REDIS':
            return 'UpdateRedisConnectionDetails'

        if type == 'MONGODB':
            return 'UpdateMongoDbConnectionDetails'

        if type == 'GOOGLE_CLOUD_STORAGE':
            return 'UpdateGoogleCloudStorageConnectionDetails'

        if type == 'AZURE_DATA_LAKE_STORAGE':
            return 'UpdateAzureDataLakeStorageConnectionDetails'

        if type == 'AMAZON_KINESIS':
            return 'UpdateAmazonKinesisConnectionDetails'

        if type == 'JAVA_MESSAGE_SERVICE':
            return 'UpdateJavaMessageServiceConnectionDetails'

        if type == 'GOLDENGATE':
            return 'UpdateGoldenGateConnectionDetails'

        if type == 'POSTGRESQL':
            return 'UpdatePostgresqlConnectionDetails'

        if type == 'MICROSOFT_SQLSERVER':
            return 'UpdateMicrosoftSqlserverConnectionDetails'

        if type == 'ORACLE_NOSQL':
            return 'UpdateOracleNosqlConnectionDetails'

        if type == 'KAFKA_SCHEMA_REGISTRY':
            return 'UpdateKafkaSchemaRegistryConnectionDetails'

        if type == 'AMAZON_S3':
            return 'UpdateAmazonS3ConnectionDetails'

        if type == 'SNOWFLAKE':
            return 'UpdateSnowflakeConnectionDetails'

        if type == 'HDFS':
            return 'UpdateHdfsConnectionDetails'

        if type == 'MYSQL':
            return 'UpdateMysqlConnectionDetails'

        if type == 'KAFKA':
            return 'UpdateKafkaConnectionDetails'

        if type == 'GENERIC':
            return 'UpdateGenericConnectionDetails'

        if type == 'AZURE_SYNAPSE_ANALYTICS':
            return 'UpdateAzureSynapseConnectionDetails'
        else:
            return 'UpdateConnectionDetails'

    @property
    def connection_type(self):
        """
        Gets the connection_type of this UpdateConnectionDetails.
        The connection type.

        Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"


        :return: The connection_type of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this UpdateConnectionDetails.
        The connection type.


        :param connection_type: The connection_type of this UpdateConnectionDetails.
        :type: str
        """
        allowed_values = ["GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            raise ValueError(
                f"Invalid value for `connection_type`, must be None or one of {allowed_values}"
            )
        self._connection_type = connection_type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConnectionDetails.
        An object's Display Name.


        :return: The display_name of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConnectionDetails.
        An object's Display Name.


        :param display_name: The display_name of this UpdateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateConnectionDetails.
        Metadata about this specific object.


        :return: The description of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateConnectionDetails.
        Metadata about this specific object.


        :param description: The description of this UpdateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateConnectionDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateConnectionDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateConnectionDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateConnectionDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def vault_id(self):
        """
        Gets the vault_id of this UpdateConnectionDetails.
        Refers to the customer's vault OCID.
        If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
        to manage secrets contained within this vault.


        :return: The vault_id of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this UpdateConnectionDetails.
        Refers to the customer's vault OCID.
        If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
        to manage secrets contained within this vault.


        :param vault_id: The vault_id of this UpdateConnectionDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this UpdateConnectionDetails.
        Refers to the customer's master key OCID.
        If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.


        :return: The key_id of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this UpdateConnectionDetails.
        Refers to the customer's master key OCID.
        If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.


        :param key_id: The key_id of this UpdateConnectionDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateConnectionDetails.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :return: The nsg_ids of this UpdateConnectionDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateConnectionDetails.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :param nsg_ids: The nsg_ids of this UpdateConnectionDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this UpdateConnectionDetails.
        The `OCID`__ of the target subnet of the dedicated connection.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this UpdateConnectionDetails.
        The `OCID`__ of the target subnet of the dedicated connection.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this UpdateConnectionDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def routing_method(self):
        """
        Gets the routing_method of this UpdateConnectionDetails.
        Controls the network traffic direction to the target:
        SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets.
        SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet.
        DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.

        Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"


        :return: The routing_method of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._routing_method

    @routing_method.setter
    def routing_method(self, routing_method):
        """
        Sets the routing_method of this UpdateConnectionDetails.
        Controls the network traffic direction to the target:
        SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets.
        SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet.
        DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.


        :param routing_method: The routing_method of this UpdateConnectionDetails.
        :type: str
        """
        allowed_values = ["SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"]
        if not value_allowed_none_or_none_sentinel(routing_method, allowed_values):
            raise ValueError(
                f"Invalid value for `routing_method`, must be None or one of {allowed_values}"
            )
        self._routing_method = routing_method

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
