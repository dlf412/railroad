from django.db import models

# Create your models here.

class Section(models.Model):
    code = models.CharField(max_length=30, verbose_name="标段号", help_text="标段号", unique=True)
    name = models.CharField(max_length=60, verbose_name="标段名称", help_text="标段名称")
    corpCode = models.CharField(max_length=30, verbose_name="承包单位企业代码", unique=True, help_text="承包单位企业代码")
    corpName = models.CharField(max_length=60, verbose_name="承包单位企业名称", db_index=True, help_text="承包单位企业名称")
    address = models.CharField(max_length=200, verbose_name="标段地址", help_text="标段建设地址", default="", blank=True)
    desc = models.CharField(max_length=500, verbose_name="标段描述", help_text="标段描述", default="", blank=True)


class WorkArea(models.Model):
    section = models.ForeignKey(to=Section, verbose_name="标段", help_text="工区所属标段", on_delete=models.CASCADE)
    corpCode = models.CharField(max_length=30, verbose_name="承包单位企业代码", unique=True, help_text="承包单位企业代码")
    corpName = models.CharField(max_length=60, verbose_name="承包单位企业名称", db_index=True, help_text="承包单位企业名称")
    address = models.CharField(max_length=200, verbose_name="工区地址", help_text="工区建设地址", default="", blank=True)
    attendanceRange = models.JSONField(verbose_name="考勤区域", help_text="考勤区域", default="", blank=True)
    attendanceBigRange = models.JSONField(verbose_name="考勤扩张区域", help_text="考勤扩张区域", default="", blank=True)
    desc = models.CharField(max_length=200, verbose_name="工区描述", help_text="工区描述", default="", blank=True)


class Team(models.Model):
    workArea = models.ForeignKey(to=WorkArea, verbose_name="工区", help_text="所属工区", on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name="班组名", help_text="班组名, 工区内唯一")
    leaderName = models.CharField(max_length=60, verbose_name="班组长姓名", help_text="班组长姓名")
    leaderPhone = models.CharField(max_length=20, verbose_name="班组长电话", help_text="班组长电话")


    class Meta:
        unique_together = (('workArea', 'name'),)






