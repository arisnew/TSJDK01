from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpustakaan.buku'
    _description = 'Data Buku'

    name = fields.Char(
        string='Nama Buku',
        required=True,
        help='Isi nama buku...'
    )
    
    publisher = fields.Text(
        string='Penerbit'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    # category_id = fields.Many2one(
    #     comodel_name='sultan.course.category',
    #     string='Category'
    # )