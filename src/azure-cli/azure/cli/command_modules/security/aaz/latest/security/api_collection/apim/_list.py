# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "security api-collection apim list",
    is_preview=True,
)
class List(AAZCommand):
    """Gets a list of API collections that have been onboarded to Microsoft Defender for APIs.
    """

    _aaz_info = {
        "version": "2023-11-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.security/apicollections", "2023-11-15"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.apimanagement/service/{}/providers/microsoft.security/apicollections", "2023-11-15"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.security/apicollections", "2023-11-15"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        _args_schema.service_name = AAZStrArg(
            options=["--service-name"],
            help="The name of the API Management service.",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
                max_length=50,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id) and has_value(self.ctx.args.service_name) is not True
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.args.service_name) and has_value(self.ctx.subscription_id)
        condition_2 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True and has_value(self.ctx.args.service_name) is not True
        if condition_0:
            self.APICollectionsListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.APICollectionsListByAzureApiManagementService(ctx=self.ctx)()
        if condition_2:
            self.APICollectionsListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class APICollectionsListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/apiCollections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.base_url = AAZStrType(
                serialized_name="baseUrl",
                flags={"read_only": True},
            )
            properties.discovered_via = AAZStrType(
                serialized_name="discoveredVia",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.number_of_api_endpoints = AAZIntType(
                serialized_name="numberOfApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_api_endpoints_with_sensitive_data_exposed = AAZIntType(
                serialized_name="numberOfApiEndpointsWithSensitiveDataExposed",
                flags={"read_only": True},
            )
            properties.number_of_external_api_endpoints = AAZIntType(
                serialized_name="numberOfExternalApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_inactive_api_endpoints = AAZIntType(
                serialized_name="numberOfInactiveApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_unauthenticated_api_endpoints = AAZIntType(
                serialized_name="numberOfUnauthenticatedApiEndpoints",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sensitivity_label = AAZStrType(
                serialized_name="sensitivityLabel",
                flags={"read_only": True},
            )

            return cls._schema_on_200

    class APICollectionsListByAzureApiManagementService(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/providers/Microsoft.Security/apiCollections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.base_url = AAZStrType(
                serialized_name="baseUrl",
                flags={"read_only": True},
            )
            properties.discovered_via = AAZStrType(
                serialized_name="discoveredVia",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.number_of_api_endpoints = AAZIntType(
                serialized_name="numberOfApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_api_endpoints_with_sensitive_data_exposed = AAZIntType(
                serialized_name="numberOfApiEndpointsWithSensitiveDataExposed",
                flags={"read_only": True},
            )
            properties.number_of_external_api_endpoints = AAZIntType(
                serialized_name="numberOfExternalApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_inactive_api_endpoints = AAZIntType(
                serialized_name="numberOfInactiveApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_unauthenticated_api_endpoints = AAZIntType(
                serialized_name="numberOfUnauthenticatedApiEndpoints",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sensitivity_label = AAZStrType(
                serialized_name="sensitivityLabel",
                flags={"read_only": True},
            )

            return cls._schema_on_200

    class APICollectionsListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Security/apiCollections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.base_url = AAZStrType(
                serialized_name="baseUrl",
                flags={"read_only": True},
            )
            properties.discovered_via = AAZStrType(
                serialized_name="discoveredVia",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.number_of_api_endpoints = AAZIntType(
                serialized_name="numberOfApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_api_endpoints_with_sensitive_data_exposed = AAZIntType(
                serialized_name="numberOfApiEndpointsWithSensitiveDataExposed",
                flags={"read_only": True},
            )
            properties.number_of_external_api_endpoints = AAZIntType(
                serialized_name="numberOfExternalApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_inactive_api_endpoints = AAZIntType(
                serialized_name="numberOfInactiveApiEndpoints",
                flags={"read_only": True},
            )
            properties.number_of_unauthenticated_api_endpoints = AAZIntType(
                serialized_name="numberOfUnauthenticatedApiEndpoints",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sensitivity_label = AAZStrType(
                serialized_name="sensitivityLabel",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]