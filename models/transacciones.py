from odoo import _, api, fields, models

class Transacciones(models.Model):
    _name = "prueba.transacciones"
    _description = "transacciones"

    comprador = fields.Many2many('usuarios')
    vendedor = fields.Many2many('usuarios')
    portatil = fields.Many2one('portatiles')
    precio_de_compra = fields.Integer(string='Precio de compra')