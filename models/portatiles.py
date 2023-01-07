from odoo import _, api, fields, models

class Portatiles(models.Model):
    _name = "portatiles"
    _rec_name = "nombre"
    _description = "portatiles"

    nombre = fields.Char(string="Nombre del portatil")
    imagen = fields.Image(string="Imagen del producto")
    descripcion = fields.Text(string="Descripcion del portatil")
    propietario = fields.Many2one('usuarios')