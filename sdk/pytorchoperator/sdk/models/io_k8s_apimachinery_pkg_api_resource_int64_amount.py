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


class IoK8sApimachineryPkgApiResourceInt64Amount(object):
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
        'scale': 'int',
        'value': 'int'
    }

    attribute_map = {
        'scale': 'scale',
        'value': 'value'
    }

    def __init__(self, scale=None, value=None):  # noqa: E501
        """IoK8sApimachineryPkgApiResourceInt64Amount - a model defined in Swagger"""  # noqa: E501
        self._scale = None
        self._value = None
        self.discriminator = None
        self.scale = scale
        self.value = value

    @property
    def scale(self):
        """Gets the scale of this IoK8sApimachineryPkgApiResourceInt64Amount.  # noqa: E501


        :return: The scale of this IoK8sApimachineryPkgApiResourceInt64Amount.  # noqa: E501
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this IoK8sApimachineryPkgApiResourceInt64Amount.


        :param scale: The scale of this IoK8sApimachineryPkgApiResourceInt64Amount.  # noqa: E501
        :type: int
        """
        if scale is None:
            raise ValueError("Invalid value for `scale`, must not be `None`")  # noqa: E501

        self._scale = scale

    @property
    def value(self):
        """Gets the value of this IoK8sApimachineryPkgApiResourceInt64Amount.  # noqa: E501


        :return: The value of this IoK8sApimachineryPkgApiResourceInt64Amount.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IoK8sApimachineryPkgApiResourceInt64Amount.


        :param value: The value of this IoK8sApimachineryPkgApiResourceInt64Amount.  # noqa: E501
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(IoK8sApimachineryPkgApiResourceInt64Amount, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgApiResourceInt64Amount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
