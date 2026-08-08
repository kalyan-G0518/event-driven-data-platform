# Event-Driven E-Commerce Data Platform

An end-to-end event-driven data engineering platform built with **Apache Kafka, Apache Spark, PySpark, and Parquet** to process e-commerce events and transform them into analytics-ready business datasets.

The platform follows a layered data architecture with **Bronze, Silver, Master, and Gold** layers. Raw events are ingested through Kafka, processed using Spark, enriched with customer and product master data, and transformed into business-oriented analytical datasets.

---

## Architecture

```text
                         ┌─────────────────────────┐
                         │    E-Commerce Events     │
                         │                          │
                         │ login                    │
                         │ search                   │
                         │ product_view             │
                         │ add_to_cart              │
                         │ purchase                 │
                         │ payment                  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │         Apache Kafka     │
                         │       Event Streaming    │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │      Spark Streaming     │
                         │      Event Processing    │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │        BRONZE LAYER      │
                         │                         │
                         │      Raw Event Data     │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │        SILVER LAYER      │
                         │                         │
                         │ • Cleaning              │
                         │ • Validation            │
                         │ • Standardization       │
                         │ • Deduplication         │
                         │ • Type Conversion       │
                         └────────────┬────────────┘
                                      │
                       ┌──────────────┴──────────────┐
                       │                             │
                       ▼                             ▼
              ┌─────────────────┐          ┌─────────────────┐
              │  PRODUCT MASTER │          │ CUSTOMER MASTER │
              │                 │          │                 │
              │ Product details │          │ Customer details│
              │ Inventory       │          │ Membership      │
              │ Pricing         │          │ Location        │
              │ Supplier        │          │ Demographics    │
              └────────┬────────┘          └────────┬────────┘
                       │                             │
                       └──────────────┬──────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │         GOLD LAYER       │
                         │     Business Analytics   │
                         └────────────┬────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │             │             │             │             │
          ▼             ▼             ▼             ▼             ▼
    ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
    │ Executive │ │   Sales   │ │  Product  │ │ Customer  │ │ Inventory │
    │  Summary  │ │  Summary  │ │Performance│ │  Metrics  │ │ Analytics │
    └───────────┘ └───────────┘ └───────────┘ └───────────┘ └───────────┘
                                      │
                         ┌────────────┼────────────┐
                         │            │            │
                         ▼            ▼            ▼
                  ┌────────────┐ ┌──────────┐ ┌──────────┐
                  │  Category  │ │Geography │ │  Funnel  │
                  │ Analytics  │ │ Analytics│ │Analytics │
                  └────────────┘ └──────────┘ └──────────┘
