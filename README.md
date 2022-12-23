# mimo-sms Python

[![](https://img.shields.io/badge/mimosms-OpenSource-blue.svg)]("https://www.mimo.it.ao/pt")

Python library to integration with MIMO SMS Service.
The library is a simple integration for software developers 
to use in their projects and they need to quickly connect to an SMS service.

# Installation

``` 
pip install mimosms 
```

# Configuration
For configuration it is necessary to add the system environment variables, the following variables with the respective values `MIMO_API_TOKEN` and `MIMO_API_HOST`

Open terminal and do this
### Linux or Mac
```
$ export MIMO_API_TOKEN=your-token-key
$ export MIMO_API_HOST=hostname
```

### Windows

``` 
set MIMO_API_TOKEN=your-token-key
set MIMO_API_HOST=hostname
```


# Use

### New message

Send sms message

``` 
from mimosms.messages import Message
message_resource = Message()
message_resource.send('mysender', ['933843893'], 'Olá, Seja bem-vindo (a)') 
```


### Consulting credits
View your balance
``` 
from mimosms import Mimo
mimo_obj = Mimo() 
balance = mimo_obj.view_credits()
print(balance)
```

### Add Credits
Add credits
``` 
from mimosms import Mimo
mimo_obj = Mimo() 
voucher_code = "your-voucher-code"
mimo_obj.charge_credits(voucher_code)
```

### Create sender
Create a new sender
```
from mimosms.senders import Sender
payload = {'sender': 'your-sender-name', 'reason': 'your-reason'}
sender_resource = Sender()
sender_resource.create(**payload)
```

### List your senders
List senders requested
```
from mimosms.senders import Sender
payload = {'sender': 'your-sender-name', 'reason': 'your-reason'}
sender_resource = Sender()
senders_requested = sender_resource.list(requested=True)
```

List all senders available

```
from mimosms.senders import Sender
sender_resource = Sender()
senders = sender_resource.list()
```
# Note
All other resources are accessed in the same way by importing a resource class and calling only the class's methods to interact with the resource's data.

# License

The library is available as open source under the terms of the MIT License.
