from odoo import models, fields ,api


class Brand(models.Model):
    _inherit = 'product.template'

    brand_name = fields.Char(string='Brand Name', required=True)
    group_name = fields.Char(string='Group Name', required=True)
    category_id = fields.Many2one('product.template', string="Category")
    brand_id = fields.Many2one('product.template', string='Brand', required=True)
    category_name = fields.Many2one('product.template', string='Category Name', required=True)

    group = fields.Char(string='Price Group Name', required=True)
    price_from = fields.Float(string='From', required=True)
    price_to = fields.Float(string='To', required=True)
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)

    @api.depends('name', 'price_from', 'price_to')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.price_from} - {record.price_to})"

    @api.depends('brand_id', 'model_id')
    def _compute_price_group(self):
        for record in self:
            # Placeholder for actual logic to compute price group based on brand and model
            record.price_group_id = None

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
