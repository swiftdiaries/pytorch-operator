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


class IoK8sApiCoreV1PortworxVolumeSource(object):
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
        'fs_type': 'str',
        'read_only': 'bool',
        'volume_id': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'read_only': 'readOnly',
        'volume_id': 'volumeID'
    }

    def __init__(self, fs_type=None, read_only=None, volume_id=None):  # noqa: E501
        """IoK8sApiCoreV1PortworxVolumeSource - a model defined in Swagger"""  # noqa: E501
        self._fs_type = None
        self._read_only = None
        self._volume_id = None
        self.discriminator = None
        if fs_type is not None:
            self.fs_type = fs_type
        if read_only is not None:
            self.read_only = read_only
        self.volume_id = volume_id

    @property
    def fs_type(self):
        """Gets the fs_type of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501

        FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this IoK8sApiCoreV1PortworxVolumeSource.

        FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def read_only(self):
        """Gets the read_only of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501

        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :return: The read_only of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this IoK8sApiCoreV1PortworxVolumeSource.

        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :param read_only: The read_only of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def volume_id(self):
        """Gets the volume_id of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501

        VolumeID uniquely identifies a Portworx volume  # noqa: E501

        :return: The volume_id of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this IoK8sApiCoreV1PortworxVolumeSource.

        VolumeID uniquely identifies a Portworx volume  # noqa: E501

        :param volume_id: The volume_id of this IoK8sApiCoreV1PortworxVolumeSource.  # noqa: E501
        :type: str
        """
        if volume_id is None:
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

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
        if issubclass(IoK8sApiCoreV1PortworxVolumeSource, dict):
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
        if not isinstance(other, IoK8sApiCoreV1PortworxVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
