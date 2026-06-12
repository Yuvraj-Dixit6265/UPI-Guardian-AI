# ADR-001

## Title

Use FastAPI as the Banking API Framework

## Status

Accepted

## Context

UPI Guardian requires a lightweight, modern, high-performance API framework capable of supporting banking simulation workloads and future AI integrations.

## Alternatives Considered

* Flask
* Django
* FastAPI

## Decision

FastAPI will be used.

## Reasons

* High Performance
* Automatic OpenAPI Documentation
* Easy Dockerization
* Strong Python Ecosystem
* Async Support
* Suitable for Microservices

## Consequences

Positive:

* Fast development
* Excellent API documentation
* Easy integration with AI components

Negative:

* Team must understand async concepts
