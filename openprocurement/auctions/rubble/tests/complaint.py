# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.complaint import (
    AuctionComplaintResourceTestMixin,
    InsiderAuctionComplaintDocumentResourceTestMixin
)
from openprocurement.auctions.core.tests.blanks.complaint_blanks import (
    # AuctionLotAwardComplaintResourceTest
    create_auction_complaint_lot
)
from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.rubble.tests.base import (
    BaseAuctionWebTest, test_auction_data, test_lots,
    test_financial_auction_data, test_financial_organization
)


@unittest.skip("option not available")
class AuctionComplaintResourceTest(BaseAuctionWebTest, AuctionComplaintResourceTestMixin):
    pass



@unittest.skip("option not available")
class AuctionLotAwardComplaintResourceTest(BaseAuctionWebTest):
    initial_lots = test_lots

    test_create_auction_complaint_lot = snitch(create_auction_complaint_lot)

@unittest.skip("option not available")
class AuctionComplaintDocumentResourceTest(BaseAuctionWebTest, InsiderAuctionComplaintDocumentResourceTestMixin):

    def setUp(self):
        super(AuctionComplaintDocumentResourceTest, self).setUp()
        # Create complaint
        response = self.app.post_json('/auctions/{}/complaints'.format(
            self.auction_id), {'data': {'title': 'complaint title', 'description': 'complaint description', 'author': self.initial_organization}})
        complaint = response.json['data']
        self.complaint_id = complaint['id']
        self.complaint_owner_token = response.json['access']['token']

@unittest.skip("option not available")
class FinancialAuctionComplaintResourceTest(BaseAuctionWebTest):
    initial_data = test_financial_auction_data
    initial_organization = test_financial_organization

@unittest.skip("option not available")
class FinancialAuctionLotAwardComplaint(BaseAuctionWebTest):
    initial_data = test_financial_auction_data
    initial_organization = test_financial_organization

@unittest.skip("option not available")
class FinancialAuctionComplaintDocumentResourceTest(BaseAuctionWebTest):
    initial_data = test_financial_auction_data
    initial_organization = test_financial_organization


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AuctionComplaintDocumentResourceTest))
    suite.addTest(unittest.makeSuite(AuctionComplaintResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
