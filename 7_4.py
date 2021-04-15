import yaml

with open('7_netplan.yaml') as f:
    c = yaml.load(f, yaml.Loader)


for k in c['network']['ethernets'].keys():
    ns = c['network']['ethernets'][k]['nameservers']['addresses']
try:
    ns[ns.index('192.168.1.1')] = '8.8.8.8'
except ValueError:
    pass

with open('7_netplan.yaml', 'w') as f:
    yaml.dump(c, f)
