import json
import endpointer.lambdaf as ep_lambdaf
import endpointer.session as ep_session
import requests

API_FOLDER = '/home/wardog1/work/endpointer/repositories/endpointer-localstack/local-node/api-folder'

LAMBDA_ALIAS = 'upload-api-module-content'

API_TOKEN = 'cluster'
LAMBDA_TOKEN = 'upload-api-module-content'

SESSION_TOKEN = 'hvZ4vXG73NbKkat'

load_manager_url = "http://local.load.endpointer.com"

query_string = f'?{ep_lambdaf.LAMBDA_ALIAS_FIELD}={LAMBDA_ALIAS}&{ep_lambdaf.LAMBDA_REFERENCE_FIELD}={API_TOKEN}.{LAMBDA_TOKEN}'

url = f'{load_manager_url}?{query_string}'

request_headers = {

    "Content-Type": "application/json",
    ep_session.SESSION_TOKEN_HEADER:SESSION_TOKEN

}

def main():

    upload_content = get_upload_content()

    request_body = {
        'api-token':'MgUuJV3bWIdYOKa',
        'uploaded-content': upload_content
    }

    try:

        response = requests.post(url, headers=request_headers, json=request_body)
        response_status = response.status_code
        response_headers = json.dumps(dict(response.headers), indent='\t')

        print(f'Status Code: {response_status}')
        print(f'Headers: {response_headers}')

        response.raise_for_status()
        
        # response_body = json.dumps(response.json(), indent='\t')
        
        # print(response_body)

    except requests.exceptions.RequestException as e:

        no_body = (response.status_code == 500)
        if not no_body:

            response_body = json.dumps(response.json(), indent='\t')
            print(response_body)

def get_upload_content():

    api_key = 'hello-world-api'

    file_path = f'{API_FOLDER}/{api_key}/api-module.py'
    
    with open(file_path, 'r') as file:
        content = file.read()

    escaped_content = json.dumps(content)

    return escaped_content

if __name__ == '__main__':
    main()