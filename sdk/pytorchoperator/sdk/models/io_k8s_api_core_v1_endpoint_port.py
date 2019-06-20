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


class IoK8sApiCoreV1EndpointPort(object):
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
        'name': 'str',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, name=None, port=None, protocol=None):  # noqa: E501
        """IoK8sApiCoreV1EndpointPort - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._port = None
        self._protocol = None
        self.discriminator = None
        if name is not None:
            self.name = name
        self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def name(self):
        """Gets the name of this IoK8sApiCoreV1EndpointPort.  # noqa: E501

        The name of this port (corresponds to ServicePort.Name). Must be a DNS_LABEL. Optional only if one port is defined.  # noqa: E501

        :return: The name of this IoK8sApiCoreV1EndpointPort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoK8sApiCoreV1EndpointPort.

        The name of this port (corresponds to ServicePort.Name). Must be a DNS_LABEL. Optional only if one port is defined.  # noqa: E501

        :param name: The name of this IoK8sApiCoreV1EndpointPort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this IoK8sApiCoreV1EndpointPort.  # noqa: E501

        The port number of the endpoint.  # noqa: E501

        :return: The port of this IoK8sApiCoreV1EndpointPort.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IoK8sApiCoreV1EndpointPort.

        The port number of the endpoint.  # noqa: E501

        :param port: The port of this IoK8sApiCoreV1EndpointPort.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this IoK8sApiCoreV1EndpointPort.  # noqa: E501

        The IP protocol for this port. Must be UDP or TCP. Default is TCP.  # noqa: E501

        :return: The protocol of this IoK8sApiCoreV1EndpointPort.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this IoK8sApiCoreV1EndpointPort.

        The IP protocol for this port. Must be UDP or TCP. Default is TCP.  # noqa: E501

        :param protocol: The protocol of this IoK8sApiCoreV1EndpointPort.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if issubclass(IoK8sApiCoreV1EndpointPort, dict):
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
        if not isinstance(other, IoK8sApiCoreV1EndpointPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
