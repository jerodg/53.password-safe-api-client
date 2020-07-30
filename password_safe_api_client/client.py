#!/usr/bin/env python3.8
"""Password Safe API Client
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
import asyncio
import logging
from typing import NoReturn, Union, List
from uuid import uuid4

from base_api_client import BaseApiClient
from base_api_client.models import Results

from password_safe_api_client.models import ManagedAccounts, ManagedSystems, ManagedAccount

logger = logging.getLogger(__name__)


class PasswordSafeApiClient(BaseApiClient):
    """Password Safe API Client"""

    def __init__(self, cfg: Union[str, dict]):
        """Initializes Class

        Args:
            cfg (Union[str, dict]): As a str it should contain a full path
                pointing to a configuration file (json/toml). See
                config.* in the examples folder for reference."""
        BaseApiClient.__init__(self, cfg=cfg)
        self.logged_in: bool = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: None, exc_val: None, exc_tb: None) -> NoReturn:
        await BaseApiClient.__aexit__(self, exc_type, exc_val, exc_tb)

    async def authenticate(self, direction: str) -> Results:
        """Authenticate (Log in/out)

        Args:
            direction (str): in|out

        Returns:
            NoReturn"""
        logger.debug(f'Logging {direction} {"in to" if direction == "in" else "out of"} Password Safe')

        tasks = [asyncio.create_task(self.request(method='post',
                                                  end_point='/Auth/SignAppin' if direction == 'in' else '/Auth/Signout',
                                                  request_id=uuid4().hex))]
        results = Results(data=await asyncio.gather(*tasks))

        logger.debug('-> Complete.')

        results = await self.process_results(results)

        if direction == 'in':
            self.logged_in = True
        else:
            self.logged_in = False

        return results

    async def get_records(self, query: Union[ManagedAccounts, ManagedSystems]) -> Results:
        logger.debug(f'Getting {type(query)}, record(s)...')

        if not self.logged_in:
            await self.authenticate(direction='in')

        tasks = [asyncio.create_task(self.request(method='get',
                                                  end_point=query.end_point,
                                                  request_id=uuid4().hex,
                                                  params={**query.dict()}))]

        results = await self.process_results(Results(data=await asyncio.gather(*tasks)), query.data_key)

        logger.debug('-> Complete.')

        return results

    async def post_records(self, models: List[Union[ManagedAccount, ManagedAccounts]]) -> Results:
        if not type(models) is list:
            models = [models]

        if not self.logged_in:
            await self.authenticate(direction='in')

        tasks = [asyncio.create_task(self.request(method=m.method,
                                                  end_point=m.end_point,
                                                  request_id=uuid4().hex,
                                                  json=m.dict())) for m in models]

        results = await self.process_results(Results(data=await asyncio.gather(*tasks)))

        logger.debug('-> Complete.')

        return results


if __name__ == '__main__':
    print(__doc__)
