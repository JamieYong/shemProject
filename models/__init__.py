import json

import peewee as pw
import sys
from src.util import Util
from shem_configs import shem_configs
from playhouse.pool import PooledMySQLDatabase

utilClass = Util()

shemdb = pw.MySQLDatabase(shem_configs['prod_db_schema'], host=shem_configs['prod_db_host'], port=3306,
                          user=shem_configs['prod_db_user'], passwd=shem_configs['prod_db_passwd'])

class JSONField(pw.TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = shemdb

class hardwareTable(MySQLModel):
    class Meta:
        db_table = 'hardwareTable'
    id = pw.IntegerField()
    value = pw.FloatField()

class houseTable(MySQLModel):
    class Meta:
        db_table = 'houseTable'
    
    id = pw.IntegerField()
    #isTrip = pw.BooleanField(default=False) # 여행모드 켰는가?
    #tripFrom = pw.DateTimeField() # 여행 모드 시작 날짜
    #tripTo = pw.DateTimeField() # 여행 모드 끝날 날짜
    created_at = pw.DateTimeField()
    updated_at = pw.DateTimeField()

class usersTable(MySQLModel):
    class Meta:
        db_table = 'usersTable'

    id = pw.IntegerField()
    username = pw.CharField()
    email = pw.CharField()
    nickname = pw.CharField()
    password = pw.CharField()
    resetPasswordToken = pw.CharField()
    confirmed = pw.IntegerField()
    name = pw.CharField()
    resetPasswordRequestDatetime = pw.DateTimeField()
    resetPasswordVerifyLink = pw.CharField()
    resetPasswordVerifyTokenID = pw.CharField()
    emailVerifyRequestDatetime = pw.CharField()
    emailVerifyDatetime = pw.CharField()
    emailVerifyTokenID = pw.CharField()
    emailVerifyLink = pw.CharField()
    emailChangeValue = pw.CharField()
    emailChangeRequestDatetime = pw.CharField()
    created_at = pw.DateTimeField()
    updated_at = pw.DateTimeField()
    emailVerifiedYN = pw.CharField()
    emailTokenCode = pw.CharField()
    token = pw.TextField()
    gender = pw.CharField()
    birth = pw.DateField
    appTokenCode = pw.CharField()
    appTokenCodeUpdatedAt = pw.DateTimeField()
    address = pw.CharField()
    isDeleteRequested = pw.IntegerField

class linkedHouseAndHardware(MySQLModel):
    class Meta:
        db_table = 'linkedHouseAndHardware'
    id = pw.IntegerField()
    houseId = pw.ForeignKeyField(houseTable, to_field='id')
    hardwareId = pw.ForeignKeyField(hardwareTable, to_field='id')
    created_at = pw.DateTimeField()
    updated_at = pw.DateTimeField()

# user, house 의 id를 연결하는 관계 테이블
class linkedUserAndHouse(MySQLModel):
    class Meta:
        db_table = 'linkedUserAndHouse'
    id = pw.IntegerField()
    houseId = pw.ForeignKeyField(houseTable, to_field='id')
    userId = pw.ForeignKeyField(usersTable, to_field='id')
    created_at = pw.DateTimeField()
    updated_at = pw.DateTimeField()
