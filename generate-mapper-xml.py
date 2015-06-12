def underline_to_camel(underline_format):
    camel_format = ''
    if isinstance(underline_format,str):
        if underline_format.find("_")!=-1:
            i=0
            for _s_ in underline_format.split('_'):
                if i!=0:
                    _s_=_s_[0].upper()+_s_[1:]
                camel_format += _s_
                i+=1
        else:
            camel_format=underline_format
    return camel_format



def generateResultMapByPropeties(filename,databaseList,propetyList):
    str="<resultMap id=\""+filename+"Map\""+" class=\""+filename+"\">\n";
    i=0
    for property in propertyList:
        line="<result property=\""+property+"\""+" column=\""+databaseList[i]+"\"/>\n"
        str=str+line
        i=i+1
    
    str=str+"</resultMap>\n"
    return str


def generateAllColumn(databaseList):
    str="<sql id=\"allColumn\">\n"
    for property in databaseList:
        str=str+property+" as "+underline_to_camel(property)+",\n"
    
    str=str+"</sql>\n"

    str=str.replace(",\n</sql>","\n</sql>")
    return str


def generateRetrieve(filename,databaseList,propertyList):
    str="<select id=\"retrieve\" parameterType=\"java.lang.Integer\" resultType=\""+filename+"\">\n"
    str=str+"select\n"
    str=str+"<include refid=\"allColumn\" />\n"
    str=str+"from "+tablename+"\n"
    str=str+"where id = #{id}"
    
    str=str+"</select>\n"

    return str
    
def generateInsert(filename,databaseList,propertyList):
    str="<insert id=\"create\" parameterType=\""+filename+"\""+" useGeneratedKeys=\"true\" keyProperty=\"id\""+">\n"
    str=str+"insert into "+tablename+"\n"
    str=str+"(\n"
    str=str+",".join(databaseList)+"\n"
    str=str+")\n"
    str=str+"values(\n"
    for property in propertyList:
        str=str+"#{"+property+"},"
    
    str=str+")"
    str=str.replace(",)",")")
    str=str+";\n"
    str=str+"</insert>"

    return str

def generateDelete(filename):
    str="<delete id=\"delete\" parameterType=\"java.lang.Integer\">\n"
    str=str+"delete from "+tablename+"\n"
    str=str+"where\n"
    str=str+"id=#{id}\n"
    str=str+"</delete>\n"
    return str


def generateUpdate(filename,databaseList,propertyList):
    str="<update id=\"update\" parameterType=\""+filename+"\">\n"
    str=str+"update "+tablename+"\n"
    str=str+"<set>\n"
    i=0
    for property in propertyList:
        str=str+"<if test=\""+property+" != null\">"+databaseList[i]+"=#{"+property+"},</if>\n"
        i+=1
    str=str+"modify_time=now()\n"
    str=str+"</set>\n"
    str=str+"where id=#{id}\n"
    str=str+"</update>\n"

    return str

def generateQueryCondition(databaseList):
    str="<sql id=\"queryPage-condition\">\n"
    for property in databaseList:
        str=str+"<if test=\""+property+" != null\">and"+property+"=#{"+underline_to_camel(property)+"}</if>\n"
    return str
    


def generateTotal(filename,databaseList,propertyList):
    str="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    str=str+"<!DOCTYPE mapper  \n"
    str=str+"PUBLIC \"-//mybatis.org//DTD Mapper 3.0//EN\" \n"
    str=str+"\"http://mybatis.org/dtd/mybatis-3-mapper.dtd\">\n"
    str=str+"<mapper namespace=\"com.netease.sentry.biz.persistence."+filename+"Mapper\">\n"

    str=str+generateAllColumn(databaseList)+"\n"
    str=str+generateInsert(filename,databaseList,propertyList)+"\n"
    str=str+generateRetrieve(filename,databaseList,propertyList)+"\n"
    str=str+generateUpdate(filename,databaseList,propertyList)+"\n"
    str=str+generateDelete(filename)+"\n"


    str=str+"</mapper>"
    return str

if __name__ == "__main__":
    filename="TaskAsignParameter"
    tablename="task_asign_parameter"
    databaseList=['id','create_time','modify_time','api_client_id','api_usage','exec_account','target_server','command_whitelist','ip_whitelist','timedue','applicant','status']
    propertyList=[]
    for field in databaseList:
        camel_field = underline_to_camel(field)
        propertyList.append(camel_field)
    
    print propertyList
    str=generateTotal(filename,databaseList,propertyList)
    print str
    file_w=open(filename+"Mapper.xml","w")
    file_w.write(str);