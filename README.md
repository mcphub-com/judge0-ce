markdown
# Judge0 CE MCP Server

## Overview

Judge0 CE is a robust, scalable, and open-source online code execution system. It serves as a powerful tool for building a wide range of applications that require online code execution features. These applications can include:

- Competitive programming platforms
- E-learning platforms
- Candidate assessment and recruitment platforms
- Online code editors
- Online IDEs

Judge0 CE is recognized as one of the most advanced online code execution systems available. It offers a comprehensive API that enables developers to integrate code execution capabilities into their applications seamlessly.

## Features

The Judge0 CE MCP Server provides several key features through its tools, which are organized into different groups:

### Submissions
- **Get a Submission**: Retrieve the details of a specific submission.
- **Create a Submission**: Create a new submission that waits in a queue to be processed. Upon successful creation, a submission token is provided, which can be used to check the submission status.

### Batched Submissions
- **Create a Batched Submission**: Create multiple submissions at once for batch processing.
- **Get a Batched Submission**: Retrieve details of multiple submissions simultaneously.

### Languages
- **Get a Language**: Retrieve information about a specific programming language supported by the system.
- **Get Languages**: Retrieve a list of all active programming languages available for code execution.

### Statuses
- **Get Statuses**: Obtain the current statuses of various operations and submissions.

### Configuration
- **Get Configuration**: Access detailed information about the configuration settings of the Judge0 system.

### Information
- **About**: Retrieve general information about the Judge0 CE system.

## Usage

The Judge0 CE MCP Server provides a variety of tools and functions to facilitate online code execution. Users can create submissions, check their statuses, and manage multiple submissions simultaneously. The server supports the retrieval of information about supported languages and system configurations, making it a versatile tool for developers.

### Tool Details

Each tool provides specific functionalities and parameters to help you interact with the server effectively. For example, when creating a submission, you can choose to send data in Base64 encoded format to handle non-printable characters, or use synchronous mode to get immediate results.

Overall, Judge0 CE is designed to be a comprehensive solution for applications requiring reliable and scalable code execution capabilities.

Explore the tools and functionalities of Judge0 CE to leverage its full potential in your applications.