import json
import requests

REQUEST_VERB = 'PATCH'
API_TOKEN = 'cluster'
RESOURCE_TOKEN = 'sessions'

def main():

    load_manager_url = "https://eur-001.endpointer.com"

    url = f'{load_manager_url}/{API_TOKEN}/{RESOURCE_TOKEN}/5pH8ERdLccppnz4'

    headers = {
        "Content-Type": "application/json"
    }

    body = {}

    try:

        print(f'\n{REQUEST_VERB} {url}')
        
        response = requests.patch(url, headers=headers, json=body)
        
        sent_headers = response.request.headers
        headers.update(sent_headers)
        print(headers)
        print(f'{body}\n')

        response_status = response.status_code
        
        response_header_dict = dict(response.headers)
        response_headers = json.dumps(response_header_dict, indent='\t')

        print(f'Status Code: {response_status}')
        print(f'Headers: {response_headers}')

        response.raise_for_status()
        
        print_response(response)

    except requests.exceptions.RequestException as e:

        is_500 = (response.status_code == 500)
        if is_500:
        
            sent_headers = response.request.headers
            headers.update(sent_headers)
            print(headers)
            print(f'{body}\n')

        no_body = (response.status_code == 500) or (response.status_code == 404)
        if not no_body:
            print_response(response)

def print_response(response):

    response_json = response.json()
    response_body = json.dumps(response_json, indent='\t')

    print(response_body)


if __name__ == '__main__':
    main()
