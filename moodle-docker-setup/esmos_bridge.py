import odoorpc
import subprocess

# --- CONFIGURATION ---
ODOO_HOST = '13.70.7.145'
ODOO_DB = 'ESMOS'
ODOO_USER = 'admin@esmos.meals.sg'
ODOO_PASS = 'Esmos1234!'
COURSE_ID = 2

def get_moodle_completions():
    # Query to find users who finished Course ID 2
    query = f"SELECT username, email, firstname, lastname FROM moodle.mdl_user WHERE id IN (SELECT userid FROM moodle.mdl_course_completions WHERE course = {COURSE_ID} AND timecompleted IS NOT NULL);"
    cmd = f"docker exec clouddb mysql -u moodleuser -p'Esmos1234!' -N -s -e \"{query}\""
    try:
        result = subprocess.check_output(cmd, shell=True).decode('utf-8')
        users = []
        for line in result.strip().split('\n'):
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 4:
                    users.append({
                        'username': parts[0],
                        'email': parts[1],
                        'firstname': parts[2],
                        'lastname': parts[3]
                    })
        return users
    except Exception as e:
        print(f"Moodle DB Connection Error: {e}")
        return []

# --- THE MISSING EXECUTION BLOCK ---
try:
    # 1. Connect to Odoo (Port 80 as we discovered)
    odoo = odoorpc.ODOO(ODOO_HOST, port=80)
    odoo.login(ODOO_DB, ODOO_USER, ODOO_PASS)
    print("Successfully connected to Odoo API.")
    
    # 2. Get list of completed users from Moodle
    completed_users = get_moodle_completions()
    
    if not completed_users:
        print("No new course completions found in Moodle.")
    
    # 3. Process each user
    res_users = odoo.env['res.users']
    for user in completed_users:
        print(f"Checking status for: {user['email']}")
        # Check if they already exist in Odoo
        existing_user = res_users.search([('login', '=', user['email'])])
        
        if not existing_user:
            print(f"Creating Odoo account for {user['firstname']} {user['lastname']}...")
            res_users.create({
                'name': f"{user['firstname']} {user['lastname']}",
                'login': user['email'],
                'email': user['email'],
                'groups_id': [(6, 0, [odoo.env.ref('base.group_portal').id])],
		'password': 'Esmos2026Password!'
            })
        else:
            print(f"User {user['email']} already exists in Odoo.")

except Exception as e:
    print(f"Odoo Sync Error: {e}")
