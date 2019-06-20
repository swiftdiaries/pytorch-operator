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
from pytorchoperator.sdk.models.io_k8s_apimachinery_pkg_apis_meta_v1_time import IoK8sApimachineryPkgApisMetaV1Time  # noqa: F401,E501


class IoK8sApiCoreV1ContainerStateRunning(object):
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
        'started_at': 'IoK8sApimachineryPkgApisMetaV1Time'
    }

    attribute_map = {
        'started_at': 'startedAt'
    }

    def __init__(self, started_at=None):  # noqa: E501
        """IoK8sApiCoreV1ContainerStateRunning - a model defined in Swagger"""  # noqa: E501
        self._started_at = None
        self.discriminator = None
        if started_at is not None:
            self.started_at = started_at

    @property
    def started_at(self):
        """Gets the started_at of this IoK8sApiCoreV1ContainerStateRunning.  # noqa: E501


        :return: The started_at of this IoK8sApiCoreV1ContainerStateRunning.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this IoK8sApiCoreV1ContainerStateRunning.


        :param started_at: The started_at of this IoK8sApiCoreV1ContainerStateRunning.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._started_at = started_at

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
        if issubclass(IoK8sApiCoreV1ContainerStateRunning, dict):
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
        if not isinstance(other, IoK8sApiCoreV1ContainerStateRunning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
