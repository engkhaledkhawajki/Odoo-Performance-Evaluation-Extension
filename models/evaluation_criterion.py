from odoo import models, fields, api, _


class EvaluationCriterion(models.Model):
    _name = 'evaluation.criterion'
    _description = 'Evaluation Criterion'

    name = fields.Char(string='Name', default=lambda x: _('New'))
    type = fields.Selection(selection=[
        ('objectives', "Objectives"),
        ('kpis', "KPIs"),
        ('behavioral_competencies', "Behavioral Competencies"),
        ('hr_department', "HR Department"),
    ], required=True)
    criterion_evaluation_type = fields.Selection([
        ('production', "Production"),
        ('administrators', "Administrators"),
        ('technician_process_administrators', "Technician Process Administrators"),
        ('employment', "Employment"),
        ('sales_and_marketing', "Sales & Marketing"),
        ('technician', "Technician"),
    ], default=False, string="In Relation with", help="Technical field for UX purpose.")
    criterion = fields.Char(string='Criterion', required=True)
    weight = fields.Float(string='Weight', required=True, default=0.0)

    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['criterion'] = vals['name']
        else:
            vals['name'] = vals['criterion']
        result = super(EvaluationCriterion, self).create(vals)
        return result

    def get_type(self, type):
        if type == 'objectives':
            return "Objectives"
        if type == 'kpis':
            return "KPIs"
        if type == 'behavioral_competencies':
            return "Behavioral Competencies"
        if type == 'hr_department':
            return "HR Department"

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s' % rec.criterion))
        return result

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = _("%s (Copy)") % self.name
        return super(EvaluationCriterion, self).copy(default=default)
