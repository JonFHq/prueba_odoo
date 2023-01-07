from odoo import _, api, fields, models

class Transacciones(models.Model):
    _name = "transacciones"
    _rec_name = "nombre"
    _description = "transacciones"

    nombre = fields.Char(string="nombre", compute='_nombre')
    comprador = fields.Many2one('usuarios')
    vendedor = fields.Many2one('usuarios')
    portatil = fields.Many2one('portatiles')
    precio = fields.Integer(string='Precio')

    @api.depends('comprador', 'vendedor', 'portatil')
    def _nombre(self):
        for record in self:
            record.nombre = record.comprador + ' compro el portatil ' + record.portatil + ' de ' + record.vendedor

    @api.onchange('vendedor')
    def _onchange_vendedor(self):
        if self.vendedor.vendedor == False:
            return Warning