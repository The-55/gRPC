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

**weather_pb2.py** - Contains generated message classes (like CityRequest and TemperatureResponse) that handle data serialization/deserialization between client and server using Protocol Buffers binary format.

**weather_pb2_grpc.py** - Provides gRPC client stubs and server base classes that handle the actual RPC communication, enabling remote method calls between distributed components.

These files were automatically generated from the .proto definition to ensure type-safe communication and eliminate manual boilerplate code for the gRPC service implementation.

- Step 3: Implementing Two Servers
- Step 4: Implementing the Client with Round-Robin Load Balancing

- Step 5: Showing the Expected Output
The output in **Results.png** demonstrates that requests are **balanced** across the two servers

- Step 6: UML Diagrams

The differents diagrams that we've drawn are present in **Component_Diagram.png** and **Sequence_Diagram.png** files.

