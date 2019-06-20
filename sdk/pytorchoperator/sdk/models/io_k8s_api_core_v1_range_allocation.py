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
from pytorchoperator.sdk.models.io_k8s_apimachinery_pkg_apis_meta_v1_object_meta import IoK8sApimachineryPkgApisMetaV1ObjectMeta  # noqa: F401,E501


class IoK8sApiCoreV1RangeAllocation(object):
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
        'api_version': 'str',
        'data': 'str',
        'kind': 'str',
        'metadata': 'IoK8sApimachineryPkgApisMetaV1ObjectMeta',
        'range': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'data': 'data',
        'kind': 'kind',
        'metadata': 'metadata',
        'range': 'range'
    }

    def __init__(self, api_version=None, data=None, kind=None, metadata=None, range=None):  # noqa: E501
        """IoK8sApiCoreV1RangeAllocation - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._data = None
        self._kind = None
        self._metadata = None
        self._range = None
        self.discriminator = None
        if api_version is not None:
            self.api_version = api_version
        self.data = data
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        self.range = range

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApiCoreV1RangeAllocation.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def data(self):
        """Gets the data of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501

        Data is a bit array containing all allocated addresses in the previous segment.  # noqa: E501

        :return: The data of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this IoK8sApiCoreV1RangeAllocation.

        Data is a bit array containing all allocated addresses in the previous segment.  # noqa: E501

        :param data: The data of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def kind(self):
        """Gets the kind of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApiCoreV1RangeAllocation.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501


        :return: The metadata of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoK8sApiCoreV1RangeAllocation.


        :param metadata: The metadata of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def range(self):
        """Gets the range of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501

        Range is string that identifies the range represented by 'data'.  # noqa: E501

        :return: The range of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this IoK8sApiCoreV1RangeAllocation.

        Range is string that identifies the range represented by 'data'.  # noqa: E501

        :param range: The range of this IoK8sApiCoreV1RangeAllocation.  # noqa: E501
        :type: str
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

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
        if issubclass(IoK8sApiCoreV1RangeAllocation, dict):
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
        if not isinstance(other, IoK8sApiCoreV1RangeAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other