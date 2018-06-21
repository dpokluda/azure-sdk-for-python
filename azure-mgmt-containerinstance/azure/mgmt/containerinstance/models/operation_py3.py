# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Operation(Model):
    """An operation for Azure Container Instance service.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the operation.
    :type name: str
    :param display: Required. The display information of the operation.
    :type display: ~azure.mgmt.containerinstance.models.OperationDisplay
    :param origin: The intended executor of the operation. Possible values
     include: 'User', 'System'
    :type origin: str or
     ~azure.mgmt.containerinstance.models.ContainerInstanceOperationsOrigin
    """

    _validation = {
        'name': {'required': True},
        'display': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, *, name: str, display, origin=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
