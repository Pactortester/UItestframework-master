# coding=utf-8

import time

from public.common import mytest
from public.pages import qdsIndexPage

from public.common.publicfunction import get_img


class bmkstest(mytest.MyTest):
    """保姆注册测试集"""

    def test_bmks(self):

        """保姆快速注册"""

        qds = qdsIndexPage.DDSIndexPage(self.dr)
        qds.into_qds_page()
        time.sleep(1)
        qds.cookies()

        """新版首页"""
        self.dr.click("css->body > div.section-banner > div.public-navbar > div > ul > li:nth-child(1) > a")

        time.sleep(1)
        self.assertIn("商标注册-权大师", qds.return_title())
        print(qds.return_title())
        # 保姆快速注册
        self.dr.click(
            "css->body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li.list.active")

        for a in self.dr.get_elements("css->#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.dr.click(
            "css->body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow")

        qds.order_info()

        get_img(self.dr, "test_bmks.png")

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
