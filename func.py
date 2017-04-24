from os import environ
from zabbix.api import ZabbixAPI


def check_stat(hosts):
    print hosts
    zapi = ZabbixAPI(url=environ['ZABBIX_URL'], user=environ['ZABBIX_USER'], password=environ['ZABBIX_PASSWORD'])
    status = "green"
    for host in hosts:
        result = zapi.do_request('trigger.get', { 'active':1, 'only_true':1, 'hostids': host })['result']
        for x in xrange(len(result)):
            if int(result[x]['priority']) > 3:
	        status = "red"
    return status 

# Tenant Services
tenant_services = [ int(x) for x in environ['TENANTS_HOSTS'].split(',')]
# platform
platform = [ int(x) for x in environ['PLATFORM_HOSTS'].split(',')]
# Authentication
auth = [ int(x) for x in environ['AUTH_HOSTS'].split(',')]
# Dependencies
dependencies = [ int(x) for x in environ['DEPS_HOSTS'].split(',')]

