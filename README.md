# Python-sdk-ewallet

Python-sdk-ewallet is a Python SDK for [OpenAPI](https://developer.lianlianglobal.com/docs/e-wallet-openapi) of LianLian Global e-wallet program.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python-sdk-ewallet.

```bash
pip install python-sdk-ewallet
```

## Usage

### Get Balances
```python
import ewallet

private_key = 'XXX'
ewallet.set_config(default_host=ewallet.TEST_HOST, private_key=private_key)
auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
data, code = ewallet.get_balances(auth)
if code == 200:
    print(data)
else:
    print(code, data)
```
For more operation, please refer to the [SDK User Guide](https://developer.lianlianglobal.com/docs/e-wallet-openapi/78xu0xel7j7ao-python-sdk).

### Test
```bash
py test_ewallet.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

If you have any questions while using the SDK, please feel free to [contact us](mailto:tech-ewallet@lianlianpay.com).

## License
[MIT](https://choosealicense.com/licenses/mit/)