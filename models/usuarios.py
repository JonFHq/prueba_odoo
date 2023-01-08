from odoo import _, api, fields, models

class Usuarios(models.Model):
    _name = "usuarios"
    _rec_name = "nombre"
    _description = "usuarios"

    dni = fields.Char(string="DNI", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True)
    imagen = fields.Image()
    telefono = fields.Integer(string="Número de telefono", size=9, required=True)
    email = fields.Char(string="Correo", required=True)
    portatiles = fields.One2many("portatiles", "vendedor", string="Portátiles del usuario")
    ventas = fields.One2many("transacciones", "vendedor", string="Ventas")
    vendedor = fields.Boolean(string="Vendedor", compute='_vendedor')
    compras = fields.One2many("transacciones", "comprador", string="Compras")

    @api.depends('portatiles')
    def _vendedor(self):
        for record in self:
            if len(record.portatiles) > 0:
                record.vendedor = True
            else:
                record.vendedor = False

    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            try:
                if len(self.dni) != 9:
                    raise ValueError("El DNI debe tener 9 caracteres")
            except:
                return {
                    'warning': {
                        'title': "Error",
                        'message': "El DNI debe tener 9 caracteres",
                    }
                }
            try:
                if self.dni[8].isalpha() == False:
                    raise ValueError("El último caracter del DNI debe ser una letra")
            except:
                return {
                    'warning': {
                        'title': "Error",
                        'message': "El último caracter del DNI debe ser una letra",
                    }
                }

    @api.onchange('email')
    def _onchange_email(self):
        try:
            if self.email:
                if '@' not in self.email:
                    raise ValueError("El email debe tener un @")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El email debe tener un @",
                }
            }