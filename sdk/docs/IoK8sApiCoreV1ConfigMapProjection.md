# IoK8sApiCoreV1ConfigMapProjection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[IoK8sApiCoreV1KeyToPath]**](IoK8sApiCoreV1KeyToPath.md) | If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the &#x27;..&#x27; path or start with &#x27;..&#x27;. | [optional] 
**name** | **str** | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | Specify whether the ConfigMap or it&#x27;s keys must be defined | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
