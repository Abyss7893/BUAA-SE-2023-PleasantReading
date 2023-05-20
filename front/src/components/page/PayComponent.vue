<template>
    <div>
    <!-- 支付弹窗 -->
        <!-- 支付方式选择，按钮显示 -->
        <div class="pay-dialog-body" v-if="payBtn">
            <p>请选择支付方式：</p>
            <el-radio-group v-model="payMethod" size="large">
                <el-radio-button label="微信支付" />
                <el-radio-button label="线下支付" />
            </el-radio-group>
            <div >
                <p>请选择充值挡位</p>
                <ElRadioGroup v-model="money">
                    <el-radio label="充值一个月" size="large" border>￥30(充值一个月)</el-radio>
                    <el-radio label="充值一个季度" size="large" border>￥90(充值一个季度)</el-radio>
                    <el-radio label="充值一整年" size="large" border>￥300(充值一整年)</el-radio>
                    
                </ElRadioGroup>
                <p >
                    选择{{ money }}
                </p>
            </div>
            <div>
                <ElButton @click="handlePayWxQRcode(payInfoRow)" style="margin-left: 260px; margin-top: 20px; ">确认充值</ElButton>
            </div>
        </div>
        <!-- 支付方式选择完成，按钮消失 -->
        <div v-else>
            <div>
                使用 
                <span v-if="payForWx" class="pay-for-method-1">微信</span>
                扫一扫二维码进行支付
            </div>
            <!-- 微信支付二维码 -->
            <div id="qrcodeImg"></div>
            <div>注：若二维码过期失效，请刷新页面重新进入支付！</div>
        </div>

    </div>
</template>

<script>
import QRCode from 'qrcodejs2';
import { ElButton, ElRadioGroup } from 'element-plus';
export default {
    components:{ ElButton, ElRadioGroup },
    data() {
        return {
            modal3: false,    // 是否打开支付弹窗
            payBtn: true,    // 是否显示方式选择按钮
            payInfoRow: {},    // 该条订单数据
            payForWx: false,    // 是否微信支付
            timer: '',    // 定时器
            money:"充值一个月",
            payMethod : '微信支付',
        }
    },
    methods: {
        qrcode(url) {  // 前端根据 URL 生成微信支付二维码
            return new QRCode('qrcodeImg', {
                width: 100,
                height: 100,
                text: url,
                colorDark: '#000',
                colorLight: '#fff'
            });
        },

        handlePayWxQRcode(row) {  // 获取微信支付二维码
            this.$api.order.getWxPayCode({    // 这里根据不同的后端接口去修改
                totalFee: row.totalAmount * 100,
                outTradeNo: row.orderSn,
            }).then(res => {
                this.payBtn = false;
                this.qrcode(res.data.url);    // 例如：res.data.url 的值为 "weixin://wxpay/bizpayurl?pr=......"，根据这个值生成相对应的微信支付二维码
                this.payForWx = true;
                this.timer = setInterval(() => {    // 通过定时器每间隔一会去请求查询微信支付状态（具体参数根据项目需要而定）
                    this.handleQueryWxPayStatus(row, res.data.outTradeNo);
                }, 1000);
            })
        },
        handleQueryWxPayStatus(row, sn) {  // 查询微信支付状态
            this.$api.order.queryWxPayStatus({    // 这里根据不同的后端接口去修改
                totalFee: row.totalAmount * 100,
                outTradeNo: sn,
            }).then(res => {
                if (res.data.paySuccess) {    // 当查询到支付成功时
                    this.$message({
                        type: 'success',
                        message: '支付成功！'
                    });
                    this.closePayDialog();    // 关闭支付弹窗
                    // 这里可以加个刷新订单列表的接口请求函数的调用
                }
            })
        },
    },

}
</script>

<style>
.el-radio {
  width: 200px;
}



#qrcodeImg {
    margin: 10px;
}

.pay-for-method-1 {
    font-weight: bold;
    color: #67c23a;
}

.pay-for-method-2 {
    font-weight: bold;
    color: #409eff;
}</style>