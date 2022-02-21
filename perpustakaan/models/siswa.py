from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    siswa = fields.Boolean(
        string='Siswa',
        default=False
    )
