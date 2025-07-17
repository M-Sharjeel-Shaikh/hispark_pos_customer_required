from odoo import fields, models, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    require_customer = fields.Boolean('Required Customer')


class PosConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"

    res_require_customer = fields.Boolean(string='Required Customer', related='pos_config_id.require_customer', readonly=False)

    @api.constrains('res_require_customer')
    def save_res_require_customer(self):
        pos_config = self.env['pos.config'].search([])
        for pos_list in pos_config:
            pos_list.write({'require_customer': self.res_require_customer})
