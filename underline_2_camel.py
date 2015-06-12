import string
def underline_to_camel(underline_format):
    camel_format = ''
    if isinstance(underline_format,str):
        for _s_ in underline_format.split('_'):
            _s_=_s_[0].upper()+_s_[1:]
            camel_format += _s_
    return camel_format

def underline_to_camel_fromfile(javafile):
    myfile=open(javafile,"r")
    alllines=""
    for line in myfile:
        if line.find("_")!=-1:
            elems=line.split("_")
            for i in range(0,len(elems)):
                if i!=0:
                    #first char capitalize
                    elems[i]=elems[i][0].upper()+elems[i][1:]
            newline=string.join(elems,'')

            alllines+=newline+"\n"
        else:
            alllines+=line+"\n"
    myfile.close()
    return alllines

#javafiles=["IAlarm_ruleService.java","IApplicationService.java","ICollectorBaseService.java","ICollector_appService.java","ICollector_baseService.java","ICollector_systemService.java","IData_modelService.java","IDevice_baseService.java","IDomainService.java","IDomain_monitorService.java","IDomain_superagentService.java","IMachine_roomService.java","IMonitor_item_configService.java","IMonitor_item_config_argumentService.java","IMonitor_item_hostService.java","IMonitor_item_status_hostService.java","INodeService.java","ISentry_groupService.java","ISentry_serverService.java","IServer_diskService.java","IServer_memoryService.java","IServer_network_cardService.java","IServer_osService.java","IServer_pciService.java","ISys_roleService.java","IUserService.java","IUser_object_roleService.java"]
#javafiles=["Alarm_ruleService.java","ApplicationService.java","CollectorBaseService.java","Collector_appService.java","Collector_baseService.java","Collector_systemService.java","Data_modelService.java","Device_baseService.java","DomainService.java","Domain_monitorService.java","Domain_superagentService.java","Machine_roomService.java","Monitor_item_configService.java","Monitor_item_config_argumentService.java","Monitor_item_hostService.java","Monitor_item_status_hostService.java","NodeService.java","Sentry_groupService.java","Sentry_serverService.java","Server_diskService.java","Server_memoryService.java","Server_network_cardService.java","Server_osService.java","Server_pciService.java","Sys_roleService.java","UserService.java","User_object_roleService.java"]
#javafiles=["Alarm_rule.java","Application.java","CollectorBase.java","Collector_app.java","Collector_base.java","Collector_system.java","Data_model.java","Data_model_field.java","Device_base.java","Domain.java","Domain_monitor.java","Domain_superagent.java","Machine_room.java","Monitor_item_config.java","Monitor_item_config_argument.java","Monitor_item_host.java","Monitor_item_status_host.java","Node.java","Sentry_group.java","Sentry_server.java","Server_cpu.java","Server_disk.java","Server_memory.java","Server_network_card.java","Server_os.java","Server_pci.java","Sys_role.java","User.java","User_object_role.java"]
javafiles=["Application.java"]
for javafile in javafiles:
	to_javafile=underline_to_camel(javafile)
	if to_javafile==javafile:
		to_javafile=to_javafile+"1"

	print to_javafile

	to_javafile_handler = open(to_javafile,'w')

	content = underline_to_camel_fromfile(javafile)
	#print content
	to_javafile_handler.write(content)
	to_javafile_handler.close()
    
    