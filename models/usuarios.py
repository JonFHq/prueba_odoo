from odoo import _, api, fields, models

class Usuarios(models.Model):
    _name = "usuarios"
    _description = "usuarios"

    dni = fields.Char(string="DNI", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido")
    telefono = fields.Integer(string="Número de telefono", required=True)
    portatiles = fields.One2many("portatiles", "propietario", string="Portátiles del usuario")
    vendedor = fields.Boolean(string="Vendedor", compute='_vendedor')
    portatiles_venta = fields.One2many("portatiles", "propietario", string="Portátiles a la venta")

    @api.depends('portatiles_venta')
    def _vendedor(self):
        for record in self:
            if len(record.portatiles_venta) > 0:
                record.vendedor = True
            else:
                record.vendedor = False
