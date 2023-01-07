from odoo import _, api, fields, models

class Portatiles(models.Model):
    _name = "portatiles"
    _rec_name = "nombre"
    _description = "portatiles"

    nombre = fields.Char(string="Nombre del portatil", required=True)
    imagen = fields.Image(string="Imagen del producto")
    descripcion = fields.Text(string="Descripcion del portatil", required=True)
    propietario = fields.Many2one('usuarios', required=True)