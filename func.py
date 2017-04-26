from os import environ
from zabbix.api import ZabbixAPI

def check_stat(hostlist):
    print hostlist
    zapi = ZabbixAPI(url=environ['ZABBIX_URL'], user=environ['ZABBIX_USER'], password=environ['ZABBIX_PASSWORD'])
    status = "green"
    for host in hostlist:
        result = zapi.do_request('trigger.get', { 'active':1, 'only_true':1, 'hostids': host })['result']
        for x in xrange(len(result)):
            if int(result[x]['priority']) > 3:
	        status = "red"
    return status 
