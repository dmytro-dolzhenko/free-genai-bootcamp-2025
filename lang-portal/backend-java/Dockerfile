# Build stage
FROM eclipse-temurin:21-jdk-jammy AS build
WORKDIR /build

# Copy Maven wrapper and pom.xml
COPY .mvn/ .mvn/
COPY mvnw pom.xml ./

# Make mvnw executable
RUN chmod +x mvnw

# Download dependencies
RUN ./mvnw dependency:go-offline -B

# Copy source
COPY src ./src

# Build
RUN ./mvnw clean package -DskipTests

# Run stage
FROM eclipse-temurin:21-jre-jammy
WORKDIR /app

# Copy jar from build stage
COPY --from=build /build/target/*.jar app.jar

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Create directory for database and migrations
RUN mkdir -p /data /app/BOOT-INF/classes/db/migration && chown -R 1000:1000 /data
WORKDIR /data

# Copy migrations to the correct location
COPY --from=build /build/src/main/resources/db/migration/* /app/BOOT-INF/classes/db/migration/

# Create entrypoint script
RUN echo '#!/bin/sh\n\
if [ ! -f "words.db" ]; then\n\
    touch words.db\n\
    chmod 666 words.db\n\
    sqlite3 words.db < /app/BOOT-INF/classes/db/migration/V1__initial_schema.sql\n\
    echo "Database initialized with schema"\n\
fi\n\
\n\
cd /app\n\
exec java -jar app.jar\n\
' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
