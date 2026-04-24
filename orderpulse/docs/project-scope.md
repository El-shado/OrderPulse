# OrderPulse - Project Scope

## Project Title
OrderPulse: Event-Driven Order & Delivery Tracking Platform on AWS

## Project Summary
OrderPulse is a portfolio-grade B2B cloud project designed to demonstrate how production-minded platform can improve order visibility, delivery tracking, customer communication, and operational awareness on AWS.

The project is intentionally scoped to remain focused, explainable, while still demonstrating strong engineering judgment, serverless architecture thinking, event-driven design, and operational maturity.

## Project Goal
The goal of this project is to build a real cloud solution that demonstrates the ability to:

- design clear APIs
- implement structured business logic
- build on AWS using a serverless approach
- use event-driven flows in a meaningful way
- handle reliability concerns such as idempotency, retries, and DLQ behavior
- explain architectural decisions professionally 

## Business Problem
Many B2B companies struggle with poor visibility into order and delivery lifecycle events. Customers often ask for status updates, support teams spend time on manual follow-up, delivery updates may arrive late or be duplicated, and communication quality is often inconsistent.

OrderPulse addresses this problem by providing a focused platform for order creation, delivery status updates, customer notifications, post-delivery feedback, and operational visibility.

## Intended Users
- Customer
- Ops User
- Support Agent
- Delivery Partner / External System

## Core APIs
The project will implement only the following core APIs:

- `POST /orders`
- `POST /deliveries/update`
- `GET /orders/{id}`
- `POST /feedback`

## Core Events
The project will use only the following core domain events:

- `order.created`
- `delivery.updated`
- `feedback.received`

## Core Capabilities
The project will focus only on the following capabilities:

- create a new order
- update delivery status
- retrieve order status
- capture post-delivery feedback
- publish meaningful domain events
- process notification workflows asynchronously
- record logs, metrics, and alarms
- demonstrate idempotency for repeated delivery updates
- provide a simple operational view of system behavior

## Architecture Direction
The project will follow a smart 3-tier serverless architecture:

### Tier 1 - Edge / Experience Layer
- Amazon API Gateway
- lightweight dashboard or minimal frontend
- basic authentication
- input validation

### Tier 2 - Application / Domain Layer
- AWS Lambda
- thin handlers
- use cases
- domain services
- business validation
- event publishing

### Tier 3 - Data / Async / Operability Layer
- Amazon DynamoDB
- Amazon EventBridge
- Amazon SQS
- Dead Letter Queue
- Amazon CloudWatch
- audit trail and idempotency support

## In Scope
The following items are included in the project scope:

- repository structure
- API contract design
- request and response schemas
- domain use cases
- DynamoDB data model
- EventBridge event publishing
- SQS-based notification processing
- DLQ configuration
- CloudWatch logs, metrics, and alarms
- IAM role planning
- Terraform-based infrastructure definition
- architecture diagrams
- validation checks
- troubleshooting notes
- portfolio-ready documentation

## Out of Scope
The following items are intentionally excluded from the project scope:

- full e-commerce storefront
- payment processing
- inventory management
- advanced user management
- enterprise-grade RBAC
- multi-region deployment
- complex analytics platform
- machine learning workflows
- advanced frontend design system
- mobile application
- large-scale reporting module
- full CI/CD platform automation
- complete production security hardening beyond portfolio scope
- dozens of event types
- microservice sprawl
- overengineered workflow orchestration

## Success Criteria
The project will be considered successful if it demonstrates all of the following:

- the core APIs work correctly
- orders can be created and retrieved
- delivery updates can be processed and published as events
- notification processing is asynchronous
- repeated delivery updates are handled safely
- operational signals are visible through logs and metrics
- failure handling includes retries and DLQ behavior
- the architecture is understandable and defensible

## Why This Scope Is Intentionally Narrow
This scope is intentionally narrow because the goal is not to build a large product. The goal is to build a focused, well-structured, production-minded system that demonstrates architectural reasoning, AWS fluency, and engineering ownership without losing clarity or quality.
