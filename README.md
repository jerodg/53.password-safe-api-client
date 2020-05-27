```
 ___                              _   ___        __     
| _ \__ _ _______ __ _____ _ _ __| | / __| __ _ / _|___ 
|  _/ _` (_-<_-< V  V / _ \ '_/ _` | \__ \/ _` |  _/ -_)
|_| \__,_/__/__/\_/\_/\___/_| \__,_| |___/\__,_|_| \___|                                                        
```
![Platform: Linux/Mac/Windows](https://img.shields.io/badge/Platform-Linux/Mac/Windows-blue.svg?style=plastic "Platform: Linux/Mac/Windows")
![Python 3.8.x](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=plastic "Python 3.8.x")
![phantom](https://img.shields.io/badge/Phantom-4.5+-blue.svg?style=plastic)
<a href="https://www.mongodb.com/licensing/server-side-public-license"><img src="https://img.shields.io/badge/License-SSPL-green.svg?style=plastic"></a>
![Coverage 68%](https://img.shields.io/badge/Coverage-75%25-yellow.svg?style=plastic "Coverage 68%")
<a href="https://saythanks.io/to/jerodg"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg?style=plastic"></a>
<a href="https://www.paypal.me/jerodgawne"><img src="https://img.shields.io/badge/Donate-orange.svg?style=plastic"></a>

# Password Safe API client.
Client library for BeyondTrust Password Safe


## Installation
```bash
pip install phantom-api-client
```

## Basic Usage
This modules primary use-case is inheritance from other REST API clients.

```python

```
## API Implementation, Categories (2/24) ~8.3%, Functions (36/123) ~29.2%
- [ ] Actions:
    - [ ] Run Action
    - [ ] Cancel Running Action
- [ ] Aggregation Rules:
    - [ ] Create Rule
    - [ ] Update Rule
    - [ ] Delete Rule
    
## Test Coverage

platform linux, python 3.8.2
-

## Performance Notes


## Documentation
[GitHub Pages](https://jerodg.github.io/password-safe-api-client/)
- Work in Process

## Known Issues
Mass deleting records quits early with timeout error. It would seem the more 
records that are being deleted adds an exponential increase in wait between 
deletes. So far in testing >= 47 (254) 114 at once results in timeout-error.


Phantom v4.2 and earlier has completely broken pagination. You will receive 
duplicate and missing records. You should set the query filter 'page_size' to 
a number greater than the max expected results in order to receive all records 
in a single page.


## License
Copyright © 2019-2020 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
