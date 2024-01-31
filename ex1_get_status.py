import requests, json

def get_status():
    robot_ip='192.168.12.20'
    
    # Get Request
    host = 'http://' + robot_ip + '/api/v2.0.0/status'

    # Format Headers
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='
    print(headers)

    get_status = requests.get(host, headers=headers)
    parsed = json.loads(get_status.content)
    
    json_formatted_str = json.dumps(parsed, indent=2)

    print(json_formatted_str)


get_status()