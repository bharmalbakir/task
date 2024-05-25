from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    category_id = fields.Many2one('product.category', string='Category')
    brand_id = fields.Many2one('custom_module.brand', string='Brand')
    model_id = fields.Many2one('custom_module.model', string='Model')
    price_group_id = fields.Many2one('custom_module.price_group', string='Price Group')

    @api.onchange('category_id')
    def _onchange_category_id(self):
        return {'domain': {'brand_id': [('category_id', '=', self.category_id.id)]}}

    @api.onchange('brand_id')
    def _onchange_brand_id(self):
        return {'domain': {'model_id': [('brand_id', '=', self.brand_id.id)]}}

    @api.onchange('price_group_id')
    def _onchange_price_group_id(self):
        return {'domain': {'product_id': [('category_id', '=', self.category_id.id),
                                          ('brand_id', '=', self.brand_id.id),
                                          ('model_id', '=', self.model_id.id),
                                          ('price_group_id', '=', self.price_group_id.id)]}}
