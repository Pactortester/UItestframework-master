# coding=utf-8

import time

from public.common import mytest
from public.pages import qdsIndexPage

from public.common.publicfunction import get_img


class bmkstest(mytest.MyTest):
    """担保无忧测试集"""

    def test_bmks(self):

        """担保无忧注册"""

        qds = qdsIndexPage.DDSIndexPage(self.dr)
        qds.into_qds_page()
        time.sleep(1)
        qds.cookies()

        """新版首页"""
        self.dr.click("css->body > div.section-banner > div.public-navbar > div > ul > li:nth-child(1) > a")

        time.sleep(1)
        self.assertIn("商标注册-权大师", qds.return_title())
        print(qds.return_title())
        # 担保无忧注册
        self.dr.click(
            "css->body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(2)")

        for a in self.dr.get_elements("css->#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.dr.click(
            "css->body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow")

        qds.order_info()

        get_img(self.dr, "test_dbwy.png")

        qds.pay_check()


