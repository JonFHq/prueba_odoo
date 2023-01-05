from odoo import _, api, fields, models

class Portatiles(models.Model):
    _name = "portatiles"
    _description = "portatiles"

    id = fields.Char(string="ID del portatil")
    nombre = fields.Char(string="Nombre del portatil")
    imagen = fields.Image(string="Imagen del producto")
    descripcion = fields.Text(string="Descripcion del portatil")
    propietario = fields.Many2one('usuarios')