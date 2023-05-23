<template>
    <div class="site-content">
        <ElDialog v-model="showPay" width="700px">
            <div class="text">
                <span>由于缺乏营业执照未能通过支付宝、微信的核验,只能采取扫码付款留下备注的方式开通VIP</span>
            </div>
            <div class="note">
                <span>注意,付款时请备注您的账号</span>
            </div>
            <div class="image">
                <img v-if="radio1=='1'" src="../../../assets/wx.jpg"/>
                <img v-else src="../../../assets/zfb.jpg"/>
            </div>
        </ElDialog>
        <div class="payWay">
            <p>支付方式</p>
            <el-radio-group v-model="radio1">
                <el-radio label="1" size="large" border>微信支付</el-radio>
                <el-radio label="2" size="large" border>支付宝支付</el-radio>
            </el-radio-group>
        </div>
        <section class="sec-spacer sec-color">
            
            <div class="container">
                <div class="spacer3"></div>
                <div class="pricing-style1">
                    <div class="Rectangle">
                        <div class="pricing-plan">
                            <div class="pricing-head">
                                <div class="name">
                                    包月VIP
                                </div>
                                <div class="price">
                                    <span class="value">
                                        ￥9
                                    </span>
                                    <span class="duration">
                                        per month
                                    </span>
                                </div>
                            </div>
                            <div class="pricing-body">
                                <ul>
                                    <li>
                                        <i class="fa fa-check"></i> 可以阅读VIP书籍
                                    </li>
                                    
                                </ul>
                            </div>
                            <div class="pricing-footer button1">
                                <a href="#" class="p-button" @click="showPay=true">购买</a>
                            </div>
                        </div>
                    </div>

                    <div class="Rectangle">
                        <div class="pricing-plan">
                            <div class="pricing-head">
                                <div class="name">
                                    季度VIP
                                </div>
                                <div class="price">
                                    <span class="value">
                                        ￥30
                                    </span>
                                    <span class="duration">
                                        per quarter
                                    </span>
                                </div>
                            </div>
                            <div class="pricing-body">
                                <ul>
                                    <li>
                                        <i class="fa fa-check"></i> 可以阅读VIP书籍
                                    </li>
                                    <li>
                                        <i class="fa fa-check"></i> 价格更加实惠
                                    </li>
                                    
                                </ul>
                            </div>
                            <div class="pricing-footer">
                                <a href="#" class="p-button button2" @click="showPay = true">购买</a>
                            </div>
                        </div>
                    </div>
                    <div class="Rectangle">
                        <div class="pricing-plan">
                            <div class="pricing-head">
                                <div class="name">
                                    年度VIP
                                </div>
                                <div class="price">
                                    <span class="value">
                                        ￥99
                                    </span>
                                    <span class="duration">
                                        per year
                                    </span>
                                </div>
                            </div>
                            <div class="pricing-body">
                                <ul>
                                    <li>
                                        <i class="fa fa-check"></i> 可以免费阅读VIP书籍
                                    </li>
                                    <li>
                                        <i class="fa fa-remove"></i> 价格超级实惠
                                    </li>
                                    <li>
                                        <i class="fa fa-remove"></i> 可以vx管理员提出诉求
                                    </li>
                                </ul>
                            </div>
                            <div class="pricing-footer button3">
                                <a href="#" class="p-button" @click="showPay = true">购买</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>

// import axios from 'axios';
import { ElDialog } from 'element-plus';
import { ref } from 'vue';
//import { ElDialog } from 'element-plus';
export default {
    name: "PricingTable",
    setup() {
        const radio1=ref('1')
        const showPay=ref(false)
        return {
            radio1,
            showPay,
           
        };
    },
    components: { ElDialog }
}; 

</script>

<style scoped>
  @keyframes animate {
  0% {
    filter: hue-rotate(0deg);
  }
  100% {
    filter: hue-rotate(360deg);
  }
}

 p {
    font-size: 24px;
    background-image: linear-gradient(45deg, #f7d157, #ffcc71, #e8a63a, #f7d157);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    margin-bottom: 20px;
    animation: animate 5s ease infinite;
  }

.text{
    color: gray;
    margin-left: 40px;
    text-decoration: line-through;
    margin-bottom:10px
}
.note{
    color: #ed4242;
    font-weight: bold;
    font-size: 20px;
}
.image {
    margin-left: 200px;
}
/* @import url('https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css'); */
body {
    background-color: #fff;
    font-family: 'Poppins', sans-serif;
    line-height: 24px;
    font-size: 16px;
    color: lightblue;
}
main > section {
    padding: 70px 0;
}
.payWay{
    font-size: 25px;
}
.button1{
    margin-top: 81px;
}
.button2{
    margin-top: 53px;
}
.button3{
    margin-top: 23px;
}
.sec-color {
    background-color: white;
}
.sec-spacer {
    padding: 50px 0;
    
}
.spacer3 {
    height: 30px;
}
.pricing-style1{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.Rectangle{
    display: inline-block;
    width: 280px;
    margin-right: 0px;
}
.name{
    margin-left: 15px;
}
.pricing-style1 .pricing-plan {position: relative;text-align: center;padding: 25px;margin-bottom: 35px;background-color: #f5f5f5;border-radius: 4px;}
.sec-color .pricing-style1 .pricing-plan {background-color: lightcyan;height: 400px;}
.pricing-style1 .pricing-plan .badge {position: absolute;top: 16px;transform: rotate(90deg);right: 0px;padding: 5px;background: #fff;color: #337ab7;border-radius: 0;font-size: 11px;}
.pricing-style1 .pricing-head .name {padding-bottom: 25px;font-size: 15px;color: #444;letter-spacing: 1px;}
.pricing-style1 .pricing-plan.featured .pricing-head .name {color: #fff;}
.pricing-style1 .pricing-plan.featured {background-color: #337ab7;}
.pricing-style1 .pricing-head .price {display: inline-block;background-color: #337ab7;color: #fff;padding: 28px 25px;border-radius: 50%;}
.pricing-style1 .pricing-plan.featured .pricing-head .price {background-color: #fff;color: #337ab7;}
.pricing-style1 .pricing-head .price sup {font-size: 16px;line-height: normal;top: 2px;margin-right: 1px;vertical-align: top;font-weight: lighter;}
.pricing-style1 .pricing-head span.value {display: block;font-size: 26px;line-height: normal;font-weight: 600;}
.pricing-style1 .pricing-head span.duration {display: block;font-size: 11px;margin-top: -6px;}
.pricing-style1 .pricing-body {padding-top: 40px;}
.pricing-style1 .pricing-body ul {padding-left: 0;list-style: none;font-size: 12px;color: #666;}
.pricing-style1 .pricing-plan.featured .pricing-body ul {color: #fff;}
.pricing-style1 .pricing-body ul li:nth-child(n+2) {padding-top: 12px;}
.pricing-style1 .pricing-footer {padding-top: 30px;}
.pricing-style1 .pricing-footer .p-button {display: inline-block; padding: 8px 20px;font-size: 13px;min-width: 130px;text-transform: uppercase;background-color: #337ab7;border-radius: 20px;color: #fff;text-decoration: none;-webkit-transition: .3s all ease;transition: .3s all ease;}
.pricing-style1 .pricing-footer .p-button:hover {background-color: #1f5f96;color: rgba(255, 255, 255, 0.8);}
.pricing-style1 .pricing-plan.featured .pricing-footer .p-button {background: #fff;color: #337ab7;-webkit-transition: .3s all ease;transition: .3s all ease;}
.pricing-style1 .pricing-plan.featured .pricing-footer .p-button:hover {background: rgba(255, 255, 255, 0.8);}

/* color stylesheet */
/* link(rel="stylesheet", href="css/colors/blue.css", id="colorSelect") */
</style>
