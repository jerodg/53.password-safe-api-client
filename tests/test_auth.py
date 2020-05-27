#!/usr/bin/env python3.8
"""Password Safe API Client: Test Login
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


@pytest.mark.asyncio
async def test_login():
    ts = time.perf_counter()

    bprint('Test: Login')
    async with BricataApiClient(cfg=f'{getenv("CFG_HOME")}/bricata_api_client.toml') as bac:
        results = await bac.login()

        assert type(results) is Results
        assert len(results.success) == 1
        assert not results.failure

        print('Header:', bac.header)

        tprint(results)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')


# @pytest.mark.asyncio
# async def test_logout():
#     """The call to self.logout() in __aexit__() throws an error due to the
#        session already being closed. This is expected behavior; comment it when
#        testing this function."""
#     ts = time.perf_counter()
#
#     bprint('Test: Logout')
#     async with BricataApiClient(cfg=f'{getenv("CFG_HOME")}/bricata_api_client.toml') as bac:
#         await bac.login()
#         print('Header after login:', bac.header)
#
#         results = await bac.logout()
#
#         assert type(results) is Results
#         assert len(results.success) == 1
#         assert not results.failure
#
#         print('Header after logout:', bac.header)
#
#         tprint(results)
#
#     bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')
