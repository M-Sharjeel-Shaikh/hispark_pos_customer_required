odoo.define('hispark_pos_customer_required.pos', function (require) {
    "use strict";

    var PaymentScreen = require('point_of_sale.PaymentScreen');
    var core = require('web.core');
    var _t = core._t;
    const Registries = require('point_of_sale.Registries');

    const PaymentScreenWidget = (PaymentScreen) => class PaymentScreenWidget extends PaymentScreen {
        async validateOrder(isForceValidate) {
            if(this.env.pos.config.require_customer && !this.env.pos.get_order().get_partner()){
                this.showPopup('ErrorPopup', {
                    title: _t('An anonymous order cannot be confirmed'),
                    body:  _t('Please select a customer for this order.'),
                });
                return;
            }
            return super.validateOrder(...arguments);
        }
    };
    Registries.Component.extend(PaymentScreen, PaymentScreenWidget);
});
