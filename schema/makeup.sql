-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

-- Table documentation comment 1 (try the PDF/RTF export)
-- Table documentation comment 2
CREATE TABLE "Product" (
    "id" int   NOT NULL,
    -- Field documentation comment 1
    -- Field documentation comment 2
    -- Field documentation comment 3
    "Name" varchar(200)   NOT NULL,
    "Price" money   NOT NULL,
    "Brand" text   NOT NULL,
    "product_type" text   NOT NULL,
    "product_category" text   NOT NULL,
    "product_id" text   NOT NULL,
    CONSTRAINT "pk_Product" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_Product_Name" UNIQUE (
        "Name"
    )
);

CREATE TABLE "Brand" (
    "id" int   NOT NULL,
    "name" text   NOT NULL,
    CONSTRAINT "pk_Brand" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Product_Type" (
    "id" int   NOT NULL,
    "name" text   NOT NULL,
    CONSTRAINT "pk_Product_Type" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Product_Category" (
    "id" int   NOT NULL,
    "name" text   NOT NULL,
    CONSTRAINT "pk_Product_Category" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "User" (
    "id" int   NOT NULL,
    "email" string   NOT NULL,
    "password" string   NOT NULL,
    "collection" string   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Collection" (
    "id" int   NOT NULL,
    "user_id" int   NOT NULL,
    "product_id" int   NOT NULL,
    CONSTRAINT "pk_Collection" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_Brand" FOREIGN KEY("Brand")
REFERENCES "Brand" ("id");

ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_product_type" FOREIGN KEY("product_type")
REFERENCES "Product_Type" ("id");

ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_product_category" FOREIGN KEY("product_category")
REFERENCES "Product_Category" ("id");

ALTER TABLE "Collection" ADD CONSTRAINT "fk_Collection_user_id" FOREIGN KEY("user_id")
REFERENCES "User" ("id");

ALTER TABLE "Collection" ADD CONSTRAINT "fk_Collection_product_id" FOREIGN KEY("product_id")
REFERENCES "Product" ("id");

