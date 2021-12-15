# Zermelo.py

[![Build Status](https://travis-ci.org/wouter173/zermelo.py.svg?branch=master)](https://travis-ci.org/wouter173/zermelo.py) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python implementation of the [Zermelo API](https://zermelo.atlassian.net/wiki/spaces/DEV).

## Features

1. Get appointments from a zermelo calendar.
2. Get data of a zermelo user.
3. Get announcements.

## Installation

To install the package run this command:

```bash
  pip install zermelo.py
```

## Usage

### Client

```python
Client()
```

params:
```
School: String ? Name of the school.
```

Result:
```
Client: Zermelo.Client()
```

Demo:
```python
from zermelo import Client

cl = Client("scalacollege")
```

### Authentication

```python
Client.authenticate()
```

Params:

```
Code: String ? A connect code you get from https://YOURSCHOOLNAME.zportel.nl/main/#connectionsModule-connectApp
```

Result:

```
Token: dict()
```

Demo:

```python
token = cl.auhtenticate("441 440 997 507")
print(token["access_token"])
```

### User

```python
Client.get_user()
```

Params: 
```
Token: String ? Access_token you get from the Client.Authenticate() function
```

Result:

```
User: dict()
```

Demo:

```python
user = cl.get_user(token["access_token"])
print(user)
```

### Appointments

```python
Client.get_appointments()
```

Params: 
```
Token: String ? Access_token you get from the Client.Authenticate() function
StartUnix: int ? Unix timestamp for the first date you want to get the appointments from.
EndUnix: int ? Unix timestamp for the last date you want to get the appointments from.
```

Result:

```
Appointments: dict()
```

Demo:

```python
appointments = cl.get_appointments(token["access_token"], 1567468800, 1568073600)
print(appointments)
```

### Announcements

```python
Client.get_announcements()
```

Params: 
```
Token: String ? Access_token you get from the Client.Authenticate() function
```

Result:

```
Announcements: dict()
```

Demo:

```python
announcements = cl.get_announcements(token["access_token"])
print(announcements)
```

### Announcements

```python
Client.get_liveschedule()
```

Params: 
```
Token: String ? Access_token you get from the Client.Authenticate() function
Week: String ? The ISO-week for which you want to request the schedule
Usercode: String ? The code of the student you want to request the schedule of 
```

Result:

```
Enrollments: dict()
```

Demo:

```python
usercode = cl.get_user(token["access_token"])["response"]["data"][0]["code"]
enrollments = cl.get_liveschedule(token["access_token"], "202150", usercode) # Requests week 50 of the year 2021
print(enrollments)
```

# License
[MIT](https://github.com/wouter173/zermelo.py/blob/master/LICENSE)
