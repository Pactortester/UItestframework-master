#coding=utf-8

from public.common import basepage
from public.common import mytest
import time

class DDSIndexPage(basepage.Page):

    def into_qds_page(self):
        """打ads首页"""
        self.dr.open('https://new.quandashi.com/')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

    def cookies(self):
        """登录"""
        self.dr.add_cookie({'name': 'QDS_COOKIE',
             'value': '4cee3ae144733628cc3ce396a7713a2cfe720901',
              'Domain': '.quandashi.com'})

    def order_info(self):
        """订单信息"""
        self.dr.clear_type("name->ownerContactPerson","全大师")
        self.dr.clear_type("css->body > div.myOrder-wrap > div.section-myorder.width1200 > div > table:nth-child(2) > tbody > tr:nth-child(2) > td.td-2 > input", "15624992498")
        self.dr.clear_type("css->body > div.myOrder-wrap > div.section-myorder.width1200 > div > table:nth-child(2) > tbody > tr:nth-child(3) > td.td-2 > input","4564564@qq.com")
        self.dr.clear_type("css->#remark","test")

    def pay_check(self):
        """支付检验"""
        for i in self.dr.get_elements(
                "css->body > div.myOrder-wrap > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text
        self.assertIn(aa, ii)
        print("价格一致")
        self.dr.click(
            "css->body > div.myOrder-wrap > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder")
        time.sleep(2)
        for o in self.dr.get_elements("class->payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text
        time.sleep(2)
        self.assertIn(oo, ii)
        print("测试通过")
        self.dr.click("id->alisubmit")

