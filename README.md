# Document Loaders Tutorial

Welcome to the Document Loaders Tutorial! This repository demonstrates how to use various document loaders from **LangChain's document loader module** to extract text from different file types and sources. Below is a simple explanation of what document loaders are and what each of the included loaders (Text Loader, CSV Loader, Directory Loader, WebBase Loader, and PDF Loader) does. This guide is designed for beginners to understand the purpose of each loader without diving into code.

## What Are Document Loaders?

Document loaders in LangChain are tools that help you read and extract text from various file formats or sources, such as text files, CSVs, PDFs, web pages, or entire folders. These loaders convert the content into a format (like text or structured data) that can be used for tasks like natural language processing, chatbots, or text analysis. Each loader is designed to handle a specific type of file or source, making it easy to work with different kinds of data.

## Included Document Loaders

Here’s a simple explanation of the five document loaders used in this tutorial:

### 1. Text Loader
The **Text Loader** is used to read plain text files (`.txt`). It extracts the content of the file as a single piece of text. This is useful when you have simple text documents, like notes or logs, and want to load their content for processing.

### 2. CSV Loader
The **CSV Loader** reads data from CSV files (`.csv`), which are spreadsheets or tables stored as text with values separated by commas. It extracts the rows and columns, allowing you to access structured data, such as lists or datasets, for analysis or feeding into AI models.

### 3. Directory Loader
The **Directory Loader** loads multiple files from a folder (directory) at once. It can handle different file types (like `.txt`, `.csv`, or `.pdf`) within the folder by using other loaders for each file type. This is helpful when you want to process a collection of documents stored in one place.

### 4. WebBase Loader
The **WebBase Loader** extracts text from web pages by fetching the content from a given URL. It pulls the main text (like articles or blog posts) from the website, ignoring most of the HTML code or formatting. This is great for scraping web content to analyze or summarize.

### 5. PDF Loader
The **PDF Loader** reads text from PDF files (`.pdf`). It extracts the text content from each page of the PDF, making it usable for tasks like summarizing reports or extracting information from scanned documents. It works with text-based PDFs and may need additional tools for scanned images.

## How to Use This Tutorial

This repository provides examples of how to use these loaders to process different types of data. Each loader is designed to be simple to use and works with LangChain to prepare text for AI applications. You can explore the examples to see how to:
- Load a single text file with the Text Loader.
- Extract data from a CSV file with the CSV Loader.
- Process multiple files in a folder with the Directory Loader.
- Scrape text from a website with the WebBase Loader.
