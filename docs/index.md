---
layout: default
title: SKU Generator
---

<!-- <link rel="shortcut icon" type="image/x-icon" href="favicon.ico"> -->
<!-- <link rel="shortcut icon" href="/favicon.ico" /> -->
<!-- <link rel="shortcut icon" href="favicon.ico" /> -->
<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico?">

# The Origin Tree

The project tree structure is as follows:

```verbatim
<YourDirectory>:~/.
├───CHARTS/
├───Results/
├───LICENSE
├───README.md
├───sku_gen_template.csv
├───sku-gen.py

```

Inside the CHARTS/ directory, you will find categories-subcategories.csv and colors.csv which are subject to be changed according to your use case scenario.

BOTH OF THESE ARE COMPULSORY FILES THAT MUST NOT BE DELETED. These are meant only to be edited accordingly.

Results/ directory is an empty placeholder for saving the output metadata after the script is executed.

Any files inside can be deleted and will be created anew on every run.

`sku_gen_template.csv` file is where you populate your product information and shall not be deleted at all cost.

Your final destination would be the CSV file generated in this directory with the name `sku_gen_template_result.csv`. This file will be rewritten at each run.

The nature of CSV file is, it can be easily imported into other systems even any spreadsheet software can easily import and format it easily.

sku-gen.py is where the magic happens. Run this file for your life:

On Windows:

```bash
python sku-gen.py
```

On Mac/Linux:

```bash
python3 sku-gen.py
```

Voilà, Bob's your uncle!

## Use Case Scenario

If you want the following SKU format:

106456-DE-43-654321

Note that the first three digits represents the Main Category Code as found in the categories-subcategories.csv follows by the Supplier Catalog No.

The hypens are automatically generated in any case. Next, the priorities in order are U_SIZE, U_VARIABLE, and ended with U_LOGO.

Feel free to substitute this header name according to your use specific criteria.

## SKU Generator GitHub Repository

Welcome to my SKU Generator GitHub Repository!

This repository contains a Python script that generates unique Stock Keeping Units (SKUs) for products using various product attributes such as color, size, and model.

The SKU Generator script takes in a CSV file containing the product data and outputs a new CSV file with the generated SKUs.

Modify the properties in categories-subcategories.csv and colors.csv according to your requirements.

Do not change the header's name as these are hard-coded in sku-gen.py script.

You can find the script and more information about how to use it in the README.md file on the repository's main page:

<p align="center"; style="font-size:20px">
<a href="https://github.com/pizofreude/sku-generator"><b>SKU Generator Repository</b>
    <img src="./img/Github_icon-icons.com_66788.png" width="20" height="20" alt="GitHub Badge">
</a>
</p>

Feel free to use and modify this script as needed for your own projects. If you have any questions or suggestions, please don't hesitate to reach out!

## Final Words

Open source contributions are an essential part of the tech community, and they help create the innovative tools and software that we all rely on. As someone who has benefited from my contributions, I'm sure you know the amount of time and effort that goes into maintaining and improving open source projects.

If you appreciate the work that I've put into these projects and want to show your support, consider buying me a coffee via Ko-fi! Your support will help me continue to work on these projects and create new ones, all while keeping them free and accessible for everyone.

Buying me a coffee is a simple and affordable way to show your appreciation and help me keep doing what I love. Plus, with Ko-fi, you can easily send a small contribution directly to me without any hassle.

So if you've found my open source contributions helpful and want to show your support, consider buying me a coffee via Ko-fi. Your contribution will help ensure that I can continue to create and maintain the tools and software that we all rely on.

Cheers!

<p align="center">
<a href="https://ko-fi.com/pizofreude">
    <img src="./img/kofi.gif" alt="Ko-Fi Badge">
</a>
</p>
