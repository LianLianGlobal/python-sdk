US_HOST = 'https://us-api.lianlianglobal.com'
TEST_HOST = 'http://192.168.132.148:8086'

_config = {
    'default_host': TEST_HOST,
    'connection_timeout': 10,  # 10 seconds
    'file_connection_timeout': 60,  # 60 seconds
    'default_upload_threshold': 1024 * 1024 * 10,  # 10MB
}


def get_config(key=None):
    if key:
        return _config[key]
    return _config


def set_config(default_host=None, default_upload_threshold=None):
    if default_host:
        _config['default_host'] = default_host
    if default_upload_threshold:
        _config['default_upload_threshold'] = default_upload_threshold
