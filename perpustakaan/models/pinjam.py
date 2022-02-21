from odoo import api, fields, models


class Pinjam(models.Model):
    _name = 'perpustakaan.pinjam'
    _description = 'Pinjam Buku'

    siswa_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Peminjam',
        domain="[('siswa','=',True)]"
    )
    
    buku_id = fields.Many2one(
        comodel_name='perpustakaan.buku', 
        string='Buku'
    )

    tanggal_pinjam = fields.Date(
        string='Session Date', 
        default=fields.Datetime.now()
    )

    # Draft, Dipinjam, Dikembalikan, batal
    state = fields.Selection(
        string='state', 
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
