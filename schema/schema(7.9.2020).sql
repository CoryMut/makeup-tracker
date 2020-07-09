-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

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
    "name" text   NOT NULL,
    "price" text   NOT NULL,
    "brand_id" int   NOT NULL,
    "product_type_id" int   NOT NULL,
    "product_category_id" int   NOT NULL,
    "external_product_id" text   NOT NULL,
    "search_terms" text   NOT NULL,
    CONSTRAINT "pk_Product" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_Product_name" UNIQUE (
        "name"
    )
);

CREATE TABLE "Brand" (
    "id" int   NOT NULL,
    "name" text   NOT NULL,
    CONSTRAINT "pk_Brand" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Type" (
    "id" int   NOT NULL,
    "name" text   NOT NULL,
    CONSTRAINT "pk_Type" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Category" (
    "id" int   NOT NULL,
    "name" text   NOT NULL,
    CONSTRAINT "pk_Category" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "User" (
    "id" int   NOT NULL,
    "email" string   NOT NULL,
    "password" string   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_User_email" UNIQUE (
        "email"
    )
);

CREATE TABLE "Users_Products" (
    "id" int   NOT NULL,
    "user_id" int   NOT NULL,
    "product_id" int   NOT NULL,
    CONSTRAINT "pk_Users_Products" PRIMARY KEY (
        "user_id","product_id"
     )
);

ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_brand_id" FOREIGN KEY("brand_id")
REFERENCES "Brand" ("id");

ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_product_type_id" FOREIGN KEY("product_type_id")
REFERENCES "Type" ("id");

ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_product_category_id" FOREIGN KEY("product_category_id")
REFERENCES "Category" ("id");

ALTER TABLE "Users_Products" ADD CONSTRAINT "fk_Users_Products_user_id" FOREIGN KEY("user_id")
REFERENCES "User" ("id");

ALTER TABLE "Users_Products" ADD CONSTRAINT "fk_Users_Products_product_id" FOREIGN KEY("product_id")
REFERENCES "Product" ("id");

