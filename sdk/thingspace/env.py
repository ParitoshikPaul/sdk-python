class Env:
    api_url = 'https://api.cloudapi.verizon.com'
    api_version = '1'
    api_cloud = api_url + '/cloud/' + api_version
    chunked_upload_size = 2097152 * 4  # 8mb
