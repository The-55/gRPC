## Objectives

* Understand the role of **Service-Oriented Architecture (SOA)** in distributed systems.
* Learn how to design and implement **gRPC services** in different programming languages.
* Implement **two backend servers** and a **client** with **round-robin load balancing**.
* Analyze and visualize the system using UML diagrams.
* Interpret the output to understand how load balancing distributes requests.


## Background

In **SOA**, services expose well-defined contracts and can be replicated for scalability and fault tolerance.
**gRPC** is a modern RPC framework based on **Protocol Buffers**. It offers:
* Strongly typed contracts.
* Multi-language support.
* High performance with HTTP/2 and binary serialization.

When multiple service instances run, requests need to be distributed across them. This is achieved with **load balancing**.
* **Client-side load balancing**: client decides which server to call.
* **Server-side load balancing**: a proxy/load balancer distributes requests.

## Process steps : 
For this lab, we're going to use Python as programming framework
- Step 1: Define the Service Contract
- Step 2: Generate gRPC Code
- Step 3: Implementing Two Servers
- Step 4: Implementing the Client with Round-Robin Load Balancing
- Step 5: Showing the Expected Output
- Step 6: UML Diagrams

Some important explanations and principles to know : 

