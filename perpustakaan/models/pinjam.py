from datetime import date, timedelta
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError

class Pinjam(models.Model):
    _name = 'perpustakaan.pinjam'
    _description = 'Pinjam Buku'
    _rec_name = "buku_id"
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

    batas_waktu_pengembalian = fields.Date(
        string='Batas Waktu Pengembalian', 
        default=fields.Datetime.now()+timedelta(days=1),
        required=True
    )

    tanggal_dikembalikan = fields.Date(
        string='Tanggal Dikembalikan',
    )
    

    @api.constrains('tanggal_pinjam', 'batas_waktu_pengembalian')
    def _check_tanggal(self):
        for r in self:
            if r.batas_waktu_pengembalian <= r.tanggal_pinjam:
                raise ValidationError("Tanggal kembali tidak boleh lebih kecil atau sama dengan dari tanggal pinjam")

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
        self.write({'state': 'done','tanggal_dikembalikan': fields.Datetime.now()})

    def action_cancel(self):
        # Validasi dulu
        # Manipulasi dulu
        self.write({'state': 'cancel'})

    def action_reset(self):
        # Validasi dulu
        # Manipulasi dulu
        self.write({'state': 'draft'})

    def unlink(self):
        for r in self:
            if r.state not in ('draft', 'cancel'):
                raise UserError('Kamu tidak bisa menghapus pinjaman yang sudah dikonfirmasi.')
        return super(Pinjam, self).unlink()