#!/usr/bin/env python3.8
"""Password Safe API Client: Models.ManagedAccounts
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
MANAGED_ACCOUNT_TYPES = ['system', 'domainlinked', 'database', 'cloud', 'application', None]


@dataclass
class ManagedAccounts(Record):
    systemName: Optional[Union[str, None]] = None
    accountName: Optional[Union[str, None]] = None
    workgroupName: Optional[Union[str, None]] = None
    applicationDisplayName: Optional[Union[str, None]] = None
    ipAddress: Optional[Union[str, None]] = None
    type: Optional[Union[str, None]] = None

    def __post_init__(self):
        if self.type not in MANAGED_ACCOUNT_TYPES:
            logger.exception(f'{self.type} is an invalid managed account type.')
            raise InvalidOptionError('ManagedAccounts', MANAGED_ACCOUNT_TYPES)

    @property
    def end_point(self):
        return '/ManagedAccounts'


@dataclass
class ManagedSystems(Record):
    type: Optional[Union[str, None]] = None
    name: Optional[Union[str, None]] = None
    limit: int = 100000
    offset: int = 0  # Must be used with limit

    @property
    def end_point(self):
        return '/ManagedSystems'

    @property
    def data_key(self):
        return 'Data'
