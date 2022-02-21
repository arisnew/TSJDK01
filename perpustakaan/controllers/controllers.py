# -*- coding: utf-8 -*-
# from odoo import http


# class Perpustakaan(http.Controller):
#     @http.route('/perpustakaan/perpustakaan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perpustakaan/perpustakaan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('perpustakaan.listing', {
#             'root': '/perpustakaan/perpustakaan',
#             'objects': http.request.env['perpustakaan.perpustakaan'].search([]),
#         })

#     @http.route('/perpustakaan/perpustakaan/objects/<model("perpustakaan.perpustakaan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perpustakaan.object', {
#             'object': obj
#         })
