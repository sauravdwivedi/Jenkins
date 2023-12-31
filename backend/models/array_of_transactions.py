# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend.models.transaction import Transaction  # noqa: F401,E501
import backend.util as util


class ArrayOfTransactions(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """ArrayOfTransactions - a model defined in Swagger"""
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "ArrayOfTransactions":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArrayOfTransactions of this ArrayOfTransactions.  # noqa: E501
        :rtype: ArrayOfTransactions
        """
        return util.deserialize_model(dikt, cls)
