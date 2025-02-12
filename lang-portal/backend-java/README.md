# Language Learning Portal - Backend (Java)

This is the Java Spring Boot backend for the Language Learning Portal, a platform for learning Japanese through interactive exercises and systematic reviews.

## Features

- RESTful API for managing Japanese words and their components
- Word grouping system for organized learning
- Study session tracking and progress monitoring
- Review system with spaced repetition
- Dashboard with learning statistics
- Swagger UI for API documentation

## Tech Stack

- Java 21
- Spring Boot 3.2.2
- SQLite (embedded database)
- Flyway for database migrations
- SpringDoc OpenAPI for API documentation
- Docker for containerization

## Prerequisites

- Docker
- Java 21 (for local development)
- Maven (for local development)

## Docker Setup

The application is containerized and can be run using Docker without any local Java installation.

### Prerequisites

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Ensure Docker service is running

### Quick Start

1. **Build the Docker image:**
```bash
docker build -t langportal-backend .
```

2. **Run the container:**
```bash
docker run -d -p 8080:8080 --name langportal langportal-backend
```

The application will be available at `http://localhost:8080`

### Development Mode

For development with hot-reload and persistent database:

```bash
# Create a volume for the database
docker volume create langportal-data

# Run with mounted volume and exposed debug port
docker run -d \
  -p 8080:8080 \
  -p 5005:5005 \
  -v langportal-data:/app/data \
  -e JAVA_TOOL_OPTIONS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005" \
  --name langportal-dev \
  langportal-backend
```

### Docker Commands Reference

```bash
# View logs
docker logs -f langportal

# Stop container
docker stop langportal

# Remove container
docker rm langportal

# Remove image
docker rmi langportal-backend

# Clean up unused volumes
docker volume prune
```

### Troubleshooting

1. **Port Conflicts**
   ```bash
   # Check if port 8080 is in use
   docker ps | grep 8080
   
   # Use a different port
   docker run -d -p 8081:8080 --name langportal langportal-backend
   ```

2. **Container Issues**
   ```bash
   # Check container status
   docker ps -a
   
   # View detailed container info
   docker inspect langportal
   ```

3. **Database Persistence**
   - The SQLite database is stored in a Docker volume
   - Data persists between container restarts
   - To reset the database, remove and recreate the volume:
     ```bash
     docker volume rm langportal-data
     docker volume create langportal-data
     ```

## API Endpoints

### Words API
- List all words:
```bash
curl http://localhost:8080/api/words
```

- Get word by ID:
```bash
curl http://localhost:8080/api/words/1
```

- Search words:
```bash
curl "http://localhost:8080/api/words/search?query=taberu"
```

- Create new word:
```bash
curl -X POST http://localhost:8080/api/words \
  -H "Content-Type: application/json" \
  -d '{
    "kanji": "見る",
    "romaji": "miru",
    "english": "to see",
    "groupId": 1
  }'
```

- Update word:
```bash
curl -X PUT http://localhost:8080/api/words/1 \
  -H "Content-Type: application/json" \
  -d '{
    "kanji": "見る",
    "romaji": "miru",
    "english": "to watch",
    "groupId": 1
  }'
```

- Delete word:
```bash
curl -X DELETE http://localhost:8080/api/words/1
```

- Get words by group:
```bash
curl http://localhost:8080/api/words/group/1
```

### Groups API
- List all groups:
```bash
curl http://localhost:8080/api/groups
```

- Get group by ID:
```bash
curl http://localhost:8080/api/groups/1
```

- Search groups:
```bash
curl "http://localhost:8080/api/groups/search?query=Verbs"
```

- Create new group:
```bash
curl -X POST http://localhost:8080/api/groups \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Common Phrases"
  }'
```

- Update group:
```bash
curl -X PUT http://localhost:8080/api/groups/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Basic Verbs"
  }'
```

- Delete group:
```bash
curl -X DELETE http://localhost:8080/api/groups/1
```

- Add word to group:
```bash
curl -X POST http://localhost:8080/api/groups/1/words/1
```

- Remove word from group:
```bash
curl -X DELETE http://localhost:8080/api/groups/1/words/1
```

### Study Activities API
- List all activities:
```bash
curl http://localhost:8080/api/activities
```

- Get activity by ID:
```bash
curl http://localhost:8080/api/activities/1
```

- Start study session:
```bash
curl -X POST http://localhost:8080/api/activities/start \
  -H "Content-Type: application/json" \
  -d '{
    "activityId": 1,
    "groupId": 1
  }'
```

### Word Reviews API
- Get review history for word:
```bash
curl http://localhost:8080/api/reviews/word/1
```

- Submit review:
```bash
curl -X POST http://localhost:8080/api/reviews \
  -H "Content-Type: application/json" \
  -d '{
    "wordId": 1,
    "correct": true
  }'
```

### Dashboard API
- Get learning statistics:
```bash
curl http://localhost:8080/api/dashboard/stats
```

- Get recent study session:
```bash
curl http://localhost:8080/api/dashboard/recent-session
```

Tips for using curl commands:
- Add `-v` flag to see detailed request/response information
- Use `| jq` to format JSON output (if jq is installed):
  ```bash
  curl http://localhost:8080/api/words | jq
  ```
- For Windows PowerShell, replace line continuations `\` with backticks `` ` ``
- URL encode query parameters when using special characters

## API Documentation

Once the application is running, you can access:
- Swagger UI: http://localhost:8080/swagger-ui.html
- OpenAPI docs: http://localhost:8080/api-docs

## Database

The application uses SQLite for data storage. The database file is created as `words.db` in the project root directory when the application starts.

When running with Docker, mount the database file to persist data between container restarts:
```bash
docker run -p 8080:8080 -v $(pwd)/db:/app/db langportal-backend
```

### Database Schema
- `words`: Stores Japanese words with their translations
- `groups`: Word categories (verbs, nouns, etc.)
- `study_activities`: Available study activities
- `word_reviews`: Tracks review history and progress

### Migrations
Database migrations are managed by Flyway and automatically run on startup. Migration files are located in `src/main/resources/db/migration/`.

## Project Structure and Implementation Details

The application follows a standard Spring Boot project structure with clear separation of concerns:

```
src/main/java/com/langportal/
├── config/                 # Configuration classes
│   ├── DatabaseConfig     # Database configuration
│   └── SecurityConfig     # Security and CORS configuration
├── controller/            # REST API endpoints
│   ├── WordController    # Word-related endpoints
│   ├── GroupController   # Group management endpoints
│   ├── ReviewController  # Study review endpoints
│   └── ActivityController # Learning activities endpoints
├── dto/                   # Data Transfer Objects
│   ├── request/          # Request DTOs
│   └── response/         # Response DTOs
├── model/                # Domain entities
│   ├── Word             # Word entity
│   ├── Group            # Group entity
│   ├── WordReview       # Review tracking
│   ├── StudyActivity    # Learning activity
│   └── StudySession     # Study session tracking
├── repository/           # Data access layer
│   ├── WordRepository
│   ├── GroupRepository
│   ├── ReviewRepository
│   └── ActivityRepository
└── service/              # Business logic layer
    ├── WordService
    ├── GroupService
    ├── ReviewService
    └── ActivityService
```

### Key Implementation Changes

1. **Controller Layer** (Flask Routes → Spring Controllers)
   - Replaced Flask's `@app.route` with Spring's `@RestController` and `@RequestMapping`
   - Example transformation:
   ```python
   # Old Flask code
   @app.route('/api/words', methods=['GET'])
   def get_words():
       return jsonify(words)
   ```
   ```java
   // New Spring Boot code
   @RestController
   @RequestMapping("/api/words")
   public class WordController {
       @GetMapping
       public ResponseEntity<List<WordDTO>> getWords() {
           return ResponseEntity.ok(wordService.getAllWords());
       }
   }
   ```

2. **Data Access Layer** (SQLAlchemy → Spring Data JPA)
   - Replaced SQLAlchemy models with JPA entities
   - Introduced repository interfaces extending JpaRepository
   - Example transformation:
   ```python
   # Old SQLAlchemy model
   class Word(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       kanji = db.Column(db.String)
   ```
   ```java
   // New JPA entity
   @Entity
   @Table(name = "words")
   public class Word {
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
       private String kanji;
   }
   ```

3. **Service Layer** (Flask Functions → Spring Services)
   - Introduced proper service layer with dependency injection
   - Implemented transaction management
   - Example:
   ```java
   @Service
   @Transactional
   public class WordService {
       private final WordRepository wordRepository;
       
       @Autowired
       public WordService(WordRepository wordRepository) {
           this.wordRepository = wordRepository;
       }
       
       public WordDTO createWord(CreateWordRequest request) {
           // Business logic implementation
       }
   }
   ```

4. **Security Implementation**
   - Replaced Flask-Login with Spring Security
   - Implemented JWT-based authentication
   - Added method-level security with `@PreAuthorize`
   - Configured CORS properly:
   ```java
   @Configuration
   public class SecurityConfig {
       @Bean
       public SecurityFilterChain filterChain(HttpSecurity http) {
           // Security configuration
       }
   }
   ```

5. **Request/Response Handling**
   - Introduced DTOs for clean data transfer
   - Added request validation:
   ```java
   public class CreateWordRequest {
       @NotBlank
       private String kanji;
       
       @NotBlank
       private String english;
       
       // getters, setters
   }
   ```

6. **Error Handling**
   - Implemented global exception handling:
   ```java
   @ControllerAdvice
   public class GlobalExceptionHandler {
       @ExceptionHandler(ResourceNotFoundException.class)
       public ResponseEntity<?> handleResourceNotFound(ResourceNotFoundException ex) {
           // Error handling logic
       }
   }
   ```

7. **Testing Approach**
   - Replaced Python unittest with JUnit and Spring Test
   - Added integration tests using `@SpringBootTest`
   - Implemented MockMvc for controller testing
   - Example:
   ```java
   @SpringBootTest
   @AutoConfigureMockMvc
   public class WordControllerTest {
       @Autowired
       private MockMvc mockMvc;
       
       @Test
       public void testGetWords() {
           // Test implementation
       }
   }
   ```

## Migration History

The project underwent a significant transformation from a Python Flask-based backend to a Spring Boot application. Here's a summary of the migration process:

### Migration Overview
1. Framework Migration:
   - From: Python Flask backend
   - To: Spring Boot Java application
   
2. Key Changes:
   - Restructured the application to follow Spring Boot conventions
   - Implemented proper dependency injection
   - Added Spring Data JPA for data access
   - Introduced proper request/response DTOs
   - Enhanced API documentation with SpringDoc OpenAPI
   - Implemented proper exception handling with @ControllerAdvice

3. Migration Challenges & Solutions:
   - REST endpoint mapping: Adapted Flask routes to Spring @RestController annotations
   - Authentication: Implemented Spring Security to replace Flask-Login
   - Database access: Migrated from SQLAlchemy to Spring Data JPA
   - Request validation: Added Bean Validation (JSR-380)
   - CORS handling: Configured proper CORS policies with WebMvcConfigurer
   - File uploads: Implemented MultipartFile handling for user content

4. Benefits:
   - Improved type safety with Java's static typing
   - Better dependency management with Maven
   - Enhanced API documentation
   - Robust error handling
   - Better testing capabilities with Spring Test
   - Improved performance with Spring Boot's optimizations

## Testing

Run tests using Maven:
```bash
mvn test
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
