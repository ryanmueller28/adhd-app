import yaml
import shutil
import os
import secrets
import string
import random

curr_dir = os.getcwd()
db_files_route = f"{curr_dir}/adhdapp_rs_db"
rs_env_files_route = f"{curr_dir}/adhd_app"

print("Let's create some configs!")

db_host = input("The Database URL (blank will be localhost): ")

if db_host == "":
    db_host = "localhost"

db_port = input("The database port (default for Postgres is 5432): ")
if db_port == "":
    db_port = "5432"

db_user = input("Database username: (leaving blank will be adhdappuser): ")
if db_user == "":
    db_user = "adhdappuser"

db_password = input("Database password (leaving blank will generate a random secure password): ")
if db_password == "":
    valid_chars = string.ascii_letters + string.digits
    pass_len = random.randrange(10, 20)
    db_password = ''.join(secrets.choice(valid_chars) for i in range(pass_len))

db_name = input("Database name (blank will be 'adhd_app'): ")
if db_name == "":
    db_name = "adhd_app"

try:
    db_port_as_num = int(db_port)
    db_port = db_port_as_num
except ValueError as err:
    print(err)
    db_port = 5432

env_db_string = f"DATABASE_URL=postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
with open('.env', 'w') as rs_env_file:
    rs_env_file.writelines(env_db_string)
    env_drop_route = f"{rs_env_files_route}/.env"

    os.remove(f"{env_drop_route}")
    shutil.move(f"{curr_dir}/.env", env_drop_route)


db_yaml = open(f"{db_files_route}/docker-compose.yml", 'r')
conf = yaml.load(db_yaml, Loader=yaml.FullLoader)
conf['services']['db']['environment'] = [
    f'POSTGRES_USER={db_user}',
    f'POSTGRES_PASSWORD={db_password}',
    f'POSTGRES_DB={db_name}'
]

conf['services']['db']['ports'] = [
    f"{db_port}:5432"
]

with open('docker-compose.yml', 'w') as db_yaml_drop:
    yaml.dump(conf, db_yaml_drop, sort_keys=False)
    yaml_drop_route = f"{db_files_route}/docker-compose.yml"
    os.remove(yaml_drop_route)
    shutil.move(f"{curr_dir}/docker-compose.yml", yaml_drop_route)
