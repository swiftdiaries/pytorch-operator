# coding: utf-8

"""
    PyTorchOperator

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from pytorchoperator.sdk.models.io_k8s_api_core_v1_endpoint_address import IoK8sApiCoreV1EndpointAddress  # noqa: F401,E501
from pytorchoperator.sdk.models.io_k8s_api_core_v1_endpoint_port import IoK8sApiCoreV1EndpointPort  # noqa: F401,E501


class IoK8sApiCoreV1EndpointSubset(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'addresses': 'list[IoK8sApiCoreV1EndpointAddress]',
        'not_ready_addresses': 'list[IoK8sApiCoreV1EndpointAddress]',
        'ports': 'list[IoK8sApiCoreV1EndpointPort]'
    }

    attribute_map = {
        'addresses': 'addresses',
        'not_ready_addresses': 'notReadyAddresses',
        'ports': 'ports'
    }

    def __init__(self, addresses=None, not_ready_addresses=None, ports=None):  # noqa: E501
        """IoK8sApiCoreV1EndpointSubset - a model defined in Swagger"""  # noqa: E501
        self._addresses = None
        self._not_ready_addresses = None
        self._ports = None
        self.discriminator = None
        if addresses is not None:
            self.addresses = addresses
        if not_ready_addresses is not None:
            self.not_ready_addresses = not_ready_addresses
        if ports is not None:
            self.ports = ports

    @property
    def addresses(self):
        """Gets the addresses of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501

        IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.  # noqa: E501

        :return: The addresses of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1EndpointAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this IoK8sApiCoreV1EndpointSubset.

        IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.  # noqa: E501

        :param addresses: The addresses of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501
        :type: list[IoK8sApiCoreV1EndpointAddress]
        """

        self._addresses = addresses

    @property
    def not_ready_addresses(self):
        """Gets the not_ready_addresses of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501

        IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.  # noqa: E501

        :return: The not_ready_addresses of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1EndpointAddress]
        """
        return self._not_ready_addresses

    @not_ready_addresses.setter
    def not_ready_addresses(self, not_ready_addresses):
        """Sets the not_ready_addresses of this IoK8sApiCoreV1EndpointSubset.

        IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.  # noqa: E501

        :param not_ready_addresses: The not_ready_addresses of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501
        :type: list[IoK8sApiCoreV1EndpointAddress]
        """

        self._not_ready_addresses = not_ready_addresses

    @property
    def ports(self):
        """Gets the ports of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501

        Port numbers available on the related IP addresses.  # noqa: E501

        :return: The ports of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1EndpointPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this IoK8sApiCoreV1EndpointSubset.

        Port numbers available on the related IP addresses.  # noqa: E501

        :param ports: The ports of this IoK8sApiCoreV1EndpointSubset.  # noqa: E501
        :type: list[IoK8sApiCoreV1EndpointPort]
        """

        self._ports = ports

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoK8sApiCoreV1EndpointSubset, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiCoreV1EndpointSubset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
