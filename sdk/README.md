The Python SDK is may to either be installed or embedded in your app and runs on Python 2.7 and 3.x .  In order to install the SDK, navigate to this directory and run `python setup.py install`. In order to embed the SDK just place the SDK in a sub-directory accessible to your app.  If you embed `thingspace` inside another module you will have to import that module as well.

To make sure everything is working, open up your python shell and run the following:

```
from thingspace.cloud import Cloud

cloud = Cloud(
            client_key='your key',
            client_secret='your secret',
            callback_url='http://127.0.0.1:8000/token',
)
```