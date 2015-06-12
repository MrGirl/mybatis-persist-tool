filename="ServerMount"
tablename="server_mount"
databaseList=['id','server_id','mount_name','mount_point']
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

propertyList=[]
for field in databaseList:
    camel_field = underline_to_camel(field)
    propertyList.append(camel_field)

print propertyList

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
        str=str+property+",\n"
    
    str=str+"</sql>\n"

    str=str.replace(",\n</sql>","\n</sql>")
    return str


def generateRetrieve(filename,databaseList,propertyList):
    str="<select id=\"retrieve\" parameterClass=\"java.util.HashMap\" resultMap=\""+filename+"Map"+"\">\n"
    str=str+"select\n"
    str=str+"<include refid=\"allColumn\" />\n"
    str=str+"from "+tablename+"\n"
    str=str+"<dynamic prepend=\"where\">\n"
    i=0
    for property in propertyList:
        str=str+"<isNotEmpty prepend=\"and\" property=\""+property+"\">\n"
        str=str+"<![CDATA["+databaseList[i]+"=#"+property+"#]]>\n"
        str=str+"</isNotEmpty>\n"

        i=i+1
    str=str+"</dynamic>\n"
    str=str+"</select>\n"

    return str

def generateList(filename,databaseList,propertyList):
    str="<select id=\"list\" parameterClass=\"java.util.HashMap\" resultMap=\""+filename+"Map"+"\">\n"
    str=str+"select\n"
    str=str+"<include refid=\"allColumn\" />\n"
    str=str+"from "+tablename+"\n"
    str=str+"<dynamic prepend=\"where\">\n"

    i=0
    for property in propertyList:
        str=str+"<isNotEmpty prepend=\"and\" property=\""+property+"\">\n"
        str=str+"<![CDATA["+databaseList[i]+"=#"+property+"#]]>\n"
        str=str+"</isNotEmpty>\n"
        i=i+1
    str=str+"</dynamic>\n"
    str=str+"</select>\n"

    return str
    
def generateInsert(filename,propertyList):
    str="<insert id=\"create\" parameterClass=\""+filename+"\">\n"
    str=str+"insert into "+tablename+"\n"
    str=str+"(\n"
    str=str+"<include refid=\"allColumn\" />\n"
    str=str+")\n"
    str=str+"values(\n"
    for property in propertyList:
        str=str+"#"+property+"#,"
    
    str=str+")"
    str=str.replace("#,)","#)")
    str=str+";\n"
    str=str+"<selectKey resultClass=\"java.lang.Integer\" keyProperty=\"id\">\n"
    str=str+"select last_insert_id() as id from "+tablename+" limit 1\n"
    str=str+"</selectKey>\n"
    str=str+"</insert>"

    return str

def generateDelete(filename):
    str="<delete id=\"delete\" parameterClass=\"java.lang.Integer\">\n"
    str=str+"delete from "+tablename+"\n"
    str=str+"where\n"
    str=str+"id=#id#\n"
    str=str+"</delete>\n"
    return str


def generateUpdate(filename,databaseList,propertyList):
    str="<update id=\"update\" parameterClass=\""+filename+"\">\n"
    str=str+"update "+tablename+"\n"
    str=str+"<dynamic prepend=\"set\">\n"

    i=0
    for property in propertyList:
        str=str+"<isNotEmpty prepend=\",\" property=\""+property+"\">\n"
        str=str+"<![CDATA["+databaseList[i]+"=#"+property+"#]]>\n"
        str=str+"</isNotEmpty>\n"
        i=i+1
    str=str+"</dynamic>\n"

    str=str+"<dynamic prepend=\"where\">\n"
    str=str+"<isNotEmpty prepend=\"and\" property=\"id\">\n"
    str=str+"<![CDATA[id=#id#]]>\n"
    str=str+"</isNotEmpty>\n"
    str=str+"</dynamic>\n"
    str=str+"</update>\n"

    return str


def generateTotal(filename,databaseList,propertyList):
    str="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    str=str+"<!DOCTYPE sqlMap PUBLIC \n"
    str=str+"    \"-//ibatis.apache.org//DTD SQL Map 2.0//EN\" \n"
    str=str+"\"http://ibatis.apache.org/dtd/sql-map-2.dtd\">\n"
    str=str+"<sqlMap namespace=\""+filename+"\">\n"

    str=str+"<typeAlias alias=\""+filename+"\" "+"type=\"com.netease.sentry.biz.domain."+filename+"\"></typeAlias>\n"
    str=str+generateResultMapByPropeties(filename,databaseList,propertyList)+"\n"
    str=str+generateAllColumn(databaseList)+"\n"
    str=str+generateRetrieve(filename,databaseList,propertyList)+"\n"
    str=str+generateInsert(filename,propertyList)+"\n"
    str=str+generateUpdate(filename,databaseList,propertyList)+"\n"
    str=str+generateDelete(filename)+"\n"
    str=str+generateList(filename,databaseList,propertyList)+"\n"
    str=str+"</sqlMap>"
    return str


str=generateTotal(filename,databaseList,propertyList)
print str
file_w=open(filename+".xml","a")
file_w.write(str);