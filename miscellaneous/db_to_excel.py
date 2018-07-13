import xlsxwriter
from peewee import *

db = SqliteDatabase('list.db')

workbook = xlsxwriter.Workbook('testing.xlsx', {'in_memory': True})
worksheet = workbook.add_worksheet()

