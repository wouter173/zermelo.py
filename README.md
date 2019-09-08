# Zermelo.py

[![Build Status](https://travis-ci.org/wouter173/zermelo.py.svg?branch=master)](https://travis-ci.org/wouter173/zermelo.py)

Zermelo api wrapper library for python.


## Features

1. Get appointments from your zermelo calender.
2. Get your zermelo user data.
3. Get the zermelo announcements from your school.

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
School: String ? Zermelo name of your school.
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
Token: String ? Access_token you get from Client.Authenticate()
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
Token: String ? Access_token you get from Client.Authenticate()
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
Token: String ? Access_token you get from Client.Authenticate()
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
