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
from pytorchoperator.sdk.models.io_k8s_apimachinery_pkg_api_resource_quantity import IoK8sApimachineryPkgApiResourceQuantity  # noqa: F401,E501


class IoK8sApiCoreV1NodeResources(object):
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
        'capacity': 'dict(str, IoK8sApimachineryPkgApiResourceQuantity)'
    }

    attribute_map = {
        'capacity': 'Capacity'
    }

    def __init__(self, capacity=None):  # noqa: E501
        """IoK8sApiCoreV1NodeResources - a model defined in Swagger"""  # noqa: E501
        self._capacity = None
        self.discriminator = None
        self.capacity = capacity

    @property
    def capacity(self):
        """Gets the capacity of this IoK8sApiCoreV1NodeResources.  # noqa: E501

        Capacity represents the available resources of a node  # noqa: E501

        :return: The capacity of this IoK8sApiCoreV1NodeResources.  # noqa: E501
        :rtype: dict(str, IoK8sApimachineryPkgApiResourceQuantity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this IoK8sApiCoreV1NodeResources.

        Capacity represents the available resources of a node  # noqa: E501

        :param capacity: The capacity of this IoK8sApiCoreV1NodeResources.  # noqa: E501
        :type: dict(str, IoK8sApimachineryPkgApiResourceQuantity)
        """
        if capacity is None:
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

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
        if issubclass(IoK8sApiCoreV1NodeResources, dict):
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
        if not isinstance(other, IoK8sApiCoreV1NodeResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other