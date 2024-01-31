import requests, json, threading, time

def send_mission(num):
    robot_ip='192.168.12.20'
    pos = [ 'f8fda182-717e-11ee-a0c8-0001299981a2', # 0
            '5d6ad2d7-7323-11ee-bad0-0001299981a2'  # 1
]
    mission_id = {"mission_id": pos[num]}

    # Get Request
    host = 'http://' + robot_ip + '/api/v2.0.0/'

    # Format Headers
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = 'Basic OmUzYjBjNDQyOThmYzFjMTQ5YWZiZjRjODk5NmZiOTI0MjdhZTQxZTQ2NDliOTM0Y2E0OTU5OTFiNzg1MmI4NTU='
    print(headers)

    post_mission = requests.post(host + 'mission_queue', json=mission_id, headers=headers)


send_mission(0)
send_mission(1)
send_mission(0)