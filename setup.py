import subprocess

# Default prefixes for installing apt or pip packages
pip_inst = "pip install "
apt_inst = "sudo apt install "

# List of commands to run from terminal
cmd_list = ["sudo apt update" , "sudo apt upgrade -y"]

apt_pkg_list = ["python", "python3", 
                "python-pip", "python3-pip"]
for apt_pkg in apt_pkg_list:
    cmd_list.append(apt_inst + apt_pkg)

pip_pkg_list = ["selenium"]
for pip_pkg in pip_pkg_list:
    cmd_list.append(pip_inst + pip_pkg)

print("List of commands to run")
for a in cmd_list:
    print(a)
print(">>>>>>>>> Running >>>>>>>>>")

for cmd in cmd_list:
    subprocess.call(cmd.split())
print(">>>>>>>>> Done! >>>>>>>>>")
