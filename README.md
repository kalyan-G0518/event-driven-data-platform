# Event-Driven Data Platform

An end-to-end event-driven data engineering platform built with **Apache Kafka, PySpark, and Parquet**, designed to ingest e-commerce events, process and standardize them through multiple data layers, enrich them with master data, and produce business-ready analytics datasets.

The project follows a **Bronze → Silver → Master → Gold** architecture and demonstrates concepts such as:

- Event-driven ingestion
- Kafka-based streaming
- Apache Spark / PySpark processing
- Data standardization and cleansing
- Master data management
- Data enrichment and joins
- Business analytics
- Layered data architecture
- Parquet-based storage
- Modular pipeline orchestration

---

## Architecture

```text
                         ┌──────────────────────┐
                         │    Event Sources     │
                         │                      │
                         │ Product / User /     │
                         │ Purchase Events      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │        Kafka         │
                         │                      │
                         │ Event Streaming      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │          BRONZE              │
                    │                              │
                    │ Raw event ingestion          │
                    │ Minimal transformation       │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │           SILVER             │
                    │                              │
                    │ Cleaning                     │
                    │ Standardization              │
                    │ Type conversion              │
                    │ Data validation              │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │  PRODUCT MASTER  │          │ CUSTOMER MASTER  │
          │                  │          │                  │
          │ Product details  │          │ Customer details │
          │ Inventory        │          │ Membership       │
          │ Pricing          │          │ Location         │
          │ Supplier data    │          │ Customer profile │
          └────────┬─────────┘          └────────┬─────────┘
                   │                             │
                   └──────────────┬──────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │            GOLD              │
                    │                              │
                    │ Business-ready analytics     │
                    └──────────────┬───────────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
      Executive Summary     Product Performance    Customer Metrics
             │                     │                     │
             ▼                     ▼                     ▼
      Sales Summary         Inventory Analytics    Geography Analytics
             │                     │                     │
             └──────────────┬──────┴─────────────────────┘
                            │
                            ▼
                  Category & Funnel Analytics
