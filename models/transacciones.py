from odoo import _, api, fields, models

class Transacciones(models.Model):
    _name = "transacciones"
    _rec_name = "nombre"
    _description = "transacciones"

    nombre = fields.Char(string="nombre", compute='_nombre')
    comprador = fields.Many2one('usuarios', required=True)
    vendedor = fields.Many2one('usuarios', required=True)
    portatil = fields.Many2one('portatiles', required=True)
    precio = fields.Integer(string='Precio', required=True)

    @api.depends('comprador', 'vendedor', 'portatil')
    def _nombre(self):
        for record in self:
            record.nombre = str(record.comprador.nombre) + ' compro el portatil ' + str(record.portatil.nombre) + ' de ' + str(record.vendedor.nombre)

    @api.onchange('vendedor')
    def _onchange_vendedor(self):
        if self.vendedor.vendedor == False:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El usuario no es vendedor",
                },
            }
    
    @api.onchange('vendedor', 'comprador')
    def _onchange_usuarios(self):
        if self.vendedor.dni == self.comprador.dni:
            return {
                'warning': {
                    'title': "Error",
                    'message': "No puede comprar un portatil a si mismo",
                },
            }

    @api.onchange('portatil', 'vendedor')
    def _onchange_portatil(self):
        if self.portatil.propietario != self.vendedor:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El portatil no pertenece al vendedor",
                },
            }