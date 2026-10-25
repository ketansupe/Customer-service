# Customer Service

This project is a Spring Boot microservice for managing customer records in the Meridian Bank 2 application.

## Project overview

- Service name: customer-service
- Port: 8081
- Framework: Spring Boot 4.1.1
- Java version: 21
- Persistence: PostgreSQL
- Main package: `Meridian2SecureOps.com.customer_service`

## Service structure

- `src/main/java/Meridian2SecureOps/com/customer_service/CustomerServiceApplication.java` - Spring Boot entry point
- `src/main/java/Meridian2SecureOps/com/customer_service/controller/CustomerController.java` - REST API controller
- `src/main/java/Meridian2SecureOps/com/customer_service/model/Customer.java` - JPA entity
- `src/main/java/Meridian2SecureOps/com/customer_service/repository/CustomerRepository.java` - repository for CRUD operations
- `src/main/resources/application.properties` - application configuration
- `src/main/resources/schema.sql` - PostgreSQL table creation script
- `src/main/resources/static/customers.html` - customer management UI

## Database configuration

The application connects to PostgreSQL using these settings:

- database: `meridian_bank_2`
- username: `customer_service_user`
- password: `Wel2come@1234`
- host: `localhost:5432`

Configuration is stored in:

- `src/main/resources/application.properties`

## API endpoints

Base URL:

- `http://localhost:8081/api/v1/customers`

### 1. Get all customers
- Method: `GET`
- URL: `/api/v1/customers`

### 2. Get one customer by ID
- Method: `GET`
- URL: `/api/v1/customers/{id}`

### 3. Create customer
- Method: `POST`
- URL: `/api/v1/customers`
- JSON body example:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "address": "Lusaka, Zambia"
}
```

### 4. Update customer
- Method: `PUT`
- URL: `/api/v1/customers/{id}`

### 5. Delete customer
- Method: `DELETE`
- URL: `/api/v1/customers/{id}`

## Health endpoint

- `GET http://localhost:8081/api/v1/customers/health`

Response example:

```json
{
  "service": "customer-service",
  "status": "UP"
}
```

## Running the service locally

From the project folder:

```bash
./mvnw spring-boot:run
```

Then open:

- `http://localhost:8081/customers.html`

## Docker support

Each service has its own Dockerfile and the project root includes a Docker Compose setup.

### Build and run with Docker Compose

From the repo root:

```bash
docker compose up --build
```

This starts:

- PostgreSQL on port `5432`
- customer-service on port `8081`
- account-service on port `8080`
- payment-service on port `8082`

## Notes

- The customer API uses snake_case JSON keys like `first_name` and `last_name`.
- The Java entity uses camelCase fields internally and maps to JSON using `@JsonProperty`.
- The database schema is created via `schema.sql` and is validated by JPA.
