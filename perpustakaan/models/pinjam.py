from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Pinjam(models.Model):
    _name = 'perpustakaan.pinjam'
    _description = 'Pinjam Buku'

    siswa_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Peminjam',
        domain="[('siswa','=',True)]",
        required=True
    )
    
    buku_id = fields.Many2one(
        comodel_name='perpustakaan.buku', 
        string='Buku',
        required=True
    )

    tanggal_pinjam = fields.Date(
        string='Tanggal Pinjam', 
        default=fields.Datetime.now(),
        required=True
    )

    tanggal_kembali = fields.Date(
        string='Tanggal Kembali', 
        default=fields.Datetime.now(),
        required=True
    )
    

    @api.constrains('tanggal_pinjam', 'tanggal_kembali')
    def _check_tanggal(self):
        for r in self:
            if r.tanggal_kembali < r.tanggal_pinjam:
                raise ValidationError("Tanggal kembali tidak boleh lebih kecil dari tanggal pinjam")

    # Draft, Dipinjam, Dikembalikan, batal
    state = fields.Selection(
        string='Status', 
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Dipinjam'),
            ('done', 'Sudah kembali'),
            ('cancel', 'Batal'),
    ], readonly=True, default="draft", required=True)

    def action_confirm(self):
        # Validasi dulu
        # Manipulasi dulu
        self.write({'state': 'confirm'})

    def action_done(self):
        # Validasi dulu
        # Manipulasi dulu
        self.write({'state': 'done'})

    def action_cancel(self):
        # Validasi dulu
        # Manipulasi dulu
        self.write({'state': 'cancel'})

    def action_reset(self):
        # Validasi dulu
        # Manipulasi dulu
        self.write({'state': 'draft'})
