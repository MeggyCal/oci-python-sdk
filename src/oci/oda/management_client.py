# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import oda_type_mapping
missing = Sentinel("Missing")


class ManagementClient(object):
    """
    API to create and maintain Oracle Digital Assistant service instances.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        :param obj circuit_breaker_strategy: (optional)
            A circuit breaker strategy to apply to all calls made by this service client (i.e. at the client level).
            This client uses :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` as default if no circuit breaker strategy is provided.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.

        :param bool client_level_realm_specific_endpoint_template_enabled: (optional)
            A boolean flag to indicate whether or not this client should be created with realm specific endpoint template enabled or disable. By default, this will be set as None.

        :param allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this client should allow control characters in the response object. By default, the client will not
            allow control characters to be in the response object.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20190506',
            'service_endpoint_template': 'https://digitalassistant-api.{region}.oci.{secondLevelDomain}',
            'service_endpoint_template_per_realm': {  },  # noqa: E201 E202
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY),
            'client_level_realm_specific_endpoint_template_enabled': kwargs.get('client_level_realm_specific_endpoint_template_enabled')
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("management", config, signer, oda_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def change_oda_private_endpoint_compartment(self, oda_private_endpoint_id, change_oda_private_endpoint_compartment_details, **kwargs):
        """
        Starts an asynchronous job to move the specified ODA Private Endpoint into a different compartment.

        To monitor the status of the job, take the `opc-work-request-id` response header
        value and use it to call `GET /workRequests/{workRequestID}`.
        When provided, If-Match is checked against ETag values of the resource.


        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.oda.models.ChangeOdaPrivateEndpointCompartmentDetails change_oda_private_endpoint_compartment_details: (required)
            The compartment to which the Digital Assistant instance should be moved.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/change_oda_private_endpoint_compartment.py.html>`__ to see an example of how to use change_oda_private_endpoint_compartment API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_oda_private_endpoint_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpoint/ChangeOdaPrivateEndpointCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_oda_private_endpoint_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_oda_private_endpoint_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_oda_private_endpoint_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def configure_digital_assistant_parameters(self, oda_instance_id, configure_digital_assistant_parameters_details, **kwargs):
        """
        This will store the provided parameters in the Digital Assistant instance and update any Digital Assistants with matching parameters.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.ConfigureDigitalAssistantParametersDetails configure_digital_assistant_parameters_details: (required)
            The parameter values to use.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/configure_digital_assistant_parameters.py.html>`__ to see an example of how to use configure_digital_assistant_parameters API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/actions/configureDigitalAssistantParameters"
        method = "POST"
        operation_name = "configure_digital_assistant_parameters"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistantParameter/ConfigureDigitalAssistantParameters"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "configure_digital_assistant_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=configure_digital_assistant_parameters_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=configure_digital_assistant_parameters_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_authentication_provider(self, oda_instance_id, create_authentication_provider_details, **kwargs):
        """
        Creates a new Authentication Provider


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.CreateAuthenticationProviderDetails create_authentication_provider_details: (required)
            Property values required to create the new Authentication Provider.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.AuthenticationProvider`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_authentication_provider.py.html>`__ to see an example of how to use create_authentication_provider API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/authenticationProviders"
        method = "POST"
        operation_name = "create_authentication_provider"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/AuthenticationProvider/CreateAuthenticationProvider"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_authentication_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_authentication_provider_details,
                response_type="AuthenticationProvider",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_authentication_provider_details,
                response_type="AuthenticationProvider",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_channel(self, oda_instance_id, create_channel_details, **kwargs):
        """
        Creates a new Channel.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.CreateChannelDetails create_channel_details: (required)
            Property values for creating the new Channel.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.CreateChannelResult`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_channel.py.html>`__ to see an example of how to use create_channel API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/channels"
        method = "POST"
        operation_name = "create_channel"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/CreateChannel"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_channel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_channel_details,
                response_type="CreateChannelResult",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_channel_details,
                response_type="CreateChannelResult",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_digital_assistant(self, oda_instance_id, create_digital_assistant_details, **kwargs):
        """
        Creates a new Digital Assistant.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.CreateDigitalAssistantDetails create_digital_assistant_details: (required)
            Property values for creating the new Digital Assistant.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_digital_assistant.py.html>`__ to see an example of how to use create_digital_assistant API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants"
        method = "POST"
        operation_name = "create_digital_assistant"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistant/CreateDigitalAssistant"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_digital_assistant got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_digital_assistant_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_digital_assistant_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_oda_private_endpoint(self, create_oda_private_endpoint_details, **kwargs):
        """
        Starts an asynchronous job to create an ODA Private Endpoint.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestID}`.


        :param oci.oda.models.CreateOdaPrivateEndpointDetails create_oda_private_endpoint_details: (required)
            Details for the new ODA Private Endpoint.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_oda_private_endpoint.py.html>`__ to see an example of how to use create_oda_private_endpoint API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = []
        resource_path = "/odaPrivateEndpoints"
        method = "POST"
        operation_name = "create_oda_private_endpoint"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_oda_private_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_oda_private_endpoint_details,
                response_type="OdaPrivateEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_oda_private_endpoint_details,
                response_type="OdaPrivateEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_oda_private_endpoint_attachment(self, create_oda_private_endpoint_attachment_details, **kwargs):
        """
        Starts an asynchronous job to create an ODA Private Endpoint Attachment.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestID}`.


        :param oci.oda.models.CreateOdaPrivateEndpointAttachmentDetails create_oda_private_endpoint_attachment_details: (required)
            Details for the new ODA Private Endpoint Attachment.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointAttachment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_oda_private_endpoint_attachment.py.html>`__ to see an example of how to use create_oda_private_endpoint_attachment API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = []
        resource_path = "/odaPrivateEndpointAttachments"
        method = "POST"
        operation_name = "create_oda_private_endpoint_attachment"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_oda_private_endpoint_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_oda_private_endpoint_attachment_details,
                response_type="OdaPrivateEndpointAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_oda_private_endpoint_attachment_details,
                response_type="OdaPrivateEndpointAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_oda_private_endpoint_scan_proxy(self, create_oda_private_endpoint_scan_proxy_details, oda_private_endpoint_id, **kwargs):
        """
        Starts an asynchronous job to create an ODA Private Endpoint Scan Proxy.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestID}`.


        :param oci.oda.models.CreateOdaPrivateEndpointScanProxyDetails create_oda_private_endpoint_scan_proxy_details: (required)
            Details for the new ODA Private Endpoint Scan Proxy.

        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointScanProxy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_oda_private_endpoint_scan_proxy.py.html>`__ to see an example of how to use create_oda_private_endpoint_scan_proxy API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}/odaPrivateEndpointScanProxies"
        method = "POST"
        operation_name = "create_oda_private_endpoint_scan_proxy"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_oda_private_endpoint_scan_proxy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_oda_private_endpoint_scan_proxy_details,
                response_type="OdaPrivateEndpointScanProxy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_oda_private_endpoint_scan_proxy_details,
                response_type="OdaPrivateEndpointScanProxy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_skill(self, oda_instance_id, create_skill_details, **kwargs):
        """
        Creates a new Skill from scratch.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.CreateSkillDetails create_skill_details: (required)
            Property values for creating the Skill.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_skill.py.html>`__ to see an example of how to use create_skill API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/skills"
        method = "POST"
        operation_name = "create_skill"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/CreateSkill"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_skill got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_skill_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_skill_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_skill_parameter(self, oda_instance_id, skill_id, create_skill_parameter_details, **kwargs):
        """
        Creates a new Skill Parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param oci.oda.models.CreateSkillParameterDetails create_skill_parameter_details: (required)
            Property values for creating the new Skill Parameter.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.SkillParameter`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_skill_parameter.py.html>`__ to see an example of how to use create_skill_parameter API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/parameters"
        method = "POST"
        operation_name = "create_skill_parameter"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/SkillParameter/CreateSkillParameter"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_skill_parameter got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_skill_parameter_details,
                response_type="SkillParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_skill_parameter_details,
                response_type="SkillParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def create_translator(self, oda_instance_id, create_translator_details, **kwargs):
        """
        Creates a new Translator


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.CreateTranslatorDetails create_translator_details: (required)
            Property values to create the new Translator.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Translator`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_translator.py.html>`__ to see an example of how to use create_translator API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/translators"
        method = "POST"
        operation_name = "create_translator"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Translator/CreateTranslator"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_translator got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_translator_details,
                response_type="Translator",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_translator_details,
                response_type="Translator",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_authentication_provider(self, oda_instance_id, authentication_provider_id, **kwargs):
        """
        Delete the specified Authentication Provider.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str authentication_provider_id: (required)
            Unique Authentication Provider identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_authentication_provider.py.html>`__ to see an example of how to use delete_authentication_provider API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'authenticationProviderId']
        resource_path = "/odaInstances/{odaInstanceId}/authenticationProviders/{authenticationProviderId}"
        method = "DELETE"
        operation_name = "delete_authentication_provider"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/AuthenticationProvider/DeleteAuthenticationProvider"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_authentication_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "authenticationProviderId": authentication_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_channel(self, oda_instance_id, channel_id, **kwargs):
        """
        Delete the specified Channel.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str channel_id: (required)
            Unique Channel identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_channel.py.html>`__ to see an example of how to use delete_channel API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'channelId']
        resource_path = "/odaInstances/{odaInstanceId}/channels/{channelId}"
        method = "DELETE"
        operation_name = "delete_channel"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/DeleteChannel"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_channel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "channelId": channel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_digital_assistant(self, oda_instance_id, digital_assistant_id, **kwargs):
        """
        Delete the specified Digital Assistant.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_digital_assistant.py.html>`__ to see an example of how to use delete_digital_assistant API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}"
        method = "DELETE"
        operation_name = "delete_digital_assistant"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistant/DeleteDigitalAssistant"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_digital_assistant got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_oda_private_endpoint(self, oda_private_endpoint_id, **kwargs):
        """
        Starts an asynchronous job to delete the specified ODA Private Endpoint.
        To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.


        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_oda_private_endpoint.py.html>`__ to see an example of how to use delete_oda_private_endpoint API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}"
        method = "DELETE"
        operation_name = "delete_oda_private_endpoint"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpoint/DeleteOdaPrivateEndpoint"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_oda_private_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_oda_private_endpoint_attachment(self, oda_private_endpoint_attachment_id, **kwargs):
        """
        Starts an asynchronous job to delete the specified ODA Private Endpoint Attachment.
        To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.


        :param str oda_private_endpoint_attachment_id: (required)
            The `OCID`__ of ODA Private Endpoint Attachment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_oda_private_endpoint_attachment.py.html>`__ to see an example of how to use delete_oda_private_endpoint_attachment API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointAttachmentId']
        resource_path = "/odaPrivateEndpointAttachments/{odaPrivateEndpointAttachmentId}"
        method = "DELETE"
        operation_name = "delete_oda_private_endpoint_attachment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpointAttachment/DeleteOdaPrivateEndpointAttachment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_oda_private_endpoint_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointAttachmentId": oda_private_endpoint_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_oda_private_endpoint_scan_proxy(self, oda_private_endpoint_scan_proxy_id, oda_private_endpoint_id, **kwargs):
        """
        Starts an asynchronous job to delete the specified ODA Private Endpoint Scan Proxy.
        To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.


        :param str oda_private_endpoint_scan_proxy_id: (required)
            Unique ODA Private Endpoint Scan Proxy identifier.

        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_oda_private_endpoint_scan_proxy.py.html>`__ to see an example of how to use delete_oda_private_endpoint_scan_proxy API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointScanProxyId', 'odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}/odaPrivateEndpointScanProxies/{odaPrivateEndpointScanProxyId}"
        method = "DELETE"
        operation_name = "delete_oda_private_endpoint_scan_proxy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpointScanProxy/DeleteOdaPrivateEndpointScanProxy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_oda_private_endpoint_scan_proxy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointScanProxyId": oda_private_endpoint_scan_proxy_id,
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_skill(self, oda_instance_id, skill_id, **kwargs):
        """
        Delete the specified Skill.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_skill.py.html>`__ to see an example of how to use delete_skill API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}"
        method = "DELETE"
        operation_name = "delete_skill"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/DeleteSkill"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_skill got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_skill_parameter(self, oda_instance_id, skill_id, parameter_name, **kwargs):
        """
        Delete the specified Skill Parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str parameter_name: (required)
            The name of a Skill Parameter.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_skill_parameter.py.html>`__ to see an example of how to use delete_skill_parameter API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId', 'parameterName']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/parameters/{parameterName}"
        method = "DELETE"
        operation_name = "delete_skill_parameter"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/SkillParameter/DeleteSkillParameter"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_skill_parameter got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id,
            "parameterName": parameter_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_translator(self, oda_instance_id, translator_id, **kwargs):
        """
        Delete the specified Translator.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str translator_id: (required)
            Unique Translator identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_translator.py.html>`__ to see an example of how to use delete_translator API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'translatorId']
        resource_path = "/odaInstances/{odaInstanceId}/translators/{translatorId}"
        method = "DELETE"
        operation_name = "delete_translator"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Translator/DeleteTranslator"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_translator got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "translatorId": translator_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def export_digital_assistant(self, oda_instance_id, digital_assistant_id, export_digital_assistant_details, **kwargs):
        """
        Exports the specified Digital Assistant as an archive to Object Storage.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param oci.oda.models.ExportDigitalAssistantDetails export_digital_assistant_details: (required)
            Where in Object Storage to export the Digital Assistant to.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/export_digital_assistant.py.html>`__ to see an example of how to use export_digital_assistant API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}/actions/export"
        method = "POST"
        operation_name = "export_digital_assistant"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/ExportDigitalAssistant"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "export_digital_assistant got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=export_digital_assistant_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=export_digital_assistant_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def export_skill(self, oda_instance_id, skill_id, export_skill_details, **kwargs):
        """
        Exports the specified Skill as an archive to Object Storage.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param oci.oda.models.ExportSkillDetails export_skill_details: (required)
            Where in Object Storage to export the Skill to.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/export_skill.py.html>`__ to see an example of how to use export_skill API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/actions/export"
        method = "POST"
        operation_name = "export_skill"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/ExportSkill"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "export_skill got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=export_skill_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=export_skill_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_authentication_provider(self, oda_instance_id, authentication_provider_id, **kwargs):
        """
        Gets the specified Authentication Provider.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str authentication_provider_id: (required)
            Unique Authentication Provider identifier.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.AuthenticationProvider`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_authentication_provider.py.html>`__ to see an example of how to use get_authentication_provider API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'authenticationProviderId']
        resource_path = "/odaInstances/{odaInstanceId}/authenticationProviders/{authenticationProviderId}"
        method = "GET"
        operation_name = "get_authentication_provider"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/AuthenticationProvider/GetAuthenticationProvider"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_authentication_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "authenticationProviderId": authentication_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AuthenticationProvider",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AuthenticationProvider",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_channel(self, oda_instance_id, channel_id, **kwargs):
        """
        Gets the specified Channel.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str channel_id: (required)
            Unique Channel identifier.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Channel`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_channel.py.html>`__ to see an example of how to use get_channel API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'channelId']
        resource_path = "/odaInstances/{odaInstanceId}/channels/{channelId}"
        method = "GET"
        operation_name = "get_channel"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/GetChannel"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_channel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "channelId": channel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_digital_assistant(self, oda_instance_id, digital_assistant_id, **kwargs):
        """
        Gets the specified Digital Assistant.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistant`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_digital_assistant.py.html>`__ to see an example of how to use get_digital_assistant API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}"
        method = "GET"
        operation_name = "get_digital_assistant"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistant/GetDigitalAssistant"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_digital_assistant got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DigitalAssistant",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DigitalAssistant",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_digital_assistant_parameter(self, oda_instance_id, digital_assistant_id, parameter_name, **kwargs):
        """
        Gets the specified Digital Assistant Parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param str parameter_name: (required)
            The name of a Digital Assistant Parameter.  This is unique with the Digital Assistant.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistantParameter`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_digital_assistant_parameter.py.html>`__ to see an example of how to use get_digital_assistant_parameter API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId', 'parameterName']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}/parameters/{parameterName}"
        method = "GET"
        operation_name = "get_digital_assistant_parameter"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistantParameter/GetDigitalAssistantParameter"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_digital_assistant_parameter got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id,
            "parameterName": parameter_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DigitalAssistantParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DigitalAssistantParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_oda_private_endpoint(self, oda_private_endpoint_id, **kwargs):
        """
        Gets the specified ODA Private Endpoint.


        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_oda_private_endpoint.py.html>`__ to see an example of how to use get_oda_private_endpoint API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}"
        method = "GET"
        operation_name = "get_oda_private_endpoint"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpoint/GetOdaPrivateEndpoint"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_oda_private_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OdaPrivateEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OdaPrivateEndpoint",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_oda_private_endpoint_attachment(self, oda_private_endpoint_attachment_id, **kwargs):
        """
        Gets the specified ODA Private Endpoint Attachment.


        :param str oda_private_endpoint_attachment_id: (required)
            The `OCID`__ of ODA Private Endpoint Attachment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointAttachment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_oda_private_endpoint_attachment.py.html>`__ to see an example of how to use get_oda_private_endpoint_attachment API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointAttachmentId']
        resource_path = "/odaPrivateEndpointAttachments/{odaPrivateEndpointAttachmentId}"
        method = "GET"
        operation_name = "get_oda_private_endpoint_attachment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpointAttachment/GetOdaPrivateEndpointAttachment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_oda_private_endpoint_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointAttachmentId": oda_private_endpoint_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointAttachment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_oda_private_endpoint_scan_proxy(self, oda_private_endpoint_scan_proxy_id, oda_private_endpoint_id, **kwargs):
        """
        Gets the specified ODA Private Endpoint Scan Proxy.


        :param str oda_private_endpoint_scan_proxy_id: (required)
            Unique ODA Private Endpoint Scan Proxy identifier.

        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointScanProxy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_oda_private_endpoint_scan_proxy.py.html>`__ to see an example of how to use get_oda_private_endpoint_scan_proxy API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointScanProxyId', 'odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}/odaPrivateEndpointScanProxies/{odaPrivateEndpointScanProxyId}"
        method = "GET"
        operation_name = "get_oda_private_endpoint_scan_proxy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpointScanProxy/GetOdaPrivateEndpointScanProxy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_oda_private_endpoint_scan_proxy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointScanProxyId": oda_private_endpoint_scan_proxy_id,
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointScanProxy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointScanProxy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_skill(self, oda_instance_id, skill_id, **kwargs):
        """
        Gets the specified Skill.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Skill`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_skill.py.html>`__ to see an example of how to use get_skill API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}"
        method = "GET"
        operation_name = "get_skill"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/GetSkill"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_skill got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Skill",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Skill",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_skill_parameter(self, oda_instance_id, skill_id, parameter_name, **kwargs):
        """
        Gets the specified Skill Parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str parameter_name: (required)
            The name of a Skill Parameter.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.SkillParameter`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_skill_parameter.py.html>`__ to see an example of how to use get_skill_parameter API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId', 'parameterName']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/parameters/{parameterName}"
        method = "GET"
        operation_name = "get_skill_parameter"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/SkillParameter/GetSkillParameter"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_skill_parameter got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id,
            "parameterName": parameter_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="SkillParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="SkillParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_translator(self, oda_instance_id, translator_id, **kwargs):
        """
        Gets the specified Translator.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str translator_id: (required)
            Unique Translator identifier.

        :param str if_none_match: (optional)
            The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the
            requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Translator`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_translator.py.html>`__ to see an example of how to use get_translator API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'translatorId']
        resource_path = "/odaInstances/{odaInstanceId}/translators/{translatorId}"
        method = "GET"
        operation_name = "get_translator"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Translator/GetTranslator"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_translator got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "translatorId": translator_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Translator",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Translator",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def import_bot(self, oda_instance_id, import_bot_details, **kwargs):
        """
        Import a Bot archive from Object Storage.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param oci.oda.models.ImportBotDetails import_bot_details: (required)
            Properties for where in Object Storage to import the Bot archive from.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/import_bot.py.html>`__ to see an example of how to use import_bot API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/actions/importBot"
        method = "POST"
        operation_name = "import_bot"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Bot/ImportBot"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "import_bot got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=import_bot_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=import_bot_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_authentication_providers(self, oda_instance_id, **kwargs):
        """
        Returns a page of Authentication Providers that belong to the specified Digital Assistant instance.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str id: (optional)
            Unique Authentication Provider identifier.

        :param str identity_provider: (optional)
            List only Authentication Providers for this Identity Provider.

            Allowed values are: "GENERIC", "OAM", "GOOGLE", "MICROSOFT"

        :param str name: (optional)
            List only the information for Authentication Providers with this name. Authentication Provider names are unique and may not change.

            Example: `MyProvider`

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

            The default sort order for `timeCreated` and `timeUpdated` is descending.
            For all other sort fields the default sort order is ascending.

            Allowed values are: "timeCreated", "timeUpdated", "name", "identityProvider"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.AuthenticationProviderCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_authentication_providers.py.html>`__ to see an example of how to use list_authentication_providers API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/authenticationProviders"
        method = "GET"
        operation_name = "list_authentication_providers"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/AuthenticationProvider/ListAuthenticationProviders"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "id",
            "identity_provider",
            "name",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_authentication_providers got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'identity_provider' in kwargs:
            identity_provider_allowed_values = ["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]
            if kwargs['identity_provider'] not in identity_provider_allowed_values:
                raise ValueError(
                    "Invalid value for `identity_provider`, must be one of {0}".format(identity_provider_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "timeUpdated", "name", "identityProvider"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "id": kwargs.get("id", missing),
            "identityProvider": kwargs.get("identity_provider", missing),
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AuthenticationProviderCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AuthenticationProviderCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_channels(self, oda_instance_id, **kwargs):
        """
        Returns a page of Channels that belong to the specified Digital Assistant instance.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str id: (optional)
            Unique Channel identifier.

        :param str name: (optional)
            List only the information for Channels with this name. Channels names are unique and may not change.

            Example: `MyChannel`

        :param str category: (optional)
            List only Channels with this category.

            Allowed values are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"

        :param str type: (optional)
            List only Channels of this type.

            Allowed values are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

            The default sort order for `timeCreated` and `timeUpdated` is descending, and the default sort order for `name` is ascending.

            Allowed values are: "timeCreated", "timeUpdated", "name"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.ChannelCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_channels.py.html>`__ to see an example of how to use list_channels API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/channels"
        method = "GET"
        operation_name = "list_channels"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/ListChannels"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "id",
            "name",
            "category",
            "type",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_channels got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'category' in kwargs:
            category_allowed_values = ["AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"]
            if kwargs['category'] not in category_allowed_values:
                raise ValueError(
                    "Invalid value for `category`, must be one of {0}".format(category_allowed_values)
                )

        if 'type' in kwargs:
            type_allowed_values = ["ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"]
            if kwargs['type'] not in type_allowed_values:
                raise ValueError(
                    "Invalid value for `type`, must be one of {0}".format(type_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "timeUpdated", "name"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "id": kwargs.get("id", missing),
            "name": kwargs.get("name", missing),
            "category": kwargs.get("category", missing),
            "type": kwargs.get("type", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ChannelCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ChannelCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_digital_assistant_parameters(self, oda_instance_id, digital_assistant_id, **kwargs):
        """
        Returns a page of Parameters that belong to the specified Digital Assistant.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param str name: (optional)
            List only Parameters with this name.

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `name`.

            The default sort order is ascending.

            Allowed values are: "name", "displayName", "type"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistantParameterCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_digital_assistant_parameters.py.html>`__ to see an example of how to use list_digital_assistant_parameters API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}/parameters"
        method = "GET"
        operation_name = "list_digital_assistant_parameters"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistantParameter/ListDigitalAssistantParameters"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "name",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_digital_assistant_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "displayName", "type"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DigitalAssistantParameterCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DigitalAssistantParameterCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_digital_assistants(self, oda_instance_id, **kwargs):
        """
        Returns a page of Digital Assistants that belong to the specified Digital Assistant instance.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str id: (optional)
            Unique Digital Assistant identifier.

        :param str category: (optional)
            List only Bot resources with this category.

        :param str name: (optional)
            List only Bot resources with this name. Names are unique and may not change.

            Example: `MySkill`

        :param str version: (optional)
            List only Bot resources with this version. Versions are unique and may not change.

            Example: `1.0`

        :param str namespace: (optional)
            List only Bot resources with this namespace. Namespaces may not change.

            Example: `MyNamespace`

        :param str platform_version: (optional)
            List only Bot resources with this platform version.

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param str lifecycle_details: (optional)
            List only Bot resources with this lifecycle details.

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

            The default sort order for `timeCreated` and `timeUpdated` is descending.
            For all other sort fields the default sort order is ascending.

            Allowed values are: "timeCreated", "timeUpdated", "name"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistantCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_digital_assistants.py.html>`__ to see an example of how to use list_digital_assistants API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants"
        method = "GET"
        operation_name = "list_digital_assistants"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistant/ListDigitalAssistants"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "id",
            "category",
            "name",
            "version",
            "namespace",
            "platform_version",
            "lifecycle_state",
            "lifecycle_details",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_digital_assistants got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "timeUpdated", "name"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "id": kwargs.get("id", missing),
            "category": kwargs.get("category", missing),
            "name": kwargs.get("name", missing),
            "version": kwargs.get("version", missing),
            "namespace": kwargs.get("namespace", missing),
            "platformVersion": kwargs.get("platform_version", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "lifecycleDetails": kwargs.get("lifecycle_details", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DigitalAssistantCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DigitalAssistantCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_oda_private_endpoint_attachments(self, oda_private_endpoint_id, compartment_id, **kwargs):
        """
        Returns a page of ODA Instances attached to this ODA Private Endpoint.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_private_endpoint_id: (required)
            The `OCID`__ of ODA Private Endpoint.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (required)
            List the ODA Private Endpoint Attachments that belong to this compartment.

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str lifecycle_state: (optional)
            List only the ODA Private Endpoint Attachments that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

            The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointAttachmentCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_oda_private_endpoint_attachments.py.html>`__ to see an example of how to use list_oda_private_endpoint_attachments API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId', 'compartmentId']
        resource_path = "/odaPrivateEndpointAttachments"
        method = "GET"
        operation_name = "list_oda_private_endpoint_attachments"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpointAttachment/ListOdaPrivateEndpointAttachments"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_oda_private_endpoint_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id,
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointAttachmentCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointAttachmentCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_oda_private_endpoint_scan_proxies(self, oda_private_endpoint_id, **kwargs):
        """
        Returns a page of ODA Private Endpoint Scan Proxies that belong to the specified
        ODA Private Endpoint.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str lifecycle_state: (optional)
            List only the ODA Private Endpoint Scan Proxies that are in this lifecycle state.

            Allowed values are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

            The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointScanProxyCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_oda_private_endpoint_scan_proxies.py.html>`__ to see an example of how to use list_oda_private_endpoint_scan_proxies API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}/odaPrivateEndpointScanProxies"
        method = "GET"
        operation_name = "list_oda_private_endpoint_scan_proxies"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpointScanProxy/ListOdaPrivateEndpointScanProxies"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_oda_private_endpoint_scan_proxies got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointScanProxyCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointScanProxyCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_oda_private_endpoints(self, compartment_id, **kwargs):
        """
        Returns a page of ODA Private Endpoints that belong to the specified
        compartment.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str compartment_id: (required)
            List the ODA Private Endpoints that belong to this compartment.

        :param str display_name: (optional)
            List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change.

            Example: `My new resource`

        :param str lifecycle_state: (optional)
            List only the ODA Private Endpoints that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

            The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.OdaPrivateEndpointCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_oda_private_endpoints.py.html>`__ to see an example of how to use list_oda_private_endpoints API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['compartmentId']
        resource_path = "/odaPrivateEndpoints"
        method = "GET"
        operation_name = "list_oda_private_endpoints"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpoint/ListOdaPrivateEndpoints"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "display_name",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_oda_private_endpoints got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OdaPrivateEndpointCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_skill_parameters(self, oda_instance_id, skill_id, **kwargs):
        """
        Returns a page of Skill Parameters that belong to the specified Skill.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str name: (optional)
            List only Parameters with this name.

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `name`.

            The default sort order is ascending.

            Allowed values are: "name", "displayName", "type"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.SkillParameterCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_skill_parameters.py.html>`__ to see an example of how to use list_skill_parameters API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/parameters"
        method = "GET"
        operation_name = "list_skill_parameters"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/SkillParameter/ListSkillParameters"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "name",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_skill_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "displayName", "type"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SkillParameterCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SkillParameterCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_skills(self, oda_instance_id, **kwargs):
        """
        Returns a page of Skills that belong to the specified Digital Assistant instance.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str id: (optional)
            Unique Skill identifier.

        :param str category: (optional)
            List only Bot resources with this category.

        :param str name: (optional)
            List only Bot resources with this name. Names are unique and may not change.

            Example: `MySkill`

        :param str version: (optional)
            List only Bot resources with this version. Versions are unique and may not change.

            Example: `1.0`

        :param str namespace: (optional)
            List only Bot resources with this namespace. Namespaces may not change.

            Example: `MyNamespace`

        :param str platform_version: (optional)
            List only Bot resources with this platform version.

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param str lifecycle_details: (optional)
            List only Bot resources with this lifecycle details.

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

            The default sort order for `timeCreated` and `timeUpdated` is descending.
            For all other sort fields the default sort order is ascending.

            Allowed values are: "timeCreated", "timeUpdated", "name"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.SkillCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_skills.py.html>`__ to see an example of how to use list_skills API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/skills"
        method = "GET"
        operation_name = "list_skills"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/ListSkills"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "id",
            "category",
            "name",
            "version",
            "namespace",
            "platform_version",
            "lifecycle_state",
            "lifecycle_details",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_skills got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "timeUpdated", "name"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "id": kwargs.get("id", missing),
            "category": kwargs.get("category", missing),
            "name": kwargs.get("name", missing),
            "version": kwargs.get("version", missing),
            "namespace": kwargs.get("namespace", missing),
            "platformVersion": kwargs.get("platform_version", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "lifecycleDetails": kwargs.get("lifecycle_details", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SkillCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SkillCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_translators(self, oda_instance_id, **kwargs):
        """
        Returns a page of Translators that belong to the specified Digital Assistant instance.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str id: (optional)
            Unique Translator identifier.

        :param str type: (optional)
            List only Translators of this type.

            Allowed values are: "GOOGLE", "MICROSOFT"

        :param str name: (optional)
            List only Translators with this name. Translator names are unique and may not change.

            Example: `MyTranslator`

        :param str lifecycle_state: (optional)
            List only the resources that are in this lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

            The default sort order for `timeCreated` and `timeUpdated` is descending.
            For all other sort fields the default sort order is ascending.

            Allowed values are: "timeCreated", "timeUpdated", "name", "type"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.TranslatorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_translators.py.html>`__ to see an example of how to use list_translators API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/translators"
        method = "GET"
        operation_name = "list_translators"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Translator/ListTranslators"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "id",
            "type",
            "name",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_translators got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'type' in kwargs:
            type_allowed_values = ["GOOGLE", "MICROSOFT"]
            if kwargs['type'] not in type_allowed_values:
                raise ValueError(
                    "Invalid value for `type`, must be one of {0}".format(type_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "timeUpdated", "name", "type"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "id": kwargs.get("id", missing),
            "type": kwargs.get("type", missing),
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TranslatorCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TranslatorCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def publish_digital_assistant(self, oda_instance_id, digital_assistant_id, **kwargs):
        """
        Publish a draft Digital Assistant.
        Once published the Digital Assistant cannot be modified.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistant`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/publish_digital_assistant.py.html>`__ to see an example of how to use publish_digital_assistant API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}/actions/publish"
        method = "POST"
        operation_name = "publish_digital_assistant"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistant/PublishDigitalAssistant"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "publish_digital_assistant got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DigitalAssistant",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DigitalAssistant",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def publish_skill(self, oda_instance_id, skill_id, **kwargs):
        """
        Publish a draft Skill.
        Once published it cannot be modified.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Skill`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/publish_skill.py.html>`__ to see an example of how to use publish_skill API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/actions/publish"
        method = "POST"
        operation_name = "publish_skill"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/PublishSkill"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "publish_skill got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Skill",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Skill",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def rotate_channel_keys(self, oda_instance_id, channel_id, **kwargs):
        """
        This will generate new keys for any generated keys in the Channel (eg. secretKey, verifyToken).
        If a Channel has no generated keys then no changes will be made.
        Ensure that you take note of the newly generated keys in the response as they will not be returned again.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str channel_id: (required)
            Unique Channel identifier.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.CreateChannelResult`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/rotate_channel_keys.py.html>`__ to see an example of how to use rotate_channel_keys API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'channelId']
        resource_path = "/odaInstances/{odaInstanceId}/channels/{channelId}/actions/rotateKeys"
        method = "POST"
        operation_name = "rotate_channel_keys"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/RotateChannelKeys"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "rotate_channel_keys got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "channelId": channel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CreateChannelResult",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CreateChannelResult",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def start_channel(self, oda_instance_id, channel_id, **kwargs):
        """
        Starts a Channel so that it will begin accepting messages.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str channel_id: (required)
            Unique Channel identifier.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Channel`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/start_channel.py.html>`__ to see an example of how to use start_channel API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'channelId']
        resource_path = "/odaInstances/{odaInstanceId}/channels/{channelId}/actions/start"
        method = "POST"
        operation_name = "start_channel"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/StartChannel"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "start_channel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "channelId": channel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def stop_channel(self, oda_instance_id, channel_id, **kwargs):
        """
        Stops a Channel so that it will no longer accept messages.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str channel_id: (required)
            Unique Channel identifier.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Channel`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/stop_channel.py.html>`__ to see an example of how to use stop_channel API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'channelId']
        resource_path = "/odaInstances/{odaInstanceId}/channels/{channelId}/actions/stop"
        method = "POST"
        operation_name = "stop_channel"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/StopChannel"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "stop_channel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "channelId": channel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_authentication_provider(self, oda_instance_id, authentication_provider_id, update_authentication_provider_details, **kwargs):
        """
        Updates the specified Authentication Provider with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str authentication_provider_id: (required)
            Unique Authentication Provider identifier.

        :param oci.oda.models.UpdateAuthenticationProviderDetails update_authentication_provider_details: (required)
            Property values to update the Authentication Provider.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.AuthenticationProvider`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_authentication_provider.py.html>`__ to see an example of how to use update_authentication_provider API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'authenticationProviderId']
        resource_path = "/odaInstances/{odaInstanceId}/authenticationProviders/{authenticationProviderId}"
        method = "PUT"
        operation_name = "update_authentication_provider"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/AuthenticationProvider/UpdateAuthenticationProvider"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_authentication_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "authenticationProviderId": authentication_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_authentication_provider_details,
                response_type="AuthenticationProvider",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_authentication_provider_details,
                response_type="AuthenticationProvider",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_channel(self, oda_instance_id, channel_id, update_channel_details, **kwargs):
        """
        Updates the specified Channel with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str channel_id: (required)
            Unique Channel identifier.

        :param oci.oda.models.UpdateChannelDetails update_channel_details: (required)
            Property values to update the Channel.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Channel`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_channel.py.html>`__ to see an example of how to use update_channel API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'channelId']
        resource_path = "/odaInstances/{odaInstanceId}/channels/{channelId}"
        method = "PUT"
        operation_name = "update_channel"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Channel/UpdateChannel"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_channel got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "channelId": channel_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_channel_details,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_channel_details,
                response_type="Channel",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_digital_assistant(self, oda_instance_id, digital_assistant_id, update_digital_assistant_details, **kwargs):
        """
        Updates the specified Digital Assistant with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param oci.oda.models.UpdateDigitalAssistantDetails update_digital_assistant_details: (required)
            Property values to update the Digital Assistant.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistant`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_digital_assistant.py.html>`__ to see an example of how to use update_digital_assistant API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}"
        method = "PUT"
        operation_name = "update_digital_assistant"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistant/UpdateDigitalAssistant"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_digital_assistant got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_digital_assistant_details,
                response_type="DigitalAssistant",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_digital_assistant_details,
                response_type="DigitalAssistant",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_digital_assistant_parameter(self, oda_instance_id, digital_assistant_id, parameter_name, update_digital_assistant_parameter_details, **kwargs):
        """
        Updates the specified Digital Assistant Parameter with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str digital_assistant_id: (required)
            Unique Digital Assistant identifier.

        :param str parameter_name: (required)
            The name of a Digital Assistant Parameter.  This is unique with the Digital Assistant.

        :param oci.oda.models.UpdateDigitalAssistantParameterDetails update_digital_assistant_parameter_details: (required)
            Property values to update the Digital Assistant Parameter.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.DigitalAssistantParameter`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_digital_assistant_parameter.py.html>`__ to see an example of how to use update_digital_assistant_parameter API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'digitalAssistantId', 'parameterName']
        resource_path = "/odaInstances/{odaInstanceId}/digitalAssistants/{digitalAssistantId}/parameters/{parameterName}"
        method = "PUT"
        operation_name = "update_digital_assistant_parameter"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/DigitalAssistantParameter/UpdateDigitalAssistantParameter"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_digital_assistant_parameter got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "digitalAssistantId": digital_assistant_id,
            "parameterName": parameter_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_digital_assistant_parameter_details,
                response_type="DigitalAssistantParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_digital_assistant_parameter_details,
                response_type="DigitalAssistantParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_oda_private_endpoint(self, oda_private_endpoint_id, update_oda_private_endpoint_details, **kwargs):
        """
        Starts an asynchronous job to update the specified ODA Private Endpoint with the information in the request body.


        :param str oda_private_endpoint_id: (required)
            Unique ODA Private Endpoint identifier which is the `OCID`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.oda.models.UpdateOdaPrivateEndpointDetails update_oda_private_endpoint_details: (required)
            The information to update.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_oda_private_endpoint.py.html>`__ to see an example of how to use update_oda_private_endpoint API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaPrivateEndpointId']
        resource_path = "/odaPrivateEndpoints/{odaPrivateEndpointId}"
        method = "PUT"
        operation_name = "update_oda_private_endpoint"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/OdaPrivateEndpoint/UpdateOdaPrivateEndpoint"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_oda_private_endpoint got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaPrivateEndpointId": oda_private_endpoint_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_oda_private_endpoint_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_oda_private_endpoint_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_skill(self, oda_instance_id, skill_id, update_skill_details, **kwargs):
        """
        Updates the specified Skill with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param oci.oda.models.UpdateSkillDetails update_skill_details: (required)
            Property values to update the Skill.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Skill`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_skill.py.html>`__ to see an example of how to use update_skill API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}"
        method = "PUT"
        operation_name = "update_skill"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Skill/UpdateSkill"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_skill got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_skill_details,
                response_type="Skill",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_skill_details,
                response_type="Skill",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_skill_parameter(self, oda_instance_id, skill_id, parameter_name, update_skill_parameter_details, **kwargs):
        """
        Updates the specified Skill Parameter with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str skill_id: (required)
            Unique Skill identifier.

        :param str parameter_name: (required)
            The name of a Skill Parameter.

        :param oci.oda.models.UpdateSkillParameterDetails update_skill_parameter_details: (required)
            Property values to update the Skill Parameter.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.SkillParameter`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_skill_parameter.py.html>`__ to see an example of how to use update_skill_parameter API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'skillId', 'parameterName']
        resource_path = "/odaInstances/{odaInstanceId}/skills/{skillId}/parameters/{parameterName}"
        method = "PUT"
        operation_name = "update_skill_parameter"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/SkillParameter/UpdateSkillParameter"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_skill_parameter got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "skillId": skill_id,
            "parameterName": parameter_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_skill_parameter_details,
                response_type="SkillParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_skill_parameter_details,
                response_type="SkillParameter",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_translator(self, oda_instance_id, translator_id, update_translator_details, **kwargs):
        """
        Updates the specified Translator with the information in the request body.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str translator_id: (required)
            Unique Translator identifier.

        :param oci.oda.models.UpdateTranslatorDetails update_translator_details: (required)
            Property values to update the Translator.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Translator`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_translator.py.html>`__ to see an example of how to use update_translator API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'translatorId']
        resource_path = "/odaInstances/{odaInstanceId}/translators/{translatorId}"
        method = "PUT"
        operation_name = "update_translator"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Translator/UpdateTranslator"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_translator got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "translatorId": translator_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_translator_details,
                response_type="Translator",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_translator_details,
                response_type="Translator",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
