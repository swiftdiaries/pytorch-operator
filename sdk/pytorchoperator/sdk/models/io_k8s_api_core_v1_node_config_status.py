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
from pytorchoperator.sdk.models.io_k8s_api_core_v1_node_config_source import IoK8sApiCoreV1NodeConfigSource  # noqa: F401,E501


class IoK8sApiCoreV1NodeConfigStatus(object):
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
        'active': 'IoK8sApiCoreV1NodeConfigSource',
        'assigned': 'IoK8sApiCoreV1NodeConfigSource',
        'error': 'str',
        'last_known_good': 'IoK8sApiCoreV1NodeConfigSource'
    }

    attribute_map = {
        'active': 'active',
        'assigned': 'assigned',
        'error': 'error',
        'last_known_good': 'lastKnownGood'
    }

    def __init__(self, active=None, assigned=None, error=None, last_known_good=None):  # noqa: E501
        """IoK8sApiCoreV1NodeConfigStatus - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._assigned = None
        self._error = None
        self._last_known_good = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if assigned is not None:
            self.assigned = assigned
        if error is not None:
            self.error = error
        if last_known_good is not None:
            self.last_known_good = last_known_good

    @property
    def active(self):
        """Gets the active of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501


        :return: The active of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :rtype: IoK8sApiCoreV1NodeConfigSource
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this IoK8sApiCoreV1NodeConfigStatus.


        :param active: The active of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :type: IoK8sApiCoreV1NodeConfigSource
        """

        self._active = active

    @property
    def assigned(self):
        """Gets the assigned of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501


        :return: The assigned of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :rtype: IoK8sApiCoreV1NodeConfigSource
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned):
        """Sets the assigned of this IoK8sApiCoreV1NodeConfigStatus.


        :param assigned: The assigned of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :type: IoK8sApiCoreV1NodeConfigSource
        """

        self._assigned = assigned

    @property
    def error(self):
        """Gets the error of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501

        Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.  # noqa: E501

        :return: The error of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this IoK8sApiCoreV1NodeConfigStatus.

        Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.  # noqa: E501

        :param error: The error of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def last_known_good(self):
        """Gets the last_known_good of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501


        :return: The last_known_good of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :rtype: IoK8sApiCoreV1NodeConfigSource
        """
        return self._last_known_good

    @last_known_good.setter
    def last_known_good(self, last_known_good):
        """Sets the last_known_good of this IoK8sApiCoreV1NodeConfigStatus.


        :param last_known_good: The last_known_good of this IoK8sApiCoreV1NodeConfigStatus.  # noqa: E501
        :type: IoK8sApiCoreV1NodeConfigSource
        """

        self._last_known_good = last_known_good

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
        if issubclass(IoK8sApiCoreV1NodeConfigStatus, dict):
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
        if not isinstance(other, IoK8sApiCoreV1NodeConfigStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
