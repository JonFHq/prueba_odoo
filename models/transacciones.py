from odoo import _, api, fields, models

class Transacciones(models.Model):
    _name = "transacciones"
    _rec_name = "nombre"
    _description = "transacciones"

    nombre = fields.Char(string="Registro", compute='_dependecias')
    comprador = fields.Many2one('usuarios', required=True)
    vendedor = fields.Many2one('usuarios', required=True)
    portatil = fields.Many2one('portatiles', required=True)
    precio = fields.Integer(string='Precio', required=True)
    fecha_venta = fields.Date(string="Fecha de venta", required=True)

    @api.depends('comprador', 'vendedor', 'portatil')
    def _dependecias(self):
        for record in self:
            record.nombre = str(record.comprador.nombre) + ' compro el portatil ' + str(record.portatil.nombre) + ' de ' + str(record.vendedor.nombre) + ' por ' + str(record.precio) + '€' + ' el dia ' + str(record.fecha_venta)

    @api.onchange('vendedor')
    def _onchange_vendedor(self):
        try:
            if self.vendedor:
                if self.vendedor.vendedor == False:
                    raise ValueError("El usuario no es vendedor")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El usuario no es vendedor",
                }
            }

    @api.onchange('vendedor', 'comprador')
    def _onchange_usuarios(self):
        try:
            if self.vendedor and self.comprador:
                if self.vendedor.dni == self.comprador.dni:
                    raise ValueError("No puede comprarse un portatil a si mismo")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "No puede comprarse un portatil a si mismo",
                }
            }

    @api.onchange('portatil', 'vendedor')
    def _onchange_portatil(self):
        try:
            if self.portatil and self.vendedor:
                if self.portatil.vendedor != self.vendedor:
                    raise ValueError("El portatil no pertenece al vendedor") 
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El portatil no pertenece al vendedor",
                }
            }

    @api.onchange('precio')
    def _onchange_precio(self):
        try:
            if self.precio:
                if self.precio <= 0:
                    raise ValueError("El precio no puede ser negativo o gratuito")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El precio no puede ser negativo o gratuito",
                }
            }
