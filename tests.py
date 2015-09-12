import os
import papi
import app
from models import Result, Listing, Product, Image, User, Catalog


class testPapi(object):
    """Test the Papi class."""

    def __init__(self):
        pass

class testDatabase(object):
    """Test database relationships and calls."""

    def __init__(self):
        self.run()

    def run(self):
        pass

    def listing(self):
        pass

    def product(self):
        pass

    def image(self):
        pass

    def user(self):
        pass

    def catalog(self):
        pass

    def catalog_relationships(self):
        with app.app_context():
            session = db.session()
            db.metadata.create_all(db.engine)
            item = Catalog.query.filter_by(upc='811636026407').first()
            product = item.product
            listings = item.listings
            image = item.image


    def product_relationships(self):
        with app.app_context():
            session = db.session()
            db.metadata.create_all(db.engine)
            upc = '811636026407'
            product = Product.query.filter_by(upc=upc).first()
            listings = product.listings
            for listing in listings:
                if listing.upc == upc:
                    print("{0} passed".format(listing))
                else:
                    #TODO: raise exception
            image = product.image

    def listing_relationships(self):
        pass

    def image_relationships(self):
        pass


class testError(object):
    pass

upcs = [
    '811636026407', '811636024281', 
    '011670112474', '811636024274',
    '811636024281', '811636024304', 
    '811636020528', '811636022799'
]

asins = [
    'B00BY5RWRY', 'B00HEATXLG', 
    'B00HEAUAE0', 'B00KHUJUA4',
    'B00KUP84L2', 'B00LAGMOGG',
    'B00M2AH2LG', 'B00M2AL91U'
]

test_response = [{'Identifiers': {'MarketplaceASIN': {'ASIN': {'value': 'B000A4TDPO'}, 'MarketplaceId': {'value': 'ATVPDKIKX0DER'}}}, 'LowestOfferListings': {'LowestOfferListing': [{'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '25.14'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '25.14'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '2'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Amazon'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '439193'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '25.99'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '25.99'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '2'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '95-97%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '93518'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '30.25'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '30.25'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'Unknown'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '66460'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '32.92'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '24.58'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '8.34'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '95-97%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'Unknown'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '8-13 days'}}}, 'SellerFeedbackCount': {'value': '199306'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '35.87'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '26.72'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '9.15'}}}, 'NumberOfOfferListingsConsidered': {'value': '2'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '506'}}]}}, {'Identifiers': {'MarketplaceASIN': {'ASIN': {'value': 'B000BNM25W'}, 'MarketplaceId': {'value': 'ATVPDKIKX0DER'}}}, 'LowestOfferListings': {'LowestOfferListing': [{'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '15.51'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '15.51'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Amazon'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '136614'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '18.84'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '18.84'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'Unknown'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '66438'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '20.94'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '15.95'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '4.99'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '90-94%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '9720'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '21.04'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '12.95'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '8.09'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '95-97%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'Unknown'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '8-13 days'}}}, 'SellerFeedbackCount': {'value': '199305'}}, {'MultipleOffersAtLowestPrice': {'value': 'True'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '21.06'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '10.07'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '10.99'}}}, 'NumberOfOfferListingsConsidered': {'value': '2'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '493'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '28.62'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '24.00'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '4.62'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '3-7 days'}}}, 'SellerFeedbackCount': {'value': '147'}}]}}, {'Identifiers': {'MarketplaceASIN': {'ASIN': {'value': 'B000BNM27U'}, 'MarketplaceId': {'value': 'ATVPDKIKX0DER'}}}, 'LowestOfferListings': {'LowestOfferListing': [{'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '24.99'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '24.99'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '2'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '95-97%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '93518'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '26.96'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '26.96'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '0.00'}}}, 'NumberOfOfferListingsConsidered': {'value': '2'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Amazon'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '167117'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '30.36'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '22.27'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '8.09'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '95-97%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'Unknown'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '8-13 days'}}}, 'SellerFeedbackCount': {'value': '199305'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '34.18'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '23.19'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '10.99'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '0-2 days'}}}, 'SellerFeedbackCount': {'value': '493'}}, {'MultipleOffersAtLowestPrice': {'value': 'False'}, 'Price': {'LandedPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '44.57'}}, 'ListingPrice': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '39.00'}}, 'Shipping': {'CurrencyCode': {'value': 'USD'}, 'Amount': {'value': '5.57'}}}, 'NumberOfOfferListingsConsidered': {'value': '1'}, 'Qualifiers': {'SellerPositiveFeedbackRating': {'value': '98-100%'}, 'ItemSubcondition': {'value': 'New'}, 'FulfillmentChannel': {'value': 'Merchant'}, 'ShipsDomestically': {'value': 'True'}, 'ItemCondition': {'value': 'New'}, 'ShippingTime': {'Max': {'value': '3-7 days'}}}, 'SellerFeedbackCount': {'value': '147'}}]}}]


