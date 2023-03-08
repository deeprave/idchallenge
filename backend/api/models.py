from django.db import models


class Gender(models.Model):
    id = models.IntegerField(verbose_name='SEX_ABS', primary_key=True, editable=False, serialize=True)
    gender = models.CharField(verbose_name='Sex', max_length=8)

    def description(self):
        return self.gender

    class Meta:
        db_table = 'gender'


class Age(models.Model):
    id = models.IntegerField(verbose_name='AGE', primary_key=True, editable=False, serialize=True)
    age = models.CharField(verbose_name='age', max_length=20)

    def description(self):
        return self.age

    class Meta:
        db_table = 'age'


class State(models.Model):
    id = models.IntegerField(verbose_name='STATE', primary_key=True, editable=False, serialize=True)
    state = models.CharField(verbose_name='State', max_length=32)

    def description(self):
        return self.state

    class Meta:
        db_table = 'state'


class RegionType(models.Model):
    id = models.CharField(verbose_name='REGIONTYPE', max_length=4, primary_key=True, editable=False, serialize=True)
    geography_level = models.CharField(verbose_name='Geography Level', max_length=32)

    def description(self):
        return self.geography_level

    class Meta:
        db_table = 'region_type'


class Region(models.Model):
    id = models.IntegerField(verbose_name='ASGS_2016', primary_key=True, editable=False, serialize=True)
    region = models.CharField(verbose_name='Region', max_length=64)

    def description(self):
        return self.region

    class Meta:
        db_table = 'region'


class Year(models.Model):
    id = models.IntegerField(verbose_name='TIME', primary_key=True, editable=False, serialize=True)
    year = models.CharField(verbose_name='Census year', max_length=6)

    def description(self):
        return self.year

    class Meta:
        db_table = 'year'


class Statistic(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    regiontype = models.ForeignKey(RegionType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    value = models.BigIntegerField(verbose_name='Value')
    flag_codes = models.CharField(verbose_name='Flag Codes', max_length=8)
    flags = models.CharField(verbose_name='Flags', max_length=12)

    def description(self):
        return self.value

    class Meta:
        db_table = 'statistic'
