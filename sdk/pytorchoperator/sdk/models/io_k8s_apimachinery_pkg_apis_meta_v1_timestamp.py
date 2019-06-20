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


class IoK8sApimachineryPkgApisMetaV1Timestamp(object):
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
        'nanos': 'int',
        'seconds': 'int'
    }

    attribute_map = {
        'nanos': 'nanos',
        'seconds': 'seconds'
    }

    def __init__(self, nanos=None, seconds=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1Timestamp - a model defined in Swagger"""  # noqa: E501
        self._nanos = None
        self._seconds = None
        self.discriminator = None
        self.nanos = nanos
        self.seconds = seconds

    @property
    def nanos(self):
        """Gets the nanos of this IoK8sApimachineryPkgApisMetaV1Timestamp.  # noqa: E501

        Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.  # noqa: E501

        :return: The nanos of this IoK8sApimachineryPkgApisMetaV1Timestamp.  # noqa: E501
        :rtype: int
        """
        return self._nanos

    @nanos.setter
    def nanos(self, nanos):
        """Sets the nanos of this IoK8sApimachineryPkgApisMetaV1Timestamp.

        Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.  # noqa: E501

        :param nanos: The nanos of this IoK8sApimachineryPkgApisMetaV1Timestamp.  # noqa: E501
        :type: int
        """
        if nanos is None:
            raise ValueError("Invalid value for `nanos`, must not be `None`")  # noqa: E501

        self._nanos = nanos

    @property
    def seconds(self):
        """Gets the seconds of this IoK8sApimachineryPkgApisMetaV1Timestamp.  # noqa: E501

        Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.  # noqa: E501

        :return: The seconds of this IoK8sApimachineryPkgApisMetaV1Timestamp.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this IoK8sApimachineryPkgApisMetaV1Timestamp.

        Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.  # noqa: E501

        :param seconds: The seconds of this IoK8sApimachineryPkgApisMetaV1Timestamp.  # noqa: E501
        :type: int
        """
        if seconds is None:
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds

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
        if issubclass(IoK8sApimachineryPkgApisMetaV1Timestamp, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1Timestamp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
