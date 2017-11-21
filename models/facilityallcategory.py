# -*- coding: utf-8 -*-


from odoo import models, fields
from datetime import date, datetime

class Facility(models.Model):
    _name='facility'
    
    name = fields.Char()
    price = fields.Float("Price")
    
class Food(models.Model):
    _name='food'
    
    name = fields.Char(string="food")
    code = fields.Char(string="code")
    price = fields.Float("Price")
    
class Room(models.Model):
    _name='room'
    
    name = fields.Char(string="Type of Room")
    price = fields.Float("Price")
#    no = fields.Integer(string="Room No")
    
