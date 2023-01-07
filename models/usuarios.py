from odoo import _, api, fields, models

class Usuarios(models.Model):
    _name = "usuarios"
    _rec_name = "nombre"
    _description = "usuarios"

    dni = fields.Char(string="DNI", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    imagen = fields.Image()
    telefono = fields.Integer(string="Número de telefono", required=True)
    email = fields.Char(string="Correo", required=True)
    portatiles = fields.One2many("portatiles", "propietario", string="Portátiles del usuario")
    portatiles_vendidos = fields.One2many("portatiles", "propietario", string="Portátiles a la venta")
    vendedor = fields.Boolean(string="Vendedor", compute='_vendedor')

    @api.depends('portatiles')
    def _vendedor(self):
        for record in self:
            if len(record.portatiles) > 0:
                record.vendedor = True
            else:
                record.vendedor = False
