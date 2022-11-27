odoo.define('sale.daily_price', function (require) {
    "use strict";

    const BasicFields = require('web.basic_fields');
    const FieldsRegistry = require('web.field_registry');

    /**
     * The sale.product_discount widget is a simple widget extending FieldFloat
     *
     *
     * !!! WARNING !!!
     *
     * This widget is only designed for sale_order_line creation/updates.
     * !!! It should only be used on a discount field !!!
     */

    const ProductDailyPriceWidget = BasicFields.FieldFloat.extend({

        /**
         * Override changes at a discount.
         *
         * @override
         * @param {OdooEvent} ev
         *
         */
        async reset(record, ev) {
            console.log('if (ev && ev.data.changes && ev.data.changes.discount >= 0)',(ev && ev.data.changes && ev.data.changes.discount >= 0))
            console.log('(ev && ev.data.changes && ev.data.changes.daily_price >= 0 )',(ev && ev.data.changes && ev.data.changes.daily_price >= 0 ))
            if (ev && ev.data.changes && ev.data.changes.discount >= 0) {
               this.trigger_up('open_discount_wizard');
            }
            if (ev && ev.data.changes && ev.data.changes.daily_price >= 0 ) {
               this.trigger_up('open_daily_price_wizard');

            }
            this._super(...arguments);
        },
    });

    FieldsRegistry.add('product_discount', ProductDailyPriceWidget);

    return ProductDailyPriceWidget;

});


odoo.define('sale.SaleOrderDailyPriceView', function (require) {
    "use strict";

    const FormController = require('web.FormController');
    const FormView = require('web.FormView');
    const viewRegistry = require('web.view_registry');
    const Dialog = require('web.Dialog');
    const core = require('web.core');
    const _t = core._t;
    console.log('kkkkkkkkkkkkkkkkkkkk dailuy')

    const SaleOrderFormController = FormController.extend({
        custom_events: _.extend({}, FormController.prototype.custom_events, {
            open_daily_price_wizard: '_onOpenDailyPriceWizard',
            open_discount_wizard: '_onOpenDiscountWizard',
        }),

        // -------------------------------------------------------------------------
        // Handlers
        // -------------------------------------------------------------------------

        /**
         * Handler called if user changes the discount field in the sale order line.
         * The wizard will open only if
         *  (1) Sale order line is 3 or more
         *  (2) First sale order line is changed to discount
         *  (3) Discount is the same in all sale order line
         */
         _onOpenDiscountWizard(ev) {
            const orderLines = this.renderer.state.data.order_line.data.filter(line => !line.data.display_type);
            const recordData = ev.target.recordData;
            const isEqualDiscount = orderLines.slice(1).every(line => line.data.discount === recordData.discount);
             // && isEqualDiscount
            if (orderLines.length >= 3 && recordData.sequence === orderLines[0].data.sequence) {
                Dialog.confirm(this, _t("Do you want to apply this discount to all order lines?"), {
                    confirm_callback: () => {
                        orderLines.slice(1).forEach((line) => {
                            this.trigger_up('field_changed', {
                                dataPointID: this.renderer.state.id,
                                changes: {order_line: {operation: "UPDATE", id: line.id, data: {discount: orderLines[0].data.discount}}},
                            });
                        });
                    },
                });
            }
        },
        _onOpenDailyPriceWizard(ev) {
            const orderLines = this.renderer.state.data.order_line.data.filter(line => !line.data.display_type);
            const recordData = ev.target.recordData;
            const isEqualDiscount = orderLines.slice(1).every(line => line.data.discount === recordData.discount);
             // && isEqualDiscount
            if (orderLines.length >= 3 && recordData.sequence === orderLines[0].data.sequence) {
                Dialog.confirm(this, _t("Do you want to apply this daily price to all order lines?"), {
                    confirm_callback: () => {
                        orderLines.slice(1).forEach((line) => {
                            this.trigger_up('field_changed', {
                                dataPointID: this.renderer.state.id,
                                changes: {order_line: {operation: "UPDATE", id: line.id, data: {daily_price: orderLines[0].data.daily_price}}},
                            });
                        });
                    },
                });
            }
        },
    });

    const SaleOrderDailyPriceView = FormView.extend({
        config: _.extend({}, FormView.prototype.config, {
            Controller: SaleOrderFormController,
        }),
    });

    viewRegistry.add('sale_discount_form', SaleOrderDailyPriceView);

    return SaleOrderDailyPriceView;

});
