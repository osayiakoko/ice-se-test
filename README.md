
<div align="center">
  <h1>ICE SE TEST</h1>
</div>

<div align="center">
  <strong>Customer payment records on a modern stack</strong>
</div>

<div align="center">
  An api backend that allows ICE Commercial Power to keep record of customers payments
</div>


<br>



## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Deployment](#deployment)
- [Links](#links)

<br>

## Features

- **Authentication app**: 
    - Staff login
    - Password change
- **Customer app**: Create, read, update & delete customer record
    - All Customer form a given state, query:  ___state=edo___
- **Payment app**: Create, read, update & delete customer's payment record
    - Fetch all payments for a single customer, query:  ___customer_id=1___
    - Fetch payments above a given amount, query: ___amount_gt=60000___ 
    - Fetch payments below a given amount, query: ___amount_lt=100000___ 
- **Admin**: Admin for api backend for superuser purpose
- **Development**: Optimized for easy development using Docker
- **Docs**: Swagger & redoc documentation for client side development

<br>

## Installation

Ensure you have git & docker installed on your local machine and follow the steps below;

- open terminal in project root folder
- run

        git clone https://github.com/osayiakoko/ice-se-test
        
        cd ice-se-test

        docker build -t ice/se-test:latest .
    
        docker-compose up

<br>

## Deployment

This project was deployed on AWS, using the following services:

- **RDS**: for postgres database
- **S3**: for static/media files
- **CloudFront**: for static and dynamic web content distribution
- **EC2**: virtual private server for django hosting

    **server software/tool suite**:
    - GUNICORN: wsgi server
    - NGINX: reverse proxy
    - SYSTEMD: service daemon

<br>

## Links
Login credentials: `admin@email.com` / `pass123`
* [Swagger ui](https://projectzap.tk/swagger)
* [Redoc](https://projectzap.tk/redoc/)
* [Admin](https://projectzap.tk/admin/login/)


<br>

#### Coded with ❤️ by [Osayi Akoko](https://osayistreams.com)

hello@osayistreams.com