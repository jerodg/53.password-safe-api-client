#!/usr/bin/env python3.8
"""Password Safe API Client: Models.ManagedAccount
Copyright © 2019-2020 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""

import datetime as dt
import logging
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Optional, Union

from base_api_client.models import Record, sort_dict
import logging
from base64 import b64encode
from dataclasses import dataclass
from os import stat
from os.path import basename
from typing import Union
from password_safe_api_client.models import InvalidOptionError


logger = logging.getLogger(basename(__file__)[:-3])

# todo: add time format validation for ChangeTime


@dataclass
class ManagedAccount(Record):
    """Managed Account"""
    systemID: int
    AccountName: str
    Password: Optional[Union[str, None]] = None  # Required if AutoManagementFlag is False
    DomainName: Optional[Union[str, None]] = None
    UserPrincipalName: Optional[Union[str, None]] = None  # Required for Active Directory managed systems.
    SAMAccountName: Optional[Union[str, None]] = None  # Requied for Active Directory managed systems.
    DistinguishedName: Optional[Union[str, None]] = None  # Required for LDAP managed systems.
    PrivateKey: Optional[Union[str, None]] = None  # Can be set if Platform.DSSFlag is True.
    Passphrase: Optional[Union[str, None]] = None  # Required when PrivateKey is encrypted.
    PasswordFallbackFlag: bool = False  # Can be set if Platform.DSSFlag is True.
    LoginAccountFlag: bool = True  # Can be set when the ManagedSystem.LoginAccountID is True.
    Description: Optional[Union[str, None]] = None
    PasswordRuleID: int = 0
    ApiEnabled: bool = False
    ReleaseNotificationEmail: Optional[Union[str, None]] = None
    ChangeServicesFlag: bool = False
    RestartServicesFlag: bool = False
    ChangeTasksFlag: bool = False
    ReleaseDuration: int = 120
    MaxReleaseDuration: int = 525600
    ISAReleaseDuration: int = 120
    MaxConcurrentRequests: int = 1
    AutoManagementFlag: bool = True  # True if auto-management is enabled.
    DSSAutoManagementFlag: bool = False  # True if DSS Key auto-management is enabled.
    CheckPasswordFlag: bool = False
    ChangePasswordAfterAnyReleaseFlag: bool = False
    ResetPasswordOnMismatchFlag: bool = False
    ChangeFrequencyType: str = 'first'
    ChangeFrequencyDays: Optional[Union[int, None]] = None  # Required if ChangeFrequencyType is 'xdays'
    ChangeTime: str = '23:30'
    NextChangeDate: Optional[Union[str, None]] = None

    def __post_init__(self):
        rng = range(1, 525600)
        if self.ReleaseDuration not in rng:
            logger.exception(f'{self.ReleaseDuration} is an invalid option; it must be in range: 1 - 525600')
            raise InvalidOptionError('ManagedAccount -> Release Duration', 'Range: 1 - 525600')

        if self.MaxReleaseDuration not in rng:
            logger.exception(f'{self.MaxReleaseDuration} is an invalid option; it must be in range: 1 - 525600')
            raise InvalidOptionError('ManagedAccount -> Max Release Duration', 'Range: 1 - 525600')

        if self.MaxConcurrentRequests not in range(0, 999):
            logger.exception(f'{self.MaxConcurrentRequests} is an invalid option; it must be in range: 0 - 999')
            raise InvalidOptionError('ManagedAccount -> Max Concurrent Requests', 'Range: 0 - 999')

        if self.ChangeFrequencyType not in ['first', 'last', 'xdays']:
            logger.exception(f'{self.ChangeFrequencyType} is an invalid option; it must be "first", "last", or "xdays"')
            raise InvalidOptionError('ManagedAccount -> Change Frequency Type', '"first", "last", or "xdays"')

        if self.ChangeFrequencyType == 'xdays' and not self.ChangeFrequencyDays:
            logger.exception(f'{self.ChangeFrequencyDays} is required when ChangeFrequencyType is "xdays". Valid range 0 - 999')
            raise InvalidOptionError('ManagedAccount -> Change Frequency Days', 'is required when ChangeFrequencyType is "xdays".')

    def dict(self, cleanup: bool = True, dct: Optional[dict] = None, sort_order: str = 'asc') -> dict:
        """
        Args:
            cleanup (Optional[bool]):
            dct (Optional[dict]):
            sort_order (Optional[str]): ASC | DESC

        Returns:
            dct (dict):"""
        dct = deepcopy(self.__dict__)
        del dct['systemID']

        if cleanup:
            dct = {k: v for k, v in dct.items() if v is not None}

        if sort_order:
            dct = sort_dict(dct, reverse=True if sort_order.lower() == 'desc' else False)

        return dct

    @property
    def end_point(self):
        return f'/ManagedSystems/{self.systemID}/ManagedAccounts'

    @property
    def method(self):
        return 'post'
