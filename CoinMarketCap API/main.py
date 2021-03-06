from __future__ import print_function

import gate_api
from gate_api.exceptions import ApiException, GateApiException

# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host="https://api.gateio.ws/api/v4",
    key='9c0825e94fc4e52be4fe93f27ceb4c16',
    secret='f4f2dcb1ac36c391fed6bc646ef2826ff296110d1ca8c7b7eb32a0bca1865d50'
)


api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
futures = gate_api.FuturesApi(api_client)
settle = 'usdt'  # str | Settle currency
contract = 'SOL_USDT'
responseLimit = 100
order = gate_api.FuturesOrder()


def requestFuturesData(contract_):
    try:
        api_response = futures.create_futures_order(settle=settle, futures_order=order)
        
        return (api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" %
            (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_contracts: %s\n" % e)

print(requestFuturesData(contract=contract))