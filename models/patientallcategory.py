# -*- coding: utf-8 -*-


from odoo import api, models, fields,_
from datetime import date, datetime

class Patient(models.Model):
    _name ='patient.patient'
    _inherit = ['mail.thread']
    
    photo = fields.Binary()
    unique_id = fields.Char(required=True)
    name = fields.Char(required=True)
    category = fields.Many2many('categorypatient', 'patient_catagorypatient_rel', 'patient_id', 'categorypatient_id', 'Category')
    birthdate = fields.Date()
    deseased_date = fields.Datetime(
        string='Deceased Date',
    )
    room_no = fields.Many2one('roomno', string='Room No')
    doctor_id = fields.Many2one('doctor')
    age = fields.Char(required=True)
    address = fields.Char()
    general_info = fields.Text(
        string='General Information',
    )
    is_deceased = fields.Selection([
        ('y', 'Yes'),
        ('m', 'No'),   
    ], )
    marital_status = fields.Selection([
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ('z', 'law marriage'),
    ], )
    doctorassigned_ids = fields.Many2many('doctor', 'patient_doctor_rel', 'patient_id', 'doctor_id', 'Assidned Doctor')
    food_id = fields.Many2one('food', string="Food")
    roomtype_id = fields.Many2one('room', string="Room")
    facility_id = fields.Many2many('facility', 'patient_facility_rel', 'patient_id', 'facility_id', string="Other Facilities")
    mobile = fields.Char("Mobile")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    
    @api.multi
    def action_patient_report_mail_sent(self):
        print "\n CalL-------------------"
        self.ensure_one()
        template = self.env.ref('hospital_management.email_template_patient_report', False)
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        ctx = dict(
            default_model='patient.patient',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
#            default_composition_mode='comment',
#            mark_invoice_as_sent=True,
#            custom_layout="account.mail_template_data_notification_email_account_invoice"
        )
        print "------ctx--------",ctx
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }

#    @api.onchange('birthdate') 
#    def onchange_name(self):
#        current_date = datetime.now()
#        current_year = current_date.year
        

class Roomno(models.Model):
    _name = 'roomno'
    
    
    name = fields.Char("Room No")
    
    
class Categorypatient(models.Model):
    _name='categorypatient'
    
    
    name = fields.Char(string = 'Type')
    code = fields.Char(string='code')
    
    
    
    
    
    