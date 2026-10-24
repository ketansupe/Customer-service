from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors

output_path = "customer-service-postgresql-guide.pdf"

content = []
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CustomTitle', parent=styles['Title'], fontSize=22, leading=26, spaceAfter=18, textColor=colors.HexColor('#1f3a5f')))
styles.add(ParagraphStyle(name='Heading', parent=styles['Heading2'], fontSize=14, leading=18, spaceBefore=12, spaceAfter=8, textColor=colors.HexColor('#1f3a5f')))
styles.add(ParagraphStyle(name='Body', parent=styles['BodyText'], fontSize=10.5, leading=15, spaceAfter=7))
styles.add(ParagraphStyle(name='Bullet', parent=styles['BodyText'], leftIndent=18, bulletIndent=10, spaceAfter=5, fontSize=10.5, leading=15))


sections = [
    ("Customer Service: PostgreSQL Integration Guide", "CustomTitle"),
    ("Overview", "Heading"),
    ("This guide explains how to connect the Spring Boot API to a PostgreSQL database. The project already includes the PostgreSQL JDBC driver in pom.xml, but the application.properties file is still configured for H2 in-memory database. The goal is to switch the service to PostgreSQL and ensure the API can persist data.", "Body"),
    ("1. Create the PostgreSQL database", "Heading"),
    ("Open PostgreSQL and run the following commands:", "Body"),
    ("CREATE DATABASE customerdb;", "Body"),
    ("CREATE USER appuser WITH ENCRYPTED PASSWORD 'your_password';", "Body"),
    ("GRANT ALL PRIVILEGES ON DATABASE customerdb TO appuser;", "Body"),
    ("2. Update application.properties", "Heading"),
    ("Replace the H2 configuration with PostgreSQL connection settings:", "Body"),
    ("spring.application.name=customer-service\nserver.port=8081\n\nspring.datasource.url=jdbc:postgresql://localhost:5432/customerdb\nspring.datasource.username=postgres\nspring.datasource.password=your_password\nspring.datasource.driver-class-name=org.postgresql.Driver\n\nspring.jpa.hibernate.ddl-auto=update\nspring.jpa.show-sql=true\nspring.jpa.properties.hibernate.format_sql=true\nspring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect", "Body"),
    ("3. Ensure the PostgreSQL dependency is present", "Heading"),
    ("The project already includes PostgreSQL in pom.xml:", "Body"),
    ("<dependency>\n    <groupId>org.postgresql</groupId>\n    <artifactId>postgresql</artifactId>\n    <scope>runtime</scope>\n</dependency>", "Body"),
    ("It is recommended to move H2 to test scope only:", "Body"),
    ("<dependency>\n    <groupId>com.h2database</groupId>\n    <artifactId>h2</artifactId>\n    <scope>test</scope>\n</dependency>", "Body"),
    ("4. Create a JPA entity", "Heading"),
    ("Example entity: Customer.java", "Body"),
    ("package Meridian2SecureOps.com.customer_service.model;\n\nimport jakarta.persistence.*;\nimport java.util.UUID;\n\n@Entity\n@Table(name = \"customers\")\npublic class Customer {\n\n    @Id\n    @GeneratedValue(strategy = GenerationType.UUID)\n    private UUID id;\n\n    @Column(nullable = false)\n    private String firstName;\n\n    @Column(nullable = false)\n    private String lastName;\n\n    @Column(nullable = false, unique = true)\n    private String email;\n\n    // getters and setters\n}", "Body"),
    ("5. Create the repository", "Heading"),
    ("Create CustomerRepository.java that extends JpaRepository.", "Body"),
    ("package Meridian2SecureOps.com.customer_service.repository;\n\nimport Meridian2SecureOps.com.customer_service.model.Customer;\nimport org.springframework.data.jpa.repository.JpaRepository;\nimport java.util.UUID;\n\npublic interface CustomerRepository extends JpaRepository<Customer, UUID> {\n}", "Body"),
    ("6. Create service and controller", "Heading"),
    ("Service layer logic should handle customer retrieval and persistence:", "Body"),
    ("@Service\npublic class CustomerService {\n    private final CustomerRepository customerRepository;\n\n    public CustomerService(CustomerRepository customerRepository) {\n        this.customerRepository = customerRepository;\n    }\n\n    public List<Customer> getAllCustomers() {\n        return customerRepository.findAll();\n    }\n\n    public Customer saveCustomer(Customer customer) {\n        return customerRepository.save(customer);\n    }\n}", "Body"),
    ("Controller example:", "Body"),
    ("@RestController\n@RequestMapping(\"/api/customers\")\npublic class CustomerController {\n    private final CustomerService customerService;\n\n    public CustomerController(CustomerService customerService) {\n        this.customerService = customerService;\n    }\n\n    @GetMapping\n    public List<Customer> getAll() {\n        return customerService.getAllCustomers();\n    }\n\n    @PostMapping\n    public Customer create(@RequestBody Customer customer) {\n        return customerService.saveCustomer(customer);\n    }\n}", "Body"),
    ("7. Run the application", "Heading"),
    ("From the project root, run:", "Body"),
    ("./mvnw spring-boot:run", "Body"),
    ("or on Windows:", "Body"),
    (".\\mvnw.cmd spring-boot:run", "Body"),
    ("8. Verify the app is connected", "Heading"),
    ("Look for startup logs such as:", "Body"),
    ("HikariPool-1 - Start completed", "Body"),
    ("Started CustomerServiceApplication", "Body"),
    ("Then test the endpoint:", "Body"),
    ("GET http://localhost:8081/api/customers", "Body"),
    ("9. Production recommendations", "Heading"),
    ("Use environment variables instead of hardcoded values.", "Body"),
    ("Prefer validate mode for Hibernate in production.", "Body"),
    ("Use Flyway or Liquibase for schema migrations.", "Body"),
    ("Example:", "Body"),
    ("spring.datasource.url=${DB_URL}\nspring.datasource.username=${DB_USERNAME}\nspring.datasource.password=${DB_PASSWORD}\nspring.jpa.hibernate.ddl-auto=validate", "Body"),
    ("Conclusion", "Heading"),
    ("Once the datasource is switched from H2 to PostgreSQL, and the JPA entity/repository are created, the API can persist customer records in PostgreSQL. This is the standard Spring Boot setup for production-ready database integration.", "Body"),
]

for title, style_name in sections:
    if style_name == 'Body':
        if '\n' in title:
            paragraphs = title.split('\n')
            for p in paragraphs:
                content.append(Paragraph(p, styles[style_name]))
        else:
            content.append(Paragraph(title, styles[style_name]))
    else:
        content.append(Paragraph(title, styles[style_name]))

# improve spacing around big code blocks by inserting spacers after sections
content = [
    item for block in [
        [content[0]],
        [Spacer(1, 10)],
        [content[1]],
        [Spacer(1, 5)],
        [content[2]],
        [Spacer(1, 6)],
        [content[3]],
        [Spacer(1, 5)],
        [content[4]],
        [Spacer(1, 6)],
        [content[5]],
        [Spacer(1, 6)],
        [content[6]],
        [Spacer(1, 6)],
        [content[7]],
        [Spacer(1, 6)],
        [content[8]],
        [Spacer(1, 6)],
        [content[9]],
        [Spacer(1, 6)],
        [content[10]],
        [Spacer(1, 6)],
        [content[11]],
        [Spacer(1, 6)],
        [content[12]],
        [Spacer(1, 6)],
        [content[13]],
        [Spacer(1, 6)],
        [content[14]],
        [Spacer(1, 6)],
        [content[15]],
        [Spacer(1, 6)],
        [content[16]],
        [Spacer(1, 6)],
        [content[17]],
        [Spacer(1, 6)],
        [content[18]],
        [Spacer(1, 6)],
        [content[19]],
        [Spacer(1, 6)],
        [content[20]],
        [Spacer(1, 6)],
        [content[21]],
        [Spacer(1, 6)],
        [content[22]],
        [Spacer(1, 6)],
        [content[23]],
        [Spacer(1, 6)],
        [content[24]],
        [Spacer(1, 6)],
        [content[25]],
        [Spacer(1, 6)],
        [content[26]],
        [Spacer(1, 6)],
        [content[27]],
        [Spacer(1, 6)],
        [content[28]],
        [Spacer(1, 6)],
        [content[29]],
        [Spacer(1, 8)],
    ] for item in block
]

# The above reconstructs a list but is clumsy; use direct write below for clean file.
# This is left intentionally because the final output is generated below.

# Rebuild a clean version using the real section list.
clean_content = []
for i, (title, style_name) in enumerate(sections):
    if i > 0:
        clean_content.append(Spacer(1, 8))
    clean_content.append(Paragraph(title, styles[style_name]))

# ensure code-like blocks are readable
for item in clean_content:
    if hasattr(item, 'text') and '\n' in item.text:
        item.text = item.text.replace('\n', '<br/>')

# create final document
pdf = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
pdf.build(clean_content)
print(f"PDF created: {output_path}")
