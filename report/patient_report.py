from odoo import api, models

class PatientReport(models.AbstractModel):
    _name = 'report.hospital_management.report_patient'

    @api.model
    def render_html(self, docids, data=None):
        print '??????????????????????????????????????????????????????'
        Report = self.env['report']
        report = Report._get_report_from_name('hospital_management.report_patient')
        records = self.env['patient.patient'].browse(docids)
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': records,
            'data': data,
        }
        return Report.render('hospital_management.report_patient',
                             docargs)
