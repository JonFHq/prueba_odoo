from odoo import _, api, fields, models

class Transacciones(models.Model):
    _name = "transacciones"
    _rec_name = "nombre"
    _description = "transacciones"

    nombre = fields.Char(string="nombre")
    comprador = fields.Many2one('usuarios')
    vendedor = fields.Many2one('usuarios')
    portatil = fields.Many2one('portatiles')
    precio = fields.Integer(string='Precio')