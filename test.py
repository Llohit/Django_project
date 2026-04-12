'''
The report must identify:
All Admin IDs: Every user who currently possesses administrative power.
All Non-Admin IDs: Every user who does not.
'''
from httplib2 import Response
from nipype.interfaces.io import unquote_id
from typing_extensions import reveal_type

records = {
    "users": [
        {"u_id": "101", "name": "Alice", "admin": True},
        {"u_id": "102", "name": "Bob", "admin": False},
        {"u_id": "103", "name": "Charlie", "admin": False},
        {"u_id": "104", "name": "David", "admin": False},
        {"u_id": "105", "name": "Eve", "admin": True}
    ],
    "groups": [
        {"g_id": "g_01", "name": "Super-Admins", "is_admin": True},
        {"g_id": "g_02", "name": "Marketing", "is_admin": False},
        {"g_id": "g_03", "name": "Incident-Response", "is_admin": True}
    ],
    "memberships": [
        {"uid": "101", "gid": "g_02"},
        {"uid": "102", "gid": "g_01"},
        {"uid": "103", "gid": "g_02"},
        {"uid": "104", "gid": "g_01"},
        {"uid": "104", "gid": "g_03"}
    ]
}
def get_grp_id_for_user(memberships_info,user_id):
    grp_ids = []
    for mem_inf in memberships_info:
        if mem_inf["uid"] == user_id:
            grp_ids.append(mem_inf["gid"])
    return grp_ids

def check_admin_access_for_group(groups_info,grp_ids):
    for grp_inf in groups_info:
        if grp_inf["g_id"] in grp_ids and grp_inf["is_admin"]:
            return True

def get_admin_non_admin_info(records: dict)-> list[str]:
    users_info = records["users"]
    memberships_info = records["memberships"]
    groups_info = records["groups"]
    admin_ids = []
    non_admin_ids = []
    for user in users_info:
        if user['admin']:
            admin_ids.append(user['u_id'])
        else:
            grp_ids = get_grp_id_for_user(memberships_info,user['u_id']) #[g_01,g_03]
            is_grp_admin_access = check_admin_access_for_group(groups_info,grp_ids) #True
            if is_grp_admin_access:
                admin_ids.append(user['u_id'])
            else:
                non_admin_ids.append(user['u_id'])

    return admin_ids,non_admin_ids

print(get_admin_non_admin_info(records))

def get_from_topic(data_to_send):
    size_of_data = calc_size(data_to_send['data_to_proc'])
    current_total_upload = 0
    total_chunks = size_of_data/100
    while(total_chunks):
        store_in_s3(size_of_data[:100])
        total_chunks-=1
        current_total_upload+=100
        current_prog = (current_total_upload/size_of_data)*100
        store_prog_for_uuid(data_to_send['uid'],current_prog)

def post(request):
    uid = 1234
    current_prg = 0
    data_recd = request.data
    #Data is sent for background processing
    data_to_send = {"uid":1234,"data_to_proc": data_recd}
    put_in_a_kafka_topic(data_to_send)
    # Store uid and current_prg in table
    return Response(f"Request created with {uid}")

def retrieve(request,id):
    current_progr_for_id = get_prog(id) #0
    return current_progr_for_id


uid = 1234
current_prg = 10

