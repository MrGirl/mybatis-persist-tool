#filenames=["Alarm_rule","Application","Collector_app","Collector_base","Collector_system","Data_model","Device_base","Domain_monitor","Domain_superagent","Domain","Machine_room","Monitor_item_config_argument","Monitor_item_config","Monitor_item_host","Monitor_item_status_host","Node","Sentry_group","Sentry_server","Server_disk","Server_memory","Server_network_card","Server_os","Server_pci","Sys_role"]
'''
Created on 2015-6-12

@author: zyd
'''
from datetime import date
import sys

if __name__ == "__main__":
    if len(sys.argv) <=1:
        print 'please enter Interface prefix,eg:python code-Service AlarmRule'
        sys.exit(-1)
    filenames=[]
    filenames=sys.argv[1:]
    for filename in filenames:
        f_w_name = filename+"ServiceImpl.java"
        f_w = open(f_w_name,"w")
    
        importstr = '''
        package com.netease.sentry.biz.service.impl;
    
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.stereotype.Service;\n'''
        importstr=importstr+"    import com.netease.sentry.biz.model."+filename+";\n";
        importstr=importstr+"    import com.netease.sentry.biz.service."+filename+"Service;\n"
        importstr=importstr+"    import com.netease.sentry.biz.persistence."+filename+"Mapper;\n"
        
        v='''
        /**
         * @author hzzhangyuandao
         * @since '''
        v+=str(date.today())
        v+='''
         */
        @Service
        '''
    
        importstr=importstr+v
    
        f_w.write(importstr+"\n");
    
        f_w.write("public class "+filename+"ServiceImpl"+" implements "+filename+"Service {\n");
        f_w.write("@Autowired\n");
        f_w.write("private "+filename+"Mapper "+"mapper;\n");
    
        f_w.write("@Override\n");
        f_w.write("public int create("+filename+" "+filename.lower()+"){\n");
        f_w.write("int num = mapper.create("+filename.lower()+");\n");
        f_w.write("return num==0?num:"+filename.lower()+".getId();\n");
        f_w.write("}\n");
    
    
        #remove
        f_w.write("@Override\n");
        f_w.write("public int delete(int id) {\n");
        f_w.write("return mapper.delete(");
        f_w.write("id);\n");
        f_w.write("}\n");
    
    
        #update
        f_w.write("@Override\n");
        f_w.write("public int update("+filename+" "+filename.lower()+"){\n");
        f_w.write("return mapper.update("+filename.lower()+");\n");
        f_w.write("}\n");
    
        #retrieve
        f_w.write("@Override\n");
        f_w.write("public "+filename+" retrieve(int id) {\n");
        f_w.write("return "+"("+filename+")"+"mapper.retrieve(id);\n");
        f_w.write("}\n");
    
        f_w.write("}");