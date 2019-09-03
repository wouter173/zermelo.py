import requests
import json

class Client():
  def __init__(self, school=""):

    self.session = requests.Session()

    if school != "":
      self.endpoint = "https://{}.zportal.nl/api".format(school)
    else: 
      raise ValueError("School is not defined.")
  

  def authenticate(self, code=""):

    if code == "":
      raise ValueError("Code is not defined.")

    url = "{}/v3/oauth/token".format(self.endpoint)
    data = {
      "grant_type": "authorization_code",
      "code": code.replace(" ", "") 
    }
    res = self.session.post(url = url, data = data)

    if res.status_code == 400:
      raise ValueError("Parsed code is not active.")
    elif res.status_code == 404:
      raise ValueError("School does not exist.")
    elif res.status_code == 200:
      return json.loads(res.text)


  def get_user(self, token=""):

    if token == "":
      raise ValueError("Token is not defined.")

    url = "{}/v3/users/~me".format(self.endpoint)
    params = {"access_token": token}

    res = self.session.get(url = url, params = params)
    
    if res.status_code == 401:
      raise ValueError("Token not active.")
    elif res.status_code == 200:
      return json.loads(res.text)
  

  def get_appointments(self, token="", start_unix="", end_unix=""):

    if token == "":
      raise ValueError("Token is not defined.")
    elif start_unix == "":
      raise ValueError("Start unix timestamp is not defined.")
    elif end_unix == "":
      raise ValueError("End unix timestamp is not defined.")

    url = "{}/v3/appointments/".format(self.endpoint)
    params = {
      "user": "~me",
      "start": start_unix,
      "end": end_unix,
      "access_token": token
    }

    res = self.session.get(url = url, params = params)

    if res.status_code == 403:
      raise ValueError("Start unix timestamp and / or end unix timestamp make no sense.")
    elif res.status_code == 401:
      raise ValueError("Token not active.")
    elif res.status_code == 200:
      return json.loads(res.text)


  def get_announcements(self, token=""):

    if token == "":
      raise ValueError("Token is not defined.")
    

    url = "{}/v2/announcements".format(self.endpoint)
    params = {
      "user": "~me",
      "access_token": token
    }

    res = self.session.get(url = url, params = params)

    if res.status_code == 401:
      raise ValueError("Token not active.")
    elif res.status_code == 200:
      return json.loads(res.text)