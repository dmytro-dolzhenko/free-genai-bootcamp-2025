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

# Create empty database file with correct permissions
RUN touch words.db && chmod 666 words.db

EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
