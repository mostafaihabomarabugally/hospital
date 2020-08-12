from odoo import models , fields , api

class Hospitlpatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'pationt Record'
    _rec_name = 'patient_Name'
    
    patient_Name = fields.Char(string = 'Name' , required = True)
    patient_Age = fields.Integer('Age')
    notes = fields.Text(string ='Notes' )
    image = fields.Binary(string = 'image')
    name = fields.Char(string = 'Test')
    name_seq = fields.Char(string = 'Oreder Referance' ,required=True ,copy=False , readonly=True,
                                index=True , default=lambda self: _('New'))


    @api.model
    def create(self , vals):
        if vals.get('name_seq', _('New')) ==  _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next.by.code('hospital.patient.sequence')or _('New')
        result = super(Hospitlpatient, self).create(vals)
        return result