from odoo import _, api, fields, models

class Portatiles(models.Model):
    _name = "portatiles"
    _rec_name = "nombre"
    _description = "portatiles"

    nombre = fields.Char(string="Nombre del portatil", required=True)
    imagen = fields.Image(string="Imagen del producto")
    descripcion = fields.Text(string="Descripcion del portatil", required=True)
    vendedor = fields.Many2one('usuarios', required=True)
    vendido = fields.Boolean(string="Vendido", compute='_vendido')
    venta = fields.One2many('transacciones', 'portatil')

    @api.depends('vendedor')
    def _vendido(self):
        for record in self:
            for venta in record.vendedor.ventas:
                if venta.portatil == self:
                    record.vendido = True
                else:
                    record.vendido = False
