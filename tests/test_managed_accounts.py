#!/usr/bin/env python3.8
"""Password Safe API Client: Test Accounts
Copyright © 2020 Jerod Gawne <https://github.com/jerodg/>

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
import time

import pytest
from os import getenv

from base_api_client import bprint, Results, tprint
from password_safe_api_client import PasswordSafeApiClient
from password_safe_api_client.models import ManagedAccounts, ManagedAccount


@pytest.mark.asyncio
async def test_get_managed_accounts():
    ts = time.perf_counter()

    bprint('Test: Get Managed Accounts')
    async with PasswordSafeApiClient(cfg=f'{getenv("CFG_HOME")}/password_safe_api_client_dev.toml') as psac:
        results = await psac.get_records(query=ManagedAccounts())

        assert type(results) is Results
        assert len(results.success) == 1
        assert not results.failure

        print('Cookie:')

        tprint(results)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')


@pytest.mark.asyncio
async def test_post_managed_account():
    ts = time.perf_counter()

    bprint('Test: Post Managed Account')
    async with PasswordSafeApiClient(cfg=f'{getenv("CFG_HOME")}/password_safe_api_client_dev.toml') as psac:
        results = await psac.post_records(model=ManagedAccount(systemID=33,
                                                               AccountName='Test McTesterton',
                                                               DistinguishedName='uid=s.McTest,ou=Test,ou=apps,ou=b2e,dc=test53,dc=com',
                                                               ApiEnabled=True,
                                                               ReleaseDuration=120,
                                                               MaxReleaseDuration=1440,
                                                               ISAReleaseDuration=120,
                                                               MaxConcurrentRequests=1,
                                                               AutoManagementFlag=True,
                                                               CheckPasswordFlag=True,
                                                               ResetPasswordOnMismatchFlag=True,
                                                               ChangePasswordAfterAnyReleaseFlag=True,
                                                               ChangeFrequencyType='xdays',
                                                               ChangeFrequencyDays=30,
                                                               ChangeTime='01:00'))

        assert type(results) is Results
        assert len(results.success) == 1
        assert not results.failure

        print('Cookie:')

        tprint(results)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')
