BEGIN;
--
-- Create model Item
--
CREATE TABLE "biddingapp_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL, "description" text NOT NULL);
--
-- Create model Vendor
--
CREATE TABLE "biddingapp_vendor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL);
--
-- Create model VendorsBid
--
CREATE TABLE "biddingapp_vendorsbid" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bid_amount" integer NOT NULL, "item_id" bigint NOT NULL REFERENCES "biddingapp_item" ("id") DEFERRABLE INITIALLY DEFERRED, "vendor_id" bigint NOT NULL REFERENCES "biddingapp_vendor" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "biddingapp_vendorsbid_item_id_9ecd4d79" ON "biddingapp_vendorsbid" ("item_id");
CREATE INDEX "biddingapp_vendorsbid_vendor_id_32ba360b" ON "biddingapp_vendorsbid" ("vendor_id");
COMMIT;
