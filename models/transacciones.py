from odoo import _, api, fields, models

class Transacciones(models.Model):
    _name = "prueba.transacciones"
    _description = "transacciones"

    id = fields.Id(string="ID de la transaccion")
    precio_de_compra = fields.Integer(string='Precio de compra')