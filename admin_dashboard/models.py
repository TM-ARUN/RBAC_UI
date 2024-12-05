from django.db import models


class Permission1(models.Model):
    Name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    Status = models.CharField(max_length=15,default="active")
class meta:
    db_table = "Permission1"
class Role(models.Model):
    Role_name = models.CharField(max_length=50)
    Description = models.TextField(max_length=150)
    Assigned_permission = models.ManyToManyField('Permission1')
    Status = models.CharField(max_length=15)
class meta:
    db_table = "Role"
class tbl_user(models.Model):
    Username = models.CharField(max_length=25)
    Email = models.CharField(max_length=50)
    Roles = models.ForeignKey('Role',on_delete=models.SET_NULL,null=True)
    Status = models.CharField(max_length=15)
class meta:
    db_table="tbl_user"

    



